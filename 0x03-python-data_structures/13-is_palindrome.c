#include "lists.h"
#include "lists.h"
/**
 * reverse - reverse list
 * @head_ref: list to reverse
 * Return: Nothing
 */
void reverse(listint_t **head_ref)
{
	listint_t *prev = NULL;
	listint_t *current = *head_ref;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head_ref = prev;
}
/**
 * is_palindrome - is_palindrome
 * @head: list
 * Return: 1 if list is palindrome 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *list_a = *head, *list_b = NULL;
	int count = 1, len = 0;

	if (head == NULL || *head == NULL)
		return (1);

	while (list_a != NULL)
		list_a = list_a->next, len++;
	if (len == 1)
		return (1);

	len = len % 2;
	while ((*head) != NULL)
	{
		add_nodeint_end(&list_b, (*head)->n);
		if (count >= len)
		{
			break;
		}
		(*head) = (*head)->next;
		count++;
	}

	reverse(&list_b);
	while (list_b != NULL)
	{
		if ((*head)->n != list_b->n)
			return (0);
		list_b = list_b->next;
		(*head) = (*head)->next;
		count++;
	}
	free(list_b);
	return (1);
}
