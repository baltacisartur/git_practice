import random


def func(num: int):
    seen = {}
    numbers = list(random.randint(1, 10) for _ in range(num))
    for i in numbers:
        if i not in seen:
            seen[i] = 1
        else:
            seen[i] += 1
    
    return [key for key, value in seen.items() if value > 1], numbers

s = 10
print(func(s))
print("hello")
