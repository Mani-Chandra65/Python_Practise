def binary_search(list,key):
    if len(list)==0:
        return False
    else:
        mid = len(list)//2
        if list[mid] == key:
            return True
        elif list[mid] > key:
            return binary_search(list[:mid],key)
        else:
            return binary_search(list[mid+1:],key)

def verify(found):
    print("Target found:",found)

list = [1,2,3,4,5,6,7,8,9]
found = binary_search(list,2)
verify(found)