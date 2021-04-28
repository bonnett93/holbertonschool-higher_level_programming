#include "lists.h"
/*
 * insert_node - 
 * @head:
 * @number:
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *tmp = *head;

	if (head == NULL || *head == NULL)
		return (0);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (0);
	new->n = number;
	if (number < tmp->n)
	{
		new->next = tmp;
		*head = new;
		return (new);
	}
	while (tmp->next != NULL)
	{
		if (number <= tmp->next->n)
		{
			new->next = tmp->next;
			tmp->next = new;
			return (new);
		}
		tmp = tmp->next;
	}
	tmp->next = new;
	return (new);
}
