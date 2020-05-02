#include "lists.h"

/**
 * insert_dnodeint_at_index - A function that inserts a new node
 * at a given position.
 * @h: Points to the header of the list
 * @idx: is the index of the list where the new node should be added.
 * Index starts at 0
 * @n: Integer as value of the new node
 * Return: the address of the new node, or NULL if it failed
 */
dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n)
{
	dlistint_t *current, *previous = NULL, *new = NULL;
	unsigned int count = 0;

	current = previous = *h;
	if (h == NULL)
		return (NULL);
	new = malloc(sizeof(dlistint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;

	if (*h == NULL && idx == 0)
	{ new->prev = new->next = NULL, *h = new;
		return (*h);
	}
	else if (*h != NULL && current->prev == NULL)
	{
		while (current)
		{
			new->next = current, current->prev = new;
			if (idx == 0)
			{ new->prev = NULL, *h = new;
				return (*h);
			}
			if (idx == count)
			{ new->prev = previous, previous->next = new;
				return (*h);
			}
			count += 1, previous = current, current = current->next;
		}
		/* adding a node at the end of list */
		if (current == NULL && idx == count)
		{
			new->next = NULL, new->prev = previous, previous->next = new;
			return (*h);
		}
	} free(new);
	return (NULL);
}
