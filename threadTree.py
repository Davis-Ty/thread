import threading
import random

# Number of random integers to make
array_size = 1000

# make array of random integers that between 1 and 1 (can be changed)
array = [random.randint(1, 1) for i in range(array_size)]

# (Function) for slave threads to sum a range of values in the array
def sum_range(start, end):
    return sum(array[start:end])

# (Function) for slave threads to spawn new threads and sum half segment of the array
def spawn_threads(start, end, parent, results):
    #get mid-point of segment
    mid = (start + end) // 2
    # sums up the array if it is smaller than 101
    if end - start <= 100:
        result = sum_range(start, end)
        results[threading.current_thread()] = result
        return
    
    
    # Spawn two new threads to sum the two halves of the segment if its bigger than 100
    left_child = threading.Thread(target=spawn_threads, args=(start, mid, threading.current_thread(), results))
    right_child = threading.Thread(target=spawn_threads, args=(mid, end, threading.current_thread(), results))
    left_child.start()
    right_child.start()
    # Wait for both child threads to finish to keep code clean
    left_child.join()
    right_child.join()
    # Adds the total of left and right child and store result in parent thread
    parent_result = results[left_child] + results[right_child]
    results[threading.current_thread()] = parent_result

    #must print after the blocks above to avoid messy print out
    print("Child L: ",results[left_child],"Child R: ",results[right_child])
    print("Parent: ",parent_result)



# (Function) to create master thread
def master():
    # Create master thread and pass it the entire array segment to sum
    results = {}
    master_thread = threading.Thread(target=spawn_threads, args=(0, array_size, None, results))
    return master_thread, results

# Create master thread
master_thread, results = master()

# Start master thread
master_thread.start()

# Wait for master thread to finish
master_thread.join()

# Get result from master thread
result = results[master_thread]

# results
print("The sum of the array is:", result)
