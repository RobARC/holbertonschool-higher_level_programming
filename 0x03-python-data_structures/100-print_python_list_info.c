#include <stdio.h>
#include <Python.h>
/**
*print_python_list_info - function in C that print info about Pyt    hon lists.
*@p: Pointer to Pyobjetc
*
*/
void print_python_list_info(PyObject *p)
{
long int size, i;
PyListObject *list; /* represent list python object */
PyObject *item; /* pointer like object pyhton */
size = Py_SIZE(p); /* access the ob_size member of a Python object    */
	printf("[*] Size of the Pyhton List = %ld\n", size);
	/*print the list size */

	list = (PyListObject *)p;/* define list like list python object*/

	printf("[*] Allocated = %ld\n", list->allocated);
	/* print how many allocated are */

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
	/*Return the object at position index in the list pointed to by list.*/
	printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	/*print each element with it type */
	}
}

