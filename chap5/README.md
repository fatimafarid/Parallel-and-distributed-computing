ASYNCIO_E.PY

An event-driven system where tasks A, B, and C are executed in a cyclic manner with random delays, running for 60 seconds using asyncio.

CONCURRENT_FEATURES_POOLING.PY

This code demonstrates sequential execution, thread pool execution, and process pool execution for a computationally intensive task, comparing the time taken by each approach.

COROUTINE.PY

This code simulates a Finite State Machine (FSM) using asyncio coroutines, where each state transitions asynchronously based on random values.

DEALING.PY

This script runs two asynchronous coroutines in parallel: one calculating the sum of integers and the other computing the factorial, using asyncio.Future to handle results and callbacks.

EVENT_LOOPS.PY

This code creates a circular sequence of tasks (A, B, C) using asyncio, where each task calls the next one after a random sleep time, and the cycle continues for a specified duration.

MANIPULATING_TASK.PY

This code uses asyncio to concurrently compute the factorial and Fibonacci sequence of a number, with each task performing its computation asynchronously while awaiting for the next iteration.

TASK.PY

This code demonstrates sequential, thread pool, and process pool execution of a computationally heavy task (simulating a count). It compares the execution time for each method using concurrent.futures.ThreadPoolExecutor and concurrent.futures.ProcessPoolExecutor.






