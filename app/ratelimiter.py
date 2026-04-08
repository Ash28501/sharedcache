import time
from threading import Lock
from collections import defaultdict
from dataclasses import dataclass

@dataclass
class Bucket:
    tokens: float
    last_refill: float

class TokenBucketLimiter:
    def __init__(self, capacity: int = 20, refill_rate: float = 10.0):
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.buckets: dict = defaultdict(lambda: Bucket(capacity, time.time()))
        self.lock = Lock()

    def allow_request(self, identifier: str) -> bool:
        with self.lock:
            bucket = self.buckets[identifier]
            now = time.time()
            time_passed = now - bucket.last_refill
            tokens_to_add = time_passed * self.refill_rate
            bucket.tokens = min(self.capacity, bucket.tokens + tokens_to_add)
            bucket.last_refill = now

            if bucket.tokens >= 1.0:
                bucket.tokens -= 1.0
                return True
            return False