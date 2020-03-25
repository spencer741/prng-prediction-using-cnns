import sys
import random as rand
from random import seed
from random import randint
# seed random number generator
seedNum = sys.argv[1]
rang = sys.argv[2]
seed(int(seedNum))
# generate some integers
for _ in range(int(rang)):
	value = rand.randrange(int(rang))
	print(value, end='')
    
    
    
