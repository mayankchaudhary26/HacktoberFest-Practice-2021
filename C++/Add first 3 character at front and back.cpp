#include<iostream>
#include<string.h>
using namespace std;

int main(){
    char s1[20],s2[26];
    cout<<"Enter a string : ";cin>>s1;
    int x=strlen(s1);
    char c;
    if(x>3){
        for(int i=0;i<3;i++)
        {
            c=s1[i];
            s2[i]=c;
            s2[x+i+3]=c;
        }
        for(int i=3;i<x+3;i++)
        {            s2[i]=s1[i-3];        }
        cout<<"New string is "<<s2;
    }
    else{ cout<<"Less than 2 characters. Original string is "<<s1;}
    return 0;
}
