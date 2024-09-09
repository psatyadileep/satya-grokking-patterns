def next_smaller_to_right(arr):
    stack = []
    result = [-1] * len(arr)  # Initialize result array with -1

    for i in range(len(arr)):
        while stack and arr[stack[-1]] > arr[i]:

            result[stack.pop()] = arr[i]
        stack.append(i)
        print(stack, result)
    return result

# Example usage:
arr = [3, 1, 4, 2, 5]
result = next_smaller_to_right(arr)
print("Array:", arr)
print("Next smaller element to the right:", result)
