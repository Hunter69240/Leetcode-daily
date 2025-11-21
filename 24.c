#include <stdio.h>
#include <stdlib.h>

// Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
};

// Function to print the linked list
void printList(struct ListNode* head) {
    struct ListNode* curr = head;
    while (curr != NULL) {
        printf("%d", curr->val);
        if (curr->next != NULL)
            printf("->");
        curr = curr->next;
    }
    printf("\n");
}

struct ListNode* swapPairs(struct ListNode* head) {
    struct ListNode *temp = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode *prev = NULL;
    struct ListNode *curr = head;
    struct ListNode *next = NULL;
     
    if (head == NULL || head->next == NULL) {
        return head; 
    }
    while(head != NULL && head->next != NULL) {
        prev=head;
        next=head->next;
        temp->val=next->val;
        next->val=prev->val;
        prev->val=temp->val;

        head->next = next->next;
        
    }
    head=curr;
    return head;


}

int main() {
    int arr[] = {1, 2, 3, 4};
    int n = sizeof(arr) / sizeof(arr[0]);
    struct ListNode* head = NULL;
    struct ListNode* temp = NULL;
    struct ListNode* curr = NULL;

    // Dynamically build the linked list from array
    for (int i = 0; i < n; i++) {
        temp = (struct ListNode*)malloc(sizeof(struct ListNode));
        temp->val = arr[i];
        temp->next = NULL;
        if (head == NULL) {
            head = temp;
            curr = head;
        } else {
            curr->next = temp;
            curr = curr->next;
        }
    }

    // Print the linked list
    printList(head);

    // Swap pairs in the linked list
    head = swapPairs(head);
    // Print the modified linked list
    printList(head);

    // Free memory
    curr = head;
    while (curr != NULL) {
        temp = curr;
        curr = curr->next;
        free(temp);
    }

    return 0;
}
