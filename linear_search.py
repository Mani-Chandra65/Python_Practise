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

list = input("Enter space seperated list elements:").split()
list = [int(i) for i in input]
found = search(list,8)
verify(found)
