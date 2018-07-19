"""
Coursera Algorithm Programming Assignemnt 3.4.1:
Knapsack Problem, Iterative solution.
@author: Tuan M. Nguyen
"""

def main():
    file = open("3.4.1_knapsack1.txt","r")
    size,num = [int(x) for x in next(file).split()]
    A = [[0] for s in range(size+1)]
    for n in range(1,num+1):
        line = file.readline()
        v,w = [int(x) for x in line.split()]
        for s in range(size+1):
            if s < w:
                A[s].append(A[s][n-1])
            else:
                A[s].append(max(A[s][n-1],A[s-w][n-1]+v))
    file.close()
    print(A[size][num])
#    expected result: 2493893

if __name__ == "__main__":
    main()