"""
Coursera Algorithm Programming Assignemnt 3.2.2:
@author: Tuan M. Nguyen
"""

def find(parent,ver):
    while parent[ver] != ver:
        ver = parent[ver]
    return ver

def union(rank,parent,ver1,ver2):
    s1 = find(parent,ver1)
    s2 = find(parent,ver2)
    if rank[s1] < rank[s2]:
        parent[s1] = s2
    elif rank[s1] == rank[s2]:
        parent[s1] = s2
        rank[s2] += 1
    else:
        parent[s2] = s1

def bitflip(bit):
    return '1' if bit == '0' else '0'

def makefriend(friends,ver):
    num = int(ver,2)
    for i in range(len(ver)):
        num1 = int(ver[:i] + bitflip(ver[i]) + ver[i+1:],2)
        friends[num1].append(num) 
        for j in range(i+1,len(ver)):
            num2 = int(ver[:i] + bitflip(ver[i]) + ver[i+1:j] + bitflip(ver[j]) + ver[j+1:],2)
            friends[num2].append(num)
        
def main():
    file = open("3.2_clustering_big.txt","r")
    v,bit = [int(x) for x in next(file).split()]
    rank = {}
    parent = {}
    friends = {ver:[] for ver in range(0,2**bit)}

    for line in file:
        line = ''.join(line.rstrip().split(' '))
        num = int(line,2)
        rank[num] = 0
        try:
            parent[num]
        except: 
            parent[num] = num
        else:
            v -= 1
        
        if friends[num] == []:
            friends[num].append(num)
        else:
            for ver in friends[num]:
                if find(parent,ver) != find(parent,num):
                    union(rank,parent,ver,num)
                    v -= 1
        makefriend(friends,line)
    print(v)
#    expected result: 6118    

if __name__ == "__main__":
    main()
    
    