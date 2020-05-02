#include "lists.h"

/**
 * get_dnodeint_at_index - Find the nth node of a dlistint_t linked list.
 * @head: Points to the head that points to the node that is the head
 * @index:  is the index of the node, starting from 0
 * Return: the nth node of a dlistint_t linked list
 * if the node does not exist, return NULL
 */
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	unsigned int count = 0;
	dlistint_t *current = head;

	while (current)
	{
		if (index == count)
			return (current);
		current = current->next;
		count += 1;
	}
	return (NULL);
}
