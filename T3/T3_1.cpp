#include <iostream>
#include <vector>
#include <string>

#include <fstream>
#include <map>

using namespace std;

string line;
string B1;
string B2;
//int lineno = 1;

map<char, int> letters = {
    { 'a', 1 },
    { 'b', 2 },
    { 'c', 3 },
    { 'd', 4 },
    { 'e', 5 },
    { 'f', 6 },
    { 'g', 7 },
    { 'h', 8 },
    { 'i', 9 },
    { 'j', 10},
    { 'k', 11},
    { 'l', 12},
    { 'm', 13},
    { 'n', 14},
    { 'o', 15},
    { 'p', 16},
    { 'q', 17},
    { 'r', 18},
    { 's', 19},
    { 't', 20},
    { 'u', 21},
    { 'v', 22},
    { 'w', 23},
    { 'x', 24},
    { 'y', 25},
    { 'z', 26},
    { 'A', 1 + 26},
    { 'B', 2 + 26},
    { 'C', 3 + 26},
    { 'D', 4 + 26},
    { 'E', 5 + 26},
    { 'F', 6 + 26},
    { 'G', 7 + 26},
    { 'H', 8 + 26},
    { 'I', 9 + 26},
    { 'J', 10 + 26},
    { 'K', 11 + 26},
    { 'L', 12 + 26},
    { 'M', 13 + 26},
    { 'N', 14 + 26},
    { 'O', 15 + 26},
    { 'P', 16 + 26},
    { 'Q', 17 + 26},
    { 'R', 18 + 26},
    { 'S', 19 + 26},
    { 'T', 20 + 26},
    { 'U', 21 + 26},
    { 'V', 22 + 26},
    { 'W', 23 + 26},
    { 'X', 24 + 26},
    { 'Y', 25 + 26},
    { 'Z', 26 + 26}
};

int part1 (string half1, string half2){
    
    for (int i =0 ; i < half1.length() ; i++ ){
        char ser = half1[i];
        if(half2.find(ser) != string::npos){
            //cout << i << endl;
            //cout << "Se encontro coincidencia: " << ser << ", value: " << letters[half1[i]] << endl;
            return letters[half1[i]];
        }
    }
    return 0;
}

int part2 (string B1, string B2, string B3){
    //cout << B1 << "---" << B2 << "---" << B3 << endl;

    for (int i =0 ; i < B1.length() ; i++ ){
        char ser = B1[i];
        if(B2.find(ser) != string::npos){
            //cout << i << endl;
            if (B3.find(ser) != string::npos){
                //cout << "Se encontro coincidencia: " << ser << ", value: " << letters[B1[i]] << endl;
                return letters[B1[i]];
            }
            
        }
    }

    return 0;
}

int main()
{
    vector<string> msg {"Hello", "C++", "World", "from", "VS Code", "and the C++ extension!"};

    for (const string& word : msg)
    {
        cout << word << " ";
    }
    cout << endl;

    string myText;
    string myText2;

    ifstream MyReadFile("input3.txt");

    int priority = 0;

    while (getline (MyReadFile,myText)){
        //cout << myText << endl << "-------" << endl;
        string half = myText.substr(0, myText.length()/2);
        string half2 = myText.substr(myText.length()/2);

        //cout << myText.length() << " : " << myText << endl;
        //cout << half.length()  << " : " << half << endl;
        //cout << half2 .length()  << " : " << half2  << endl;

        //cout << "--------------------------" << endl;
        priority += part1(half ,half2);
        
    }
    MyReadFile.close();

    ifstream MyReadFile2("input3.txt");

    int temp1 = 0;
    int priority2 = 0;

    for (int lineno = 0; getline (MyReadFile2,myText2); lineno++){
        
            if(temp1 == 2){
                string B3 = myText2;
                priority2 += part2 (B1,B2,B3);
                temp1 = 0;
            }
            else{
                if(temp1 == 1){
                    string *ptr_B2 = &B2; //give the address
                    *ptr_B2 = myText2;    //modify the direct value
                    temp1 ++;
                }
                if(temp1 == 0){
                    string *ptr_B1 = &B1;
                    *ptr_B1 = myText2;
                    temp1 ++;
                }
            }
    }

    cout << "total priority: " << priority << endl;
    cout << "total priority 2: " << priority2 << endl;

    MyReadFile2.close();
}

