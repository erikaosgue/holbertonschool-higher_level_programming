#include "lists.h"
/**
 * delete_dnodeint_at_index - A function that deletes the node
 * at index index of a dlistint_t linked list.
 * @head: Points to the head pointer that points to the head node of the list
 * @index:is the index of the node that should be deleted. Index starts at 0
 * Return:1 if it succeeded, -1 if it failed
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *current = NULL, *previous = NULL, *temp = NULL;
	unsigned int count = 0;

	current = previous = *head;
	if (head == NULL || *head ==  NULL)
		return (-1);
	while (current)
	{
		if (index == 0)
		{
			if (current->next == NULL)
			{
				free(current), *head = NULL;
				return (-1);
			}
			temp = current, current = current->next, free(temp);
			current->prev = NULL, *head = current;
			return (1);
		}
		count += 1, previous = current, current = current->next;
		if (current->next == NULL && index == count)
		{
			previous->next = NULL, free(current);
			return (1);
		}
		if (index == count)
		{
			temp = current, current = current->next, free(temp);
			previous->next = current, current->prev = previous;
			return (1);
		}
	}
	return (-1);
}
