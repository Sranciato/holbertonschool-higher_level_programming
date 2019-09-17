#include "lists.h"
/**
 * is_palindrome - checks if list is palindrome.
 * @head: beginning of list.
 * Return: 1 if true, 0 if false.
 */
int is_palindrome(listint_t **head)
{
	listint_t *start = *head, *length = *head;
	listint_t *list_half = *head;
	int len = 0, half = 0;

	if (!length)
		return (1);
	while (length)
	{
		len++;
		length = length->next;
	}
	while (half < len / 2)
	{
		half++;
		list_half = list_half->next;
	}
	while (half < len / 2)
	{
		if (start->n != list_half->n)
			return (0);
		list_half = list_half->next;
	}
	return (1);
}
