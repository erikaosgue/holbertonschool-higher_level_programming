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
	dlistint_t *head_dlink = NULL, *head_to_free = NULL, *tail = NULL;
	dlistint_t *node_added = NULL, *head_ = NULL;
	listint_t *main_head = *head;
	int num_nodos = 0;

	while (main_head)
	{
		node_added = add_dnodeint(&head_dlink, main_head->n);
		num_nodos++;
		if (num_nodos == 1)
			tail = node_added;
		main_head = main_head->next;
	}
	head_to_free = head_ = head_dlink;
	while (head_)
	{
		if (head_->n == tail->n)
		{
			if (num_nodos % 2 == 0 && head_->next == tail)
			{
				free_dlistint(head_to_free);
				return (1);
			}
			else if (num_nodos % 2 != 0 && head_ == tail)
			{
				free_dlistint(head_to_free);
				return (1);
			}
			head_ = head_->next;
			tail = tail->prev;
		}
		else
			break;
	}
	free_dlistint(head_to_free);
	return (0);
}

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

/**
 * add_dnodeint - adds a new node at the beginning of a dlistint_t list
 * @head: Points to the head that points to the node that is the head
 * of the list
 * @n: Integer value of the new node
 * Return: the address of the new element, or NULL if it failed
 */
dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *current;
	dlistint_t *new;

	if (head == NULL)
		return (NULL);
	current = *head;
	new = malloc(sizeof(dlistint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->prev = NULL;

	if (current == NULL)
	{
		new->next = NULL;
		*head = new;
		return (new);
	}
	current->prev = new;
	new->next = current;
	*head = new;
	return (new);
}
