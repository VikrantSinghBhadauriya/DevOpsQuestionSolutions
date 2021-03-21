
  
def minimum_replacement(word): 
    replacementList=list() 
      
    for items in word:
    
        length_of_string = len(items) 
        #print(length_of_string)
    
       
        no_of_replacements_needed = 0
        
  
        index = 0
        
        while index < length_of_string: 
            mover = index 
            
          
            while mover < length_of_string and (items[mover] == items[index]): 
                mover = mover + 1
            
            
            
            matching_substring = mover - index 
            
            #
            no_of_replacements_needed =no_of_replacements_needed+ matching_substring // 2
            
            
            index = mover 
        replacementList.append(no_of_replacements_needed)

    print(" number of replacement needed ",replacementList)     
   
      
# Main Block
if __name__=="__main__": 
      
    #word = "boook"
    
    finalList = list()
    count=0
    n = int(input("Enter the size of N "))
    print("\n")
    for i in range(0, n):
        print("Enter number of N", i+1, )
        item = (input())
        finalList.append(item)
    print(finalList)
    minimum_replacement(finalList)
      
