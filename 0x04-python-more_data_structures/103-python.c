#define PY_SSIZE_T_CLEAN
#include <python3.4/Python.h>
/**
 * print_python_bytes - prints basic pyobject
 * @p: PyObject list
 *
 */
void print_python_bytes(PyObject *p)
{
	int size, i;
	PyObject *obj;

	size = Py_SIZE(p);


	for (i = 0; i < size; i++)
	{
		obj = PyList_GetItem(p, i);
		printf("[.] bytes object info\n");
		printf("  size: %d\n", PyBytes_GET_SIZE(obj));
		printf("  trying string: %s\n", Py_TYPE(obj)->tp_name);
		printf("  first %d bytes: %x\n", PySIZE(obj),
		       PyBytes_AS_STRING(obj));
	}

}

/**
 * print_python_lists - prints basic pythonlist
 * @p: PyObject list
 *
 */
void print_python_list(PyObject *p)
{
	int size, alloc, i;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);
		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
