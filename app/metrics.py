from prometheus_client import Counter, CollectorRegistry, generate_latest

registry = CollectorRegistry()

http_requests_total = Counter(
    'http_requests_total', 'Total HTTP requests',
    ['method', 'endpoint', 'status'], registry=registry
)

cache_hits = Counter('cache_hits_total', 'Cache hits', registry=registry)
cache_misses = Counter('cache_misses_total', 'Cache misses', registry=registry)
rate_limit_rejections = Counter(
    'rate_limit_rejections_total', 'Rate limit rejections',
    ['identifier'], registry=registry
)

def get_metrics():
    return generate_latest(registry)