"""
Coursera Algorithm Programming Assignemnt 3.4.2:
Knapsack Problem for a much bigger dataset. Calculate recursively
@author: Tuan M. Nguyen
"""

A = {}
V = [0]
W = [0]

def recurrence(s,n):
    if n == 0 or s == 0:
        return 0
    else:
        if A.get((s,n-1)) is None:
            A[(s,n-1)] = recurrence(s,n-1)
        a = A[(s,n-1)]
        if s < W[n]:
            c = a
        else:
            if A.get((s-W[n],n-1)) is None:
                A[(s-W[n],n-1)] = recurrence(s-W[n],n-1)
            b = A[(s-W[n],n-1)] + V[n]
            c = max(a,b)
        return c

def main():
    file = open("3.4.2_knapsack_big.txt","r")
    size,num = [int(x) for x in next(file).split()]
    for line in file:
        v,w = [int(x) for x in line.split()]
        V.append(v)
        W.append(w)
    file.close()
    print(recurrence(size,num))
#    expected result: 4243395
    
if __name__ == "__main__":
    main()