'''
Tutorial Video:
https://youtu.be/m2Elp9ubY3w

Description:
Return most effective change with user decided coin values
'''

# Function to create the matrix we'll use for the optimization
def _change_matrix(coin_set, change_amount):
    matrix = [[0 for m in range(change_amount + 1)] for m in range(len(coin_set) + 1)]
    for i in range(change_amount + 1):
        matrix[0][i] = i
    return matrix

# Function we'll use to optimize the default above matrix
def change_making(coins, change):
    matrix = _change_matrix(coins, change)
    for c in range(1, len(coins) + 1):
        for r in range(1, change + 1):

            if coins[c-1] == r:
                matrix[c][r] = 1

            elif coins[c-1] > r:
                matrix[c][r] = matrix[c-1][r]

            else:
                matrix[c][r] = min(matrix[c - 1][r], 1 + matrix[c][r - coins[c - 1]])

    return matrix[-1][-1]


print(change_making([1,10,25], 86)) # List contains arbitrary coins
# The second value contains the sum you're trying to get to
