'''
This file contains all of the PRNG methods used in this experiment.
<notes>
    Listed below are the PRNG implementations we are focusing on (this covers a good amount of them from 1946-1998);

        Done  [Middle-square method (1946)](https://en.wikipedia.org/wiki/Middle-square_method)
        Done  [Linear congruential generator (1958)](https://en.wikipedia.org/wiki/Linear_congruential_generator)
        Done  [Lagged Fibonacci (1965)](https://en.wikipedia.org/wiki/Lagged_Fibonacci_generator)
        Done  [Park-Miller (1988)](https://en.wikipedia.org/wiki/Lehmer_random_number_generator)
        Done  [Mersenne Twister (1998)](https://en.wikipedia.org/wiki/Mersenne_Twister)
        

    Note that many of the notes in the below comments are mostly indirectly or directly referenced to the wiki pages. 

    The call definition of any given PRNG function should be as follows:

    PRNGfunc(seed, n, optionalparam=default, anotherparam=default). 

    This is so we can experimentally automate the calling of each PRNG without getting too complex.

    The given PRNG function should return a list of n generated numbers using the generation method.
    All other parameters outside of the seed and n need to have default values.

    For example, if I call PRNG(seed, 10)
    It might return something like
    [3,5,10,1,31,17,2,4,6,7]

    We will control parsing the n-length list and handling seeds externally. 
    This plays logically with separation of concerns for our usecase.

    While python generators can be useful iterating over previously generated iterables,
    we did not want to clutter our experimental execution code, so we stuck to a classical
    internal handling of all iterations.

    Please read Core.SeedMethods.py for notes about the seed generation methods used.
</notes>
'''

import sys
from decimal import *
from Core.IsPrime import *
import numpy as np # For Mersenne Twister
from numpy.random import Generator, MT19937, SeedSequence # For Merseene Twister


def Get_Defs():
    return {
        'Middle_Square': '1946',
        'Linear_Congruential':'1958',
        'Lagged_Fibonacci' : '1958',
        'Park_Miller' : '1988',
        'Mersenne_Twister':'1998'   
        }


'''
<Middle_Square finished=true/>
<notes>
    Weaknesses:
        For a generator of n-digit numbers, the period can be no longer than 8n.
        If the middle n digits are all zeroes, the generator then outputs zeroes forever.
        If the first half of a number in the sequence is zeroes, the subsequent
        numbers will be decreasing to zero. 
        While these runs of zero are easy to detect, they occur too frequently for this
        method to be of practical use.
        The middle-squared method can also get stuck on a number other than zero.
        
    An already_seen list is NOT included in the original middle square method and will not be used.
</notes>
'''
def Middle_Square(seed, listlength):
    numlist = []
    for i in range(listlength):
        seedlength = len(str(seed))
        # The value of n must be even in order for the method to work ... 
        # It is acceptable to pad the seeds with zeros to the left in order to create
        # an even valued n-digit (eg: 540 → 0540).
        if (seedlength % 2 != 0):  
            seedlength += 1
            seed = str(int(seed)).zfill(seedlength)
            
        #fill leading zeros if seed*seed is less than (2*seed) digits long    
        seed = str(int(seed) * int(seed)).zfill(2 * seedlength) 
        half = int(seedlength / 2)
        seed = seed[(half):(seedlength + half)]
        numlist.append(seed)
    return(numlist)


'''
<Linear_Congruential finished=true/>
<notes>
    The generator is not sensitive to the choice of c, 
    as long as it is relatively prime to the modulus 
    (e.g. if m is a power of 2, then c must be odd), 
    so the value c=1 is commonly chosen.
    

    If c = 0, the generator is often called a multiplicative
    congruential generator (MCG), or Lehmer RNG. If c ≠ 0, the
    method is called a mixed congruential generator.

    Parameters were chosen based on 2^32 in table 2 of 
    https://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=BBA0C7ED3ADAB606642BB8D939774B4F?doi=10.1.1.34.1024&rep=rep1&type=pdf
</notes>
'''
def Linear_Congruential(seed, listlength, modulus=4294967291, a=1588635695, c=1):
    numlist = []
    for i in range(listlength):
        seed = (a * seed + c) % modulus
        numlist.append(seed)
    return numlist
              
