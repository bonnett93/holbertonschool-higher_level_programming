#include "lists.h"
/*
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: Pointer to linkedlist head.
*/
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	if (list == NULL || list->next == NULL)
		return (0);

	while(fast->next != NULL && fast->next->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (fast == slow)
			return (1);
	}

	return (0);
}
