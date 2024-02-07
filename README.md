#threads.py
- The threads.py script utilizes threading to parallelize the summation of an array. It prompts the user to input the number of threads to use. Then, it divides the array into segments based on the thread count, assigns each segment to a thread, and calculates the sum concurrently. Finally, it aggregates the results from all threads to compute the total sum. This approach leverages multiple CPU cores, improving performance for large datasets.

- #threadtree.py
- - This script, named thread_tree.py, utilizes threading to implement a tree structure for parallelized computation. It divides the array into segments, assigning each to a thread, resembling a tree with parent and child threads. Threads recursively split segments until reaching a threshold, then compute and aggregate results. The script leverages multicore processing for efficient computation.
