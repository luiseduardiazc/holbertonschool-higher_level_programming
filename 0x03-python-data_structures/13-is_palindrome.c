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
	listint_t *list_a = NULL;
	listint_t *list_b = NULL;
	listint_t *current = *head;

	if (head == NULL || *head == NULL)
		return (1);


	while (current != NULL)
	{
		add_nodeint_end(&list_a, current->n);
		add_nodeint_end(&list_b, current->n);
		current = current->next;
	}
	reverse(&list_b);
	while (list_a != NULL && list_b != NULL)
	{
		if (list_a->n != list_b->n)
			return (0);
		list_a = list_a->next;
		list_b = list_b->next;
	}
	return (1);
}
