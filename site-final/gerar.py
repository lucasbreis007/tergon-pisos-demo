#!/usr/bin/env python3
"""
Gerador do site da Tergon.

    python gerar.py

Lê  : modelos/*.html  +  dados/*.json  +  estaticos/
Gera: dist/  — a pasta pronta para subir no Netlify.

Telefone, WhatsApp, e-mail, endereço, horário, menu e rodapé existem num
lugar só: dados/site.json. Mude lá, rode este arquivo, e todas as páginas
saem atualizadas.

Sem dependências: só a biblioteca padrão do Python.
"""

import html
import json
import sys
import re
import shutil
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
MODELOS = RAIZ / "modelos"
DADOS = RAIZ / "dados"
ESTATICOS = RAIZ / "estaticos"
DEMO = "--demo" in sys.argv
DIST = RAIZ / ("publicar" if DEMO else "dist")

META_ROBOTS = ('\n<meta name="robots" content="noindex, nofollow">' if DEMO else "")

# Preenchido por gerar(): o og:image e igual em todas as paginas, mas o
# endereco absoluto depende do dominio, que so e lido la dentro.
META_IMAGEM = ""


# --------------------------------------------------------------- utilidades --

def ler_json(nome):
    with open(DADOS / nome, encoding="utf-8") as f:
        return json.load(f)


def ler_modelo(nome):
    with open(MODELOS / nome, encoding="utf-8") as f:
        return f.read()


def preencher(modelo, valores):
    """Troca {{chave}} pelo valor. Chave que sobrar vira string vazia."""
    for chave, valor in valores.items():
        modelo = modelo.replace("{{" + chave + "}}", str(valor))
    return re.sub(r"\{\{\w+\}\}", "", modelo)


def canonico(url):
    """No modo demonstracao nao ha dominio real: sem canonical e sem og:url."""
    if DEMO or not url:
        return ""
    return ('<meta property="og:url" content="' + url + '">\n'
            + '<link rel="canonical" href="' + url + '">')


def monta_og_imagem(site):
    """Imagem da previa ao compartilhar. Precisa de endereco absoluto.

    Na demonstracao nao ha canonical nem og:url, mas ha og:image: o
    endereco vem de 'dominio_demo', usado so para isso.
    """
    base = (site["dominio_demo"] if DEMO else site["dominio"]).rstrip("/")
    if not base:
        return ""
    img = site["og_imagem"]
    return "\n".join([
        '<meta property="og:image" content="' + esc(base + "/" + img["arquivo"]) + '">',
        '<meta property="og:image:width" content="' + str(img["largura"]) + '">',
        '<meta property="og:image:height" content="' + str(img["altura"]) + '">',
        '<meta property="og:image:alt" content="' + esc(img["alt"]) + '">',
    ])


def esc(texto):
    return html.escape(str(texto), quote=True)


def normaliza_url(url):
    """'aplicacoes/' vira 'aplicacoes/index.html'. Âncora e externo passam."""
    if url.startswith(("#", "http://", "https://", "mailto:", "tel:")):
        return url
    if url.endswith("/"):
        return url + "index.html"
    return url


def prefixo(profundidade):
    return "../" * profundidade


# ------------------------------------------------------------ peças comuns --

def monta_cabecalho(site, profundidade, na_home):
    raiz = prefixo(profundidade)
    itens = []
    for item in site["menu"]:
        url = normaliza_url(item["url"])
        if item.get("apenas_home"):
            # âncora da home: de dentro de uma subpasta, aponta para a home
            url = url if na_home else raiz + "index.html" + url
        elif not url.startswith(("#", "http")):
            url = raiz + url
        itens.append(f'      <a href="{esc(url)}">{esc(item["rotulo"])}</a>')
    menu = "\n".join(itens)
    moveis = "\n".join(i.replace("      <a ", "        <a ") for i in itens)
    inicio = "#topo" if na_home else raiz + "index.html"
    return f'''<header class="topo" id="topo">
  <div class="topo-in">
    <a class="marca" href="{esc(inicio)}" aria-label="{esc(site["site_nome"])}, início">{esc(site["marca"])}<span>&reg;</span></a>
    <nav class="menu" aria-label="Principal">
{menu}
    </nav>
    <a class="botao botao--topo" href="{esc(whatsapp_url(site))}">WhatsApp</a>
    <details class="menu-movel">
      <summary class="menu-botao">Menu</summary>
      <nav class="menu-painel" aria-label="Menu">
{moveis}
      </nav>
    </details>
  </div>
</header>'''


