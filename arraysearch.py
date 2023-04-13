def search(item,array):
    '''Searches the item in the given list, rearranges list in descending order of matches. In each element of the returned list, first part is item name and second part is match value(out of 1).'''
    tmp = []
    for each in array:
        a = each
        itm = item
        ins = False
        total = len(item)
        matched = 0
        match = 0
        if len(a) > len(item):
            for rep in range(len(a) - len(item)):
                itm += '!'
            total = len(a)
        elif len(item) > len(a):
            for rep in range(len(item) - len(a)):
                a += '!'
            total = len(item)
        # print(a,itm)    
        for i in range(len(itm)):
            if itm[i] == a[i]:
                matched += 1
        
        match = matched/total
        if match > 0:
            if len(tmp) == 0:
                tmp.append((each,match))
                ins = True
            else:
                for el in range(len(tmp)):
                    if tmp[el][1] < match:
                        tmp.insert(el,(each,match))
                        ins = True
                        break
                if not ins:
                    tmp.append((each,match))
    return tmp

def best(searchedlist):
    '''Returns the best match from search results (list returned from search() function).'''
    if len(searchedlist) > 0:
        return searchedlist[0][0]