#include <stdio.h>
#include <stdlib.h>

// Define the structure for a node in the linked list
struct Node {
    int data;              // Data part of the node
    struct Node* next;     // Pointer to the next node
};

// Function to print the linked list
void printList(struct Node* head) {
    struct Node* temp = head;

    // Traverse the list until the end
    while (temp != NULL) {
        printf("%d", temp->data);
        if (temp->next != NULL)
            printf(" -> ");  // Add arrow if not the last node
        temp = temp->next;
    }
    printf("\n");
}

// Function to reverse the linked list
struct Node* reverseList(struct Node* head) {
    if(head == NULL){
        return head;  // Return NULL if list is empty
    }

    struct Node* prev = NULL;     // Will become the new tail
    struct Node* current = head;  // Pointer to current node

    // Iterate through the list
    while(head != NULL){
        current = head;           // Store current node
        head = head->next;        // Move head to next node
        current->next = prev;     // Reverse the current node's link
        prev = current;           // Move prev to current
    }

    return prev;  // New head of the reversed list
}

int main() {
    // Manually allocate memory for 5 nodes
    struct Node* head = (struct Node*)malloc(sizeof(struct Node));
    struct Node* second = (struct Node*)malloc(sizeof(struct Node));
    struct Node* third = (struct Node*)malloc(sizeof(struct Node));
    struct Node* fourth = (struct Node*)malloc(sizeof(struct Node));
    struct Node* fifth = (struct Node*)malloc(sizeof(struct Node));

    // Assign values and link nodes together: 1 -> 2 -> 3 -> 4 -> 5
    head->data = 1;
    head->next = second;

    second->data = 2;
    second->next = third;

    third->data = 3;
    third->next = fourth;

    fourth->data = 4;
    fourth->next = fifth;

    fifth->data = 5;
    fifth->next = NULL;

    // Print original list
    printf("Original List:\n");
    printList(head);

    // Reverse the list and update head
    head = reverseList(head);

    // Print reversed list
    printf("Reversed List:\n");
    printList(head);

    return 0;
}