def monta_rodape(site, profundidade, na_home):
    raiz = prefixo(profundidade)
    colunas = []
    for col in site["rodape_colunas"]:
        links = "\n".join(
            f'        <li><a href="{esc(raiz + normaliza_url(l["url"]))}">{esc(l["rotulo"])}</a></li>'
            for l in col["links"]
        )
        colunas.append(
            f'''      <div>
        <h3>{esc(col["titulo"])}</h3>
        <ul>
{links}
        </ul>
      </div>'''
        )
    endereco = "<br>".join(esc(l) for l in site["endereco_linhas"])
    horario = "<br>".join(esc(l) for l in site["horario_linhas"])
    contato = f'''      <div class="rodape-contato">
        <h3>Contato</h3>
        <p><a href="{esc(whatsapp_url(site))}">WhatsApp</a></p>
        <p><a href="tel:{esc(site["telefone_link"])}">{esc(site["telefone"])}</a></p>
        <p><a href="mailto:{esc(site["email"])}">{esc(site["email"])}</a></p>
        <p><address>{endereco}</address></p>
        <p>{horario}</p>
      </div>'''
    colunas.append(contato)
    if DEMO:
        aviso = preencher(ler_modelo("aviso-demo.html"), {
            "aviso_demo": esc(site["aviso_demo"]),
            "aviso_imagens": esc(site["aviso_imagens"]),
        }).rstrip() + "\n"
    else:
        aviso = ""
    return f'''<footer class="rodape">
  <div class="wrap rodape-in">
    <div class="rodape-colunas">
{chr(10).join(colunas)}
    </div>
    <p class="rodape-marca">{esc(site["marca"])}<span>&reg;</span> Pisos Industriais</p>
    <p class="rodape-copy">&copy; {esc(site["copyright_ano"])} {esc(site["site_nome"])} &mdash; {esc(site["cidade"])}/{esc(site["uf"])}</p>
{aviso}  </div>
</footer>'''


def whatsapp_url(site):
    return "https://wa.me/" + site["whatsapp"]


def monta_cta(site, titulo="Fale com um de nossos consultores"):
    return f'''<section class="cta" aria-labelledby="t-cta">
  <div class="demarcacao" aria-hidden="true"></div>
  <div class="wrap">
    <h2 id="t-cta" data-revela>{esc(titulo)}</h2>
    <div class="cta-canais" data-revela>
      <a class="botao" href="{esc(whatsapp_url(site))}">Falar no WhatsApp</a>
      <a class="botao botao--vazado" href="tel:{esc(site["telefone_link"])}">{esc(site["telefone"])}</a>
      <a class="botao botao--vazado" href="mailto:{esc(site["email"])}">{esc(site["email"])}</a>
    </div>
  </div>
</section>'''


def monta_migalhas(trilha, profundidade):
    """trilha: lista de (rotulo, url_relativa_a_raiz ou None para a atual)."""
    raiz = prefixo(profundidade)
    itens = []
    for rotulo, url in trilha:
        if url is None:
            itens.append(f'      <li><span aria-current="page">{esc(rotulo)}</span></li>')
        else:
            itens.append(f'      <li><a href="{esc(raiz + normaliza_url(url))}">{esc(rotulo)}</a></li>')
    return f'''<nav class="migalhas" aria-label="Você está aqui">
    <ol>
{chr(10).join(itens)}
    </ol>
  </nav>'''


def schema_breadcrumb(trilha, dominio):
    itens = []
    for i, (rotulo, url) in enumerate(trilha, start=1):
        alvo = dominio.rstrip("/") + "/" + (normaliza_url(url) if url else "")
        itens.append({
            "@type": "ListItem",
            "position": i,
            "name": rotulo,
            "item": alvo,
        })
    return json.dumps(
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": itens},
        ensure_ascii=False, indent=2,
    )


def paragrafos(lista):
    return "\n".join(f'    <p data-revela>{esc(p)}</p>' for p in lista)


