import sys
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

            
'''Other Attempted implementation code

def Middle_Square(seed, listlength):
    print("Middle_Square")
    
    #Create a list of length listlength
    numlist = []
    
    
    #seed_number = int(input("Please enter a four digit number:\n[####] "))
    #number = seed_number
    
    
    for i in range(listlength):
        #list that is one number, broken up into digits, since we are generating a digit at a time. the length is based on the seed.
        tempnumlist = []
        #initializers for inner looping to work
        already_seen = set()
        counter = 0
        count = 0
        number = 0
        while number not in already_seen:
            counter += 1
            already_seen.add(number)
            number = int(str(seed * seed).zfill(8)[2:6])  # zfill adds padding of zeroes
            while (number > 0):
                number = number//10
                count = count + 1
                #print (count)
                #print (number)
                if (count % 10 != 0):
                    tempnumlist.append(number)
                    #print(f"{number}", end = '')
                elif (count % 10 == 0):
                    tempnumlist.append(number)
                    #print(f"{number}")
        numlist.append(int(''.join(map(str,tempnumlist)))) #add tempnumlist to numlist as one number.
        
    print("numlist", numlist)
      
        
def midsquare(seed, listlength):
    seed_number = int(seed)
    number = seed_number
    already_seen = set()
    counter = 0

    while number not in already_seen:
        counter += 1
        already_seen.add(number)
        number = int(str(number * number).zfill(8)[2:6])  # zfill adds padding of zeroes
        print(f"#{counter}: {number}")

    print(f"We began with {seed_number}, and"
          f" have repeated ourselves after {counter} steps"
          f" with {number}.")



'''
