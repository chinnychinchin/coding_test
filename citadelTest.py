


from operator import index


def getUniqueCharacter(s):
    # Write your code here
    from collections import Counter   

    unique_chars = Counter(s)
    
    for c in unique_chars:
        if unique_chars[c] == 1:
            index = s.index(c)+1
            break
        
    try:
        
        return index
    except:
        return -1





def missingWords(s, t):
    # Write your code here

    res = []
    words_in_t = t.split(" ")
    
    for word in words_in_t:
        start_index = s.index(word)
        end_index = start_index + len(word)
        res.append(s[0:start_index].strip())
        res.append(s[end_index:].strip())

    return res


missingWords('I like cheese','like')