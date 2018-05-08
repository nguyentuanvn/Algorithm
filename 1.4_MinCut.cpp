#include <iostream>
#include <fstream>
#include <sstream>
#include <stdlib.h>

#define verNum 200
#define repCount 1500
using namespace std;

void arrayPrint(int A[300][300])
{
    for (int row=1;row<=verNum;row++)
    {
        for (int col=0;col<=verNum;col++)
            cout << A[row][col] << "\t";
        cout << endl;
    }
}

void readInput(int A[300][300])
{
    int row,col;
    for (row=1;row<=verNum;row++)
        A[row][0] = row;
    for (row=1;row<=verNum;row++)
        for (col=1;col<=verNum;col++)
            A[row][col] = 0;
    fstream inputfile;
    inputfile.open("1.4_kargerMinCut.txt",fstream::in);
    for (row=1;row<=verNum;row++)
    {
        string line;
        getline(inputfile,line);
        istringstream ss(line);
        int num;
        ss >> num;
        while (ss >> num)
            A[row][num] = 1;
    }
    inputfile.close();
}

void resetArray(int old[300][300],int update[300][300])
{
    for (int row=1;row<=verNum;row++)
        for (int col=0;col<=verNum;col++)
            update[row][col] = old[row][col];
}

void edgeContraction(int A[300][300],int a, int b)
{
//    Find "root" vertex
    while (A[b][0] != b)
    {
        b = A[b][0];
    }
//    Merge the second vertex into the first one (root)
    for (int index=1;index<=verNum;index++)
    {
        A[a][index] += A[b][index];
    }
    A[a][a] = 0;
    A[a][b] = 0;
//    Set A[b][0] equal to root-a. Can be used to track to root later
    A[b][0] = a;
}

int main()
{
    int A[300][300],B[300][300];
    readInput(B);
    int min = verNum;
//    Repeat contraction process for a repCount times
    for (int rep=0;rep<repCount;rep++)
    {
        resetArray(B,A);
        int verCount = verNum;
        int ver1,ver2;
//        Loop until number of vertices == 2
        while (verCount > 2)
        {
//            Find first vertex randomly, should be a root
            do
            {
                ver1 = rand() % verNum + 1;
            } while (A[ver1][0] != ver1 );
//            Find second vertex randomly which has edge to first vertex
            do
            {
                ver2 = rand() % verNum + 1;
            } while (A[ver1][ver2] == 0);
            edgeContraction(A,ver1,ver2);
            verCount--;
        }
        int edgeCount = 0;
//        Find one among two root vertices left
        ver1 = 1;
        while (A[ver1][0] != ver1)
        {
            ver1 = A[ver1][0];
        }
//        For each other vertices
        for (ver2=1;ver2<=verNum;ver2++)
        {
            int parent = ver2;
//            Find root of the vertex
            while (A[parent][0] != parent)
            {
                parent = A[parent][0];
            }
//            If root of the vertex is not the first vertex, then add the number of edges to edgeCount
            if (ver1 != parent)
                edgeCount += A[ver1][ver2];
        }
        if (min > edgeCount)
            min = edgeCount;
    }
    cout << "min " << min << endl;
}
