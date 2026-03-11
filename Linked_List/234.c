#include <stdio.h>
#include <stdlib.h>

// Definition for singly-linked list
struct ListNode {
    int val;
    struct ListNode *next;
};

// Function to print the linked list
void printList(struct ListNode* head) {
    while (head != NULL) {
        printf("%d", head->val);
        if (head->next != NULL)
            printf(" -> ");
        head = head->next;
    }
    printf("\n");
}

bool isPalindrome(struct ListNode* head) {
    if(head==NULL  || head->next==NULL){
        return true;
    }
    int a[100000];
    int length=0;
    struct ListNode* temp = head;
    while(temp != NULL) {
        a[length++] = temp->val;
        temp = temp->next;
    }
    for(int i=0; i<length/2; i++) {
        if(a[i] != a[length-i-1]) {
            return false;
        }
    }
    return true;
}

int main() {
    // Allocate memory for 4 nodes
    struct ListNode* node1 = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* node2 = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* node3 = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* node4 = (struct ListNode*)malloc(sizeof(struct ListNode));

    // Assign values
    node1->val = 1;
    node2->val = 2;
    node3->val = 2;
    node4->val = 1;

    // Link the nodes: 1 -> 2 -> 2 -> 1
    node1->next = node2;
    node2->next = node3;
    node3->next = node4;
    node4->next = NULL;

    // Print the linked list
    printf("Linked List: ");
    printList(node1);

    bool a= isPalindrome(node1);
    if(a) {
        printf("The linked list is a palindrome.\n");
    } else {
        printf("The linked list is not a palindrome.\n");
    }
    return 0;
}
