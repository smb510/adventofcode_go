#include <stdio.h>
#include <stdlib.h>

#define STEPS 394

typedef struct node {
    int val;
    struct node* next;
} node_type;

int main(int argc, char** arv) {
    node_type* curr;
    node_type n = {.val = 0};
    n.next = &n;
    curr = &n;

    for (int i = 1; i <= 50000; i++) {
        if (i % 100000 == 0) {
            printf("Progress: %.2f\n", ((double)((double)i) / 50000) * 100);
        }
        for (int j = 0; j < STEPS; j++) {
            curr = curr->next;
        }
        node_type* next = curr-> next;
        node_type* k = (node_type*)malloc(sizeof(node_type));
        k->val = i;
        k->next = next;
        curr->next = k;
        curr = k;
    }
    // while (curr->val != 2017) {
        // curr = curr->next;
    // }

    printf("Part 1 is %d!\n", curr->next->val);
    printf("Part 2 is %d!\n", n.next->val);
    return 0;
}