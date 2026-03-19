var _paq = window._paq = window._paq || [];
_paq.push(['trackPageView']);
_paq.push(['enableLinkTracking']);
(function() {
  var u = "http://localhost:8081/";
  _paq.push(['setTrackerUrl', u+'matomo.php']);
  _paq.push(['setSiteId', '1']);   // Match your Matomo site ID
  var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
  g.async=true;
  g.src=u+'matomo.js';
  s.parentNode.insertBefore(g,s);
})();

