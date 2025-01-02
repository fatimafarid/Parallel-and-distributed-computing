from mpi4py import MPI


comm = MPI.COMM_WORLD
size = comm.Get_size()  # Total number of processes
rank = comm.Get_rank()  # Rank of the current process


data = (rank + 1) ** 2


data = comm.gather(data, root=0)


if rank == 0:
    print("rank = %s " % rank)
    print("...receiving data from other processes")
    for i in range(1, size):
        value = data[i]
        print("process %s received %s from process %s" % (rank, value, i))
