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


def sum_two(nums: list, target: int) -> list:
    seen = {}
    for i, num in enumerate(nums):
        compliment = target - num
        if compliment in seen:
            return seen[compliment], i
        seen[num] = i

    return []


s = 10
print(func(s))
print("hello")


# _________________________________________________

def if_palindrome(tmp: list) -> bool:
    return tmp.lower() == tmp.lower()[::-1]
