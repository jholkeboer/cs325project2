import sys

def get_coins(inputfile):

    coins = []
    with open(inputfile) as f:
        while True:
            line1 = f.readline().strip().strip(']').strip('[').replace(' ','').split(',')
            line2 = f.readline().strip()
            line1arr = [int(x) for x in line1 if x != '']
            if not line2:
                break
            coins.append([int(line2), line1arr])

    return coins

def write_output(outputfile, results):
    with open(outputfile, 'w+') as f:
        for result in results:
            line1 = '['
            for i in range(0, len(result[0])):
                if i <= len(result[0]) - 2:
                    line1 += str(result[0][i]) + ', '
                elif i == len(result[0]) - 1:
                    line1 += str(result[0][i]) + ']\n'
            f.write(line1)
            f.write(str(result[1]) + '\n')

        f.close


#####################
# Divide and Conquer
#####################
def changeslow():
    return [[[1,2,3],4]]
# To make change for A cents:
#  If there is a K-cent coin, then that one coin is the minimum
#  Otherwise, for each value i < K,
#   Find the minimum number of coins needed to make i cents
#   Find the minimum number of coins needed to make K - i cents
#   Choose the i that minimizes this sum
# This algorithm can be viewed as divide-and-conquer, or as brute force.
# This solution is very recursive and runs in exponential time.

# def changeslow(coinarr, value, coins, amt, i):
#
#     if value == coinarr[i]:
#         return coins[i] + 1, amt + 1
#     else:
#
#
#
#
#     for x in xrange(len(coins)):
#


#####################
# Greedy algorithm
#####################
# Use the largest value coin possible.
# Subtract the value of this coin from the amount of change to be made.
# Repeat.
def changegreedy():
    return [[[1,2,3],4]]


#####################
# Dynamic Programming
#####################
def changedp():
    return [[[1,2,3],4]]



# execution
if len(sys.argv) > 1:
    inputfile = sys.argv[1]
    outputfile = inputfile.split('.')[0] + "change.txt"

    coins = get_coins(inputfile)
    print coins


    # let user choose algorithm
    alg = input("Choose an algorithm.\n1. Brute Force\n2. Greedy\n3. Dynamic Programming\n")
    results = []
    if int(alg) == 1:
        print "\nExecuting Brute Force Algorithm...\n"
        results = changeslow()
        write_output(outputfile, results)
    elif int(alg) == 2:
        print "\nExecuting Greedy Algorithm...\n"
        results = changegreedy()
        write_output(outputfile, results)
    elif int(alg) == 3:
        print "\nExecuting Dynamic Programming Algorithm...\n"
        results = changedp()
        write_output(outputfile, results)    
    else:
        "Not a valid choice.\n"
    


else:
    print "Usage: python CS325Project2.py [filename.txt].\n"
