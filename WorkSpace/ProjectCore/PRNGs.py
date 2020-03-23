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

'''

import sys

def Middle_Square():
    print("Middle_Square")
    seed_number = int(input("Please enter a four digit number:\n[####] "))
    number = seed_number
    already_seen = set()
    counter = 0
    count = 0
    while number not in already_seen:
        counter += 1
        already_seen.add(number)
        number = int(str(number * number).zfill(8)[2:6])  # zfill adds padding of zeroes
        while (number > 0):
            number = number//10
            count = count + 1
            #print (count)
            #print (number)
            if (count % 10 != 0):
                print(f"{number}", end = '')
            elif (count % 10 == 0):
                print(f"{number}")

        
    
def Lehmer():
    print("Lehmer")
    
def Linear_Congruential():
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
    
    



