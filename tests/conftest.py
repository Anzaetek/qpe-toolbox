import multiprocessing

# fix os.fork() warning in test with already multu-threaded pytest
# Switching to "forkserver" avoids this: child processes are forked from a
# dedicated single-threaded server, eliminating the deadlock risk.
if multiprocessing.get_start_method(allow_none=True) is None:
    multiprocessing.set_start_method("forkserver")
