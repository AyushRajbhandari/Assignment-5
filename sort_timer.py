# Author: Ayush Rajbhandari
# GitHub username: AyushRajbhandari
# Date: 6-13-26
# Description: Compares the execution time of bubble sort and insertion sort
#              on randomly generated lists of varying sizes and generates
#              a graph of the results using matplotlib.

import time
import random
from matplotlib import pyplot

def bubble_time(a_list):
    """Sorts a list using bubble sort and returns the time it took in seconds."""
    start_time = time.perf_counter()

    # Standard Bubble Sort logic
    for pass_num in range(len(a_list) - 1, 0, -1):
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp

    end_time = time.perf_counter()
    return end_time - start_time
def insertion_time(a_list):
    """Sorts a list using insertion sort and returns the time it took in seconds."""
    start_time = time.perf_counter()
    # Exact Insertion Sort logic from image_86a768.png
    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
        while pos >= 0 and a_list[pos] > value:
            a_list[pos + 1] = a_list[pos]
            pos -= 1
        a_list[pos + 1] = value

    end_time = time.perf_counter()
    return end_time - start_time
def sort_times_for_random_list(n):
    """
    Generates a list of n random integers, copies it, and times both
    bubble sort and insertion sort on identical unsorted lists.
    """
    # Generate list of n random integers between 1 and n
    list_1 = []
    for _ in range(n):
        list_1.append(random.randint(1, n))

    # Make a copy so both algorithms sort the exact same data
    list_2 = list(list_1)
    # Get sort times
    b_time = bubble_time(list_1)
    i_time = insertion_time(list_2)
    return (b_time, i_time)

def compare_sorts():
    """Generates a graph comparing bubble sort and insertion sort times."""
    # List lengths to test
    lengths = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

    bubble_times = []
    insertion_times = []

    # Gather timing data
    print("Gathering data... this may take a moment.")
    for length in lengths:
        print(f"Sorting lists of size {length}...")
        b_time, i_time = sort_times_for_random_list(length)
        bubble_times.append(b_time)
        insertion_times.append(i_time)
    # Graph the data
    pyplot.plot(lengths, bubble_times, 'ro--', linewidth=2, label='Bubble Sort')
    pyplot.plot(lengths, insertion_times, 'go--', linewidth=2, label='Insertion Sort')
    pyplot.xlabel("Size of List Being Sorted")
    pyplot.ylabel("Seconds to Sort")
    pyplot.legend(loc='upper left')

    # Display the graph
    pyplot.show()
def main():
    """Main function to run the comparison script."""
    compare_sorts()
if __name__ == "__main__":
    main()
