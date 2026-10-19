class Solution:
    def findDuplicate(self, arr: List[int]) -> int:
        n = len(arr)
        for i in range(n): #? 0
            v=arr[i] % n
            if arr[v] >= n: return v
            else: arr[v] +=n