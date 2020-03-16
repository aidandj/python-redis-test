import os
import redis

redis_host = os.environ["REDIS_HOST"]
redis_port = os.environ["REDIS_PORT"]

r = redis.Redis(host=redis_host,
    port=int(redis_port))

r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})
print(r.get("Bahamas"))