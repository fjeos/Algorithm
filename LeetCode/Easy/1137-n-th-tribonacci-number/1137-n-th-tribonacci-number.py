class Solution:
    def tribonacci(self, n: int) -> int:
        arr = [1] * (n+1)
        arr[0] = 0
        
        for i in range(3, n+1):
            arr[i] = arr[i-1] + arr[i-2] + arr[i-3]

        return arr[n]
