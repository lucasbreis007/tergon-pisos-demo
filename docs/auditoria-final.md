# Auditoria SEO do site novo — mesma régua do diagnóstico

Medição de `site-final/dist` (12 páginas) com os **mesmos 24 critérios** usados em
`diagnostico.md` sobre o `site-antes/` (5 páginas), na mesma ordem e pelo mesmo
método.

Medido em `dist`, não em `publicar` — a pasta de demonstração tem `noindex` de
propósito e distorceria metade dos critérios.

Data: 11/11/2026

**Nenhum arquivo do site foi alterado nesta auditoria.**

---

## Como os critérios foram extraídos

Do `diagnostico.md` saíram 24 itens, assim distribuídos:

| Gravidade | Itens | Numeração no diagnóstico |
|---|---|---|
| Grave | 9 | 1 a 9 |
| Médio | 8 | 10 a 17 |
| Detalhe | 7 | sem numeração, lista final |

Os critérios de detalhe não eram numerados no original; aqui recebem os números
18 a 24 apenas para caber na tabela, na mesma ordem em que aparecem lá.

**Nenhum critério foi acrescentado ou removido.**

### Critérios que não podem ser medidos no site novo

| Nº | Critério | Por quê |
|---|---|---|
| 9 | Formulário de contato | **O site novo não tem formulário.** A decisão de projeto substituiu o formulário por links diretos de WhatsApp, telefone e e-mail. O defeito não foi corrigido: o elemento deixou de existir. Medi em seu lugar se os três canais funcionam. |
| 13 | Links internos para a página Obras | **Não existe página Obras.** O conteúdo das 4 obras foi distribuído entre a Home, as páginas de aplicação e os artigos. Medi a distribuição em lugar da contagem de links para uma página única. |

Além destes, três trechos do diagnóstico original já eram explicitamente não
mensuráveis e continuam sendo:

- o **peso do fator mobile no ranqueamento** (item 1) — o diagnóstico já dizia
  que o Google não divulga;
- os **termos de busca plausíveis** (item 4) — o diagnóstico já os marcava como
  "hipóteses, não dados", dependentes de pesquisa de volume;
- o **efeito do canonical** (item 11) e a **utilidade do sitemap** (item 12)
  dependem do domínio real, que ainda não existe.

---

## Medição, critério a critério

### GRAVE

**1. O site funciona em celular?** — MEDIDO
`<meta name="viewport">` em **12 de 12 páginas** (ex.: `dist/index.html`, linha 5).
**24 media queries** (18 em `estilo.css`, 6 em `estilo-interno.css`).
**Zero** larguras fixas de três dígitos em px e **zero** `float` no layout.
Em 390 px, nas 5 páginas testadas no navegador: **rolagem lateral 0 px**, **menor
fonte 16 px**, escala 1 (sem redução forçada).
No site antigo: 0 viewport, 0 media queries, layout fixo de 960 px, texto renderizado
a ~5,6 px.

**2. Páginas por serviço** — MEDIDO
**6 páginas de aplicação**, uma por sistema, em `dist/aplicacoes/`:
poliuretano-cimenticio, antiderrapante-multicamada, epoxi-autonivelante,
protecao-quimica, demarcacao-de-areas, recuperacao-de-pisos.
Total do site: **12 páginas HTML**.
O diagnóstico previa "de 5 para cerca de 12 páginas". É exatamente 12.

**3. A cidade aparece em lugar relevante?** — MEDIDO
"Indaiatuba" no site: **41 ocorrências**. Por zona:

| Zona | Páginas com "Indaiatuba" |
|---|---|
| `<title>` | **1 de 12** (só a Home) |
| meta description | **6 de 12** |
| `<h1>` | **1 de 12** (só a Home) |
| corpo (`<main>`) | **1 de 12** (Home, 3 vezes) |
| rodapé | 12 de 12 (2 vezes cada) |

"Campinas": **0 ocorrências** — igual ao site antigo.
No antigo: 2 ocorrências, ambas no bloco de endereço, nenhuma em título, heading
ou texto corrido.

