#include "lists.h"
/**
 * check_cycle - check the cycle list.
 * @list: list for be checked
 * Return: 0 if list is cycle -1 otherwise.
 */
int check_cycle(listint_t *list)
{
	listint_t *ptrIni = list;
	listint_t *ptrEnd = list;

	if (list == NULL)
	{
		return (-1);
	}
	while (ptrIni && ptrEnd && ptrEnd->next)
	{
		ptrIni = ptrIni->next;
		ptrEnd = ptrEnd->next->next;
		if (ptrIni == ptrEnd)
			return (0);
	}
	return (-1);
}
