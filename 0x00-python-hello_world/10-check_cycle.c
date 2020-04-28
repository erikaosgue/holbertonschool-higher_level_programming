#include "lists.h"
/**
 * check_cycle - checks if a list has a cicle or loop in it
 * @list: the list of nodes
 * Return: 1 if there is a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	if (list == NULL)
		return (0);
	while (list->next)
	{
		if ((list - (list->next)) <= 0)
			return (1);
		list = list->next;
	}
	return (0);
}
