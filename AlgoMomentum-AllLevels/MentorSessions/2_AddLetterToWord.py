'''
Given a dictionary (represented by an array of string) and a word, return an array containing all words that can be created by adding one letter to the word.


EXAMPLE(S)
dictionary: `["CAT", "CART", "ACTS", "BAT"]`
word: "CAT"
would return `["ACTS", "CART"]`

because these words can be formed with the letters "C", "A", "T", and exactly one more letter.

- - - -


Assumptions:
- everything's UPPERCASE
- only English letter alphabet
- min length of dictionary is 1
- guaranteed to have word
- ordering of the output doesn't matter


- - - - -

CART -> ACRT --> CART
        ACT

Approach


dictionary: `["CAT", "CART", "ACTS", "BAT"]`
word: "CAT"

Brute Force:
-> iterate through words in the disctionary
    -> check if letters of the word contains all the leters in the target word
    -
    -> check count is plus1

N = Num of words
M = Size of biggest word

Sorting
Time: N * M Log M + N * M-> O(N * M Log M)
Space: O(N * M)

Counting
create output array
map word into key: char, value: count of char
["CAT", "CART", "ACTS", "BAT"]`
{
    C: 1,
    A: 1,
    T: 1,
}

{
    A: 1,
    C: 1,
    T: 1,
    S: 1,
}
Loop through dictionary strings if length of the string is equal to length word + 1


-----
C :2
T: 1

C: 3
T: 1

CCT
CCCT
{

}
N = Num of words
M = Size of biggest word variable + 1
V = size of word variable

["CART", "ACTS", "BAT"]`
Time: O(M*N)
Space:O(N^2)
- map for word O(V)
- map for biggest DictionaryWord O(m)


'''
from collections import counter
def possible_words(dictionary, word):

    word_count = counter(word)
    response = []


    for dictword in dictionary:

        if len(dictword)==len(word)+1
            dict_word_counter = counter(word)

            for key in  word_count.keys():

                if key not in dict_word_counter and :
                    continue

                else:
                    not dict_word_counter[key]>= word_count

            response.append(dictword)







    print("hi")

26 letters

 let primes = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
    73, 79, 83, 89, 97, 101,
  ];


#   https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/



function possibleWords(dictionary, word) {
  if (dictionary.length === 0) return [];
  const result = [];

  let totalPrimeToDictionaryWord = new Map();
  // max value primes -> original dictionary word
  let primes = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
    73, 79, 83, 89, 97, 101,
  ];

  for (let w of dictionary) {
    let tempProduct = 1;

    for (let char of w) {
      tempProduct *= primes[char.charCodeAt(0) - "A".charCodeAt(0)];
    }

    totalPrimeToDictionaryWord.set(tempProduct, w);
  }

  // iterate through all 26
  // 65 - 90 => A -Z --> String.fromCharCode(65)
  let totalPrimeValWord = 1;
  let tempPrimeValWord = 1;
  for (let char of word) {
    totalPrimeValWord *= primes[char.charCodeAt(0) - "A".charCodeAt(0)];
  }

  tempPrimeValWord = totalPrimeValWord;

  for (let i = 1; i <= primes.length; i++) {
    tempPrimeValWord *= primes[i - 1];
    if (totalPrimeToDictionaryWord.has(tempPrimeValWord)) {
      result.push(totalPrimeToDictionaryWord.get(tempPrimeValWord));
    }
    tempPrimeValWord = totalPrimeValWord;
  }

  return result
}










dictionary = ["CAT", "CART", "ACTS", "BAT"]
word = "CAT"
print(possible_words(["ACTS", "CART"], word))

dictionary = ["CAATT", "TAACT", "ACTS", "TAACTT"]
word = "CAAT"
print(possible_words(["CAATT", "TAACT"], word))

dictionary = ["CART", "CAT", "CART"]
word = "CAT"
print(possible_words(["CART", "CART"], word))
