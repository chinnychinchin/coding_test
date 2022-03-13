#### Given two strings, determine if they share a common substring. A substring may be as small as one character.

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


#### get a list of all possible substrings of a string

def getAllSubstrings(s):
    from itertools import combinations
  
    # initializing string 
    test_str = s

    # Get all substrings of string
    # Using itertools.combinations()
    res = [test_str[x:y] for x, y in combinations(
                range(len(test_str) + 1), r = 2)]
    
    return res


#### check if 2 strings are anagrams of each other

def checkIfAnagram(s1,s2):
    # the sorted strings are checked
    are_Anagrams = False
    if(sorted(s1)== sorted(s2)):
        are_Anagrams = True
    return are_Anagrams
        


#### Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string. 
# Given a string, find the number of pairs of substrings of the string that are anagrams of each other.

# Brute force way
def sherlockAndAnagrams(s):
    # Write your code here

    # Step 1: find all possible substrings 
    allSubstrings = getAllSubstrings(s)
    # Step 2: write a method that accepts 2 substrings and check if they are anagrams 
    counter = 0 
    for i in range(len(allSubstrings)-1):
        j = 1 + i
        for k in range(j, len(allSubstrings)):
            if len(allSubstrings[i]) == len(allSubstrings[k]) and checkIfAnagram(allSubstrings[i], allSubstrings[k]):
                counter+=1

    # Step 3: Count the number of pairs 
    return counter


# Optimized
def sherlockAndAnagrams(s):
    # find all substrings, sort and to dictionary 
    allSubstrings = getAllSubstrings(s)
    count = 0
    dic = {}
    for i in range(len(allSubstrings)):
        ss = "".join(sorted(allSubstrings[i]))
        try:
            existing_count = dic[ss]
        except:
            existing_count = 0
        dic.update({ss: existing_count+1})
    
    for k,v in dic.items():
        count = count + v*(v-1)/2 # single forward slash returns float. To return int, either enclose count in int() or use double forward slash
        
    return int(count) 
