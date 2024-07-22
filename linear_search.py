def search(list,key):
    for i in range(0, len(list)):
        if(list[i] == key):
            return i
    return None

def verify(found):
    if found is not None:
        print("Target is found at index",found)
    else:
        print("Target is not found!!")

list = [1,2,3,4,5,6,7,8,9]
found = search(list,8)
verify(found)