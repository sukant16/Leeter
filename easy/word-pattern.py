# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str
#
# Example 1:
#
# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true


class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:

        pat_list = list(pattern)
        word_list = str.split()

        if len(pat_list) != len(word_list):
            return False

        else:
            len_uni_letters = len(set(pat_list))
            len_uni_word = len(set(word_list))
            # get unique mapping between words and letters and check whether it is of same length as that of
            # unique letters and unique words
            if len(set(zip(pat_list, word_list))) == len_uni_letters == len_uni_word:
                return True
            else:
                return False
