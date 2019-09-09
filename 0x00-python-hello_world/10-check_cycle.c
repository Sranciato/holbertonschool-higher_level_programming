#include "lists.h"
/**
 * check_cycle - check if linked list is a loop.
 * @list: head of linked list.
 * Return: 0 if false | 1 if true.
 */
int check_cycle(listint_t *list)
{
	listint_t *turtle, *hare;

	turtle = list;
	hare = list;

	while (turtle && hare && hare->next)
	{
		turtle = turtle->next;
		hare = hare->next->next;
		if (turtle == hare)
			return (1);
	}
	return (0);
}