**4. Títulos** — MEDIDO (o valor) / INFERIDO (a adequação)
12 títulos únicos, de 41 a 72 caracteres, nenhum começando pelo nome da marca:

```
 64  Piso industrial de alta resistência em Indaiatuba | Tergon Pisos
 44  Aplicações de piso industrial | Tergon Pisos
 55  Piso em poliuretano cimentício, 6 a 9 mm | Tergon Pisos
 56  Piso antiderrapante multicamada, 3 a 5 mm | Tergon Pisos
 61  Piso epóxi autonivelante, 2 a 3 mm, sem juntas | Tergon Pisos
 72  Revestimento de proteção química para bacias de contenção | Tergon Pisos
 68  Demarcação de áreas: faixas, corredores e sinalização | Tergon Pisos
 64  Recuperação de pisos danificados, juntas e cantos | Tergon Pisos
 41  Blog sobre piso industrial | Tergon Pisos
 65  Por que o piso descola depois da lavagem com água quente | Tergon
 66  Resíduo nas juntas do piso: o ponto que reprova auditoria | Tergon
 56  Piso escorregadio onde há água, gordura ou óleo | Tergon
```

**Medido:** todos trazem termo de serviço ou de problema; nenhum é genérico.
**Inferido:** se são os termos certos. O diagnóstico já marcava isso como hipótese
a validar com pesquisa de volume, e essa pesquisa continua não feita.
Dois títulos passam de 60 caracteres (72 e 68) e devem ser cortados no resultado
do Google.

**5. H1** — MEDIDO
**Exatamente 1 H1 por página, em 12 de 12.** Nenhuma página com zero ou com dois.
No antigo: 0 H1 em 5 páginas.

**6. Imagens** — MEDIDO
**19 tags `<img>`** no site, **0 sem `alt`** preenchido.
34 arquivos em `dist/img/`, **todos WebP**, com nomes descritivos
(`painel-corredor-800.webp`, `mini-setas.webp`), nenhum `IMG_xxxx`.
**0 regras** de `background-image` em CSS — nenhuma imagem depende de fundo CSS
para existir.
`loading="lazy"` em 7 imagens, `fetchpriority="high"` em 12 (uma por página).
**19 de 19 com `width` e `height`.**
No antigo: 0 tags `<img>`, 1 imagem só por fundo CSS, sem `alt` possível.

**7. Meta descriptions** — MEDIDO
**12 de 12 páginas**, de 103 a 160 caracteres. Nenhuma vazia, nenhuma duplicada.
Duas no limite alto (160 e 157) podem ser cortadas no resultado.
No antigo: 0 de 5.

**8. Schema.org** — MEDIDO

| Tipo | Site novo | O diagnóstico recomendava |
|---|---|---|
| `LocalBusiness` | 1 página (Home) | todas as páginas |
| `BreadcrumbList` | **11 páginas** internas | páginas internas |
| `Service` | **0 páginas** | cada página de serviço |
| `FAQPage` | 0 | correto: deixou de produzir efeito em 07/05/2026 |

No antigo: nenhum dos quatro.

**9. Formulário de contato** — NÃO COMPARÁVEL (ver acima)
**0 tags `<form>`** no site novo. Os três canais estão em **12 de 12 páginas**:
`tel:+5519999990000`, `mailto:contato@tergonpisos.com.br`,
`https://wa.me/5519999990000`. Todos sintaticamente válidos.
O problema do antigo (formulário que não enviava nada) não existe mais porque o
formulário não existe mais.

### MÉDIO

**10. `lang`** — MEDIDO
`lang="pt-BR"` em **12 de 12** páginas (linha 2 de cada arquivo).
No antigo: 0 de 5.

**11. Canonical** — MEDIDO
`rel="canonical"` em **12 de 12**, uma URL por página, sem repetição.
Exemplo: `https://www.tergonpisos.com.br/aplicacoes/antiderrapante-multicamada.html`.
**Ressalva:** o domínio é marcador, não endereço real. A tag está correta na
forma; o valor só passa a valer quando o domínio existir.

