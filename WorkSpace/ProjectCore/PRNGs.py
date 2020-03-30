'''
Listed below are the PRNG implementations we want to focus on (this covers most of them from 1946-1998); however, 
ideally we can implement all of the ones in this list https://en.wikipedia.org/wiki/List_of_random_number_generators

    [Middle-square method (1946)](https://en.wikipedia.org/wiki/Middle-square_method)
    [Lehmer generator (1951)](https://en.wikipedia.org/wiki/Lehmer_random_number_generator)
    [Linear congruential generator (1958)](https://en.wikipedia.org/wiki/Linear_congruential_generator)
    [Lagged Fibonacci (1965)](https://en.wikipedia.org/wiki/Lagged_Fibonacci_generator)
    [Wichmann-Hill generator (1982)](https://en.wikipedia.org/wiki/Wichmann%E2%80%93Hill)
    [Park-Miller generator (1988)](https://en.wikipedia.org/wiki/Lehmer_random_number_generator)
    [Maximally periodic reciprocals (1992)](https://en.wikipedia.org/wiki/Sophie_Germain_prime)
    [Mersenne Twister (1998)](https://en.wikipedia.org/wiki/Mersenne_Twister)
'''

'''
There is a list of random number generators we need to find/ create python implementations for. (Wiki links in the project proposal). It looks like the call definition will look something like 

PRNGfunc(seed, n). 
The function should return a list of n generated numbers using the generation method

For example if I call PRNG(seed, 10)
It might return something like
[3,5,10,1,31,17,2,4,6,7]

We will control parsing the n-length list and handling seeds externally. This plays logically with separation of concerns for our usecase.

NOTE: Please read SeedGenerator.py for notes about the seed generation method used.

'''

import sys


'''
[Middle-square method (1946)](https://en.wikipedia.org/wiki/Middle-square_method)

Weakness Note from link ...
For a generator of n-digit numbers, the period can be no longer than 8n. If the middle n digits are all zeroes, the generator then outputs zeroes forever. If the first half of a number in the sequence is zeroes, the subsequent numbers will be decreasing to zero. While these runs of zero are easy to detect, they occur too frequently for this method to be of practical use. The middle-squared method can also get stuck on a number other than zero.

'''

#note, an already_seen list is not included in the original middle square method and will not be used.

def Middle_Square(seed, listlength):
    print("Middle_Square")
    numlist = []
    for i in range(listlength):
        seedlength = len(str(seed))
        # The value of n must be even in order for the method to work ... 
        # It is acceptable to pad the seeds with zeros to the left in order to create an even valued n-digit (eg: 540 → 0540).
        if (seedlength % 2 != 0):  
            seedlength += 1
            seed = str(int(seed)).zfill(seedlength)
        #print("seedlen", seedlength)
        seed = str(int(seed) * int(seed)).zfill(2 * seedlength) #fill leading zeros if seed*seed is less than (2*seed) digits long
        #print("newseed", seed)
        half = int(seedlength / 2)
        seed = seed[(half):(seedlength + half)]
        #print("finalseed", seed)
        #print(seed)
        numlist.append(seed)
    #print(numlist)
    return(numlist)
        
def Lehmer():
    print("Lehmer")
    
def Linear_Congruential(limits=[0,1], size=1, int_param=1):
    series = []
    modulus = 12387409   
    seed = time.clock()       
    multiplier = 11234345 
    increment = 7569
    #Generate the first pseudorandom number and add it to the empty list.
    next = (seed * multiplier + increment) % modulus
    series = series + [next]
    #Then generate the remaining pseudorandom numbers with LCG. 
    for n in range(0, size-1):
        next = (series[n] * multiplier + increment) % modulus
        series = series + [next]
    #Adjust the numbers to account for the range specified.
    limit_divisor = modulus/limits[1]
    for i in range(0, len(series)):
        series[i] = series[i]/limit_divisor
        print(series[i])
    #Check the integer parameter
    if int_param:
        if size == 1:
            return int(series[0])
        intify = lambda a: int(a)
        return map(intify, series)
    else:
        if size == 1:
            return series[0]
        return series
    print("Linear_Congruential")
    
    
def Lagged_Fibonacci():
    print("Lagged_Fibonacci")
    
    
def Wuchmann_Hill():
    print("Wuchmann_Hill")
    
    
def Park_Miller():
    print("Park_Miller")
    
    
def Maximally_Periodic_Reciprocals():
    print("Maximally_Periodic_Reciprocals")
    

def Mersenne_Twister():
    print("Mersenne_Twister")
    
    



