maxNum =  0
maxLength = 0
storage = {}


def getLength(n):
    length = 0
    test = n

    while test > 1:
        if test%2==0:
            if test in storage:
                return storage[test] + length
            else:
                test=test/2
                length+=1
        else:
            if test in storage:
                return storage[test] + length
            else:
                test=3*test+1
                length+=1
    return length

for num in range(1000000):
    length = getLength(num)
    if length > maxLength:
        maxNum = num
        maxLength = length
print("{}: {}".format(biggestNum,max))
