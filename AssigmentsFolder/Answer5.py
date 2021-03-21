
def takinginput():

    finalList = list()
    count=0
    n = int(input("Enter the size of N "))
    print("\n")
    for i in range(0, n):
        print("Enter number of N", i+1, )
        item = (input())
        y = list(item)  # converting to list
       # print(y)

        y = set(item)  # converting to set
       # print(y)
        finalList.append(y)
       ##finalList.append(z)
    #print("Final List ",finalList)
    intersection=(finalList[0].intersection(*finalList))  #To count the intersection between sets(no of common elements)
    count=len(intersection)
    print("count of special ingredient ",count)
    


if __name__ == "__main__":
    takinginput()
    #print(finalList)
