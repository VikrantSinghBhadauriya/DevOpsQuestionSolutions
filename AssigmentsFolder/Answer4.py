
def numberOfSquare(n_val):
    #n_val=112
    h_val=n_val//2
    sqr_count=0

    for i in range(1,h_val+1,1):
        for j in range(i,h_val+1,1):
            if ((i*i) + (j*j) == n_val):
                print("I:: ",i," J:: ",j)
                sqr_count=sqr_count+1

    print("No. of Squares:: ",sqr_count)

if __name__ == "__main__":
    number=int(input("Enter the number N "))
    numberOfSquare(number)
    #print(finalList)
