import collections
import itertools

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



def rotLeft(a, d):
    # Write your code here
    d = d%len(a)
    l1 = a[0:d]
    l2 = a[d:len(a)]
    return l2+l1


def sockMerchant(n, ar):
    # Write your code here
    num_of_socks_by_color = collections.Counter(ar)
    num_of_pairs = 0
    for ele in num_of_socks_by_color:
        num_of_pairs = num_of_pairs + num_of_socks_by_color[ele]//2
    return num_of_pairs


def repeatedString(s, n):
    # Write your code here

    # Case 1: count the number of 'a's in substring s[0:n]
    if n <= len(s):
        my_counter = collections.Counter(s[0:n])
        num_of_a = my_counter['a']
        return num_of_a

    # Case 2
    else:
        # find how many multiples is n of length of s
        multiples = n//len(s)

        # find remainder of n divided by length of s
        remainder = n%len(s)

        # count the  number of 'a's in string s and multiply by multiples
        # add to total count
        my_counter = collections.Counter(s)
        num_of_a = my_counter['a'] * multiples
        
        # count the number of 'a's in substring s[0:remainder]
        # add to total count 
        my_counter_2 = collections.Counter(s[0:remainder])
        num_of_a += my_counter_2['a']
        
        return num_of_a



def charToRemove(distinct_chars):    # returns a list of lists

        char_to_remain = []
        for i in range(len(distinct_chars)):
            k = i
            while k < len(distinct_chars) -1:
                char_to_remain.append([distinct_chars[i],distinct_chars[k+1]])
                k+=1

        char_to_remove = []
        
        for i in range(len(char_to_remain)):
            l3 = [x for x in distinct_chars if x not in char_to_remain[i]]
            char_to_remove.append(l3)

        return char_to_remove

def isTwoAlter(s):
 
    # Check if ith character matches
    # with the character at index (i + 2)
    for i in range ( len( s) - 2) :
        if (s[i] != s[i + 2]) :
            return False
         
     
 
    #If string consists of a single
    #character repeating itself
    if (s[0] == s[1]):
        return False
 
    return True

def alternate(s):
    # Write your code here
    if len(s) == 1:
        return 0
   

    # Step 1: determine the distinct characters present
    distinct_chars = list(set(s))
    
    # simple cases where there are no distinct characters and when the string has only 2 distinct characters
    if len(distinct_chars) < 2:
        return 0
    elif len(distinct_chars) == 2 and len(s) == 2:
        return 2


    # Step 2: determine the choices for characters to leave
    # Step 3: for each pair of characters to leave behind, determine the characters to remove\
    # see chars to remove function above
    

    # Step 3i: remove all instances of the characters determined in step 3 - call it 'sb'
    list_chars_to_remove = charToRemove(distinct_chars)
    possible_sb = {}
    for i in list_chars_to_remove:
        sb = s
        for k in range(len(i)):
            sb = sb.replace(i[k],"")

        # Step 3ii: determine the validity of 'sb' after step 4 - has to have only 2 distinct characters that are alternating
        # Step 3iii: find the length of the 'sb'
        #  write a function to determine if a string has alternative characters
        if isTwoAlter(sb):
            possible_sb.update({sb:len(sb)})
    
    if len(possible_sb): # take care of the case where there are no sb with alternating characters
        # Step 4: of all the characters to leave behind, find the max(sb)
        new_maximum_val = max(possible_sb.keys(), key=(lambda new_k: possible_sb[new_k]))

        return possible_sb[new_maximum_val]
    
    else: 
        return 0
    


def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def superReducedString(s):
    # Write your code here
    if len(s) == 1:
        return s

    new_string = s
    while len(new_string):
        #  get list of possible pairwise
        list_of_pairwise = list(pairwise(new_string))
      
        i = 0
        pair_to_remove = ''
        while i < len(list_of_pairwise):
            
            
            if list_of_pairwise[i][0] != list_of_pairwise[i][1]:
                i += 1
        
            
            else: 
                pair_to_remove = list_of_pairwise[i][0]+list_of_pairwise[i][1]
                break
        
        
        # code to remove pairs
        
        # find index of substring within the string
        if pair_to_remove:
            start_index = new_string.find(pair_to_remove)

            new_string = new_string[:start_index] + new_string[start_index+2:]

        else: break


    if new_string: return new_string
    else: return 'Empty String'   
   


        
def icecreamParlor(m, arr):
    # Write your code here
    # Step 1: write a func that returns all permutations of 2 ice-creams
    list_of_pairs = list(itertools.permutations(arr, r=2))
   
    # Step 2: for each permutation, if sum == m, find index in arr. Add to integer array
    # Step 3: sort the array by ascending order
    for pair in list_of_pairs:
        if pair[0]+pair[1] == m:
            ice_cream_pair_cost = pair
            break
    
    indices = [i+1 for i, x in enumerate(arr) if x == ice_cream_pair_cost[0]]
    if len(indices) == 2:
        return sorted(indices)
    
    indices.append(arr.index(ice_cream_pair_cost[1])+1)
    return(sorted(indices))
    



def icecreamParlor2(m,arr):
    for i in range(len(arr)):
        remainder = m - arr[i]
        if not remainder:
            continue
        indices = [i+1 for i, x in enumerate(arr) if x == remainder]
        if not len(indices):
            continue

        if len(indices) == 2:
            return indices

        
        return [i+1,indices[0]]




def kangaroo(x1, v1, x2, v2):
    # Write your code here

    if v2 >= v1:
        return 'NO'
    
    elif (x1-x2)%(v2-v1) == 0:

        if (x1-x2)/(v2-v1) > 0:
            return 'YES'
        else: return 'NO'
    


print(kangaroo(2,1,1,2))