#include "lists.h"

/**
 * is_palindrome - checks if list is a palindrome
 * @head: pointer to head node
 * Return: 0 if it is not a palindrome, 1 if it is
 * a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *second_half;

	listint_t *fptr = *head;
	listint_t *sptr = *head;
	listint_t *prev_of_sptr = *head;
	listint_t *midnode = NULL;
	int res = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fptr != NULL && fptr->next != NULL)
		{
			fptr = fptr->next->next;
			prev_of_sptr = sptr;
			sptr = sptr->next;
		}
		if (fptr != NULL)
		{
			midnode = sptr;
			sptr = sptr->next;
		}
		second_half = sptr;
		prev_of_sptr->next = NULL;
		reverse(&second_half);
		res = compareLists(*head, second_half);
		reverse(&second_half);
		if (midnode != NULL)
		{
			prev_of_sptr->next = midnode;
			midnode->next = second_half;
		}
		else
			prev_of_sptr->next = second_half;
	}
	return (res);
}
/**
 * reverse - reverses a head
 * @head: node head
 */
void reverse(listint_t **head)
{
	listint_t *next;

	listint_t *prev = NULL;
	listint_t *current = *head;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}
/**
 * compareLists - compares a list
 * @head1: head one
 * @head2: head two
 * Return: 1 if same, 0 if otherwise
 */
int compareLists(listint_t *head1, listint_t *head2)
{
	listint_t *t1 = head1;
	listint_t *t2 = head2;

	while (t1 && t2)
	{
		if (t1->n == t2->n)
		{
			t1 = t1->next;
			t2 = t2->next;
		}
		else
			return (0);
	}
	if (t1 == NULL && t2 == NULL)
		return (1);

	return (0);
}
