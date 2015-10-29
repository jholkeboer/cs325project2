# Jack Holkeboer
# Michael Loo
# Susan Eldridge
# CS324 Project Group 4



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
# [(4, [1, 1, 1, 1]), (4, [0, 1, 2, 1]), (3, [0, 0, 1, 2])]
def write2(outputfile, results):
    with open(outputfile, 'w+') as f:
        for result in results:
            line1 = '['
            for i in range(0, len(result[1])):
                if i <= len(result[1]) - 2:
                    line1 += str(result[1][i]) + ', '
                elif i == len(result[1]) - 1:
                    line1 += str(result[1][i]) + ']\n'
            f.write(line1)
            f.write(str(result[0]) + '\n')            
    
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

def changeslow(coin_arr, value):
    coin_index = [0]*len(coin_arr)
    
    min_coins = value
    
    if value in coin_arr:
        coin_index[coin_arr.index(value)] = 1
        return 1, coin_index
    else:
        for coin in coin_arr: 
            if coin > value:
                pass
            else:
                i_coins, i_coins_index = changeslow(coin_arr, coin)
                k_coins, k_coins_index = changeslow(coin_arr, value-coin)
                
                sum_two = i_coins + k_coins
            if sum_two < min_coins:
                min_coins = sum_two
                coin_index = [sum(x) for x in zip(i_coins_index, k_coins_index)]

    return min_coins, coin_index


#####################
# Greedy algorithm
#####################
# Use the largest value coin possible.
# Subtract the value of this coin from the amount of change to be made.
# Repeat.
def changegreedy(coins, value):
    change_sum = 0

    # coin_counts holds the number of each denomination of coins used 
    coin_counts = [0] * len(coins)
    
    # sort coins with largest coin first
    sorted_coins = sorted(coins, reverse = True)

    # keep adding largest coin to sum until it's bigger than value,
    # then move on to the next largest coin, and repeat
    while change_sum < value:
        for c in sorted_coins:
            # move on when the next coin puts us over the limit
            while change_sum + c <= value:
                change_sum += c
                coin_counts[coins.index(c)] += 1

    return [ coin_counts, sum(coin_counts) ]

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


#####################
# Execution
#####################
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
        write2(outputfile, results)
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

