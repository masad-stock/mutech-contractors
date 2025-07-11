self.addEventListener('install', function(e) {
  e.waitUntil(
    caches.open('fundamental-design').then(function(cache) {
      return cache.addAll([
        '/',
        '/static/style.css',
        '/static/logo.png'
      ]);
    })
  );
});
self.addEventListener('fetch', function(e) {
  e.respondWith(
    caches.match(e.request).then(function(response) {
      return response || fetch(e.request);
    })
  );
});