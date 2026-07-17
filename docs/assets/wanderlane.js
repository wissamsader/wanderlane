// Wanderlane — tiny progressive-enhancement layer (no dependencies)
(function () {
  var head = document.getElementById('siteHead');
  var onScroll = function () { if (head) head.classList.toggle('scrolled', window.scrollY > 12); };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  var t = document.getElementById('navToggle');
  var links = document.getElementById('navLinks');
  if (t && links) {
    t.addEventListener('click', function () { links.classList.toggle('open'); });
    links.addEventListener('click', function (e) { if (e.target.tagName === 'A') links.classList.remove('open'); });
  }

  var toc = document.querySelector('.toc');
  if (toc && 'IntersectionObserver' in window) {
    var map = {};
    toc.querySelectorAll('a').forEach(function (a) { map[a.getAttribute('href').slice(1)] = a; });
    var obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          Object.values(map).forEach(function (a) { a.classList.remove('active'); });
          var a = map[en.target.id]; if (a) a.classList.add('active');
        }
      });
    }, { rootMargin: '-15% 0px -70% 0px' });
    document.querySelectorAll('.prose h2[id]').forEach(function (h) { obs.observe(h); });
  }
})();
