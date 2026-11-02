/******************************************************************************

File        : List.c

Date        : Wednesday 14th October 2026

Author      : Gavin Cawley

Description : Implementation of a basic singly-linked list of pointers to
              Exoplanet structures.

History     : 14/10/2026 - v1.00 Initial prototype

******************************************************************************/
//bug fix: included <stdbool.h> for bool arguments
#include <stdlib.h>
#include <stdbool.h>
//bug fix: was a const using variable array size not valid in all instances
//changed to a macro for consistency
#define BUFFER_SIZE 1024
#include "List.h"

//bug fix: result of warning because link and list are already typedef in List.h
struct LinkStruct
{
   Exoplanet *planet;

   struct LinkStruct *next;
};

//bug fix: see comment above
struct ListStruct
{
   Link *first;
};

Link* link_new(Exoplanet *planet, Link *next)
{
   Link *link = (Link*)malloc(sizeof(Link));

   //bug fix: malloc result not checked, check for null value to prevent crash
   if (link == NULL) {
      return NULL;
   }
   link->planet = planet;
   link->next   = next;

   return link;
}

void link_free(Link *link)
{
   free(link);
}

List* list_new(void)
{
   List *list = (List*)malloc(sizeof(List));
//bug fix: malloc not checked, check prevents crash
   if (list != NULL) {
      list->first = NULL;
   }
   return list;
}

void list_add(List *list, Exoplanet *planet)
{
   Link *link = link_new(planet, list->first);

   //bug fix: link_new can fail, so null value can cause crash
   // null value check prevents crash
   if (link != NULL) {
      list->first = link;
   }
}

void list_free(List *list)
{
   //bug fix: if value is null, list can be freed without crash
   if (list == NULL) {
      return;
   }
   while (list->first != NULL)
   {
      Link *link = list->first;

      list->first = link->next;

      link_free(link);
   }

   free(list);
}

void list_print(const List *list, FILE *fd)
{
   for (Link *link = list->first; link != NULL; link = link->next)
   {
      fprintf(fd, "%s\n", exoplanet_toString(link->planet));
   }
}

List *list_load(FILE *fd)
{

   char buffer[BUFFER_SIZE];

   //bug fix: null file would be passed straight to fgets
   //check prevents null file pass, preventing crash
   if (fd == NULL) {
      return NULL;
   }

   List *list = list_new();
   if (list == NULL) {
      return NULL;
   }

   while (fgets(buffer, BUFFER_SIZE, fd) != NULL)
   {
      Exoplanet *planet = exoplanet_parse(buffer);

      //bug fix: parse would reject null line added to list, causing a crash
      //null lines now skipped
      if (planet != NULL) {
         list_add(list, planet);
      }
   }

   return list;
}

void list_sort(List *list, Comparator compare)
{
   if (list->first == NULL || list->first->next == NULL)
   {
      return;
   }

   //bug fix: bool sorted caused wrong result, set to true when swapped
   //caused infinite loop, swapped flag lets while loop continue
   bool swapped;

   do
   {
      swapped = false;

      for (Link *link = list->first; link->next != NULL; link=link->next)
      {
         if (compare(link->planet, link->next->planet) > 0)
         {
            Exoplanet *planet  = link->planet;
            link->planet       = link->next->planet;
            link->next->planet = planet;

            swapped = true;
         }
      }
   }
   while (swapped);
}

Iterator list_begin(const List *list)
{
   return list->first;
}

Iterator list_end(const List *list)
{
   //bug fix: unused parameter warning, voided to remove
   (void)list;
   return NULL;
}

Iterator iterator_next(const Iterator iterator)
{
   return iterator->next;
}

Exoplanet* iterator_get(const Iterator iterator)
{
   return iterator->planet;
}

/*****************************************************************************/
