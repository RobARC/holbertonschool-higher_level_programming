#include "lists.h"
/**
*check_cycle - Checks if the single linkedlist contains a cycle.
*@list: pointer to the head of the list.
*Return: 0 if there is no loop. Otherwise 1
*/

int check_cycle(listint_t *list)
{
	
	/*we will use the algorithm turtle and rabbit*/
	
	listint_t *turtle;
	listint_t *rabbit;

	turtle = list;
	rabbit = list;
	
	if(list == NULL) /* if list is equal to NULL there is no loop */
		return(0);

	while (turtle && rabbit && rabbit->next)
	{
		turtle = turtle->next; /* move turtle forward one */
		rabbit = rabbit->next->next; /* move rabbit forward two */
		if (turtle == rabbit) /* if they are equal means loop found */
			return(1);
	}
	return(0); /* loop exit means no loops found */
}
