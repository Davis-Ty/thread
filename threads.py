import threading
import random

# Number of random integers to make
array_size = 1000



# make array of random integers that between 1 and 1 (can be changed)
array = [random.randint(1, 1) for i in range(array_size)]

# (Function) for slave threads to sum a range of values in the array
def sum_range(start, end, result,i):

    print("Section ",i,": ",sum(array[start:end]))
    
    result[0] += sum(array[start:end])
# (Function) for slave threads to spawn new threads and sum half segment of the array
def spawn_threads(num_threads):
    # getting size of each section
    segment_size = array_size // num_threads
    # Creating a list of thread objects
    threads = []
    # Creating a shared result variable
    result = [0]
    # (Spawning) slave threads to sum each segment of the array
    for i in range(num_threads):
        start = i * segment_size
        end = start + segment_size
        # (safty)correcting end of last segment to account for any remaining elements
        if i == num_threads - 1:
            end = array_size
        # Create and start new thread
        t = threading.Thread(target=sum_range, args=(start, end, result,i+1))
        threads.append(t)
        t.start()
    # Wait for all threads to finish
    for t in threads:
        
        t.join()
    # Return the final sum
    return result[0]

#stopping the user from inputting numbers bigger than the list size

# Getting number of threads from user input
num_threads =int(input("Enter the amount of threads you want: "))

#stopping the user from inputting numbers bigger than the list size
while (num_threads>array_size):
    num_threads =int(input("Enter the amount of threads you want: "))
    

# Spawn threads and sum array segments
result = spawn_threads(num_threads)
# Print result
print("The sum of the array is:", result)