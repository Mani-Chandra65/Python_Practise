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

list = input("Enter space seperated list elements:").split()
list = [int(i) for i in input]
found = binary_search(list,2)
verify(found)
