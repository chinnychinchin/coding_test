# The problem statement
# 
# Time Limit: 15min + 45min
# 
# We were working with rhyme schemes. To tell if the
# two words rhyme, we have to compare their rhyme-
# patterns. like 
# We need your help to write a program that can find
# out the rhyme-pattern of any word.
# 
# Vowel
# A vowel is any of: `a`, `e`, `i`, `o`, `u` or `y`.
# NOTE: we consider `​y`​ as a vowel too, as long as
# it is not at the start or end of a word. So, as an
# example, the `y`​ in `rhythm`​ is considered a vowel
# 
# ​Rhyme-pattern​
# A ​rhyme-pattern​ is a substring of a word such that:
#   1. The word ends with that substring.
#   2. The first letter of the substring is always a
#       vowel.
#   3. The substring contains exactly one contiguous
#       string of vowel(s).
#   4. The substring must either be the whole word,
#       or the letter immediately preceding the
#       start of the substring must be a non-vowel.
# 
# For example,
#  the rhyme-pattern​ of `star` would be `ar`,
#  the rhyme-pattern​ of `rainbow` would be `ow`,
#  the rhyme-pattern​ of `noise` would be`e`, 
#  the rhyme-pattern​ of `sunny` would be `unny`,
#  the rhyme-pattern​ of `s​pying​` would be `​ying​`, 
#  and the rhyme-pattern​ of `​all​` would be `​all​`.
# 
# Input will:
#  1. always be in lower case
#  2. always have vowels
#  3. have no other character than [a-z]
# 
# Task: you need to implement the function
# `getRhymePattern` below to return the rhyme-pattern
# as described.
# 
# [Bonus marks for good commenting, brevity, and modularity]

# -------

import json


# find all possible substrings
# write a function that determines if an alphabet is a vowel
# write a function to check if a word ends with a certain substring
# condition 3: write a function to detemine if a substring only one continuous string of vowels
# cond 4: write a function to determine if a substring  is a whole word of if the letter preceding the substring is a non-vowel


def isVowel(letter, word):

    if letter in ['a','e','i','o','u']:
        return True
    elif letter == 'y' and (letter != word[0] and letter != word[-1]):
        return True
    
    return False

def wordEndsWithSb(sb,word):
    # find index of sb in the word
    # index of sb in word + length of substring has to be equal length of word
    index_of_sb = word.find(sb)

    if word[-1] == sb:
        return True

    elif index_of_sb + len(sb) == len(word):
        return True

    return False


def checkCond3(sb):
    
    indexes_of_vowels = []
    for i in range(len(sb)):
        if isVowel(sb[i],sb):
            indexes_of_vowels.append(i)
    
    def checkConsecutive(l):
        return sorted(l) == list(range(min(l), max(l)+1))
    

    return checkConsecutive(indexes_of_vowels)


def checkCond4(sb,word):
    if sb == word:
        return True
    index_of_sb = word.find(sb)
    if index_of_sb == 0:
        return True
    if not isVowel(word[index_of_sb-1],word):
        return True
    
    return False

def getAllSubstrings(s):
    from itertools import combinations
  
    # initializing string 
    test_str = s

    # Get all substrings of string
    # Using itertools.combinations()
    res = [test_str[x:y] for x, y in combinations(
                range(len(test_str) + 1), r = 2)]
    
    return res

def getRhymePattern(word):

    allSubstrings = getAllSubstrings(word)
    rhyme_ptt = ''
    for sb in allSubstrings:

        if wordEndsWithSb(sb,word) and isVowel(sb[0],word) and checkCond3(sb) and checkCond4(sb,word):
            rhyme_ptt = sb 
            break

    return rhyme_ptt

# -------

print(checkCond4('a','alpha'))