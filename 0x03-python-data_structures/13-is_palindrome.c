#include "lists.h"

/**
 * is_palindrome - checks if list is a palindrome
 * @head: pointer to head node
 * Return: 0 if it is not a palindrome, 1 if it is
 * a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *fptr = *head;
	listint_t *sptr = *head;

	if (*head == NULL)
		return (1);

	while (fptr != NULL && fptr->next != NULL && sptr != NULL)
	{
		sptr = sptr->next;
		fptr = fptr->next->next;

		if (fptr->n == sptr->n)
			return (1);
	}

	return (0);
}
