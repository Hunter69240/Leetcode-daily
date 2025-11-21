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

struct ListNode* deleteDuplicates(struct ListNode* head) {
   struct ListNode* current = head;
   struct ListNode* temp = head;
  while(head!=NULL){
    if(current->val == head->val){
        current->next=head->next;
        head=head->next;
    }
    else{
current=current->next;
    head=head->next;
    }
    
  }
  current=temp;
    return current;
}

int main() {
    // Allocate memory for 3 nodes
    struct ListNode* node1 = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* node2 = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* node3 = (struct ListNode*)malloc(sizeof(struct ListNode));

    // Assign values
    node1->val = 1;
    node2->val = 1;
    node3->val = 2;

    // Link nodes: 1 -> 1 -> 2
    node1->next = node2;
    node2->next = node3;
    node3->next = NULL;

    // Print the list
    printf("Linked List: ");
    printList(node1);

    // Delete duplicates
    struct ListNode* newHead = deleteDuplicates(node1);
    // Print the modified list
    printf("After removing duplicates: ");  
    printList(newHead);
    return 0;
}
