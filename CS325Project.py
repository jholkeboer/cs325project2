import sys
sys.setrecursionlimit(10000)

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
# To make change for K cents:
#  If there is a K-cent coin, then that one coin is the minimum
#  Otherwise, for each value i < K,
#   Find the minimum number of coins needed to make i cents
#   Find the minimum number of coins needed to make K - i cents
#   Choose the i that minimizes this sum
# This algorithm can be viewed as divide-and-conquer, or as brute force.
# This solution is very recursive and runs in exponential time.
def changeslow(coins, value):
    def find_min(sub_coins, k):
        if k == 0:
            ret_coins = [0] * len(sub_coins)
            return [ret_coins, 0]
        elif k == 1:
            ret_coins = [0] * len(coins)
            ret_coins[0] = 1
            return [ret_coins, 1]            
        elif k in sub_coins:
            ret_coins = [0] * len(sub_coins)
            ret_coins[sub_coins.index(k)] = 1
            return [ret_coins, 1]
        else:
            min_combos = []
            for i in range(0, k):
                min1 = find_min(sub_coins, i)
                min2 = find_min(sub_coins, k - i)
                combined_min = [[], k]
                for j in range(0, len(sub_coins)):
                    combined_min[0][j] = min_1[0][j] + min_2[0][j]
                min_combos.append(combined_min)
            mins = [min_combos[c][1] for c in range(0, len(min_combos))]
            return min_combos[mins.indexof(min(mins))]

    # if value == 0:
    #     ret_coins = [0] * len(coins)
    #     return [ret_coins, 0]
    # elif value == 1:
    #     ret_coins = [0] * len(coins)
    #     ret_coins[0] = 1
    #     return [ret_coins, 1]
    # elif k in coins:
    #     ret_coins = [0] * len(coins)
    #     ret_coins[coins.index(k)] = 1
    #     return [ret_coins, 1]
    # else:
    #     # return [[1,2,3], 4]
    return find_min(coins, value)



#####################
# Greedy algorithm
#####################
# Use the largest value coin possible.
# Subtract the value of this coin from the amount of change to be made.
# Repeat.
def changegreedy(coins, value):
    return [[1,2,3], 4]


#####################
# Dynamic Programming
#####################
def changedp(coins, value):

    min_coins = [0] * value
    coin_vals = [[0]* len(coins) for i in range(value)]
    
    for x in range(0,value):
        
        money = x + 1
        if money < coins[0]:
            pass
        
        elif money in coins:
            min_coins[x] = 1
            coin_vals[x][coins.index(money)] = 1
            
        else:
            coin_test = []
            coin_val_test = []
            for y in coins:
                if y > money:
                    break
                else:
                    coin_test.append(min_coins[x - y])
                    coin_val_test.append(coin_vals[x - y])
                    
            min_val = min(coin_test)
            min_ind = coin_test.index(min_val)
            min_coins[x] = min(coin_test) + 1
            coin_vals[x]= coin_val_test[min_ind][::]
            coin_vals[x][min_ind] = coin_val_test[min_ind][min_ind] + 1
            
    return [ coin_vals[value-1], min_coins[value-1] ]



# execution
if len(sys.argv) > 1:
    inputfile = sys.argv[1]
    outputfile = inputfile.split('.')[0] + "change.txt"

    coins = get_coins(inputfile)

    # let user choose algorithm
    alg = input("Choose an algorithm.\n1. Brute Force\n2. Greedy\n3. Dynamic Programming\nEnter your choice: ")
    results = []
    
    if int(alg) == 1:
        print "\nExecuting Brute Force Algorithm..."
        for c in coins:
            results.append(changeslow(c[1], c[0]))
        print "Writing results to " + outputfile + "..."
        # write_output(outputfile, results)
        print results
        print "Done."
    
    elif int(alg) == 2:
        print "\nExecuting Greedy Algorithm..."
        for c in coins:
            results.append(changegreedy(c[1], c[0]))
        print "Writing results to " + outputfile + "..."
        write_output(outputfile, results)
        print "Done."
    
    elif int(alg) == 3:
        print "\nExecuting Dynamic Programming Algorithm..."
        for c in coins:
            results.append(changedp(c[1], c[0]))
        print "Writing Results to " + outputfile + "..."
        write_output(outputfile, results)
        print "Done."
    
    else:
        "Not a valid choice.\n"

else:
    print "Usage: python CS325Project2.py [filename.txt].\n"

