import os
import redis

redis_host = os.environ["REDIS_HOST"]

r = redis.Redis(redis_host)

r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})
print(r.get("Bahamas"))