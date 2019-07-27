import time
import functools
import operator
import random
import math

print('Number Time quiz!')
time.sleep(2)
print('Answer the multiplcation problems before time runs out!')
time.sleep(3)
print('Ready? Go!')
start_time = time.time()

score = 0

# Game Logic

while True:
    difficulty_setting = 2
    difficulty_progression = math.floor(score/10)
    overall_difficulty = difficulty_setting + difficulty_progression

    numbers_list = []
    for x in range(overall_difficulty):
        value = random.randint(1,9)
        numbers_list.append(value)

    answer = functools.reduce(operator.mul, numbers_list, 1)
    print('Multiple these numbers', numbers_list)

    guess = int(input())

    if guess == answer:
        score = score + (1 * overall_difficulty)
        continue

    else:
        print('Game over! The answer was', answer)
        elapsed_time = time.time() - start_time
        print('Your score was', score, 'In only', elapsed_time)
        break
