#include <iostream>
#include <fstream>

using namespace std;

void swap (int &a,int &b)
{
    int temp = a;
    a = b;
    b = temp;
}

int *insert (int *H,int &num, int key, int mode /*1: minHeap -1: maxHeap*/)
{
    num++;
    int *H1 = NULL;
    H1 = (int*) realloc(H,sizeof(int)*num);
    if (H1 != NULL)
    {
        H = H1;
        H[num-1] = key;
        int node = num-1;
        while (node > 0 && mode*H[node] < mode*H[(node-1)/2])
        {
            swap(H[node],H[(node-1)/2]);
            node = (node-1)/2;
        }
    }
    return H;
}

int extractMinMax(int *H, int &num,int mode /*1: minHeap -1:maxHeap*/)
{
    int min = H[0];
    swap (H[0],H[num-1]);
    num--;
    int node = 0;
    int left,right;
    int smallChild;
    while (1)
    {
        left = node*2+1;
        right = node*2+2;
        if (right > num-1)
        {
            if (left <= num-1)
                smallChild = left;
            else
                break;
        }
        else
        {
            if (mode*H[left] < mode*H[right])
                smallChild = left;
            else smallChild = right;
        }
        if (mode*H[smallChild] < mode*H[node])
        {
            swap(H[node],H[smallChild]);
            node = smallChild;
        }
        else
            break;
    }
    return min;
}

int main()
{
    int *Hhigh = NULL;
    int *Hlow = NULL;
    int numLow = 0;
    int numHigh = 0;
    int maxLow,minHigh;
    int numRead;
    int sum = 0;

    fstream inputFile;
    inputFile.open("2.3_Median.txt",fstream::in);
    int first,second;
    inputFile >> first;
    inputFile >> second;
    if (first > second)
    {
        Hlow = insert(Hlow,numLow,second,-1);
        Hhigh = insert(Hhigh,numHigh,first,1);
    }
    else
    {
        Hlow = insert(Hlow,numLow,first,-1);
        Hhigh = insert(Hhigh,numHigh,second,1);
    }
    sum = first + Hlow[0];
    while(!inputFile.eof())
    {
        inputFile >> numRead;
        maxLow = Hlow[0];
        minHigh = Hhigh[0];
        if (numLow <= numHigh)
        {
            if (numRead > minHigh)
            {
                minHigh = extractMinMax(Hhigh,numHigh,1);
                Hlow = insert(Hlow,numLow,minHigh,-1);
                Hhigh = insert(Hhigh,numHigh,numRead,1);
            }
            else
            {
                Hlow = insert(Hlow,numLow,numRead,-1);
            }
        }
        else
        {
            if (numRead < maxLow)
            {
                maxLow = extractMinMax(Hlow,numLow,-1);
                Hhigh = insert(Hhigh,numHigh,maxLow,1);
                Hlow = insert(Hlow,numLow,numRead,-1);
            }
            else
            {
                Hhigh = insert(Hhigh,numHigh,numRead,1);
            }
        }
        sum += Hlow[0];
    }
    cout << sum%10000 << endl;
//	  expected result: 1213
    return 0;
}
