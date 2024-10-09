string = 'salam my name is mohammadreza'
counter = dict()

for letter in string:
    if letter in counter:
        counter[letter] += 1
    else:
        counter[letter] = 1
    

for this_one in list(counter.keys()):
    print('%s appeared %s times'%(this_one,counter[this_one]))
    