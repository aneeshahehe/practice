// A chocolate factory is packing chocolates into the packets. The chocolate packets here represent an array  of N number of 
// integer values. The task is to find the empty packets(0) of chocolate and push it to the end of the conveyor belt(array).

#include<iostream>
#include<vector>
using namespace std;

int main()
{
    int n, count;
    int num;
    std::vector<int> res;
    std::vector<int> arr;
    cout<<"enter the number of packets:";
    cin>>n;
    
    for(int i=0;i<n;i++)
    {   
        cout<<"enter packet number: " ;
        cin>>num;
        if (num!=0)
        {
            res.push_back(num);
        }
        else if(num==0)
        {
            count++;
        }


    }
    for(int i=1;i<=count;i++)
    {
        res.push_back(0);
    }

    for(int i=0;i<n;i++)
    {
        cout<<res[i]<<" ";
    }


}