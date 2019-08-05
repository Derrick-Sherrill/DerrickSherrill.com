# greedy method
def num_coins(cents):
    coins = [25, 10, 5, 1]
    count = 0
    for coin in coins:
        while cents >= coin:
            cents = cents - coin
            count = count + 1

    return count

print(num_coins(32))
