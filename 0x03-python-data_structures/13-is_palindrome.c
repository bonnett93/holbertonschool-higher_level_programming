#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to list head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int i, j, len = 0;
	listint_t *tmp, *final;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	final = *head;
	while (final->next != NULL)
	{
		final = final->next;
		len++;
	}
	tmp = *head;
	for (i = 0; tmp < final; i++)
	{
		final = tmp;
		for (j = 0; j < len; j++)
			final = final->next;
		if (tmp->n != final->n)
			return (0);
		tmp = tmp->next;
		len -= 2;
	}
	return (1);
}