'''
<Lagged_Fibonacci finished=true/>
<notes>
    This is two tap, not three tap...
    It's a "lagged" generator, because "j" and "k" lag behind the generated pseudorandom value. 
    Also, this is called a "two-tap" generator, in that you are using 2 values in the sequence 
    to generate the pseudorandom number. However, a two-tap generator has some problems with 
    randomness tests, such as the Birthday Spacings. Apparently, creating a "three-tap" generator
    addresses this problem.
</notes>
'''    
def Lagged_Fibonacci(seed, listlength, j=7 , k=10):
    
    # 0 < j < k
    if(not(0 < j and j < k)):
        return
    
    #If addition is used, it is required that at least one of the first k values 
    # chosen to initialise the generator be odd
    flag = False
    for i in range(len(str(seed))):
        if(i > k):
            flag = True
            break
            
        if(int(str(seed)[i]) % 2 != 0):
            flag = True
            break
    
    numlist = []
    seedlist = []
    
    for i in range(len(str(seed))):
        seedlist.append(str(seed)[i])
        
    if(flag):
        for n in range(listlength):
            for i in range(len(seedlist)):
                if i is 0:
                    val = int(seedlist[j-1]) + int(seedlist[k-1]) % 10 #arbitrary mod?
                    numlist.append(val)
                elif 0 < i < len(seedlist) - 1:
                    seedlist[i] = seedlist[i+1] # shift array
                else:
                    seedlist[i] = val
    return numlist

'''
<Park-Miller finished=true/>
<notes>
    The Lehmer generator is an lcg. Park Miller is a specific lcg.
    
    The Lehmer random number generator (named after D. H. Lehmer), 
    sometimes also referred to as the Park–Miller random number generator
    (after Stephen K. Park and Keith W. Miller), is a type of linear congruential generator (LCG).
    
    Park miller generator, because they essentially the same.
    Park-miller request the use of certain modulos.
    Lehmer is an lcg where c = 0...
    If c = 0, the generator is often called a multiplicative congruential generator (MCG),
    or Lehmer RNG. If c ≠ 0, the method is called a mixed congruential generator.

    While the Lehmer RNG can be viewed as a particular case of the linear congruential generator
    with c=0, it is a special case that implies certain restrictions and properties.
    In particular, for the Lehmer RNG, the initial seed must be coprime to the modulus m that is
    not required for LCGs in general. 
    
    The choice of the modulus m and the multiplier a is also more restrictive for the Lehmer RNG.
    In contrast to LCG, the maximum period of the Lehmer RNG equals m−1 and it is such when m is 
    prime and a is a primitive root modulo m. 
</notes>
'''    
def Park_Miller(seed, listlength):
    #initialize the state to any number greater than zero and less than the modulus.                        
    if(not(seed > 0 and seed < 2147483647)):
        print("Seed needs to be any number greater than zero and less than the modulus.")
        return
    
    numlist = []
    for i in range(listlength):
        seed = seed * 48271 % 2147483647 # hex = 0x7fffffff;
        numlist.append(seed)

    return numlist

'''
<Mersenne_Twister finished=true/>
<notes>
    Closely related with LFSRs. In its MT19937 implementation is probably the most commonly used modern PRNG. 
    Default generator in the Python language starting from version 2.3. 
    
    We used numpy's version of the Mersenne Twister.
</notes>
'''
def Mersenne_Twister(seed, listlength):
    numlist = []
    np.random.seed(seed)
    # numpy uses Mersenne Twister Algorithm
    for i in range(listlength):
        numlist.append(np.random.RandomState().randint(seed))
        
    return numlist
    
    



    
    

    
    
    


