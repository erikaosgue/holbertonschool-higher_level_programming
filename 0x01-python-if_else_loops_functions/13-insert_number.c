#include "lists.h"
/**
 * insert_node - Add a ned node sorted by the number
 * @head: Points to the head of the node of the list
 * @number: The int of the new node that is going to be add
 * Return: the address of the New node, NULL otherwise
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *previous;
	listint_t *current;

	if (head == NULL ||  *head == NULL)
		return (NULL);

	previous = *head;
	current = *head;

	while (current)
	{
		if (current->n >= number)
		{
			new = malloc(sizeof(listint_t));
			if (new == NULL)
				return (NULL);

			new->n = number;
			new->next = current;
			previous->next = new;
			return (new);
		}
		else
		{
			previous = current;
			current = current->next;
		}
	}
	return (NULL);
}
