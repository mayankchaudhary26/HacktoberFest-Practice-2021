/* 
File: Stack menu program.c
Author: Pavithra (Bharati Vidhyapeeth University)
Description: This is a menu driven program implementing stack data structure using aaray.
*/


#include <stdio.h>
#include <stdlib.h> // for while loop fn
int top=-1,stack[5];
void push();
void pop();
void display();
void count();
void main()
{
    int ch;
    while(1)   //infinite
    {
        printf("\n****Stack menu\n""");
        printf("1.Push\n 2.pop 3.display 4.count\n");
        printf("\nEnter your choice\n");
        scanf("%d",&ch);
       
 switch(ch)
        {
        
        case 1:
            push();
            break;
        case 2:
            pop();
            break;
        case 3:
            display();
            break;

        case 4:
            count();
            break;
        
        case 5:
         exit(0);
         default:
         printf("\nWrong choice\n");
        }
    }
}
void push()
{
    int num;
    if(top==4)
    {
        printf("Stack is full");
     }
    else
    {
 printf("Enter element to push\n");
        scanf("%d",&num);
        top=top+1;
        stack[top]=num;
    }
}
void pop()
{
    if(top==-1)
    {
        printf("Stack is empty"); 
    }
    

else
    {
        int x;
        x=stack[top];
        printf("The deleted item is %d ",x);
        top=top-1;    
    }
}
void display()
{
    int i;
    if(top==-1)
    {
printf("\nSTACK IS EMPTY");
    }
    else
    {
        printf("\nTHE STACK IS \n");
        for(i=top;i>=0;--i)
        {
            printf("%d\n",stack[i]);
        }
    }
}
void count()
{
    if(top==-1)
    {
printf("\nSTACK IS EMPTY");
    }
    
else
{  
    int i,j=0;
    
    for(i=top;i>=0;--i) 
    {
        j++;
    } 
    
    
    printf("The no of elements in the stack are %d",j);
}  
}
