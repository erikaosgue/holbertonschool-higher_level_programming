#include "lists.h"
#include <time.h>

listint_t *palindrome(listint_t *tail, listint_t *head);

/**
 *palindrome - this function evaluates if singly linked list is palindrome
 *@head: head of the singly linked list
 *@tail: tail of the end of the  linked list
 *Return: 0 if it is not palidrome or 1 if it is palindrome
 */
listint_t *palindrome(listint_t *tail, listint_t *head)
{

	if (tail->next != 0)
		head = palindrome(tail->next, head);
	if (head != 0)
	{
		if (head->next == 0)
			return (tail);
		if (head->n == tail->n)
			return (head->next);
	}
	return (0);
}

/**
 *is_palindrome - this function evaluates if singly linked list is palindrome
 *@head: head of the singly linked list
 *Return: 0 if it is not palidrome or 1 if it is palindrome
 */
int is_palindrome(listint_t **head)
{

	if (head[0] == 0)
		return (1);
	if (palindrome(head[0], head[0]) == 0)
		return (0);

	return (1);
}
