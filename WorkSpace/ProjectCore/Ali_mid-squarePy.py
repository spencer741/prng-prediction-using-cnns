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

