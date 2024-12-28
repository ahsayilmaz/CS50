// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>
#include "dictionary.h"
#include <strings.h>
#include <stdio.h>
#include <string.h>

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];
node *head=NULL;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int n=0;
    node *temp=NULL;
    int num=hash(word);
    temp=table[num];
    while(temp!=NULL){
        if(strcasecmp(temp->word,word)==0){
            return true;
        }else{
            temp=temp->next;
        }
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    char word[LENGTH +1];
    FILE *f = fopen(dictionary, "r");
    if (f == NULL) {
        return false;
    }
    while(fscanf(f,"%s",word)==1){
        node *new_node=malloc(sizeof(node));
        if(new_node==NULL){
            return 1;
        }
        int first=hash(word);
        strcpy(new_node->word, word);
        new_node->next=table[first];
        table[first]=new_node;
    }
    fclose(f);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    int counter=0;
    int n=0;
    node *temp=NULL;
    temp=table[n];
    while(n<26){
        if(temp==NULL){
            n++;
            while(table[n]==NULL){
                n++;
                if(n==26){
                    return counter;
                }
            }
            temp=table[n];
        }else if(temp!=NULL){
            temp=temp->next;
            counter++;
        }
    }
    return counter;
}



// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    int un=0;
    node *temp=table[un];
    node *freet;
    while(un<26)
    {
        while(temp!=NULL&&un<26){
            freet=temp;
            temp=temp->next;
            free(freet);
        }
        while(temp==NULL&&un<26){
            un++;
            temp=table[un];
        }
    }
    if(un==26){
            return true;
    }else{
        return false;
    }
}
