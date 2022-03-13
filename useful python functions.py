def twoStrings(s1, s2):
    # Write your code here
    
    # Step 1: make s1 and s2 into sets of characters
    s1_set = set(s1)
    s2_set = set(s2)


    flag = 'NO'

    # Step 2: loop through each character in s1_set and find if there is a same character in s2_set
    for character in s1_set:
        if character in s2_set:
            flag = 'YES'
            break
    
    return flag


def sherlockAndAnagrams(s):
    # Write your code here

    # Step 1: find all possible substrings 
    
    # Step 2: write a method that accepts 2 substrings and check if they are anagrams 
    # Step 3: Count the number of pairs 
