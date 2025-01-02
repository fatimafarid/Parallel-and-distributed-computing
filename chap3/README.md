COMMUNICATING_WITH_PIPE.PY

This script demonstrates producer-consumer communication using Python's multiprocessing.Queue, where the producer adds items to the queue and the consumer processes them.

COMMUNICATION_WITH_QUEUE.PY

This script demonstrates the use of multiprocessing in Python, where one process is set as a background (daemon) process and another as a non-background process. The background process runs briefly and terminates when the program exits, while the non-background process completes its task before the program finishes.

DEROM.PY

This script demonstrates the creation and management of a multiprocessing process in Python. The process executes a function foo() that prints numbers from 0 to 9 with a 1-second delay. The script starts the process, immediately terminates it, and then joins it back, showing the process state and exit code.

MYFUNC.PY

This function, myFunc(i), is designed to be called from a process. It prints the process number i and then iterates from 0 to i-1, printing the current iteration index during each cycle. The function doesn't return any value, it simply prints output.

NAMING_PROCESSES.PY

This code demonstrates how to create and run multiple processes using the multiprocessing module. It defines the function myFunc, which prints the name of the process, sleeps for 3 seconds, and then prints that the process is exiting.

In the main block, two processes are created:

One with a custom name (myFunc process).
One with the default process name (which will be automatically assigned by the system).
Both processes are started, and the program waits for their completion using join().

POINT_TO_POINT_COMMUNICATION.PY

This code demonstrates the use of message passing between different processes using mpi4py, an MPI (Message Passing Interface) library for Python.

Each process gets a rank which identifies it in the communicator COMM_WORLD.
Process 0 sends a large integer (10000000) to process 4.
Process 1 sends the string "hello" to process 8.
Process 4 receives data from process 0 and prints it.
Process 8 receives data from process 1 and prints it.
The communication is achieved using comm.send() to send data and comm.recv() to receive data between specified processes.

PROCESS_IN_SUBCLASS.PY

This code demonstrates the creation and execution of multiple processes using the multiprocessing module in Python:

The MyProcess class inherits from multiprocessing.Process and overrides the run() method, where it simply prints the name of the process.
In the if __name__ == '__main__': block, a loop creates 10 instances of the MyProcess class.
Each process is started with process.start() and then the program waits for the process to finish using process.join() before starting the next process.
This ensures each process runs sequentially, one after the other, as the join() method blocks the main program until the current process completes.

PROCESSES_BARRIER.PY

This code demonstrates the use of multiprocessing.Pool to perform parallel processing:

The function_square() function takes a number as input and returns its square.
The inputs list contains numbers from 0 to 99.
A pool of 4 processes is created using multiprocessing.Pool(processes=4).
The pool.map() method is used to apply function_square() to each element in the inputs list in parallel.
After the tasks are completed, pool.close() closes the pool, and pool.join() ensures all processes finish before the main program continues.
Finally, the squared results are printed with print(pool_outputs).
This code efficiently distributes the square calculation task across multiple processes using the pool.


RUN_BACKGROUND_PROCESSES_NO_DAMEONS.PY

This code demonstrates the use of a Barrier for synchronizing processes and a Lock for serialization:

Barrier Synchronization:

The test_with_barrier() function is used by two processes (p1 and p2) which synchronize their execution using a Barrier. Both processes must wait for each other at the barrier point (synchronizer.wait()), ensuring they proceed simultaneously after both have reached the barrier.
The processes print their names and the current time after the synchronization point.
Lock for Serialization:

The test_with_barrier() function also uses a Lock (serializer) to serialize access to the print statement, ensuring that the output from the synchronized processes is printed one after another.
Without Barrier:

The test_without_barrier() function is used by two processes (p3 and p4) that run independently without synchronization. Their output is printed as soon as each process reaches the print statement.
Key points:

The barrier ensures that p1 and p2 start their execution at the same time, while p3 and p4 are not synchronized and execute as they reach the print statement.
The Lock ensures that the output is serialized, meaning only one process can print at a time.
The output will show the synchronized processes (p1 and p2) printing the time after the barrier point, and the unsynchronized processes (p3 and p4) printing their times independently.

RUN_BACKGROUND_PROCESSES.PY

This code demonstrates the creation of two processes in Python using the multiprocessing module:

background_process:

The process named 'background_process' will print numbers from 0 to 4, simulating a background task.
The process is set to run without being daemonized (i.e., it will block the program from exiting until it finishes its work).
NO_background_process:

The process named 'NO_background_process' will print numbers from 5 to 9, simulating a foreground task.
Similarly, this process is also non-daemon, meaning the program will wait for it to finish before it terminates.

SPAWNING_PROCEESSES_NAMESPACE.PY

This code creates two processes in Python using the multiprocessing module:

background_process:

This process is named 'background_process' and will print numbers from 0 to 4. It is set as a daemon process (daemon = True), meaning it will run in the background and the program will not wait for it to finish before exiting.
NO_background_process:

This process is named 'NO_background_process' and will print numbers from 5 to 9. It is set as a non-daemon process (daemon = False), meaning the program will wait for it to finish before exiting.

SPAWNING_PROCESSES.PY
Function myFunc(i):

This function prints a message indicating which process is calling it (i), followed by a loop that prints output from 0 to i-1.
Main Program Flow:

The main() function creates and starts 6 processes, one for each value of i from 0 to 5.
For each process, myFunc is called with the argument i, and the process is started using process.start().
process.join() ensures that the main program waits for each process to finish before starting the next one.
Process Execution:

Each process executes myFunc(i) independently, but since process.join() is used, they are executed sequentially (not concurrently).
Expected Output:
For each value of i from 0 to 5, the program prints:

"calling myFunc from process n°: i"
Then prints the output from myFunc is : j for each j from 0 to i-1.


OUTPUTS:
![Screenshot (962)](https://github.com/user-attachments/assets/c490f8de-5034-4d19-9d62-6f80c45384d0)
![Screenshot (963)](https://github.com/user-attachments/assets/5b4c4a3a-3e99-49a3-951c-90373f9eb293)
![Screenshot (964)](https://github.com/user-attachments/assets/b0f29131-5910-4445-b9b7-db976754b836)
![Screenshot (965)](https://github.com/user-attachments/assets/77a88432-d2e0-44b7-afa3-a67824a5d24b)
![Screenshot (966)](https://github.com/user-attachments/assets/124582fb-8ceb-48ba-96ff-9aa63b472c3b)
![Screenshot (967)](https://github.com/user-attachments/assets/d80c488c-c2c5-4224-9436-ff19743c1aef)
![Screenshot (968)](https://github.com/user-attachments/assets/f1477337-25d0-4eaa-86f6-d9fd9c17578c)
![Screenshot (969)](https://github.com/user-attachments/assets/7cefd4ba-c543-476d-87d2-508e246e360c)
![Screenshot (970)](https://github.com/user-attachments/assets/083e6718-3056-4af7-ab99-c48f0f1ff748)
![Screenshot (971)](https://github.com/user-attachments/assets/a13f351f-3775-4e97-9341-96feeca49396)
![Screenshot (972)](https://github.com/user-attachments/assets/2f2e9671-6f77-4526-91cc-b46870131815)
![Screenshot (973)](https://github.com/user-attachments/assets/1197801c-ce6e-442b-8e12-4f76eca6e860)
![Screenshot (975)](https://github.com/user-attachments/assets/d3aafe11-b897-4e78-ae4b-f36f04b515a4)
