class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False

        divisors = [1]
        i = 2
        while i * i <= num:
            if num % i == 0:
                divisors.append(i)
                if i != num // i:
                    divisors.append(num // i)
            i += 1

        return sum(divisors) == num