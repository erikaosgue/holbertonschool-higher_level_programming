#include "lists.h"

/**
 * dlistint_len - Count the number of elements in a linked dlistint_t list
 * @h:Points to the node which is the head of the list
 * Return: the number of elements in a linked dlistint_t list.
 */
size_t dlistint_len(const dlistint_t *h)
{
	size_t count_node = 0;

	if (h == NULL)
		return (0);
	while (h)
	{
		count_node += 1;
		h = h->next;
	}
	return (count_node);
}
