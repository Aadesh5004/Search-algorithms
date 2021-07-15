list = [1,7,2,4,5,100,6,7,8,90,12,3,4,4,5,6,3,23,34,54,34,23,98]
# bubble sort algorithm
def bubbleSort(arr):
    for i in range(0,len(list)):
        for i in range(0,len(list)-1):
            a = list[i]
            if i != 0 and a > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                i+=1
            else:
                i+=1


# binary search algorithm
def binarySearch(arr,low,high,x): 
    bubbleSort(arr)
    if high>=low:
        mid = (low + high)//2
        if arr[mid]==x:
            return mid
        elif arr[mid] > x:
            high = mid-1
            return binarySearch(arr, low, high, x)
        else:
            low = mid+1
            return binarySearch(arr, low, high, x)
    else:
        return  -1

try:
    searchNum = int(input("enter the search number from the list: "))
    result = binarySearch(list, 0, len(list)-1, searchNum)
    if result == -1:
        print("your input value is not found in the list")
    else:
        print(f"The index value of {searchNum} is {result}")
        print(list)
except ValueError:
    print("\nType a number, not a string or any value")

def linearSearch(arr,searchNum):
    for i in range(0,len(arr) - 1):
        if arr[i] == searchNum:
            print(f"The index of the searched number {searchNum} is {i} in an unsorted array")
            break
        else:
            i+=1
# can pass an unsorted array
linearSearch(list, 12)


    
            
    


