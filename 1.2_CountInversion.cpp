#include <iostream>
#include <fstream>
#define max 1000000

using namespace std;

void merge(int A[], int first, int mid, int last, long long int *countInversion)
{
    int lastB = mid-first,lastC = last-mid-1;
    int B[lastB+2],C[lastC+2],index;
    for (index = 0; index <= lastB; index++)
    {
        B[index] = A[first+index];
    }
    B[index] = max;
    for (index = 0; index <= lastC; index++)
    {
        C[index] = A[mid+index+1];
    }
    C[index] = max;
    int indexA, indexB = 0, indexC = 0;
    for (indexA = first; indexA <= last; indexA++)
    {
        if (B[indexB] < C[indexC])
        {
            A[indexA] = B[indexB];
            indexB++;
        }
        else
        {
            A[indexA] = C[indexC];
            indexC++;
            *countInversion += lastB-indexB+1 > 0 ? lastB-indexB+1 : 0;
        }
    }
}

void count_inversion(int A[], int first, int last, long long int *countInversion)
{
    int mid = (last + first)/2;
    if (last - first > 1)
    {
        count_inversion(A,first,mid,countInversion);
        count_inversion(A,mid+1,last,countInversion);
    }
    merge(A,first,mid,last,countInversion);
}
int main()
{
    int A[100000]; int index = 0;
    fstream inputFile;
    inputFile.open("1.2_IntegerArray.txt",fstream::in);
    while(!inputFile.eof())
    {
        inputFile >> A[index];
        index++;
    }
    inputFile.close();
    long long int *countInversion = (long long int*) malloc(sizeof (long long int));
    *countInversion = 0;
    count_inversion(A,0,index-2,countInversion);
    cout << *countInversion << endl;
}
