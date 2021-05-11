#include "lists.h"
#include <limits.h>
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to list head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int i;
	listint_t *tmp, *final;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	final = *head;
	tmp = *head;
	while (final->next != NULL)
		final = final->next;

	for (i = 0; tmp < final; i++)
	{
		if (tmp->n != final->n)
		{
			return (0);
		}
		final -= 2;
		tmp = tmp->next;
	}
	return (1);
}
