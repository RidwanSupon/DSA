#include <iostream>
using namespace std;
int main(){
    
    string s;
    cin>>s;
    
    bool isPalindrome = true;
    int n = s.length();
    for(int i=0; i<n/2; i++){
        if(s[i] != s[n-i-1]){
            isPalindrome = false;
            break;
        }
    }
    
    if(isPalindrome){
        cout<<s<<" Palindrome";
    }
    else
    cout<<s<<" is not Palindrome";
}