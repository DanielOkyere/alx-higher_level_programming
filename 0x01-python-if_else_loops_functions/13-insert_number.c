#include "lists.h"
/**
 * insert_node - inserts a node in sorted linked list
 * @head: head node
 * @number: number to be inserted
 * Return: Address of node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *cptr;

	listint_t *new_node_ptr = newNode(number);

	if (new_node_ptr == NULL)
		return (NULL);

	if (*head == NULL || (*head)->n >= new_node_ptr->n)
	{
		new_node_ptr->next = *head;
		*head = new_node_ptr;
	}
	else
	{
		cptr = *head;
		while (cptr->next != NULL && cptr->next->n < new_node_ptr->n)
			cptr = cptr->next;
		new_node_ptr->next = cptr->next;
		cptr->next = new_node_ptr;
	}
	return (new_node_ptr);
}
/**
 * newNode - creates a new node
 * @new_number: New data value
 * Return: new node with data
 */
listint_t *newNode(int new_number)
{
	listint_t *new_node = malloc(sizeof(listint_t));

	new_node->n = new_number;
	new_node->next = NULL;

	return (new_node);
}
