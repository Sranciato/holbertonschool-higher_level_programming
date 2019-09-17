#include "lists.h"
/**
 * is_palindrome - checks if list is palindrome.
 * @head: beginning of list.
 * Return: 1 if true, 0 if false.
 */
int is_palindrome(listint_t **head)
{
	listint_t *start = *head, *length = *head;
	listint_t *end = *head, *restart = *head;
	int len = 0, i = 0, j;

	if (!length)
		return (1);
	while (length)
	{
		len++;
		length = length->next;
	}
	while (i < len / 2)
	{
		j = i;
		while (j < len - 1)
		{
			end = end->next;
			j++;
		}
		if (start->n != end->n)
			return (0);
		end = restart;
		start = start->next;
		i++;
	}
	return (1);
}
