/*
   stack.c
   VenkataBabji S
   venkatababji@gmail.com

   Stack Implementation using a linked list.
*/
#include <stdio.h>
#include <stdlib.h>

struct BackwardLink_t
{
    struct BackwardLink_t* pPrev;
};
typedef struct BackwardLink_t BackwardLink;

typedef int value_type;

struct Entry_t
{
    BackwardLink link;
    value_type val;
};
typedef struct Entry_t Entry;

struct Stack_t
{
    Entry* pTop;
    unsigned int nSize;
};
typedef struct Stack_t Stack;

Stack* stack_new(void)
{
    Stack* pStack = (Stack*) malloc( sizeof(Stack) );
    pStack->pTop = NULL;
    pStack->nSize = 0;
    return pStack;
}

void stack_clear(Stack* pStack)
{
    while(pStack->pTop)
    {
        Entry* pPrev = pStack->pTop->link.pPrev;
        free(pStack->pTop);
        pStack->pTop = pPrev;
    }

    return;
}

void stack_delete(Stack* pStack)
{
    stack_clear(pStack);
    free(pStack);
}

void stack_push(Stack* pStack, value_type val)
{
    Entry* pEntry = (Entry*) malloc(sizeof(Entry));
    pEntry->val = val;
    pEntry->link.pPrev = pStack->pTop;
    pStack->pTop = pEntry;
    pStack->nSize++;
    return;
}

value_type* stack_pop(Stack* pStack)
{
    value_type* pRet = NULL;
    if(pStack->pTop)
    {
        Entry* pTemp = pStack->pTop;
        pRet = &(pTemp->val);
        pStack->pTop = pTemp->link.pPrev;
        free(pTemp);
        pStack->nSize--;
    }
    return pRet;
}

value_type* stack_peek(Stack* pStack)
{
    if(pStack->pTop)
        return &(pStack->pTop->val);
    else
        return NULL;
}

int main(int argc, char** argv)
{
    int nRet = 0;

    if(argc < 2)
        exit(0);

    /* number of push and pops */
    int count = atoi(argv[1]);

    /* calculate the step size to limit the number of printfs */
    int step = 1;
    if(1)
    {
        int temp = count;
        while(temp)
        {
            temp /= 10;
            if(temp >= 10)
                step *= 10;
        }
    }

    Stack* pStack = stack_new();
    int i=0;

    for(i = 0;i<count;i++)
        stack_push(pStack, i);

    int x,y;
    for(i = 0;i<count;i++)
    {
        x = *(stack_peek(pStack));
        y = *(stack_pop(pStack));
        if((i < 10) || (i%step == 0))
        {
            printf("%d,%d - %d, %d\n", i,pStack->nSize, x, y);
        }
    }

    stack_delete(pStack);

    return nRet;
}

