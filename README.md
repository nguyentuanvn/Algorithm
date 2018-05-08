# Algorithm
Stanford's Algorithm Specialization on Coursera

Course content and Programming Assignment can be found in [Coursera](https://www.coursera.org/specializations/algorithms)

## 1. Divide and Conquer, Sorting and Searching, and Randomized Algorithms

Course can be found in [Coursera](https://www.coursera.org/learn/algorithms-divide-conquer)

- Week 1:
  - Problem: In this programming assignment you will implement one or more of the integer multiplication algorithms described in lecture.
To get the most out of this assignment, your program should restrict itself to multiplying only pairs of single-digit numbers. You can implement the grade-school algorithm if you want, but to get the most out of the assignment you'll want to implement recursive integer multiplication and/or Karatsuba's algorithm.
So: what's the product of the following two 64-digit numbers?
3141592653589793238462643383279502884197169399375105820974944592
2718281828459045235360287471352662497757247093699959574966967627
[TIP: before submitting, first test the correctness of your program on some small test cases of your own devising. Then post your best test cases to the discussion forums to help your fellow students!]
[Food for thought: the number of digits in each input number is a power of 2. Does this make your life easier? Does it depend on which algorithm you're implementing?]
  - [Multiplication](https://github.com/nguyentuanvn/Algorithm/blob/master/1.1_Multiplication.cpp) by C++
- Week 2:
  - [1.2_IntegerArray.txt](https://github.com/nguyentuanvn/Algorithm/blob/master/1.2_IntegerArray.txt) contains all of the 100,000 integers between 1 and 100,000 (inclusive) in some order, with no integer repeated.
Your task is to compute the number of inversions in the file given, where the ith row of the file indicates the ith entry of an array.
Because of the large size of this array, you should implement the fast divide-and-conquer algorithm covered in the video lectures.
  - [CountInversion](https://github.com/nguyentuanvn/Algorithm/blob/master/1.2_CountInversion.cpp) by C++

- Week 3:
  - [1.3_quicksort.txt](https://github.com/nguyentuanvn/Algorithm/blob/master/1.3_quicksort.txt) contains all of the integers between 1 and 10,000 (inclusive, with no repeats) in unsorted order. The integer in the ith row of the file gives you the ith entry of an input array.
Your task is to compute the total number of comparisons used to sort the given input file by QuickSort. As you know, the number of comparisons depends on which elements are chosen as pivots, so we'll ask you to explore three different pivoting rules.
You should not count comparisons one-by-one. Rather, when there is a recursive call on a subarray of length m, you should simply add m-1 to your running total of comparisons. (This is because the pivot element is compared to each of the other m-1 elements in the subarray in this recursive call.)
WARNING: The Partition subroutine can be implemented in several different ways, and different implementations can give you differing numbers of comparisons. For this problem, you should implement the Partition subroutine exactly as it is described in the video lectures (otherwise you might get the wrong answer).
There are three ways to choose pivot element: the first element, the last element and the median among the first, middle and last element of the array.
  - [QuickSort](https://github.com/nguyentuanvn/Algorithm/blob/master/1.3_Quicksort.cpp) by C++

- Week 4:
  - [1.4_kargerMinCut.txt](https://github.com/nguyentuanvn/Algorithm/blob/master/1.4_kargerMinCut(17).txt) contains the adjacency list representation of a simple undirected graph. There are 200 vertices labeled 1 to 200. The first column in the file represents the vertex label, and the particular row (other entries except the first column) tells all the vertices that the vertex is adjacent to. So for example, the 6th row looks like : "6	155	56	52	120	......". This just means that the vertex with label 6 is adjacent to (i.e., shares an edge with) the vertices with labels 155,56,52,120,......,etc
Your task is to code up and run the randomized contraction algorithm for the min cut problem and use it on the above graph to compute the min cut. (HINT: Note that you'll have to figure out an implementation of edge contractions. Initially, you might want to do this naively, creating a new graph from the old every time there's an edge contraction. But you should also think about more efficient implementations.) (WARNING: As per the video lectures, please make sure to run the algorithm many times with different random seeds, and remember the smallest cut that you ever find.)
  - [MinCut](https://github.com/nguyentuanvn/Algorithm/blob/master/1.4_MinCut.cpp) by C++