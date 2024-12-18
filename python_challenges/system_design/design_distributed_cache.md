## Design a Distributed Cache
### Key Components:

- Cache Store: A key-value store that temporarily holds frequently accessed data to reduce database load (e.g., Redis, Memcached).
- Cache Expiration: Data in the cache should have an expiration time to ensure freshness.
- Eviction Policy: When the cache is full, older data should be evicted to make room for newer data. Common eviction policies include Least Recently Used (LRU).
- Consistency: Ensure consistency across distributed cache nodes (e.g., replication, sharding).

### Considerations:

- Scalability: As the system grows, the cache needs to scale horizontally across multiple nodes.
- Fault Tolerance: Cache replication across nodes to ensure availability even if some nodes go down.
- Cache Invalidation: Cache should be invalidated when underlying data changes to prevent stale data.

### Technologies:

- Redis or Memcached for caching.
- Sharding for distributing cache data across multiple nodes.
- Replication for fault tolerance.
