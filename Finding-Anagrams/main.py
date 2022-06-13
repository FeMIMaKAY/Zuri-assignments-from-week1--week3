# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


from xmlrpc.client import boolean


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = input("Enter the first word: ")
    anagram = input("Enter the second word:")

    str1 = word.lower()
    str2 = anagram.lower()

    if len(str1) == len(str2):
        sort_str1 = sorted(str1)
        sort_str2 = sorted(str2)

    if sort_str1 == sort_str2:

        return True

    else:
        return False


print(find_anagram('space', 'paces'))
