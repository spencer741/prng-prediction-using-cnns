'''
<notes>
    Listed below are the PRNG implementations we want to focus on (this covers most of them from 1946-1998); however, 
    we need to implement as many in this list as possible: https://en.wikipedia.org/wiki/List_of_random_number_generators

        [Middle-square method (1946)](https://en.wikipedia.org/wiki/Middle-square_method)
        [Lehmer generator (1951)](https://en.wikipedia.org/wiki/Lehmer_random_number_generator)
        [Linear congruential generator (1958)](https://en.wikipedia.org/wiki/Linear_congruential_generator)
        [Lagged Fibonacci (1965)](https://en.wikipedia.org/wiki/Lagged_Fibonacci_generator)
        [Wichmann-Hill generator (1982)](https://en.wikipedia.org/wiki/Wichmann%E2%80%93Hill)
        [Park-Miller generator (1988)](https://en.wikipedia.org/wiki/Lehmer_random_number_generator)
        [Maximally periodic reciprocals (1992)](https://en.wikipedia.org/wiki/Sophie_Germain_prime)
        [Mersenne Twister (1998)](https://en.wikipedia.org/wiki/Mersenne_Twister)

    The call definition of any given PRNG function should be as follows:

    PRNGfunc(seed, n, optionalparam=default, anotherparam=default). 

    The function should return a list of n generated numbers using the generation method and all other params outside of seed and n need to have default values.

    For example if I call PRNG(seed, 10)
    It might return something like
    [3,5,10,1,31,17,2,4,6,7]

    We will control parsing the n-length list and handling seeds externally. This plays logically with separation of concerns for our usecase.

    NOTE: Please read SeedGenerator.py for notes about the seed generation method used.
</notes>
'''

import sys


'''
<Middle_Square finished=true/>
<notes>
    Weakness Note:
        For a generator of n-digit numbers, the period can be no longer than 8n. If the middle n digits are all zeroes, 
        the generator then outputs zeroes forever. If the first half of a number in the sequence is zeroes, the subsequent
        numbers will be decreasing to zero. While these runs of zero are easy to detect, they occur too frequently for this
        method to be of practical use. The middle-squared method can also get stuck on a number other than zero.
        
    An already_seen list is NOT included in the original middle square method and will not be used.
</notes>
'''
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



'''--------------------------------------LEHMER UNDER CONSTRUCTION--------------------------------
Notes:
If c = 0, the generator is often called a multiplicative congruential generator (MCG), or Lehmer RNG. If c ≠ 0, the method is called a mixed congruential generator.


While the Lehmer RNG can be viewed as a particular case of the linear congruential generator with c=0, it is a special case that implies certain restrictions and properties. In particular, for the Lehmer RNG, the initial seed must be coprime to the modulus m that is not required for LCGs in general. The choice of the modulus m and the multiplier a is also more restrictive for the Lehmer RNG. In contrast to LCG, the maximum period of the Lehmer RNG equals m−1 and it is such when m is prime and a is a primitive root modulo m. 

'''    
'''
def Lehmer():
    class Lehmer:
    def __init__(self,a,m,q,r):
        self.a = a
        self.m = m
        self.q = q
        self.r = r
        self.seed = 0
    def lehmerRNG(self,seed):
        if(seed <= 0):
            self.seed = seed
    def Next(self):
        hi = self.seed / self.q
        lo = self.seed % self.q
        self.seed = (self.a * lo) - (self.r- hi)
        if(self.seed <= 0):
            self.seed += self.m
        return(self.seed * 1.0 / self.m)
        
    import random
    hi = 10 
    lo = 0
    a = 16807
    q = 2147483647
    m = 127773
    r = 2836
    lehmer = Lehmer(a,m,q,r)
    lehmer.lehmerRNG(3)
    for i in range(20):
        x = lehmer.Next()
        ri = (hi - lo) * x + lo
        print(x)
    
    
    
    print("Lehmer")
    --------------------------------------LEHMER UNDER CONSTRUCTION--------------------------------
    '''
    



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
def Linear_Congruential(seed, listlength, modulus=4294967291, a=1588635695, c=1 ):
    print("Linear_Congruential")
    numlist = []
    for i in range(listlength):
        seed = (a * seed + c) % modulus
        numlist.append(seed)
    
    
    
    
    
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
    print("Lagged_Fibonacci")
    #litte dirty and expensive with validation checks
    #validation checks
    # 0 < j < k && k has to be greater than seed length.
    if(not(0 < j and j < k) or len(str(seed)) < k ):
        return
    
    #If addition is used, it is required that at least one of the first k values chosen to initialise the generator be odd;
    print("Lagged_Fibonacci")
    
    flag = False
    for i in range(k):
        if(int(str(seed)[i]) % 2 != 0):
            flag = True
            break
    
    #implementation  
    numlist = []
    seedlist = []
    
    for i in range(len(str(seed))):
        seedlist.append(str(seed)[i])
        
    if(flag):
        for n in range(listlength):
            for i in range(len(seedlist)):
                if i is 0:
                    val = int(seedlist[j-1]) + int(seedlist[k-1]) % 10 #arbitrary mod?
                    numlist.append(out)
                elif 0 < i < len(seedlist) - 1:
                    seedlist[i] = seedlist[i+1] # shift array
                else:
                    seedlist[i] = val
    return numlist
    
    
def Wichmann_Hill():
    print("Wichmann_Hill")
    
'''
A specific implementation of a Lehmer generator, widely used because built-in in the C and C++ languages as the function `minstd'. 

def Park_Miller():
    print("Park_Miller")
''' 
    
def Maximally_Periodic_Reciprocals():
    print("Maximally_Periodic_Reciprocals")
    

def Mersenne_Twister():
    print("Mersenne_Twister")
    
    



