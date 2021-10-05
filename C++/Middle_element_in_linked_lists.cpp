#include<iostream>
#include<bits/stdc++.h>
using namespace std;
class node{ //class for creation of node
    public:
    int data;
    node* next;

    node(int val){ //constructor call
    data=val;
    next=NULL;
    }
};

void insertAtTail(node* &head,int val){ //insert function to insert a node
    node*n=new node(val);
    if(head==NULL)//when no element is present
    {
        head=n;
        return;
    }
    node*temp=head;
    while(temp->next!=NULL){
    temp=temp->next;
    }
    temp->next=n;
}
void middle(node* head){  // to get the middle element
    if(head==NULL)
    return;
    //taking pointers slow and fast and initialising both as head
    node* slow=head;
    node* fast=head;
    while(fast!=NULL &&fast->next!=NULL){
        slow=slow->next; // moving slow pointer one step next
        fast=fast->next->next; // moving fast pointer two steps
    }
    //when there is no node next to next then
    // the node at which slow pointer is will give the middle of linked lists
    cout<<slow->data<<" "; 
}

void display(node* head){ //to display the linked lists
    node* temp=head;
    while(temp!=NULL){
        cout<<temp->data<<"-> ";
        temp=temp->next;
    }
    cout<<"NULL"<<endl;

}

int main(){
    node* head=NULL;
    insertAtTail(head,5);
    insertAtTail(head,10);
    insertAtTail(head,15);
    insertAtTail(head,20);
    insertAtTail(head,25);
    display(head);
    cout<<"Middle element: ";
    middle(head);
    return 0;
}