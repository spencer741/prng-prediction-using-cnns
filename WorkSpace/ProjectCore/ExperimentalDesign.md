## **Observation:**
Society relies on Pseudo-random numbers for a multitude of reasons. Whether the usecases fall in Information Security or, more broadly, modeling and simulation, we shall not highlight their importance in computing.

We think it is important to not only push the boundary for the modern pseudo random number directly, but to also analyze the history of pseudo randomness to aide in that effort.

Whether true randomness is a inhibition of the human perception or not, there is clear need to push the modern pseudo-random number closer to converging on perceived "true" randomness.

## **Questions/Aim:**
To train a neural net to predict PRNs from a chosen PRNGs output. We aim to train neural nets to predict values of assigned PRNGs and track attributes of each to make generalized conclusions about the development of PRNGs with respect to time and any PRN correlations we uncover.


## **Hypotheses:**
1) We predict there will be a positive trend over time on the cryptographic strength of each subsequent PRNG, given the nature of the increasing importance of stronger PRNGs.

2) We also predict that as we get into cryptographically stronger generation methods, our prediction success rates (even with learning) will be less effective.

3) We expect to uncover correlations in Pseudo-random numbers based on each individual generator, and aim to extract more generalized correlations between generators themselves.

## **Experimental Design:**



### **Seeding Method:**

We went with a seed generation method that allowed a way to introduce some level of semi-controlled "entropy" for the sake of simplicity, while still maintaining a baseline of integrity for most given PRNGs to exercise individual "potential."

The seed generation method we chose derives directly from Microsoft's [.NET system.datetime.ticks](https://docs.microsoft.com/en-us/dotnet/api/system.datetime.ticks?view=netframework-4.8) property. We chose to single out this method due to its documentation and unqiue simplicity, in addition to system time being widely used as a parameter for modern seed generation methods (more on reasoning at the bottom).

> A single tick represents one hundred nanoseconds or one ten-millionth of a second. There are 10,000 ticks in a millisecond, or 10 million ticks in a second. The value of this property represents the number of 100-nanosecond intervals that have elapsed since 12:00:00 midnight, January 1, 0001 in the Gregorian calendar.

**We found this implementation on StackOverflow that ported this method over to python for ease-of-use:**

[Python Implementation of .NET system.datetime.ticks](https://stackoverflow.com/questions/29366914/what-is-python-equivalent-of-cs-system-datetime-ticks)

As noted by the author . . .
   > * UTC times are assumed.
   > * The resolution of the datetime object is given by datetime.resolution, which is datetime.timedelta(0, 0, 1) or microsecond resolution (1e-06 seconds). C# Ticks are purported to be 1e-07 seconds.
   
**The reasoning behind our chosen method:**

This method will allow enough spread between occaisonally retreived ticks, where we can assume reasonable pseudo-unpredictabililty. This serves as a simplistic and constantly changing control mechanism for being able to seed PRNGs and test experimental outcomes. While not the most cryptographically strong, we needed a way to have some controlled aspect of seed generation to feed into generators of varying cryptographic complexity (to have some baseline of comparison).

**Here is a more trivial explanation that we found appropriate to include in summarization:**

[source](https://stackoverflow.com/users/33708/mehrdad-afshari)

> Normally, a (pseudo-)random number generator is a deterministic algorithm that given an initial number (called seed), generates a sequence of numbers that adequately satisfies statistical randomness tests. Since the algorithm is deterministic, the algorithm will always generate the exact same sequence of numbers if it's initialized with the same seed. That's why system time (something that changes all the time) is usually used as the seed for random number generators.


### **PRNG implementations:**
Pull notes from .py file and elaborate on how each PRNG plays into experimental design.

#### **Middle_Square**

<notes>
    
    A note on weakness: For a generator of n-digit numbers, the period can be no longer than 8n. If the middle n digits are all zeroes, 
    the generator then outputs zeroes forever. If the first half of a number in the sequence is zeroes, the subsequent
    numbers will be decreasing to zero. While these runs of zero are easy to detect, they occur too frequently for this
    method to be of practical use. The middle-squared method can also get stuck on a number other than zero.

    An already_seen list is NOT included in the original middle square method and will not be used.
</notes>


#### **Linear_Congruential**

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


#### **Lagged_Fibonacci**

<notes>
    
    This is two tap, not three tap...
    It's a "lagged" generator, because "j" and "k" lag behind the generated pseudorandom value. 
    Also, this is called a "two-tap" generator, in that you are using 2 values in the sequence 
    to generate the pseudorandom number. However, a two-tap generator has some problems with 
    randomness tests, such as the Birthday Spacings. Apparently, creating a "three-tap" generator
    addresses this problem.
</notes>


#### **Wichmann_Hill**

<notes>
    
    Consists of three linear congruential generators with different prime moduli, 
    each of which is used to produce a uniformly distributed number between 0 and 1.
    These are summed, modulo 1, to produce the result.

    This function is a direct derivative of the original AS 183 generator by Wichmann and Hill.
    
    Here is a great article... https://jamesmccaffrey.wordpress.com/2016/05/14/the-wichmann-hill-random-number-algorithm/
    
    Previous issue:
        seed1, seed2, seed3 should be random from 1 to 30,000? -> answer from Wichmann Hill Fortran Code 
        INTEGER ARITHMETIC UP TO 30323 IS REQUIRED
        ... so I am assuming it can be over 30,000.
</notes>


#### **Maximally_Periodic_Reciprocals** mneumonic="Sophie German Prime" 

<notes>
    
    Sophie Germain primes may be used in the generation of pseudo-random numbers.
    The decimal expansion of 1/q will produce a stream of q − 1 pseudo-random digits,
    if q is the safe prime of a Sophie Germain prime p, with p congruent to 3, 9, or 11 (mod 20).
    Thus "suitable" prime numbers q are 7, 23, 47, 59, 167, 179, etc. (OEIS: A000353) 
    (corresponding to p =  3, 11, 23, 29, 83, 89, etc.) (OEIS: A000355). 
    The result is a stream of length q − 1 digits (including leading zeros). 
    So, for example, using q = 23 generates the pseudo-random digits 0, 4, 3, 4, 7, 8, 2, 6, 0, 8, 6, 9, 5, 6, 5, 2, 1, 7, 3, 9, 1, 3.
    Note that these digits are not appropriate for cryptographic purposes, as the value of each can be derived from its predecessor in 
    the digit-stream. 
    
    This only works when you input a prime number that
    a. is a sophie prime.(if p is prime and 2*p + 1 is also a prime, p is a sophie prime)
    b. listlength >= safeprime
    
    --and--
    
    listlength > decprec
    
    Note that this will not accurately return the list length requested. It will return listlength - 2
    
    
    If p is a Sophie Germain prime greater than 3, then p must be congruent to 2 mod 3. 
    For, if not, it would be congruent to 1 mod 3 and 2p + 1 would be congruent to 3 mod 3,
    impossible for a prime number....
    ... We are taking a brute force approach and just checking if the alleged safe prime is indeed prime, instead of 
    checking modulo restrictions to short circuit the operation. This is less efficient, but it is OK for now to brute force it.
    
</notes>

### **Predictive Network Setup:**


### **Experiment Overview:**


### **Environment Setup:**


### **Trials:**