#include "lists.h"
/**
 *check_cycle - checks a singly linked list if it has a loop
 *@fast - pointer that will iterate through a list 2 items at a time
 *@slow: pointer that will iterate through a list
 *Return: if it has a cycle(1) else (0)
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (fast == slow)
		{
			return (1);
		}
	}
	return (0);
}
