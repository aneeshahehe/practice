// // Maximize count of pairs (i, j) from two arrays having element from first array not exceeding that from second array.

// Given two arrays arr1[] and arr2[] of lengths N and M respectively, the task is to find the maximum number of pairs (i, j) such that 2 * arr1[i] ≤ arr2[j] (1 ≤ i ≤ N and 1 ≤ j ≤ M).

// Note: Any array element can be part of a single pair.



# include<iostream>
# include<algorithm>
# include<queue>
using namespace std;

int numOfPairs(int arr1[],int arr2[],int m, int n)
{
    std::priority_queue<int>pq;
    int i,j;
    int ans = 0;
    sort(arr1, arr1+n);
    for(j=0;j<n;j++)
    {
        pq.push(arr2[j]);
    }

    for (i=n-1; i>=0;i--)
    {
        if (pq.top() >= 2*arr1[i])
        {
            ans++;
            pq.pop();
        }
    }

    return ans;

}

int main()
{
    // Given arrays
    int arr1[] = { 3, 1, 2 };
    int arr2[] = { 3, 4, 2, 1 };
 
    int N = sizeof(arr1) / sizeof(arr1[0]);
    int M = sizeof(arr2) / sizeof(arr2[0]);
 
    // Function Call
    cout << "number of pairs:" << numOfPairs(arr1, arr2, N, M);
    return 0;
}

