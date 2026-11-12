# Diagnóstico de SEO — Tergon Pisos Industriais

Auditoria técnica do site atual: 5 páginas HTML, 1 folha de estilo e 1 imagem
(`site-antes/`). Foram verificados o código de cada página, a estrutura de títulos, as
tags de metadados, a marcação de dados estruturados, o comportamento em telas pequenas e
os arquivos de apoio à indexação.

Data: 09/11/2026

---

## Resumo

| Gravidade | Itens | O que significa |
|---|---|---|
| **Grave** | 9 | Impede ou limita diretamente a presença do site na busca |
| **Médio** | 8 | Reduz desempenho ou credibilidade, sem bloquear |
| **Detalhe** | 7 | Ajuste pontual, de baixo impacto |

**Os 9 itens graves.** A numeração abaixo é a mesma do corpo do documento e segue o impacto
estimado sobre a presença do site na busca — o item 1 é o de maior efeito:

1. O site não funciona em celular
2. Seis serviços empilhados numa página só
3. A cidade não aparece em lugar nenhum relevante
4. Os títulos das páginas estão desperdiçados
5. Nenhuma página tem H1
6. Uma única imagem, e ela não é indexável
7. Zero meta descriptions
8. Nenhuma marcação Schema.org
9. O formulário de contato não funciona

Os itens 1 a 3 são os de maior efeito sobre o volume de visitas: definem quantas buscas
diferentes o site tem condição de alcançar. Os itens 4 a 8 afetam sobretudo como o site
aparece no resultado — e os itens 7 e 8 não alteram posição nenhuma, apenas a aparência do
resultado.

O item 9 é o único que não afeta a busca, e está em último lugar por esse critério. Vale
ler em separado: é o de maior consequência comercial imediata, porque o formulário de
contato não envia nada hoje, e é também o de menor custo de correção. A recomendação é
corrigi-lo primeiro, apesar da posição que ocupa nesta ordem.

---

## GRAVE

### 1. O site não funciona em celular

**O que é:** falta a tag `<meta name="viewport">` em todas as páginas, e a folha de estilo
é toda de largura fixa em 960px com `float` (`site-antes/estilo.css`, linhas 4, 15 e 30).
Não há nenhuma `media query`, que é o recurso de CSS que adapta o layout ao tamanho da
tela.

**O que acontece na prática:** sem a tag `viewport`, o navegador do celular não assume a
largura real da tela. Ele adota uma largura virtual — em torno de 980px nos navegadores
móveis atuais —, desenha a página nessa largura e depois reduz o resultado inteiro para
caber na tela física.

O layout de 960px cabe nessa largura virtual, então a página não aparece cortada: aparece
desenhada em escala reduzida. Num aparelho de 390px de largura, a redução é de cerca de 2,5
vezes. O texto base de 14px definido no CSS é exibido com aproximadamente 5,6px, e o menu
de 12px com cerca de 4,8px. O visitante precisa ampliar com os dedos para ler qualquer
coisa.

**Por que atrapalha:** desde 2019 o Google indexa pela versão mobile do site — ele analisa
a página como se fosse um celular, e é essa versão que serve de base para a posição no
resultado. Texto ilegível sem ampliação e layout que não se adapta estão entre os problemas
de usabilidade em telas pequenas que o Google identifica.

A consequência **provável** é perda de posição, principalmente em buscas feitas no celular.
O peso exato desse fator no ranqueamento não é divulgado pelo Google, então não é possível
afirmar com certeza o tamanho do efeito. Ainda assim, é o item com maior potencial de
impacto desta auditoria: atinge as 5 páginas, e parcela relevante das buscas é feita em
celular.

### 2. Seis serviços empilhados numa página só

**O que é:** `site-antes/servicos.html` apresenta os 6 serviços como `<h3>` na mesma
página, com 1 a 3 frases cada.

**Por que atrapalha:** o Google ranqueia páginas, não sites. Uma página que trata de 6
assuntos não ranqueia bem para nenhum deles. "Piso epóxi autonivelante" e "piso
poliuretano cimentício" são buscas distintas, de clientes distintos, com problemas
distintos.

Cada um dos 6 serviços comporta uma página própria, com texto específico sobre o problema
que resolve, onde se aplica e qual obra já comprova o resultado. Isso levaria o site de 5
para cerca de 12 páginas.

