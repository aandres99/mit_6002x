###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows, limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    herdl= sorted(cows.items(), key=lambda x: x[1], reverse=True)
    all_trips = []
    trip = []
    used = []
    trip_wt = 0
    while len(used) < len(herdl):
        for cow in herdl:
           if cow[0] not in used and (trip_wt + cow[1]) <= limit:
                trip_wt += cow[1]
                used.append(cow[0])
                trip.append(cow[0])
        all_trips.append(trip)
        trip = []
        trip_wt = 0
    return all_trips


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    c_cows = cows.copy()
    good_trips = []
#    test_count = 0
    for trip_list in (get_partitions(c_cows)):
#        test_count += 1
        print('Trip list: ', trip_list)
        heavy_trip = False
        for trip in trip_list:
            trip_wt = 0
            for cow in range(len(trip)):
                trip_wt += c_cows[trip[cow]]
            print('last cow in trip: ', trip[cow], 'total trip wt: ', trip_wt)
            if trip_wt > limit:
                print('Trip too heavy')
                heavy_trip = True
                continue
        if heavy_trip == False:
            good_trips.append(trip_list)
#        if test_count == 50:
#            break
    return good_trips

# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""
cows = load_cows("ps1_cow_data.txt")
'''
limit = 10
print(cows)
print(greedy_cow_transport(cows, limit))

cows = load_cows("ps1_cow_data2.txt")
limit = 100
print(cows)
print(greedy_cow_transport(cows, limit))
'''

print(brute_force_cow_transport(cows))