def monta_prova(obra):
    if not obra:
        return ""
    ficha = "\n".join(
        f'          <div><dt>{esc(d)}</dt><dd>{esc(v)}</dd></div>'
        for d, v in obra.get("ficha", [])
    )
    bloco_ficha = f'''
      <dl class="prova-ficha" data-revela>
{ficha}
      </dl>''' if ficha else ""
    return f'''<section class="prova" aria-labelledby="t-prova">
  <div class="wrap prova-in">
    <div>
      <h2 id="t-prova" data-revela>A prova</h2>
      <p class="prova-num" data-revela>{esc(obra["numero"])}</p>
      <p class="prova-local" data-revela>{esc(obra["titulo"])}</p>
      <p class="prova-texto" data-revela>{esc(obra["texto"])}</p>
    </div>{bloco_ficha}
  </div>
</section>'''


def foto_capa(fdef, raiz):
    """Foto nitida da capa. Acima da dobra: sem lazy, com width e height para
    nao haver pulo de layout, e fetchpriority alto."""
    larguras = fdef["larguras"]
    srcset = ", ".join(f'{raiz}img/{fdef["base"]}-{L}.webp {L}w' for L in larguras)
    return (f'<img src="{raiz}img/{fdef["base"]}-{larguras[0]}.webp" '
            f'srcset="{srcset}" '
            f'sizes="(min-width: 900px) 520px, 100vw" '
            f'width="800" height="533" fetchpriority="high" decoding="async" '
            f'alt="{esc(fdef["alt"])}">')


def monta_corte(minmm, maxmm, rotulo):
    """Corte do sistema em SVG, na mesma proporcao da regua da Home:
    9 px por milimetro; a parte cheia e a espessura minima e a caixa
    inteira vai ate a maxima."""
    px = 9
    alto_max, alto_min = maxmm * px, minmm * px
    altura = alto_max + 6
    y_min = 3 + alto_max - alto_min
    svg = (f'<svg class="corte" viewBox="0 0 170 {altura}" width="170" height="{altura}" '
           f'aria-hidden="true" focusable="false">'
           f'<rect x="1" y="1" width="168" height="{alto_max + 4}" rx="3" '
           f'fill="rgba(242,246,248,.07)" stroke="rgba(242,246,248,.42)" stroke-width="1.4"/>'
           f'<rect x="3" y="{y_min}" width="164" height="{alto_min}" fill="#C7D2DA"/>'
           f'<rect x="3" y="{y_min}" width="164" height="3" fill="#F5A623"/>'
           f'</svg>')
    return (f'<div class="capa-grafico">{svg}'
            f'<p class="capa-mm">{esc(rotulo)}</p></div>')


def monta_icone(paths):
    tracos = "".join(f'<path d="{d}"/>' for d in paths)
    return ('<div class="capa-grafico">'
            '<svg class="icone-grande" viewBox="0 0 24 24" width="64" height="64" '
            f'aria-hidden="true" focusable="false">{tracos}</svg></div>')


def monta_capa(migalhas, h1, resumo, fdef, raiz, grafico=""):
    """Capa no mesmo estilo da secao de fotos da Home: a propria foto
    minuscula e ja suavizada ao fundo, a nitida na frente com borda de
    degrade metalico, e o reflexo logo abaixo."""
    mini = f"{raiz}img/{fdef['mini']}"
    return (f'<section class="capa">\n'
            f'  <div class="capa-fundo" style="--mini:url(&quot;{mini}&quot;)" aria-hidden="true"></div>\n'
            f'  <div class="wrap capa-in">\n'
            f'    <div class="capa-texto">\n'
            f'      {migalhas}\n'
            f'      <h1>{h1}</h1>\n'
            f'      <p class="capa-resumo">{resumo}</p>\n'
            f'      {grafico}\n'
            f'    </div>\n'
            f'    <figure class="capa-figura">\n'
            f'      <span class="capa-moldura">{foto_capa(fdef, raiz)}</span>\n'
            f'      <span class="capa-reflexo" style="--mini:url(&quot;{mini}&quot;)" aria-hidden="true"></span>\n'
            f'    </figure>\n'
            f'  </div>\n'
            f'</section>')


