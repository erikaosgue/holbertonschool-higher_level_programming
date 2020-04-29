#include "lists.h"
#include <stdio.h>
/**
 * insert_node - Add a ned node sorted by the number
 * @head: Points to the head of the node of the list
 * @number: The int of the new node that is going to be add
 * Return: the address of the New node, NULL otherwise
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *previous, *current;

	if (head == NULL)
		return (NULL);

	previous = *head;
	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (current == NULL)
	{ *head = new;
		return (new);
	}
	if (number < current->n)
	{ new->next = current;
		*head = new;
		return (new);
	}
	while (current)
	{
		if (current->n >= number)
		{ new->next = current;
			previous->next = new;
			return (new);
		}
		else
		{ previous = current;
			current = current->next;
			if (current->next == NULL)
			{
				new->next = NULL;
				current->next = new;
				return (new);
			}
		}
	}
	return (NULL);
}
