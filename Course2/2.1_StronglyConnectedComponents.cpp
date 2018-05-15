#include <iostream>
#include <fstream>
#include <vector>

#define MAX 1000000
using namespace std;

int leader;
vector<int> Rnodes[MAX];
vector<int> nodes[MAX];
vector<int> finishTime;
bool explored[MAX];
int scc[MAX];
int largest[5];

void findMax(int node,int rank)
{
    if (scc[node] > largest[rank])
    {
        for (int index=4;index>rank;index--)
            largest[index] = largest[index-1];
        largest[rank] = scc[node];
    }
    else if (rank < 4)
        findMax(node,rank+1);
}

void FirstDFS(int node)
{
    explored[node] = true;
    for (vector<int>::iterator index = Rnodes[node].begin();index != Rnodes[node].end();index++)
    {
        if (!explored[*index])
            FirstDFS(*index);
    }
    finishTime.insert(finishTime.begin(),node);
}

void SecondDFS(int node)
{
    explored[node] = true;
    scc[leader] += 1;
    for (vector<int>::iterator index = nodes[node].begin();index != nodes[node].end();index++)
    {
        if (!explored[*index])
            SecondDFS(*index);
    }
}

void FirstDFSLoop(int num)
{
    for (int index=num;index>0;index--)
    {
        if (!explored[index])
            FirstDFS(index);
    }
}

void SecondDFSLoop()
{
    for (vector<int>::iterator index=finishTime.begin();index!=finishTime.end();index++)
    {
        if (!explored[*index])
        {
            leader = *index;
            SecondDFS(*index);
        }
    }
}

int main()
{
    fstream inputfile;
    inputfile.open("2.1_SCC.txt",fstream::in);
    int head,tail,max=0;
    while (!inputfile.eof())
    {
        inputfile >> head;
        inputfile >> tail;
        if (head > max)
            max = head;
        nodes[head].push_back(tail);
        Rnodes[tail].push_back(head);
    }
    inputfile.close();
    finishTime.reserve(max);
    for (int index=0;index<=max;index++)
        explored[index] = false;

    FirstDFSLoop(max);
    for (int index=0;index<=max;index++)
        explored[index] = false;
    SecondDFSLoop();

    for (int index=1;index<=max;index++)
        if (scc[index] > largest[4])
            findMax(index,0);
    for (int index=0;index<=4;index++)
        cout << largest[index] << "\t";
    return 0;
}
