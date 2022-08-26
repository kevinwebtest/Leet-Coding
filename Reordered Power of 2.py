class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        n_str = sorted(str(n))
        powerOf2 = [sorted(str(1 << i)) for i in range(33)]
        return n_str in powerOf2
