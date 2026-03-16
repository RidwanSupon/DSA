#include<iostream>
using namespace std;
int main(){
    int arr[] = {12, 7, 16, 7, 6, 21, 2};
    int n = 7;
    int maxVal = 0;
    for(int i=1; i<n; i++){
        if(maxVal < arr[i]){
            maxVal = arr[i];
        }
    }
    cout<<"Max value is: "<<maxVal;
}