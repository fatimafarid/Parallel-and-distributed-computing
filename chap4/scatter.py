from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    array_to_share = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # The array to be scattered
else:
    array_to_share = None  # Non-root processes start with None


recbuf = comm.scatter(array_to_share, root=0)

comm.Barrier()  # Synchronize processes before printing
print(f"Process = {rank}, variable shared = {recbuf}")