def cartao(url, titulo, sub, extra=""):
    return f'''      <li><a href="{esc(url)}">
        <span class="cartao-titulo">{esc(titulo)}</span>
        <span class="cartao-sub">{esc(sub)}</span>{extra}
      </a></li>'''


# ----------------------------------------------------------------- páginas --

def gerar():
    site = ler_json("site.json")
    if DEMO:
        site.update(ler_json("site.demo.json"))
    apps = ler_json("aplicacoes.json")["aplicacoes"]
    artigos = ler_json("artigos.json")["artigos"]
    fotos = ler_json("fotos.json")["fotos"]
    dominio = site["dominio"].rstrip("/")
    global META_IMAGEM
    META_IMAGEM = monta_og_imagem(site)

    por_slug = {a["slug"]: a for a in apps}
    artigo_por_slug = {a["slug"]: a for a in artigos}

    # ignore_errors: no Windows, um servidor local rodando de dentro de dist/
    # segura a pasta e o apagamento falha. Com isso o gerador segue e
    # sobrescreve os arquivos em vez de quebrar.
    shutil.rmtree(DIST, ignore_errors=True)
    DIST.mkdir(parents=True, exist_ok=True)
    for item in ESTATICOS.iterdir():
        if item.is_dir():
            shutil.copytree(item, DIST / item.name, dirs_exist_ok=True)
        else:
            shutil.copy2(item, DIST / item.name)

    base = ler_modelo("base.html")
    paginas = []   # (caminho relativo, prioridade)

    # ---------------------------------------------------------------- home --
    home = ler_modelo("home.html")

    # O LocalBusiness e preenchido aqui, antes de entrar na pagina: preencher()
    # troca numa passada so, e um valor inserido depois nao teria mais a sua vez.
    # Escapa como texto JSON, nao como HTML: <script type=application/ld+json>
    # nao decodifica entidade. Mesmo criterio de schema_breadcrumb().
    campos_ld = ("site_nome", "telefone_link", "email", "endereco_rua", "cidade")
    ld_home = "" if DEMO else preencher(
        ler_modelo("ld-local.html"),
        {c: json.dumps(site[c], ensure_ascii=False)[1:-1] for c in campos_ld},
    )
    if '""' in ld_home:
        print("  AVISO: LocalBusiness saiu com campo vazio em index.html")

    saida = preencher(home, {
        "cabecalho": monta_cabecalho(site, 0, na_home=True),
        "rodape": monta_rodape(site, 0, na_home=True),
        "whatsapp_url": whatsapp_url(site),
        "telefone": esc(site["telefone"]),
        "telefone_link": esc(site["telefone_link"]),
        "email": esc(site["email"]),
        "endereco_html": "<br>".join(esc(l) for l in site["endereco_linhas"]),
        "endereco_rua": esc(site["endereco_rua"]),
        "horario_html": "<br>".join(esc(l) for l in site["horario_linhas"]),
        "cidade": esc(site["cidade"]),
        "site_nome": esc(site["site_nome"]),
        "canonical": dominio + "/",
        "dominio": dominio,
        "canonico": canonico(dominio + "/" if dominio else ""),
        "robots": META_ROBOTS,
        "og_imagem": META_IMAGEM,
        "json_ld_home": ld_home,
    })
    (DIST / "index.html").write_text(saida, encoding="utf-8")
    paginas.append(("", "1.0"))

    # --------------------------------------------------- índice aplicações --
    trilha = [("Início", "index.html"), ("Aplicações", None)]
    lista = "\n".join(
        cartao(f'{a["slug"]}.html', a["nome"], a["resumo"],
               f'<span class="cartao-mm">{esc(a["espessura"])}</span>' if a.get("espessura") else "")
        for a in apps
    )
    corpo = preencher(ler_modelo("indice-aplicacoes.html"), {
        "capa": monta_capa(
            monta_migalhas(trilha, 1),
            "Aplicações de piso industrial",
            "Seis sistemas, cada um escolhido pelo que acontece sobre o piso.",
            fotos["galpao"], "../"),
        "lista": lista,
        "cta": monta_cta(site),
    })
    escrever(base, DIST / "aplicacoes" / "index.html", {
        "title": "Aplicações de piso industrial | Tergon Pisos",
        "description": "Seis aplicações de piso industrial de alta resistência: poliuretano cimentício, antiderrapante, epóxi autonivelante, proteção química, demarcação e recuperação.",
        "og_title": "Aplicações de piso industrial",
        "og_type": "website", "site_nome": site["site_nome"],
        "canonical": f"{dominio}/aplicacoes/index.html",
        "raiz": "../", "json_ld": schema_breadcrumb(trilha, dominio),
        "cabecalho": monta_cabecalho(site, 1, False),
        "rodape": monta_rodape(site, 1, False),
        "conteudo": corpo,
    })
    paginas.append(("aplicacoes/index.html", "0.9"))

    # ------------------------------------------------- páginas de aplicação --
    modelo_app = ler_modelo("aplicacao.html")
    for a in apps:
        trilha = [("Início", "index.html"), ("Aplicações", "aplicacoes/index.html"), (a["nome"], None)]
        veja = []
        for outro in a.get("veja_tambem", []):
            o = por_slug[outro]
            veja.append(cartao(f'{o["slug"]}.html', o["nome"], o["resumo"]))
        if a.get("artigo_relacionado"):
            art = artigo_por_slug[a["artigo_relacionado"]]
            veja.append(cartao(f'../blog/{art["slug"]}.html', art["h1"], art["resumo"]))

        if a.get("espessura_mm"):
            grafico = monta_corte(a["espessura_mm"][0], a["espessura_mm"][1], a["espessura"])
        else:
            grafico = monta_icone(a["icone"])

        corpo = preencher(modelo_app, {
            "capa": monta_capa(monta_migalhas(trilha, 1), esc(a["h1"]), esc(a["resumo"]),
                               fotos[a["foto"]], "../", grafico),
            "problema": paragrafos(a["problema"]),
            "beneficio_frase": esc(a["beneficio_frase"]),
            "beneficio": paragrafos(a["beneficio"]),
            "prova": monta_prova(a.get("obra")),
            "veja_tambem": "\n".join(veja),
            "cta": monta_cta(site),
        })
        escrever(base, DIST / "aplicacoes" / f'{a["slug"]}.html', {
            "title": a["title"], "description": a["description"],
            "og_title": a["h1"], "og_type": "website", "site_nome": site["site_nome"],
            "canonical": f'{dominio}/aplicacoes/{a["slug"]}.html',
            "raiz": "../", "json_ld": schema_breadcrumb(trilha, dominio),
            "cabecalho": monta_cabecalho(site, 1, False),
            "rodape": monta_rodape(site, 1, False),
            "conteudo": corpo,
        })
        paginas.append((f'aplicacoes/{a["slug"]}.html', "0.8"))

    # --------------------------------------------------------- índice blog --
    trilha = [("Início", "index.html"), ("Blog", None)]
    lista = "\n".join(cartao(f'{t["slug"]}.html', t["h1"], t["resumo"]) for t in artigos)
    corpo = preencher(ler_modelo("indice-blog.html"), {
        "capa": monta_capa(
            monta_migalhas(trilha, 1), "Blog",
            "Problemas de piso industrial que aparecem na manutenção antes de aparecerem no orçamento.",
            fotos["garagem"], "../"),
        "lista": lista,
        "cta": monta_cta(site),
    })
    escrever(base, DIST / "blog" / "index.html", {
        "title": "Blog sobre piso industrial | Tergon Pisos",
        "description": "Artigos sobre problemas de piso industrial: descolamento na lavagem quente, resíduo nas juntas e piso escorregadio em área com água, gordura ou óleo.",
        "og_title": "Blog sobre piso industrial",
        "og_type": "website", "site_nome": site["site_nome"],
        "canonical": f"{dominio}/blog/index.html",
        "raiz": "../", "json_ld": schema_breadcrumb(trilha, dominio),
        "cabecalho": monta_cabecalho(site, 1, False),
        "rodape": monta_rodape(site, 1, False),
        "conteudo": corpo,
    })
    paginas.append(("blog/index.html", "0.9"))

    # ------------------------------------------------------------- artigos --
    modelo_artigo = ler_modelo("artigo.html")
    for t in artigos:
        trilha = [("Início", "index.html"), ("Blog", "blog/index.html"), (t["h1"], None)]
        partes = []
        for b in t["corpo"]:
            if b["tipo"] == "h2":
                partes.append(f'    <h2 class="pagina-h2-meio" data-revela>{esc(b["texto"])}</h2>')
            elif b["tipo"] == "lista":
                its = "\n".join(f'      <li>{esc(i)}</li>' for i in b["itens"])
                partes.append(f'    <ul class="lista-texto" data-revela>\n{its}\n    </ul>')
            else:
                partes.append(f'    <p data-revela>{esc(b["texto"])}</p>')
        veja = []
        if t.get("aplicacao_relacionada"):
            o = por_slug[t["aplicacao_relacionada"]]
            veja.append(cartao(f'../aplicacoes/{o["slug"]}.html', o["nome"], o["resumo"]))
        for outro in artigos:
            if outro["slug"] != t["slug"]:
                veja.append(cartao(f'{outro["slug"]}.html', outro["h1"], outro["resumo"]))

        corpo = preencher(modelo_artigo, {
            "capa": monta_capa(monta_migalhas(trilha, 1), esc(t["h1"]), esc(t["resumo"]),
                               fotos[t["foto"]], "../"),
            "corpo": "\n".join(partes),
            "prova": monta_prova(t.get("obra")),
            "veja_tambem": "\n".join(veja),
            "cta": monta_cta(site),
        })
        escrever(base, DIST / "blog" / f'{t["slug"]}.html', {
            "title": t["title"], "description": t["description"],
            "og_title": t["h1"], "og_type": "article", "site_nome": site["site_nome"],
            "canonical": f'{dominio}/blog/{t["slug"]}.html',
            "raiz": "../", "json_ld": schema_breadcrumb(trilha, dominio),
            "cabecalho": monta_cabecalho(site, 1, False),
            "rodape": monta_rodape(site, 1, False),
            "conteudo": corpo,
        })
        paginas.append((f'blog/{t["slug"]}.html', "0.7"))

    # ------------------------------------- 404, sitemap e robots -----------
    if DEMO:
        corpo404 = preencher(ler_modelo("404.html"), {"raiz": ""})
        escrever(base, DIST / "404.html", {
            "title": "Página não encontrada | " + site["site_nome"],
            "description": "A página procurada não existe neste site.",
            "og_title": "Página não encontrada", "og_type": "website",
            "site_nome": site["site_nome"], "canonical": "",
            "raiz": "", "json_ld": "",
            "cabecalho": monta_cabecalho(site, 0, False),
            "rodape": monta_rodape(site, 0, False),
            "conteudo": corpo404,
        })
        paginas.append(("404.html", "0.1"))

    if not DEMO:
        urls = "\n".join(
            f"  <url>\n    <loc>{dominio}/{caminho}</loc>\n    <priority>{prio}</priority>\n  </url>"
            for caminho, prio in paginas
        )
        (DIST / "sitemap.xml").write_text(
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            f"{urls}\n</urlset>\n", encoding="utf-8")

        (DIST / "robots.txt").write_text(
            "User-agent: *\nAllow: /\n\n"
            f"Sitemap: {dominio}/sitemap.xml\n", encoding="utf-8")
    else:
        # a demonstracao fica fora dos buscadores
        (DIST / "robots.txt").write_text(
            "# Site de demonstracao: fora dos buscadores.\n"
            "User-agent: *\nDisallow: /\n", encoding="utf-8")

    print(f"{DIST.name}/ gerada com {len(paginas)} páginas:")
    for caminho, _ in paginas:
        print("  " + (caminho or "index.html"))
    print("  sitemap.xml" if not DEMO else "  (sem sitemap.xml)")
    print("  robots.txt")


def escrever(base, destino, valores):
    valores.setdefault("robots", META_ROBOTS)
    valores.setdefault("canonico", canonico(valores.get("canonical", "")))
    valores.setdefault("og_imagem", META_IMAGEM)
    # Sem conteudo, a pagina sai sem o bloco: um <script> vazio nao e JSON valido.
    ld = valores.get("json_ld", "")
    valores["json_ld"] = (
        '<script type="application/ld+json">\n' + ld + '\n</script>' if ld else ""
    )
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(preencher(base, valores), encoding="utf-8")


if __name__ == "__main__":
    gerar()
