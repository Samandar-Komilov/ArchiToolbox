from datetime import datetime, timedelta, timezone
import random

http_methods = ["GET", "POST", "PUT", "DELETE"]
test_paths = ["/home", "/login", "/api/users", "/products", "/checkout", "/cart", "/home", "/api/products", "/contact"]

with open("server.log", "a") as f:
    now = datetime.now(timezone.utc)
    for i in range(500):
        time_to_add = now + timedelta(seconds=i*30)
        f.write(f"{time_to_add} {random.choice(http_methods)} {random.choice(test_paths)} {random.randint(1, 100)} 200\n")