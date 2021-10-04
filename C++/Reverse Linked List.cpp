// A C++ program to reverse a Linked List
#include<bits/stdc++.h>
using namespace std;

struct ListNode{
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {} 
};

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* revHead, *temp= new ListNode();
        revHead = temp;
        vector<int> valLL;
        while(head!=nullptr){
            valLL.push_back(head->val);
            head = head->next;
        }
        for(int i=valLL.size()-1; i>=0; i--){
            temp->next = new ListNode(valLL[i]);           
            temp = temp->next;
        }
        return revHead->next;
    }

    void printLL(ListNode* head){
        while(head!=nullptr){
            cout << " -> " << head->val;
            head = head -> next;
        } cout << endl;
    }
};

int main(){
    // Defining Nodes and Adding Data to Linked List
    ListNode *n1, *n2, *n3, *n4, *n5;
    n1 = new ListNode(1);
    n2 = new ListNode(2);
    n3 = new ListNode(3);
    n4 = new ListNode(4);
    n5 = new ListNode(5);
    n1->next = n2;
    n2->next = n3;
    n3->next = n4;
    n4->next = n5;

    Solution s;
    // printing original Linked List
    cout << "Inserted Linked List: ";
    s.printLL(n1);

    // Revese the Linked List 
    ListNode* res = s.reverseList(n1);
    cout << endl;
    // printing reversed Linked List
    cout << "Reversed Linked List: ";
    s.printLL(res);

    return 0;
}
