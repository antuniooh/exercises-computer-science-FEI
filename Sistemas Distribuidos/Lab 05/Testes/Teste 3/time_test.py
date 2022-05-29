import random
from ProcessOne import ProcessOne
import time

# five minutes
t_end = time.time() + 5

while time.time() < t_end:
    n = random.randint(5000, 15000)
    code = random.randint(10000000, 20000000)
    process = ProcessOne(str(code), str(n))
    process.send_message()
    process.wait_callback()
