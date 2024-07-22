def binary_search(list,key):
    low = 0
    high = len(list)-1
    while low<=high:
        mid = (low+high)//2
        if list[mid] == key:
            return mid
        elif list[mid] < key:
            low = mid+1
        elif list[mid] > key:
            high = mid-1
    return None

def check(found):
    if found == None:
        print("The element is not found.")
    else:
        print("The element is found at index",found)


list = [1,2,3,4,5,6,7,8,9]

found = binary_search(list,8)
check(found)