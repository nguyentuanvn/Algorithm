"""
Coursera Algorithm Programming Assignemnt 3.3.3:
Maximum weight independent set. Dynamic Programming Algorithm
@author: Tuan M. Nguyen
"""
        
def main():
    file = open("3.3.3_mwis.txt","r")
    file.readline()
    A = [0,int(next(file))]
    index = 1

    for line in file:
        index += 1
        A.append(max(A[index-1],A[index-2]+int(line)))
    file.close()
    
    S = []
    while index >= 1:
        if A[index] == A[index-1]:
            index -= 1
        else:
            S.append(index)
            index -= 2
    
    check = [1,2,3,4,17,117,517,997]
    for vertex in check:
        print (1,end = "") if vertex in S else print(0,end = "")
#    expected result: 10100110
            
if __name__ == "__main__":
    main()
    
    