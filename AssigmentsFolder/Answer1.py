

def maximum_recurring(a):
    
    #creating a list
    lst=list(a)
    #print("list ",lst)

    #sorting the list for every 3rd character
    print("Sorted list is",lst[2::3])

    dic=dict() #defining a dictionary
    
    for name in lst:
        if name not in dic:
                dic[name]=1
        else:
                dic[name]=dic[name]+1
    #print(dic)
    largekey=None
    largevalue=None
    for key,value in dic.items():
        if largevalue is None or largevalue<value:
                largevalue=value
                largekey=key
    print(" Maximum recurring character:",largekey)

# Main Block
if __name__=="__main__": 
      
    #a='abcbjjfgqaazckuccccpcp'
    a=input("Enter a String ")
    #print(a)

    #calling the function
    maximum_recurring(a) 
      


