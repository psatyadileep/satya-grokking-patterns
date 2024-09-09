"""
https://leetcode.com/problems/next-greater-element-i/
LC496
Given an array, print the Next Greater Element (NGE) for every element.

The Next Greater Element for an element x is the first greater element on the right side of x in the array.

Elements for which no greater element exist, consider the next greater element as -1.


Examples
Example 1:

 Input: [4, 5, 2, 25]
 Output: [5, 25, 25, -1]
Example 1:

 Input: [13, 7, 6, 12]
 Output: [-1, 12, 12, -1]
Example 1:

 Input: [1, 2, 3, 4, 5]

 [-1,-1,-1,-1]


  Input: [4, 5, 2, 25]
 Output: [5, 25, 25, -1]
"""

class Solution:
    def nextLargerElement(self, arr):
        res = [-1]*len(arr)

        i =0
        while i<len(arr):
            for j in range(i+1, len(arr)):
                if arr[j]> arr[i]:
                    res[i]=arr[j]
                    break
            i+=1



        return res


    def nextLargerElement2(self, arr):
        res = [-]*len(arr)

        greater_value = -1
        for i in range(len(arr)-1,-1,-1):

            if i== len(arr)-1:
                if arr[i]> greater_value:
                    greater_value = arr[i]
                continue

            if greater_value>arr[i]:
                arr[i] = greater_value
            else:
                greater_value = arr[i]



        return res


print(Solution().nextLargerElement([1,2,3,4,5]))

print(Solution().nextLargerElement([1, 3, 5, 2, 4]
))


print(Solution().nextLargerElement2([1, 3, 5, 2, 4]
))