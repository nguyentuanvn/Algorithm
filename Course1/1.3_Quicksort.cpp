#include <iostream>
#include <conio.h>
#include <fstream>
using namespace std;

int median(int a,int b,int c)
{
    return a > b ? (b > c ? b : (a > c ? c : a)) : (a > c ? a : (b > c ? c : b));
}

void swap(int *a,int *b)
{
    int *temp = a;
    a = b;
    b = temp;
}

int partitionFirst(int A[],int first,int last)
{
    int pivot = A[first];
    int largerIndex = first+1;
    for (int index=first+1;index<=last;index++)
    {
        if (A[index] < pivot)
        {
            swap(A[index],A[largerIndex]);
            largerIndex++;
        }
    }
    swap(A[first],A[largerIndex-1]);
    return largerIndex-1;
}

int quicksort(int A[],int first,int last)
{
    if (first < last)
    {
//        last element as pivot
//        swap(A[first],A[last]);
//        median element as pivot
        int med = median(A[first],A[(last+first)/2],A[last]);
        if (med == A[(last+first)/2])
            swap(A[first],A[(last+first)/2]);
        else if (med == A[last])
            swap(A[first],A[last]);
//        first element as pivot
        int pivot = partitionFirst(A,first,last);
        return last-first+quicksort(A,first,pivot-1)+quicksort(A,pivot+1,last);
    }
    else return 0;
}

int main()
{
    int A[10000]; int index=0;
    fstream inputfile;
    inputfile.open("1.3_quicksort.txt",fstream::in);
    for (index=0;index<1000;index++)
    {
        inputfile >> A[index];
    }
    cout << quicksort(A,0,index-1) << endl;
    inputfile.close();
    return 0;
}
