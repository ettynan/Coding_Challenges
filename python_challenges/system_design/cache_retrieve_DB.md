## Implement a Cache to Retrieve DB Results (Changing Every 3 Hours)
### Key Components:

- Cache Layer: Store query results in a cache (e.g., Redis) with a 3-hour TTL (time-to-live).
- Database Querying: When the cache expires, re-fetch data from the database and store it back in the cache.
- Automatic Cache Refresh: Periodically refresh the cache even if there’s no query to avoid stale data.
- Cache Expiration: Cache data should expire every 3 hours as per the given requirement.
### Considerations:

- Cache Freshness: Ensure the data in the cache is up-to-date and refreshed after 3 hours.
- Database Load: The database should only be queried when the cache has expired.
### Technologies:

- Redis or Memcached for caching with TTL.
- Background Jobs to refresh the cache periodically.