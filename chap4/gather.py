from mpi4py import MPI

# Initialize MPI environment
comm = MPI.COMM_WORLD
size = comm.Get_size()  # Total number of processes
rank = comm.Get_rank()  # Rank of the current process

# Each process generates its own data
data = (rank + 1) ** 2

# Gather data from all processes to the root process (rank 0)
data = comm.gather(data, root=0)

# Root process handles the gathered data
if rank == 0:
    print("rank = %s " % rank)
    print("...receiving data from other processes")
    for i in range(1, size):
        value = data[i]
        print("process %s received %s from process %s" % (rank, value, i))
