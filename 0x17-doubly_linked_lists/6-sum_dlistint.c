#include "lists.h"

/**
 * sum_dlistint -  sum all the data (n) of a dlistint_t linked list.
 * @head: Points to the head that points to the node that is the head
 * Return: the sum of all the data (n) of a dlistint_t linked list.
 */
int sum_dlistint(dlistint_t *head)
{
	dlistint_t *current = head;
	int sum = 0;

	if (head == NULL)
		return (0);

	if (head->next == NULL && head->prev == NULL)
		sum = head->n;

	else if (head->next == NULL)
	{
		while (current)
			sum += current->n, current = current->prev;
	}

	else
	{
		while (current)
			sum += current->n, current = current->next;
	}
	return (sum);
}
