def getAllSubstrings(s):
    from itertools import combinations
  
    # initializing string 
    test_str = s

    # Get all substrings of string
    # Using itertools.combinations()
    res = [test_str[x:y] for x, y in combinations(
                range(len(test_str) + 1), r = 2)]
    
    return res


def checkIfIsVowel(letter, word):
    
    isVowel = False
    list_of_vowels = ['a','e','i','o','u']
    if letter in list_of_vowels:
        isVowel = True

    elif letter == 'y':

        if not word[0] == 'y' and not word[-1] == 'y':
            isVowel = True
        
    return isVowel

def getRhymePattern(word):

    
    # Step 1 write a function to determine if 'y' is considered a vowel 
    

    
    # Step 2: find all possible substrings of a given word 
    all_possible_substrings = getAllSubstrings(word)

    # Step 3: loop through all substrings and return the substring that meet the following conditions: 
        # 1. The word ends with that substring.

    
    rhyme_pattern = 'test1'
    for s in all_possible_substrings:

        # get the last N characters of the word to check if it is == substring
        N = len(s)
        if not word[-1*N:] == s:
            # print('condition 1 failed')
            continue
        else: 
            pass

        #   2. The first letter of the substring is always a
        #       vowel.
        if checkIfIsVowel(s[0],word):
            pass
        else: 
            # print('condition 1 failed')
            continue

        #   3. The substring contains exactly one continuous
        #       string of vowel(s).

        # check if there is a non-vowel in the substring and if so, check if the non-vowel is between 2 vowels
        pass_cond_3 = True
        non_vowel = 0
        for i in range(len(s)):
            
            if not checkIfIsVowel(s[i],s):
                if i - non_vowel <= 1:
                    non_vowel = non_vowel + 1
                else:
                    pass_cond_3 = False
        
        if non_vowel > 0:
            if non_vowel < len(s)-1:
                pass_cond_3 = False
        

        if not pass_cond_3:

            continue
        print("pass cond 3")
        #   4. The substring must either be the whole word,
        #       or the letter immediately preceding the
        #       start of the substring must be a non-vowel. 
        
        # find first index of substring in the word
        first_index = word.find(s)
        print(s)
        print(first_index)
        letter_preceding = word[first_index - 1]

        if s == word or first_index - 1 < 0:
            pass

        else: 
            # check if letter preceding is not vowel
            print('check if vowe;')
            if checkIfIsVowel(letter_preceding,word): 
                print(letter_preceding)
                continue
            else: 
                pass
        
        rhyme_pattern = s
        
        

    # print(all_possible_substrings)
    return rhyme_pattern


# print(getRhymePattern('height'))


print('a','a')


