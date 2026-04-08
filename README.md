# ShardCache

**A sharded in-memory Key-Value Store with Redis persistence, rate limiting, and observability** — built with FastAPI & Python.

A lightweight hybrid cache (fast LRU in-memory shards + durable Redis backend) designed to demonstrate systems design concepts like sharding, eviction policies, persistence, and production-grade features.

## ✨ Features

- **4-way consistent hashing sharding** for distributed-like behavior
- **LRU eviction** with per-key TTL support (using `OrderedDict`)
- **Token Bucket rate limiting** (burst + sustained rate per IP)
- **Hybrid persistence**: Write-through to Redis + automatic load on startup
- **Prometheus metrics** for cache hits/misses, HTTP requests, and rate limit rejections
- Graceful fallback (works even if Redis is unavailable)
- Background sync and manual snapshot support
- Clean FastAPI architecture with lifespan events

## 🛠 Tech Stack

- Python 3.12
- FastAPI + Uvicorn
- Redis (for persistence)
- Prometheus Client (observability)
- OrderedDict for O(1) LRU operations

## 🚀 Quick Start

### Using Docker Compose (Recommended)

```bash
# Clone the repo and navigate to the project
git clone <your-repo-url>
cd shardcache

# Start Redis + ShardCache
docker-compose up --build