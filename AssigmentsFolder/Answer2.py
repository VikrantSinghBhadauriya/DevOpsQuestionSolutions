





def UniqueNumber(array,size):
     
    FirstNumber = array[0]
    print(FirstNumber)
     
    # Do XOR of all elements and return
    for i in range(1,size):
        FirstNumber = FirstNumber ^ array[i]
     
    return FirstNumber
 
# Driver code
if __name__ == "__main__":
    arr = input("Please type the number separated by space ")   
    l = list(int(num) for num in arr.strip().split())
    print("User list is ", l)
    #print(type(l))
    Distnictnumber=UniqueNumber(l, len(l))
    print("The number which is occuring only one time is ",Distnictnumber)