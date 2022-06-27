#include "lists.h"
/**
 * check_cycle - checks cyle of linked list
 * @list: linked list
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr = malloc(sizeof(listint_t));

	ptr = list;
	if (list == NULL)
		return (1);
	while (ptr != NULL)
	{
		ptr = ptr->next;
		if (ptr == list)
			return (1);
	}
	return (0);
}
