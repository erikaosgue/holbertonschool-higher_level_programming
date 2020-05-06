#include "lists.h"

/**
 * is_palindrome -  checks if a singly linked list is a palindrome
 * @head: points to the head of the node
 * Return: 1 if it is palidrome or 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL)
		return (1);
	else
		return (palindrome_verification(head));
}
/**
 * palindrome_verification - verifies if the list is polindrome
 * @head: points to the head of the node
 * Return: 1 if it is palidrome or 0 otherwise
 */
int palindrome_verification(listint_t **head)
{
	listint_t *current_node = NULL, *head_ = NULL;
	listint_t *main_head = *head;
	int i;
	int len_list = 0, is_palindrome = 1;
	int midpoint = 0;

	len_list = listint_len(main_head);
	midpoint = len_list / 2;

	for (i = 0; i < len_list; i++)
	{
		if (i < midpoint)
			current_node = add_nodeint(&head_, main_head->n);
		else if (i == midpoint && len_list % 2 == 1)
		{	main_head = main_head->next;
			continue;
		}
		else
		{

			if (current_node->n != main_head->n)
			{
				is_palindrome = 0;
				break;
			}
			current_node = pop_listint(&head_);
		}
		main_head = main_head->next;
	}
	if (!is_palindrome)
		free_listint(head_);
	return (is_palindrome);
}
/**
 * listint_len - function that prints all the elements of a listint_t list.
 * @h: Address of the head pointer
 * Return: the number of nodes there are in the list
 */
int listint_len(listint_t *h)
{
	listint_t *t;
	int i;

	t = h;

	for (i = 0; t != NULL; i++)
		t = t->next;
	return (i);
}

/**
 * add_nodeint - adds a new node at the beginning of a listint_t list.
 * @head: Its the pointer to the Address of the head pointer
 * @n: its the data of the node (an int)
 * Return: the address of the new element, or NULL if it failed
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = *head;
	*head = new;
	return (new);


}
/**
 * pop_listint - deletes the head node of a listint_t linked list
 * @head: Its a double pointer to the addres of the head pointer
 * Return: the head node’s data (n -> int).
 */
listint_t *pop_listint(listint_t **head)
{
	listint_t *t;

	if (*head == NULL)
		return (0);
	t = (*head);
	(*head) = (*head)->next;
	free(t);
	return (*head);
}
