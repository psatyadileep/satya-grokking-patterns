

from typing import List


class Solution:
    def subsets(self, str) :
        response = []

        def subsets_helper(ind,curr):
            if ind >= len(str):
                response.append(curr)
                return

            ch = str[ind]
            subsets_helper(ind + 1,curr+ch)
            subsets_helper(ind + 1,curr)

        subsets_helper(0,"")
        return response


print(Solution().subsets("abc"))