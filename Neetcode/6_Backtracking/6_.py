from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        response = []

        candidates.sort()
        def helper(index, combo, remaining):  # Changed 'target' to 'remaining'
            print(f"index: {index}, combo: {combo}, remaining: {remaining}, response: {response}")

            if remaining == 0:
                response.append(combo[:])
                return

            if index >= len(candidates) or candidates[index] > remaining:
                return

            if remaining > 0:
                combo.append(candidates[index])
                helper(index + 1, combo, remaining - candidates[index])
                combo.pop()

            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            helper(index + 1, combo, remaining)

        helper(0, [], target)
        return response

result = Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], target=8)
print(result)
