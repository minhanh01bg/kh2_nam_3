#include <bits/stdc++.h>
using namespace std;

string s;
stack<int> st;

bool check(string s)
{
    while (!st.empty())
        st.pop();
    int l = s.length();
    for (int i = 0; i < l; ++i)
    {
        if (s[i] == '(')
            st.push(0);
        else if (s[i] == '[')
            st.push(1);
        else if (s[i] == '{')
            st.push(2);
        else if (s[i] == ')')
        {
            if (!st.empty() && st.top() == 0)
                st.pop();
            else
                return false;
        }
        else if (s[i] == ']')
        {
            if (!st.empty() && st.top() == 1)
                st.pop();
            else
                return false;
        }
        else if (s[i] == '}')
        {
            if (!st.empty() && st.top() == 2)
                st.pop();
            else
                return false;
        }
    }
    if (st.empty())
        return true;
    return false;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int t;
    cin >> t;
    cin.ignore();
    while (t--)
    {
        getline(cin, s);
        if (check(s))
            cout << "yes";
        else
            cout << "no";
        cout << endl;
    }
}