### 3. A cidade não aparece em lugar nenhum relevante

**O que é:** "Indaiatuba" aparece duas vezes no site, sempre dentro do bloco de endereço.
Não está em nenhum título, nenhum heading e nenhum texto corrido. "Campinas" e "região
metropolitana de Campinas" não aparecem nenhuma vez.

**Por que atrapalha:** a empresa atende SP, MG, PR e SC a partir de Indaiatuba. Busca por
serviço industrial é quase sempre geográfica: quem procura digita a cidade ou a região
junto com o serviço. Hoje o site não informa ao Google onde atua de forma que ele possa
usar. Esse conjunto de sinais é o que se chama de SEO local, e aqui ele é inexistente.

### 4. Os títulos das páginas estão desperdiçados

**O que é:** o `<title>` é o texto azul clicável no resultado do Google. Os atuais:

| Página | Título atual | Observação |
|---|---|---|
| index | `Tergon Pisos Industriais - Home` | "Home" não corresponde a nenhuma busca |
| empresa | `... - A Empresa` | sem termo de serviço |
| servicos | `... - Serviços` | genérico |
| obras | `... - Obras` | genérico |
| contato | `... - Contato` | adequado, mas sem a cidade |

**Por que atrapalha:** o título é fator direto de ranqueamento. Os cinco começam pelo nome
da marca, o que atende bem quem já conhece a Tergon e busca pelo nome — e para essas
buscas o site tende a aparecer de qualquer forma. O que os títulos não cobrem é a busca de
quem ainda não conhece a empresa e procura pelo serviço.

Termos plausíveis para esse público: "piso epóxi industrial", "piso para frigorífico",
"piso antiderrapante cozinha industrial", "piso poliuretano cimentício". **São hipóteses,
não dados** — precisam ser validadas com pesquisa de volume de busca antes de definir os
títulos finais. O que já é certo é que nenhum termo de serviço aparece em nenhum título
hoje.

### 5. Nenhuma página tem H1

**O que é:** H1 é o título principal dentro da página — o texto que declara o assunto
dela. As cinco páginas pulam direto para `<h2>` e `<h3>`. O logotipo "TERGON" é uma
`<div>` (`site-antes/index.html:12`), não um título.

**Por que atrapalha:** o H1 é um dos sinais mais diretos que o Google usa para entender
sobre o que é a página. Sem ele, a interpretação fica por dedução. Na Home, o texto que
cumpriria essa função é o `<h2>` do banner (`site-antes/index.html:26`), mas ele está
marcado como `<h2>`, um nível abaixo.

### 6. Uma única imagem, e ela não é indexável

**O que é:** o site tem uma imagem — `banner.jpg`, 1600 × 660 px, 22,7 KB — aplicada como
fundo do hero da Home pela folha de estilo (`site-antes/estilo.css:10`). Nas 5 páginas não
existe nenhuma tag `<img>`: não há foto de obra, de equipe ou de aplicação.

**Por que atrapalha:**

- imagem aplicada como fundo via CSS não entra no Google Imagens e não aceita texto
  alternativo (`alt`), que é a descrição usada pelo Google para interpretar a figura. Para
  um fundo decorativo isso é tecnicamente correto — o problema é que essa é a única imagem
  do site.
- uma empresa de pisos industriais que não exibe piso executado deixa de usar um canal de
  busca inteiro e perde argumento de venda. As 4 obras descritas na página Obras não têm
  nenhuma foto.
- a compressão do banner é forte para a resolução: 22,7 KB para 1,05 milhão de pixels.
  Vale conferir visualmente se há perda de qualidade aparente. A dimensão, por outro lado,
  está adequada — 660px de altura para um hero de 330px atende telas de alta densidade.

Quando houver fotos de obra: nome de arquivo descritivo
(`piso-poliuretano-frigorifico-amparo.jpg` em vez de `IMG_4821.jpg`), atributo `alt` em
todas, formato WebP com JPG de reserva, e `loading="lazy"` nas que ficam abaixo da primeira
tela.

### 7. Zero meta descriptions

**O que é:** a meta description é o texto de aproximadamente 155 caracteres que aparece
abaixo do título azul no resultado do Google. Nenhuma das 5 páginas tem.

**Por que atrapalha:** sem ela, o Google recorta um trecho qualquer da página. Na Home, o
trecho provável é "Qualidade e tradição há mais de 18 anos no mercado!" — uma frase que
não informa nem diferencia.

