/* --------------------------------------------------------------------------
   Menu em tela estreita: o <details> abre e fecha sozinho, sem JavaScript.
   Isto aqui so acrescenta duas conveniencias: fechar ao tocar num link e
   fechar com Esc. Fica fora do bloco principal de propósito, para rodar
   tambem quando o visitante pediu menos movimento.
   -------------------------------------------------------------------------- */
(function () {
  'use strict';
  var painel = document.querySelector('.menu-movel');
  if (!painel) return;

  painel.addEventListener('click', function (e) {
    var alvo = e.target;
    while (alvo && alvo !== painel) {
      if (alvo.tagName === 'A') { painel.open = false; return; }
      alvo = alvo.parentNode;
    }
  });

  document.addEventListener('keydown', function (e) {
    if ((e.key === 'Escape' || e.key === 'Esc') && painel.open) {
      painel.open = false;
      var botao = painel.querySelector('summary');
      if (botao) botao.focus();
    }
  });
})();

/* ==========================================================================
   Tergon v3 — coreografia de rolagem

     1. cabeçalho encolhe ao sair do topo;
     2. blocos entram uma vez, escalonados dentro de cada lista;
     3. a foto do hero desliza mais devagar que o conteúdo (paralaxe);
     4. a seção de fotos fixa na tela e troca de painel a cada ~80% de tela
        rolada, até o último, e então solta.

   A TRIAGEM funciona sem este arquivo (rádio + label em CSS).
   A seção de fotos também: sem o script, sem IntersectionObserver ou com
   prefers-reduced-motion, a classe .rolo--fixo nunca é adicionada e os
   painéis voltam a abrir por clique e toque, sem fixar.
   ========================================================================== */

(function () {
  'use strict';

  var menosMovimento = window.matchMedia('(prefers-reduced-motion: reduce)');
  var telaGrande = window.matchMedia('(min-width: 900px)');
  var topo = document.getElementById('topo');
  var heroImg = document.querySelector('.hero-foto img');

  var rolo = document.querySelector('.rolo');
  var trilho = rolo ? rolo.querySelector('.rolo-trilho') : null;
  var fotos = rolo ? rolo.querySelectorAll('.painel-radio') : [];
  var pontos = rolo ? rolo.querySelectorAll('.rolo-pontos li') : [];
  var PASSO = 0.8;   /* fração da altura da tela por painel */

  function mostrarTudo() {
    var todos = document.querySelectorAll('[data-revela]');
    for (var i = 0; i < todos.length; i++) todos[i].classList.add('revelado');
    if (heroImg) heroImg.style.transform = '';
  }

  function marcarCabecalho() {
    if (!topo) return;
    if (window.scrollY > 40) topo.classList.add('fixo');
    else topo.classList.remove('fixo');
  }

  /* quem pediu menos movimento recebe o estado final e a seção de fotos
     continua no modo clique/toque, sem fixar */
  if (menosMovimento.matches || !('IntersectionObserver' in window)) {
    mostrarTudo();
    marcarCabecalho();
    window.addEventListener('scroll', marcarCabecalho, { passive: true });
    return;
  }

  /* ------------------------------------- 2. entrada dos blocos --------- */

  var escalonar = ['.casos .caso', '.reguas li', '.prazo-par .prazo', '.placa > div'];
  for (var g = 0; g < escalonar.length; g++) {
    var grupo = document.querySelectorAll(escalonar[g]);
    for (var i = 0; i < grupo.length; i++) grupo[i].dataset.atraso = String(i * 80);
  }

  var observador = new IntersectionObserver(function (entradas) {
    entradas.forEach(function (entrada) {
      if (!entrada.isIntersecting) return;
      var alvo = entrada.target;
      var atraso = Number(alvo.dataset.atraso || 0);
      if (atraso) setTimeout(function () { alvo.classList.add('revelado'); }, atraso);
      else alvo.classList.add('revelado');
      observador.unobserve(alvo);
    });
  }, { rootMargin: '0px 0px -10% 0px', threshold: 0.12 });

  var alvos = document.querySelectorAll('[data-revela]');
  for (var k = 0; k < alvos.length; k++) observador.observe(alvos[k]);

  /* ----------------------------- 3. paralaxe da foto do hero ----------- */

  function deslizarHero() {
    if (!heroImg) return;
    if (!telaGrande.matches) { heroImg.style.transform = ''; return; }
    var altura = window.innerHeight || document.documentElement.clientHeight;
    var y = window.scrollY;
    if (y > altura) return;
    var d = Math.min(y * 0.16, altura * 0.07);
    heroImg.style.transform = 'translate3d(0,' + d.toFixed(1) + 'px,0)';
  }

  /* ---------------------------- 4. fotos que fixam e avançam ----------- */

  var fixoLigado = false;
  if (rolo && trilho && fotos.length > 1) {
    rolo.classList.add('rolo--fixo');
    fixoLigado = true;
  }

  function avancarFotos() {
    if (!fixoLigado) return;
    var caixa = trilho.getBoundingClientRect();
    var alturaTela = window.innerHeight || document.documentElement.clientHeight;
    var percorrido = -caixa.top;
    if (percorrido < 0) percorrido = 0;

    var i = Math.floor(percorrido / (PASSO * alturaTela));
    if (i < 0) i = 0;
    if (i > fotos.length - 1) i = fotos.length - 1;

    if (!fotos[i].checked) fotos[i].checked = true;
    for (var j = 0; j < pontos.length; j++) {
      if (j === i) pontos[j].classList.add('ativo');
      else pontos[j].classList.remove('ativo');
    }
  }

  /* ------------------------------------------- laço único de rolagem --- */

  var agendado = false;
  function aoRolar() {
    if (agendado) return;
    agendado = true;
    window.requestAnimationFrame(function () {
      agendado = false;
      deslizarHero();
      avancarFotos();
      marcarCabecalho();
    });
  }

  window.addEventListener('scroll', aoRolar, { passive: true });
  window.addEventListener('resize', aoRolar);
  aoRolar();

  /* se a preferência mudar durante a visita: volta ao clique/toque */
  var aoMudar = function (e) {
    if (!e.matches) return;
    mostrarTudo();
    if (rolo) { rolo.classList.remove('rolo--fixo'); fixoLigado = false; }
  };
  if (menosMovimento.addEventListener) menosMovimento.addEventListener('change', aoMudar);
  else if (menosMovimento.addListener) menosMovimento.addListener(aoMudar);
})();
