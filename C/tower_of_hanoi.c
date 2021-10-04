/* 
File: tower_of_hanoi.c
Author: Sahil Ahmad (Kashmir University)
Description: This is the implementation of tower of hanoi.
*/

#include <stdio.h>
#include <conio.h>
void hanoi(char,char,char,int);
void main()
{
    int num;
    clrscr();
    printf("\nENTER NUMBER OF DISKS: ");
    scanf("%d",&num);
    printf("\nTOWER OF HANOI FOR %d NUMBER OF DISKS:\n", num);
    hanoi('A','B','C',num);
    getch();
}
void hanoi(char from,char to,char other,int n)
{
    if(n<=0)
        printf("\nILLEGAL NUMBER OF DISKS");
    if(n==1)
        printf("\nMOVE DISK FROM %c TO %c",from,other);
    if(n>1)
        {
            hanoi(from,other,to,n-1);
            hanoi(from,to,other,1);
            hanoi(to,from,other,n-1);
        }
}