A meta description não altera a posição do site na busca; ela influencia quantas pessoas
clicam no resultado. O ganho é de taxa de clique, não de ranqueamento.

### 8. Nenhuma marcação Schema.org

**O que é:** Schema.org é um bloco de código invisível ao visitante que descreve ao Google,
em formato de ficha, o que a página contém. Em vez de o Google ler "Rua Industrial, 1200"
e deduzir que é um endereço, a página declara: isto é uma empresa, este é o endereço, este
é o telefone, este é o horário. O formato atual é JSON-LD, um `<script>` no `<head>`.

**Por que atrapalha:** sem a marcação, o Google precisa inferir cada informação. Com ela, o
resultado pode exibir elementos adicionais — endereço, horário de funcionamento, caminho
de navegação — que ocupam mais espaço na tela de resultados.

O que se aplica a este site:

| Tipo | Onde | Para quê |
|---|---|---|
| `LocalBusiness` | todas as páginas | endereço, telefone, horário, área atendida |
| `Service` | cada página de serviço | descrição de cada aplicação |
| `BreadcrumbList` | páginas internas | caminho "Home > Serviços > Epóxi" no resultado |

Dois registros importantes:

- Schema.org não altera a posição do site na busca. Ele altera a aparência do resultado.
- O tipo `FAQPage`, que gerava perguntas expansíveis no resultado, **deixou de produzir
  qualquer elemento adicional no Google em 07/05/2026**. Blocos de perguntas nas páginas
  continuam úteis para o visitante, mas não têm mais efeito sobre a aparência na busca.

### 9. O formulário de contato não funciona

**O que é:** `site-antes/contato.html`, linhas 39 a 43. Três defeitos no mesmo formulário
de quatro campos:

- a tag `<form>` não tem `action` nem `method` — não há destino definido para o envio;
- os campos não têm atributo `name` — não têm identificação para serem transmitidos;
- os campos não têm `<label>` nem `id`. Os textos "Nome:", "E-mail:", "Telefone:" e
  "Mensagem:" estão soltos antes de cada `<input>`, separados por um `<br>`.

**Por que atrapalha — envio:** **o formulário não envia nada hoje.** Sem `action`, acionar
o botão ENVIAR apenas recarrega a página; e sem `name` não haveria o que transmitir mesmo
que existisse um destino.

**Por que atrapalha — campos sem `<label>`:** este efeito é independente do envio e
continuaria existindo mesmo com o destino corrigido. O `<label>` é o elemento que vincula o
texto ao campo. Sem ele, três coisas deixam de funcionar:

- quem usa leitor de tela ouve "campo de texto" quatro vezes, sem saber o que preencher;
- no celular, tocar no texto "Nome:" não ativa o campo — e esse toque é o alvo maior, o que
  torna o erro frequente;
- o preenchimento automático do navegador não opera, porque sem `name` nem `label` ele não
  identifica que ali vai um e-mail.

Acessibilidade não é fator direto de ranqueamento, mas é medida por auditorias
automatizadas de qualidade, como o Lighthouse do Chrome.

**Correção:** o formulário precisa ser refeito, não ajustado — destino definido, `name` em
cada campo e `<label>` vinculado a cada um. São quatro campos: é o item de menor custo de
correção entre os graves desta lista, e não há conflito entre as duas coisas. "Refazer" diz
respeito ao método, não ao tamanho do trabalho.

---

## MÉDIO

### 10. `<html>` sem idioma declarado

Falta `lang="pt-BR"` na tag `<html>`. É o atributo que informa ao Google em que idioma o
site está e para qual país se destina. Correção de uma linha por página.

### 11. Sem tag canonical

A tag canonical declara qual é o endereço oficial de cada página. Sem ela, se o site
responder em `tergonpisos.com.br`, `www.tergonpisos.com.br`, com e sem `/index.html`, o
Google pode tratar os endereços como páginas duplicadas e dividir entre eles a relevância
que deveria ser de uma só.

De correção simples hoje, e recomendável de incluir junto com qualquer ampliação do número
de páginas.

### 12. Sem sitemap.xml e sem robots.txt

O sitemap é a lista de endereços do site entregue ao Google; o robots.txt informa quais
partes podem ser percorridas.

