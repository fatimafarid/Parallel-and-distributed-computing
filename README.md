

BASICS FOLDER

CODE 1: Basic calculator using Python.

CODE 2: Python code implementing lists, dictionaries, and tuples.

CODE 3: Function to calculate sum.

CODE 4: Using classes and objects.

CHAP 1

BANK.PY: 

Uses multithreading to perform deposit and withdrawal operations on a shared balance while measuring execution time.

DATA_PARALLELISM.PY:

 Uses a thread pool to execute two tasks (task_1 and task_2) concurrently using ThreadPoolExecutor.

DO_SOMETHING.PY:

 Defines a function do_something that generates random numbers and adds them to a given list for a specified count.

FIBONACCI.PY:

 Creates multiple threads to calculate the 35th Fibonacci number concurrently and measures the total execution time.

HELLO.PY:

 Performs data-parallel vector addition using NumPy, measures computation time, and displays the first 10 results.

IPC.PY:

 Demonstrates inter-process communication using a queue, where a producer adds items and a consumer retrieves them in separate processes.

MPI.PY:

 Uses MPI to enable communication between processes, where process 0 sends data to process 1, and other processes remain idle.

MULTIPROCESSING.PY: 

Compares the performance of multiprocessing and multithreading for a task that generates large random numbers and 
measures their execution times.

PARALLELIZATION.PY:

 Performs parallel vector addition using threads and measures execution time.

PROCESS_CREATION.PY:

 Demonstrates multiprocessing to calculate the square and cube of a number concurrently.

SHARED_MEM.PY:

 Demonstrates threading with a lock to safely manage deposits and withdrawals on a shared balance.

SYNCHRONIZATION.PY:

 Demonstrates the use of a semaphore to control access to a shared resource, allowing only one thread at a time.

CHAP 2

BARRIER.PY:

 Simulates a race between three runners using threads and a barrier to synchronize their arrival at the finish line.

CONDITION.PY:

 Implements a producer-consumer problem using threading and a condition variable to synchronize the producer and consumer threads.

EVENT.PY:

 Implements a simple producer-consumer problem using threading and an event to synchronize threads.

MYTHREADCLASS.PY:

 Creates and runs 9 threads using the Thread class, with each thread simulating a task with a random duration.

MYTHREADCLASS_LOCK.PY: 

Runs 9 threads with a lock mechanism to ensure only one thread executes its critical section at a time.

MYTHREADCLASS_LOCK2.PY:

 Threads simulate random durations while ensuring mutual exclusion using a lock for printing messages.

RLOCK.PY:

 Demonstrates the use of threads and reentrant locks to add and remove items from a shared box concurrently.

SEMAPHORE.PY:

 Demonstrates the use of semaphores to synchronize producer and consumer threads.

THREADDEFINITON.PY: 

Creates and starts 10 threads, each calling the my_func function with a unique thread number.

THREAD_DETERMINE.PY: 

Creates three threads, each executing a different function (function_A, function_B, function_C).

THREAD_NAME_AND_PROCESSES.PY:

 Creates two threads, each printing the thread name and process ID, and joins them to wait for completion.

CHAP 3

COMMUNICATING_WITH_PIPE.PY:

 Demonstrates producer-consumer communication using multiprocessing.Queue.

COMMUNICATION_WITH_QUEUE.PY:

 Demonstrates multiprocessing with both daemon and non-daemon processes.

DEROM.PY:

 Demonstrates creation and management of a multiprocessing process that runs a task, terminates, and joins back.

MYFUNC.PY: 

Function designed to be called from a process, printing process number and iteration indices.

NAMING_PROCESSES.PY:

 Demonstrates naming and execution of multiple processes using the multiprocessing module.

POINT_TO_POINT_COMMUNICATION.PY:

 Demonstrates message passing between processes using mpi4py.

PROCESS_IN_SUBCLASS.PY:

 Demonstrates creation and execution of processes using subclasses.

PROCESSES_BARRIER.PY:

 Demonstrates parallel processing using multiprocessing.Pool.

RUN_BACKGROUND_PROCESSES_NO_DAMEONS.PY:

 Demonstrates synchronization using barriers and serialization with locks.

RUN_BACKGROUND_PROCESSES.PY:

 Demonstrates the creation of processes using the multiprocessing module.

SPAWNING_PROCEESSES_NAMESPACE.PY:

 Creates two processes using the multiprocessing module.

SPAWNING_PROCESSES.PY: 

Prints messages and simulates tasks with different processes.

CHAP 4

GATHER.PY: 

Collects data from all processes at the root process for aggregation or further processing.

POINT_TO_POINT_COMMUNICATION.PY:

 Implements point-to-point communication between specific processes using send and recv.

BROADCAST.PY:

 Broadcasts a variable from the root process to all other processes in the communicator.

VIRTUALTOPOLOGY.PY:

Python script demonstrating grid topology creation and neighbor communication using MPI and mpi4py.

SCATTER.PY:

Python script demonstrating array scattering across processes using MPI and mpi4py.

REDUCTION.PY:

Python script demonstrating MPI Reduce operation with mpi4py to sum arrays across processes

ALLTOALL.PY:

Python script demonstrating MPI All-to-All communication with mpi4py for exchanging data among processes

DEADLOCKPROBLEMS.PY:

Python script demonstrating point-to-point communication using mpi4py with send and recv

CHAP 5

ASYNCIO_E.PY

An event-driven system where tasks A, B, and C are executed cyclically with random delays. The cycle continues for 60 seconds, with each task calling the next after a delay, demonstrating asynchronous execution with asyncio.

CONCURRENT_FEATURES_POOLING.PY

This script compares the execution time for sequential, thread pool, and process pool approaches for a computationally intensive task. It uses concurrent.futures.ThreadPoolExecutor and concurrent.futures.ProcessPoolExecutor to demonstrate multi-threading and multi-processing in Python.

COROUTINE.PY

A simulation of a Finite State Machine (FSM) using asyncio coroutines. The system transitions asynchronously between states based on random values, providing a demonstration of coroutine-based state management and event-driven programming.

DEALING.PY

This script runs two asynchronous coroutines in parallel: one computes the sum of integers, and the other calculates the factorial. The use of asyncio.Future helps manage their results, allowing callbacks upon completion of each task.

EVENT_LOOPS.PY

This code creates a cyclic sequence of tasks (A, B, C) using asyncio. Each task calls the next one after a random sleep, creating a loop that continues for a set duration. It demonstrates task scheduling and event loop management in asyncio.

MANIPULATING_TASK.PY

This code concurrently computes the factorial and Fibonacci sequence for a number using asyncio. Each task performs its respective computation asynchronously, demonstrating the flexibility of async functions in handling multiple calculations in parallel.

TASK.PY

This script compares the execution times of sequential, thread pool, and process pool executions of a heavy computational task. It uses concurrent.futures.ThreadPoolExecutor and concurrent.futures.ProcessPoolExecutor to illustrate how multi-threading and multi-processing impact performance.