**12. sitemap.xml e robots.txt** — MEDIDO
Ambos presentes em `dist/`. O sitemap lista **12 URLs**, uma por página.
O robots.txt libera tudo e aponta o sitemap.
Mesma ressalva do domínio.

**13. Distribuição do conteúdo das obras** — NÃO COMPARÁVEL (ver acima)
Onde cada obra aparece no site novo:

| Obra | Páginas | Quais |
|---|---|---|
| Amparo/SP | **3** | Home, página do poliuretano, artigo sobre descolamento |
| Hortolândia/SP | **3** | Home, página do epóxi, artigo sobre juntas |
| Jundiaí/SP | **3** | Home, página do antiderrapante, artigo sobre escorregamento |
| Cabreúva/SP | **1** | só a Home, na seção de prazos |

Links internos para âncora de obra: **3**, todos partindo da própria Home para
seções dela mesma. **Nenhuma página interna linka para as obras da Home** — o
texto da obra é repetido na própria página de aplicação, na seção "A prova".
No antigo: 1 página com o conteúdo, recebendo apenas os links repetidos de menu e
rodapé.

**14. HTML semântico** — MEDIDO
Presença por página, em 12 páginas:

```
<header>   12/12      <section>  12/12
<nav>      12/12      <figure>   11/12
<main>     12/12      <address>  12/12
<footer>   12/12      <article>   4/12
```

No antigo: nenhuma dessas tags; só `<div class="...">`.

**15. Contagem de palavras** — MEDIDO

| Página | Palavras |
|---|---|
| blog/index | 116 |
| aplicacoes/index | 138 |
| demarcação de áreas | 221 |
| recuperação de pisos | 246 |
| proteção química | 262 |
| epóxi autonivelante | 356 |
| antiderrapante multicamada | 359 |
| poliuretano cimentício | 383 |
| Home | 501 |
| artigo: resíduo nas juntas | 590 |
| artigo: piso escorregadio | 601 |
| artigo: piso descola | 633 |
| **Total** | **4.406** |

No antigo: 583 palavras no site inteiro, maior página com 171.

**16. Telefone** — MEDIDO
`(19) 99999-0000` em **12 de 12 páginas**. **É o mesmo número do site antigo**,
com o mesmo formato de preenchimento provisório.

**17. Casos com nome e data** — MEDIDO
**Nenhum nome de cliente final** em nenhuma das 12 páginas.
**Nenhuma data de execução** — o único ano no texto visível é 2026, do copyright.
Idêntico ao site antigo: os casos continuam identificados só por cidade e tipo de
indústria.

### DETALHE

**18. Erro "coccção"** — MEDIDO. **0 ocorrências** da grafia errada; 4 ocorrências
de "cocção" correto. Corrigido.

**19. Copyright** — MEDIDO. **2026** nas 12 páginas. No antigo: 2019.

**20. Favicon** — MEDIDO. **12 de 12** páginas, SVG embutido em data URI.
No antigo: nenhum.

**21. Open Graph** — MEDIDO, **com defeito**

| Tag | Páginas |
|---|---|
| og:title, og:description, og:type, og:locale, og:site_name, og:url | **12 de 12** |
| **og:image** | **0 de 12** |

Seis das sete tags estão presentes. A sétima, `og:image`, **sumiu** — e sumiu numa
alteração minha recente, não no projeto original. Detalhe no fim deste documento.
No antigo: nenhuma tag Open Graph.

**22. Analytics e Search Console** — MEDIDO.
**0 de 12** páginas com Google Analytics, GTM ou qualquer script de medição.
**0 de 12** com `google-site-verification`.
Idêntico ao site antigo.

**23. URLs com `.html`** — MEDIDO. **220 links internos** terminam em `.html`.
Idêntico ao antigo em natureza; o número cresceu porque o site tem mais páginas.

**24. Entidades HTML de acento** — MEDIDO. **0 ocorrências** de `&ccedil;`,
`&atilde;` e similares no código. No antigo: espalhadas por todas as páginas.

