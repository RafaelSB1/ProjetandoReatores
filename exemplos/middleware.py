from django.core.cache import cache
from django.utils.deprecation import MiddlewareMixin

class ClearCacheMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Limpa o cache antes de cada solicitação
        cache.clear()