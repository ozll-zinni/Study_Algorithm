class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        n -= 1
        rounds = k // n
        holder = k % n

        return holder if rounds % 2 == 0 else n - holder