---

## Antes e depois

| Nº | Critério | Site antigo | Site novo | Situação |
|---|---|---|---|---|
| 1 | Funciona em celular | 0 viewport, 0 media query, 960 px fixo, texto a ~5,6 px | 12/12 viewport, 24 media queries, 0 px de rolagem lateral, fonte mínima 16 px | **melhorou** |
| 2 | Páginas por serviço | 1 página com 6 serviços | 6 páginas, uma por sistema; 12 no total | **melhorou** |
| 3 | Cidade em lugar relevante | 2 ocorrências, só no endereço | 41 ocorrências, mas título/H1 só na Home (1/12) | **melhorou em parte** |
| 4 | Títulos | 5 genéricos, todos começando pela marca | 12 únicos, com termo de serviço; 2 acima de 60 caracteres | **melhorou** |
| 5 | H1 | 0 em 5 páginas | 1 por página, 12/12 | **melhorou** |
| 6 | Imagens | 0 `<img>`, 1 fundo CSS, sem `alt` | 19 `<img>`, 0 sem `alt`, 34 WebP, 0 fundo CSS | **melhorou** |
| 7 | Meta descriptions | 0 em 5 | 12 em 12, de 103 a 160 caracteres | **melhorou** |
| 8 | Schema.org | nenhum | LocalBusiness 1, BreadcrumbList 11, **Service 0** | **melhorou em parte** |
| 9 | Formulário de contato | não enviava nada | não existe; 3 canais válidos em 12/12 | **não comparável** |
| 10 | `lang` | 0 em 5 | 12 em 12 | **melhorou** |
| 11 | Canonical | nenhum | 12 em 12, com domínio marcador | **melhorou** |
| 12 | sitemap e robots | nenhum dos dois | ambos, sitemap com 12 URLs | **melhorou** |
| 13 | Conteúdo das obras | 1 página, só links de menu e rodapé | 3 obras em 3 páginas cada; Cabreúva em 1 | **não comparável** |
| 14 | HTML semântico | nenhuma tag semântica | header/nav/main/footer em 12/12 | **melhorou** |
| 15 | Quantidade de texto | 583 palavras no site | 4.406 palavras; menor página 116 | **melhorou** |
| 16 | Telefone | `(19) 99999-0000` provisório | **o mesmo número** | **igual** |
| 17 | Casos com nome e data | sem nome, sem data | **sem nome, sem data** | **igual** |
| 18 | Erro "coccção" | 1 ocorrência | 0 | **melhorou** |
| 19 | Copyright | 2019 | 2026 | **melhorou** |
| 20 | Favicon | nenhum | 12/12 | **melhorou** |
| 21 | Open Graph | nenhuma tag | 6 das 7; **og:image ausente** | **melhorou em parte** |
| 22 | Analytics e Search Console | nenhum | **nenhum** | **igual** |
| 23 | URLs `.html` | todas | todas (220 links) | **igual** |
| 24 | Entidades HTML | espalhadas | 0 | **melhorou** |

**Resumo:** 15 melhoraram, 3 melhoraram em parte, 4 iguais, 2 não comparáveis.

---

## O que ainda está fraco, em ordem de impacto

**1. `Service` em nenhuma página de aplicação.**
O diagnóstico recomendava `Service` em cada página de serviço. Há seis páginas de
aplicação e zero marcações. É o único dos três tipos recomendados que ficou de
fora, e é o que descreveria ao Google o que cada página oferece.

**2. A cidade não entra nas páginas internas.**
"Indaiatuba" aparece no título e no H1 apenas da Home. Nas 11 internas ela existe
só no rodapé e, em 6 delas, na meta description. Uma página chamada "Piso em
poliuretano cimentício" sem cidade no título compete em busca nacional, não local
— e busca por piso industrial é quase sempre geográfica. "Campinas" segue com
zero ocorrências, como no site antigo.

