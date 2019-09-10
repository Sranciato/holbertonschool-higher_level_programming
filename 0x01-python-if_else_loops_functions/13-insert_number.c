#include "lists.h"
/**
 * insert_node - insert node into sorted list.
 * @head: beginning of list.
 * @number: number to be added to list.
 * Return: new inserted node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *search = *head;

	if (*head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	if (search->n > number)
	{
		new->n = number;
		new->next = *head;
		*head = new;
		return (new);
	}
	while (search)
	{
		if (search->n <= number && search->next->n >= number)
		{
			new->n = number;
			new->next = search->next;
			search->next = new;
			return (new);
		}
		if (search->next->next == NULL)
		{
			if (search->n < number)
			{
				new->n = number;
				new->next = NULL;
				search->next = new;
				return (new);
			}
		}
		search = search->next;
	}
	free(new);
	return (NULL);
}
