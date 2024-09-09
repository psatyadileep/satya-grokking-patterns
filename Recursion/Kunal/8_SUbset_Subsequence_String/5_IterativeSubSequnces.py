def find_subsequences(arr):
    subsequences = [[]]  # Start with an empty subsequence

    # Iterate through each element in the array
    for num in arr:
        # Store the current length of subsequences
        current_length = len(subsequences)

        # Create new subsequences by adding the current element to existing ones
        print(current_length)
        for i in range(current_length):
            print("*************************************")

            new_subsequence = list(subsequences[i])  # Create a new copy of subsequence
            print(f"Before Appending :{new_subsequence}")
            new_subsequence.append(num)  # Add the current element
            print(f"After Appening:{new_subsequence}")
            subsequences.append(new_subsequence)  # Add the new subsequence
            print(f"Final Result AFter Iteration:{subsequences}")
            print("*************************************")


    return subsequences

# Example usage
input_array = [1, 2, 3]
find_subsequences(input_array)