**3. `og:image` ausente nas 12 páginas.**
Link compartilhado no WhatsApp ou LinkedIn aparece sem imagem. **Esta é uma
regressão que eu introduzi**, não um item herdado — detalhe no fim.

**4. Nenhuma medição instalada.**
Sem Analytics e sem Search Console, não há como provar que qualquer coisa desta
auditoria produziu efeito. Era item de detalhe no diagnóstico antigo e continua
pendente; agora pesa mais, porque há 12 páginas para acompanhar em vez de 5.

**5. Páginas internas não linkam para as obras.**
Os três links para âncora de obra partem todos da Home para ela mesma. As páginas
de aplicação repetem o texto da obra em vez de apontar para ela. Funciona para o
leitor, mas não distribui relevância entre as páginas.

**6. Dois títulos acima de 60 caracteres.**
Proteção química (72) e demarcação de áreas (68) serão cortados no resultado do
Google.

**7. Duas páginas de índice com pouco texto.**
`blog/index` com 116 palavras e `aplicacoes/index` com 138 são as mais magras do
site. São páginas de navegação, então o peso é menor, mas estão abaixo das demais.

---

## O que depende de dados reais do cliente

Nenhum número abaixo foi inventado; são campos vazios à espera de informação.

| Dado | Onde entra | Efeito enquanto não vier |
|---|---|---|
| **Domínio** | canonical (12 páginas), og:url (12), sitemap.xml, robots.txt | Todos usam `https://www.tergonpisos.com.br`, que é marcador. Trocar em `dados/site.json` e rodar `gerar.py`. |
| **Telefone e WhatsApp** | 12 páginas, LocalBusiness, rodapé | `(19) 99999-0000` quebra a correspondência de nome-endereço-telefone que o Google cruza para busca local. |
| **Perfil da Empresa no Google** | fora do site | O diagnóstico já apontava: para aparecer no bloco de mapas, é o perfil que decide, não o site. Continua sem verificação. |
| **Nome e data das obras** | 3 páginas de aplicação, Home, 3 artigos | Os casos seguem identificados só por cidade e setor. |
| **Avaliações de clientes** | nenhuma no site | Sem avaliação não há o que marcar, e `AggregateRating` sem base real seria invenção. |
| **Fotos de obra identificadas** | 19 imagens em uso | Nenhuma das 8 fotos pode ser ligada a uma obra. As legendas descrevem só o que se vê — correto, mas não é prova visual. |
| **CNPJ** | rodapé, LocalBusiness | Ausente. |

---

## Uma regressão que esta auditoria encontrou

`og:image` existia na Home e **sumiu quando eu criei o modo demonstração**.

O patch substituiu três linhas do `modelos/home.html` — canonical, og:url e
og:image — por um único marcador, e a função que gera esse marcador devolve
apenas canonical e og:url. A tag og:image não foi recolocada.

Afeta `dist`, não só `publicar`. Como esta tarefa é só de leitura, **não
corrigi**. A correção é acrescentar og:image ao retorno da função `canonico()`
em `gerar.py`, condicionada à existência de domínio, e rodar o gerador.

---

## Procedência de cada critério

**Medidos de fato (20 de 24):** 1, 2, 3, 5, 6, 7, 8, 10, 11, 12, 14, 15, 16, 17,
18, 19, 20, 21, 22, 23, 24 — todos por contagem direta nos arquivos de `dist` ou
por medição no navegador a 390 px e 1440 px.

**Medidos em parte, com um componente inferido (1):** critério 4. O valor (12
títulos únicos, com termo de serviço, com os comprimentos acima) é medido; a
adequação dos termos ao que as pessoas buscam é inferida, porque a pesquisa de
volume que o próprio diagnóstico pedia nunca foi feita.

**Não comparáveis (2):** critérios 9 e 13, pelos motivos registrados no início —
o formulário e a página Obras deixaram de existir como elementos.

**Não mensuráveis, e já assim no diagnóstico original (3 trechos):** o peso do
fator mobile no ranqueamento, o volume de busca dos termos escolhidos, e o efeito
real de canonical e sitemap antes de existir domínio.

