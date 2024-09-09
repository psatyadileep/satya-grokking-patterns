from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # Count the frequency of each letter in the tiles
        letter_counts = Counter(tiles)
        print(f"Letter Counts: {letter_counts}")

        # Call the backtrack method to count the number of valid sequences
        return self.backtrack(letter_counts)

    def backtrack(self, letter_counts):
        count = 0
        for letter, freq in letter_counts.items():
            # Check if the current letter has a frequency greater than 0
            if freq > 0:
                count += 1  # Count the current letter as a separate sequence
                letter_counts[letter] -= 1  # Use the current letter by decreasing its frequency

                # Recursively explore further with the remaining letters
                count += self.backtrack(letter_counts)

                letter_counts[letter] += 1  # Revert the letter count for backtracking

        return count