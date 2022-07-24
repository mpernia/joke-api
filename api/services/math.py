import math
from typing import List


class Maths:
    @staticmethod
    def lcm(numbers: List[int]):
        number = numbers[0]
        for i in range(1, len(numbers)):
            number = number * numbers[i] // math.gcd(number, numbers[i])
        return number

    @staticmethod
    def inc(number: int):
        return number + 1