**Nenhuma nota ou pontuação foi atribuída.** O `diagnostico.md` não define método
de pontuação, apenas três faixas de gravidade, então aqui há só valores medidos e
a classificação melhorou / melhorou em parte / igual / não comparável.

---

## Correções posteriores (11/11/2026)

Feitas depois da auditoria acima, no mesmo `site-final/dist`. O corpo do
documento não foi alterado: esta seção registra o que mudou desde então.

### og:image: 0/12 → 12/12

A regressão apontada no fim da auditoria está corrigida. As 12 páginas de `dist`
trazem agora `og:image`, `og:image:width`, `og:image:height` e `og:image:alt`,
com endereço absoluto. A imagem é um recorte 1200×630 de uma das 8 fotos que já
estavam no site, em JPEG de 133,9 KB, sem texto e sem logo.

O critério 21 passa de **melhorou em parte** para **melhorou**: as sete tags
Open Graph estão nas 12 páginas.

### Títulos: dois encurtados, seis ainda acima de 60

| Página | Antes | Depois |
|---|---|---|
| proteção química | 72 car. | **56 car.** |
| demarcação de áreas | 68 car. | **62 car.** |

Em proteção química saiu "Revestimento de", que o H1 mantém. Em demarcação só a
marca encurtou, para "\| Tergon": descer dos 62 exigiria tirar um dos três itens
da lista (faixas, corredores, sinalização), o que removeria um fato.

Continuam acima de 60 os cinco títulos que não foram tocados:

| Caracteres | Página |
|---|---|
| 66 | `blog/residuo-nas-juntas-do-piso` |
| 65 | `blog/piso-descola-lavagem-agua-quente` |
| 64 | `index` |
| 64 | `aplicacoes/recuperacao-de-pisos` |
| 61 | `aplicacoes/epoxi-autonivelante` |

Com o de demarcação em 62, são **6 títulos de 12 acima de 60 caracteres**, contra
7 na auditoria original.

### LocalBusiness: agora conferido por conteúdo

A auditoria contou o critério 8 pela **presença** do bloco, não pelo conteúdo
dele. Uma verificação posterior mostrou que o `LocalBusiness` de
`dist/index.html` saía com `name`, `telephone`, `email`, `streetAddress` e
`addressLocality` **vazios**: o gerador trocava os marcadores numa passada só, e
o bloco entrava na página depois que a vez deles já tinha passado.

Corrigido. Os cinco campos saem preenchidos com os valores de `dados/site.json`,
e o bloco passa por `json.loads`. Os 11 `BreadcrumbList` das páginas internas
também passam: **23 blocos JSON-LD válidos, 0 inválidos**, contando as duas
pastas.

O critério 8 segue **melhorou em parte**, pelo mesmo motivo de antes: `Service`
continua em 0 das 6 páginas de aplicação.

### Correção na contagem de critérios

A auditoria escreveu "medidos de fato (20 de 24)" e em seguida listou 21 números.
A contagem certa é **21**:

| | Quantos | Quais |
|---|---|---|
| Medidos | **21** | 1, 2, 3, 5, 6, 7, 8, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 |
| Medidos em parte | 1 | 4 (os títulos são medidos; a adequação dos termos é inferida) |
| Não comparáveis | 2 | 9 e 13 |
| **Total** | **24** | |

### Resumo antes/depois recalculado

| Situação | Auditoria original | Agora |
|---|---|---|
| Melhoraram | 15 | **16** |
| Melhoraram em parte | 3 | **2** (critérios 3 e 8) |
| Iguais | 4 | 4 |
| Não comparáveis | 2 | 2 |
| **Total** | 24 | 24 |

A única mudança de classificação é o critério 21, por causa do `og:image`. Os
critérios 16 (telefone provisório), 17 (casos sem nome nem data), 22 (sem
Analytics nem Search Console) e 23 (URLs com `.html`) continuam **iguais** ao
site antigo, e o que depende de dados reais do cliente continua como está na
lista acima.
