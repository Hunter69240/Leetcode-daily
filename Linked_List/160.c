#include <stdio.h>
#include <stdlib.h>

// Definition for singly-linked list
struct ListNode {
    int val;
    struct ListNode* next;
};

// Create a new node
struct ListNode* createNode(int val) {
    struct ListNode* node = (struct ListNode*)malloc(sizeof(struct ListNode));
    node->val = val;
    node->next = NULL;
    return node;
}

// Print a linked list
void printList(struct ListNode* head) {
    while (head) {
        printf("%d", head->val);
        if (head->next) printf(" -> ");
        head = head->next;
    }
    printf("\n");
}

struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    if(headA == NULL || headB == NULL) return NULL;
    struct ListNode *a = headA, *b = headB;
    int m=0,n=0;
    while(a != NULL) {
        m++;
        a = a->next;
    }
    while(b != NULL) {
        n++;
        b = b->next;
    }
    a = headA;
    b = headB;
    if(m > n) {
        for(int i = 0; i < m - n; i++) {
            a = a->next;
        }
    } else {
        for(int i = 0; i < n - m; i++) {
            b = b->next;
        }
    }
    while(a != NULL && b != NULL) {
        if(a == b) return a;
        a = a->next;
        b = b->next;
    }
    return NULL;
}

int main() {
    // Create shared tail: 8 -> 4 -> 5
    struct ListNode* shared8 = createNode(8);
    shared8->next = createNode(4);
    shared8->next->next = createNode(5);

    // List A: 4 -> 1 -> [shared8...]
    struct ListNode* listA = createNode(4);
    listA->next = createNode(1);
    listA->next->next = shared8;

    // List B: 5 -> 6 -> 1 -> [shared8...]
    struct ListNode* listB = createNode(5);
    listB->next = createNode(6);
    listB->next->next = createNode(1);
    listB->next->next->next = shared8;

    // Print both lists
    printf("List A: ");
    printList(listA);
    printf("List B: ");
    printList(listB);

    // ✅ Call before freeing memory
    struct ListNode* intersection = getIntersectionNode(listA, listB);
    if (intersection) {
        printf("Intersection at node with value: %d\n", intersection->val);
    } else {
        printf("No intersection found.\n");
    }

    // Free list A up to intersection
    struct ListNode* temp = listA;
    while (temp != shared8) {
        struct ListNode* next = temp->next;
        free(temp);
        temp = next;
    }

    // Free list B up to intersection
    temp = listB;
    while (temp != shared8) {
        struct ListNode* next = temp->next;
        free(temp);
        temp = next;
    }

    // Free the shared tail
    while (shared8) {
        struct ListNode* next = shared8->next;
        free(shared8);
        shared8 = next;
    }

    return 0;
}
