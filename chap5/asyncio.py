import asyncio
import time
import random

# Define task A
def task_A(end_time, loop):
    print('task A called')
    time.sleep(random.randint(0, 5))
    if loop.time() + 1.0 < end_time:
        loop.call_later(1, task_B, end_time, loop)
    else:
        loop.stop()

# Define task B
def task_B(end_time, loop):
    print('task B called')
    time.sleep(random.randint(0, 5))
    if loop.time() + 1.0 < end_time:
        loop.call_later(1, task_C, end_time, loop)
    else:
        loop.stop()

# Define task C
def task_C(end_time, loop):
    print('task C called')
    time.sleep(random.randint(0, 5))
    if loop.time() + 1.0 < end_time:
        loop.call_later(1, task_A, end_time, loop)
    else:
        loop.stop()

# Main event loop
loop = asyncio.get_event_loop()
end_loop = loop.time() + 60  # Run for 60 seconds
loop.call_soon(task_A, end_loop, loop)
loop.run_forever()
loop.close()
