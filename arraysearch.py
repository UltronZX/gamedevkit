def search(item,array,extrachar = '!',minimum = 0.1):
    '''Searches the item in the given list, rearranges list in descending order of matches. In each element of the returned list, first part is item name and second part is match value(out of 1). Extrachar parameter should be a character which is not used in any item of the list. Only matches that are greater than 'minimum' parameter will be added.'''
    tmp = []
    for each in array:
        a = list(each)
        itm = list(item)
        ins = False
        total = len(item)
        matched = 0
        match = 0
        big = 0
        if len(a) > len(item):
            big = 'a'
            for rep in range(len(a) - len(item)):
                itm.append(extrachar)
            total = len(a)
        elif len(item) > len(a):
            big = 'itm'
            for rep in range(len(item) - len(a)):
                a.append(extrachar)
            total = len(item)
        for i in range(len(itm)):
            if itm[i] == a[i]:
                matched += 1
            else:
                if big == 'a':
                    itm.insert(i,extrachar)
                elif big == 'itm':
                    a.insert(i,extrachar)
        
        match = matched/total
        if match >= minimum:
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
