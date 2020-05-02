#include "lists.h"

/**
 * free_dlistint - free a dlistint_t list.
 * @head: Points to the head that points to the node that is the head
 * Return:Nothing
 */
void free_dlistint(dlistint_t *head)
{
	dlistint_t *temp;

	while (head)
	{
		temp = head;
		head = head->next;
		free(temp);
	}
}
