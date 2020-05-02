#include "lists.h"

/**
 * add_dnodeint_end - adds a new node at the end of a dlistint_t list.
 * @head: Points to the head that points to the node that is the head
 * of the list
 * @n: Integer value of the new node
 * Return: the address of the new element, or NULL if it failed
 */
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *current, *new;

	if (head == NULL)
		return (NULL);
	new = malloc(sizeof(dlistint_t));
	if (new == NULL)
		return (NULL);
	current = *head, new->n = n;
	/* sera la cabeza del nodo */
	if (*head == NULL)
	{
		new->next = new->prev = NULL, *head = new;
		return (*head);
	}
	while (current->next)
		current = current->next;

	if (current->next == NULL)
	{
		current->next = new, new->next = NULL, new->prev = current;
		return (*head);
	}
	else
		return (NULL);
}