Para 5 páginas, o impacto é baixo — o Google percorre o site inteiro sozinho a partir do
menu. Passa a ter valor real quando o site crescer em número de páginas.

### 13. A página Obras recebe poucos links internos

`site-antes/obras.html` concentra o melhor conteúdo do site: 4 casos com problema,
solução e resultado numérico. Ela recebe link apenas do menu e do rodapé — links que se
repetem em todas as páginas e por isso têm peso reduzido. Nenhum texto do site aponta para
ela.

**Por que atrapalha:** os links internos são o mecanismo pelo qual a relevância se
distribui dentro de um site. A página mais forte está recebendo o mínimo. Cada caso
deveria ser referenciado de dentro da página do serviço correspondente — o frigorífico de
Amparo na página de poliuretano, a cozinha de Jundiaí na de antiderrapante.

### 14. HTML sem marcação semântica

A estrutura usa `<div class="topo">`, `<div class="rodape">` e similares. Existem tags
próprias para isso: `<header>`, `<nav>`, `<main>`, `<footer>`, `<article>`. Elas ajudam o
Google a distinguir o conteúdo principal da moldura que se repete em todas as páginas, e
são necessárias para leitores de tela.

### 15. Pouco texto

Contagem de palavras do conteúdo de cada página:

| Página | Palavras |
|---|---|
| Home | 131 |
| A Empresa | 124 |
| Serviços | 110 |
| Obras | 171 |
| Contato | 47 |

São 583 palavras no site inteiro. A página de Serviços tem 110 palavras divididas entre 6
assuntos — de 1 a 3 frases por serviço. É pouco para ranquear em termo concorrido, e é
pouco para dar a um gestor industrial a informação técnica que ele precisa antes de pedir
um orçamento. A página de Contato, com 47 palavras, é praticamente só o endereço.

### 16. Telefone com formato de preenchimento provisório

O número `(19) 99999-0000` aparece nas 5 páginas.

**Por que atrapalha:** para busca local, o Google cruza nome, endereço e telefone do site
com o Perfil da Empresa no Google (antigo Google Meu Negócio) e com outros diretórios, e
espera que coincidam. Um número com essa aparência quebra essa correspondência.

Recomendações: confirmar o número real e aplicá-lo nas 5 páginas; e verificar se o Perfil
da Empresa no Google está criado e com os dados completos. Para aparecer no bloco de mapas
da busca, é o perfil que determina o resultado, não o site.

### 17. Os casos não têm nome nem data

**O que é:** os 4 casos da página Obras trazem número e resultado, mas nenhum nome de
cliente, data de execução ou foto.

**Por que atrapalha:** um caso sem identificação transmite menos confiança a quem está
lendo. O visitante não tem como verificar nada do que está descrito, e o texto fica
indistinguível de um exemplo hipotético. Os números são bons — é justamente por isso que
vale ancorá-los em algo verificável.

Recomendações: levantar quais obras podem ser nomeadas com autorização do cliente final, a
data de execução de cada uma e fotos do resultado.

---

## DETALHE

- **Erro de português na página Obras.** `site-antes/obras.html:52` traz "coccção", com
  três cês, em "áreas de coccção e lavagem" — o correto é "cocção". No código está escrito
  `cocc&ccedil;&atilde;o`. Sem impacto em SEO, mas está na página de melhor conteúdo do
  site.
- **Copyright 2019** nos 5 rodapés. Não afeta a posição na busca, mas o visitante lê como
  site desatualizado.
- **Sem favicon.** É o ícone que aparece na aba do navegador e nos favoritos.
- **Sem Open Graph.** São as tags que controlam a prévia do link quando ele é compartilhado
  no WhatsApp ou LinkedIn. Hoje o link é exibido sem título e sem imagem.
- **Sem Google Analytics e sem Google Search Console.** Não há nenhuma forma de medir
  visitas, origem do tráfego ou posição nas buscas. Sem os dois instalados, qualquer
  alteração futura fica sem forma de comprovação.
- **URLs terminando em `.html`.** `/servicos` é mais limpo que `/servicos.html`. Ganho
  mínimo; só vale alterar se a estrutura de páginas mudar.
- **Entidades HTML** (`&ccedil;`, `&atilde;`) espalhadas pelo código em vez de caracteres
  acentuados diretos. Renderiza corretamente e não afeta SEO; dificulta apenas a edição.
