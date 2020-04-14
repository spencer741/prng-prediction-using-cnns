'''
Normally, a (pseudo-)random number generator is a deterministic algorithm that given an initial number (called seed), generates a sequence of numbers that adequately satisfies statistical randomness tests. Since the algorithm is deterministic, the algorithm will always generate the exact same sequence of numbers if it's initialized with the same seed. That's why system time (something that changes all the time) is usually used as the seed for random number generators.

The seed for each PRNG will be the result of this.


A single tick represents one hundred nanoseconds or one ten-millionth of a second. There are 10,000 ticks in a millisecond, or 10 million ticks in a second. This will allow enough spread between occaisonally retreived ticks, where we can assume reasonable pseudo-unpredictabililty. This serves as a simplistic and constantly changing control mechanism for being able to seed PRNGs and test experimental outcomes. While not the most cryptographically strong, we needed a way to have some controlled aspect of seed generation to feed into generators of varying cryptographic complexity (to have some baseline of comparison).

'''

from datetime import *

def ticks(t):
    return int( str( int( (datetime.utcnow() - datetime(1, 1, 1)).total_seconds() * 10000000 ))[-6:])
    #return (datetime.utcnow() - datetime(1970, 1, 1)).total_seconds()


def ticks_LF(t):
    return  int(str( int( (datetime.utcnow() - datetime(1, 1, 1)).total_seconds() * 10000000 ))[-10:])
    



