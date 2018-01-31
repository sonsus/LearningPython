"""Count words."""

def get_listOfWords(s):
    string=""
    wordslist=[]
    counter=0
    for letter in s:
        counter+=1
        if (letter==" ")or(counter==len(s)):
            if counter==len(s): 
                string+=letter
            wordslist.append(string)
            string=""
        else:
            string+=letter        
    return wordslist

def wrap_with_freq_toList(listname):
    unordered_list=[]
    for item in listname:
        freq=listname.count(item)
        if (item,freq) in unordered_list: continue
        item_tup=(item,freq)
        unordered_list.append(item_tup)
    return unordered_list

def sortit(listname):
    listname=sorted(listname, key=lambda ele: ele[0][0])
    fin=sorted(listname,key=lambda ele: ele[1],reverse=True)
    return fin

def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    list_of_words=get_listOfWords(s)
    res=wrap_with_freq_toList(list_of_words)
    res=sortit(res)
    top_n=res[0:n]
    return top_n
    
    # TODO: Count the number of occurences of each word in s
    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    # TODO: Return the top n words as a list of tuples (<word>, <count>)


def test_run():
    """Test count_words() with some inputs."""
    print(count_words("cat bat mat cat bat cat", 3))
    print(count_words("betty bought a bit of butter but the butter was bitter", 3))


if __name__ == '__main__':
    test_run()
