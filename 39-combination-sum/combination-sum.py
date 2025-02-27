class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i,arr,total):
            if total == target:
                res.append(arr.copy())
                return
            if i>=len(candidates) or total > target:
                return
            
            arr.append(candidates[i])
            backtrack(i,arr,total + candidates[i])
            arr.pop()
            backtrack(i+1,arr,total)
                
        backtrack(0,[],0)
        return res