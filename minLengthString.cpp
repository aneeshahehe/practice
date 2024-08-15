//Given a string str consisting of lowercase and uppercase characters, the task is to find the minimum possible length the string can be reduced to after performing the given operation any number of times. In a single operation, any two consecutive characters can be removed if they represent the same character in different cases i.e. “aA” and “Cc” can be removed but “cc” and “EE” cannot be removed.

#include <iostream>
#include <string.h>
#include <stack>

using namespace std;
int SmallestLexicostring(string str, int len )
{
    stack<char> st;
    for(int i=0; i<len;i++)
    {
        if (st.empty())
        {
            st.push(str[i]);
        }

        else{
            char c = st.top();
            if(c != str[i] && toupper(c) == toupper(str[i]))
            {
                st.pop();
            }
            else{
                st.push(str[i]);
            }
        }

    }

    return st.size();


}

int main()
{
    string str = "ASbBsd";
    int len = str.length();
 
    cout << SmallestLexicostring(str, len);
 
    return 0;
}