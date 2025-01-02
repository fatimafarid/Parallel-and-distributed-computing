from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Only the root process initializes the array to scatter
if rank == 0:
    array_to_share = [1,2,3,4,5,6,7,8,9,10]
else:
    array_to_share = None


recvbuf= comm.scatter(array_to_share, root=0)
comm.barrier()


print(f"Process = %d" % rank+ "variable shared = %d" % recvbuf )
