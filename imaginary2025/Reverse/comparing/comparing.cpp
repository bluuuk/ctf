#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <numeric>
#include <map>
#include <cmath>
#include <set>
#include <fstream>
#include <queue>
#include <unordered_map>
#include <cstring>
#include <list>
#include <cassert>
#include <tuple>
using namespace std;

class Compare {
public:
    bool operator()(tuple<char, char, int> a, tuple<char, char, int> b) {
        return static_cast<int>(get<0>(a)) + static_cast<int>(get<1>(a)) > static_cast<int>(get<0>(b)) + static_cast<int>(get<1>(b));
    }
};

string even(int val1, int val3, int ii) { // --> val1 + val3 + ii + reverse(val1 + val3)
    // https://en.cppreference.com/w/cpp/string/basic_string/to_string
    string out = to_string(val1) + to_string(val3) + to_string(ii);
    // val1 + val3 + ii 
    //                      max 256                 256
    string x = to_string(val1) + to_string(val3);
    // val + val3

    // max size should be 6
    for (int i = x.size() - 1; i >= 0; i--) {
        out += x[i];
    }
    // val1 + val3 + ii + reverse(val1 + val3)
    return out;
}

string odd(int val1, int val3, int ii) { // --> int(string(val1) + string(val3) + string(ii))
    int out = stoi(to_string(val1) + to_string(val3) + to_string(ii));
    // int(val1 + val3 + ii)
    int i = 0;
    int addend = 0;
    // n*(n-1)//2 added
    while (i < 100) { addend += i; i++; }
    i--;
    // n*(n-1)//2 removed
    while (i >= 0) { addend -= i; i--; }

    // this is then int(val1 + val3 + ii) + 0
    return to_string(out + addend);
}

int main()
{
    string flag = "REDACTED";
    // creation of a heap as prio queue
    /*
            a = a0,a1,a2
            b = b0,b1,b2
            where ai and bi are char2int
            cmp= a0 + a1 > b0 + b1

            we should have a min heap

    */
    priority_queue<tuple<char, char, int>, vector<tuple<char, char, int>>, Compare> pq;
    for (int i = 0; i < flag.size() / 2; i++) {
        tuple<char, char, int> x = { flag[i * 2],flag[i * 2 + 1],i };
        pq.push(x);
    }
    vector<string> out;
    while (!pq.empty()) {
        // get A0
        int val1 = static_cast<int>(get<0>(pq.top()));
        // get A1
        int val2 = static_cast<int>(get<1>(pq.top()));
        // get Ai
        int i1 = get<2>(pq.top());
        
        pq.pop();

        // get B0
        int val3 = static_cast<int>(get<0>(pq.top()));
        // get B1
        int val4 = static_cast<int>(get<1>(pq.top()));
        // get Bi
        int i2 = get<2>(pq.top());
        pq.pop();

        /*
            if Ai is even
                out.push_back(even(A0, B0, Ai)
            else:
                out.push_back(odd(A0, B0, Ai)

            if Bi is even:
                out.push_back(even(A1, B1, Bi))
            else:
                out.push_back(odd(A1, B1, Bi))
        */
        if (i1 % 2 == 0) { out.push_back(even(val1, val3, i1)); }
        else { out.push_back(odd(val1, val3, i1)); }
        if (i2 % 2 == 0) { out.push_back(even(val2, val4, i2)); }
        else { out.push_back(odd(val2, val4, i2)); }
    }
    for (int i = 0; i < out.size(); i++) {
        cout << out[i] << endl;
    }
}
