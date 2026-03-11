#include <stdio.h>
#include <stdlib.h>

// Define the structure for a node in the linked list
struct ListNode {
    int data;
    struct ListNode* next;
};

// Function to print the linked list
void printList(struct ListNode* head) {
    struct ListNode* temp = head;
    while (temp != NULL) {
        printf("%d", temp->data);
        if (temp->next != NULL)
            printf(" -> ");
        temp = temp->next;
    }
    printf("\n");
}

// Function to rotate the list right by k places
struct ListNode* rotateRight(struct ListNode* head, int k) {
    if (head == NULL || head->next == NULL || k == 0)
        return head;

    // Step 1: Count the length
    int length = 1;
    struct ListNode* tail = head;
    while (tail->next != NULL) {
        tail = tail->next;
        length++;
    }

    // Step 2: Connect tail to head (make it circular)
    tail->next = head;

    // Step 3: Normalize k
    k = k % length;   //if k is greater than length ex k=8 it is equivalent to k=3 for length=5
    int stepsToNewTail = length - k;

    // Step 4: Traverse to new tail
    struct ListNode* newTail = head;
    for (int i = 1; i < stepsToNewTail; i++) {
        newTail = newTail->next;
    }

    // Step 5: Set new head and break the circle
    struct ListNode* newHead = newTail->next;
    newTail->next = NULL;

    return newHead;
}

int main() {
    // Create and link nodes: 1 -> 2 -> 3 -> 4 -> 5
    struct ListNode* head = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* second = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* third = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* fourth = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* fifth = (struct ListNode*)malloc(sizeof(struct ListNode));

    head->data = 1; head->next = second;
    second->data = 2; second->next = third;
    third->data = 3; third->next = fourth;
    fourth->data = 4; fourth->next = fifth;
    fifth->data = 5; fifth->next = NULL;

    printf("Original List:\n");
    printList(head);

    int k = 11;
    head = rotateRight(head, k);

    printf("List after rotating by %d:\n", k);
    printList(head);

    return 0;
}
