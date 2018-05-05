#include <iostream>
#include <conio.h>
#include <math.h>
#include <string.h>
using namespace std;

char *makeString(int length)
{
	char *result = new char[length];
	memset(result,'0',length);
	result[length] = '\0';
	return result;
}

char *fillArray(int arraySize, char *A)
{
	char *result = makeString(arraySize);
	for (int index = strlen(A)-1;index >=0;index--)
	{
		result[arraySize-1] = A[index];
		arraySize--;
	}
	return result;
}

char *fillTailArray(int num0,char *A)
{
	char *result = makeString(strlen(A) + num0);
	strncpy(result,A,strlen(A));
	return result;
}

char *add(int arraySize, char *A,char *B)
{
	char *result = makeString(arraySize);
    int carry = 0;
	for (int index = arraySize-1;index>=0;index--)
	{
		int cur = A[index] - '0' + B[index] - '0' + carry;
		if (cur > 9)
		{
			cur -= 10;
			carry = 1;
		}
		else carry = 0;
		result[index] = cur + '0';
	}
	return result;
}
char *addArray(char *A, char *B)
{
	int lenA = strlen(A);
	int lenB = strlen(B);
	int maxLen;
	if (lenA >= lenB)
		maxLen = lenA;
	else maxLen = lenB;
	A = fillArray(maxLen+1,A);
	B = fillArray(maxLen+1,B);
	return add(maxLen+1,A,B);
}

char *product(char *A,char *B)
{
	int arraySize = strlen(A);
	if (arraySize > 2)
	{
		char *A1 = makeString(arraySize/2);
 		char *A2 = makeString(arraySize/2);
  		char *B1 = makeString(arraySize/2);
  		char *B2 = makeString(arraySize/2);
		strncpy(A1,A,arraySize/2);
		strcpy(A2,A+arraySize/2);
		strncpy(B1,B,arraySize/2);
		strcpy(B2,B+arraySize/2);

		char *result1 = fillTailArray(arraySize/2,addArray(product(A1,B2),product(A2,B1)));
		char *result2 = fillTailArray(arraySize,product(A1,B1));
		char *result3 = addArray(product(A2,B2),result2);
		return addArray(result1,result3);
	}
	else
	{
		char *result = makeString(4);
		int product = ((A[0]-'0')*10+(A[1]-'0'))*((B[0]-'0')*10+(B[1]-'0'));
		for (int count = 3; count >= 0; count--)
		{
			result[count] = product % 10 + '0';
			product /= 10;
		}
		return result;
	}
}

int main()
{
	char A[100] = "3141592653589793238462643383279502884197169399375105820974944592";
	char B[100] = "2718281828459045235360287471352662497757247093699959574966967627";
	cout << "A: " << A << endl;
	cout << "B: " << B << endl;
	char *result = product(A,B);
	int num0 = 0,index = 0;
	while (result[num0] == '0')
	{
	    num0++;
	}
	for (index=0;index<strlen(result)-num0;index++)
	{
		result[index] = result[index+num0];
	}
	result[index] = '\0';
	cout << "A * B = " << result;
	getch();
}
