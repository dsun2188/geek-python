# import time
from time import sleep as std_sleep, time as std_time

start = std_time()
print(f"Start at {start}")

std_sleep(2)

end = std_time()
print(f"End at {end}")
