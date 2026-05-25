import json
import random
from uuid import uuid4


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


def new_func(name: str, count: str):
    test = {}
    try:
        with open("info.json", "r", encoding="utf-8") as file:
            info = json.load(file)
        
        if info == test:
            raise ValueError("Файд пустой")
        else:
            print("Файл прочитан")
        
    except (FileNotFoundError, json.JSONDecodeError):
        info = {}
    
    info[name] = count

    with open("info.json", "w", encoding="utf-8") as file:
        json.dump(info, file, ensure_ascii=False, indent=2)
        print(f"файл загружен")


s = 10
print(func(s))
print("hello")


# _________________________________________________

def if_palindrome(tmp: list) -> bool:
    return tmp.lower() == tmp.lower()[::-1]

#___________________________________________________

name = "Barsik"
count = str(uuid4())[0:8]

if __name__ == "__main__":
    print(new_func(name, count))