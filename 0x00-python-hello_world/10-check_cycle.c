#include "lists.h"
/**
 * check_cycle - checks cyle of linked list
 * @list: linked list
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fptr = malloc(sizeof(listint_t));
	listint_t *sptr = malloc(sizeof(listint_t));

	fptr = list;
	sptr = list;
	while (fptr != NULL && fptr->next != NULL && sptr != NULL)
	{
		sptr = sptr->next;
		fptr = fptr->next->next;
		if (sptr == fptr)
			return (1);
	}
	return (0);
}
