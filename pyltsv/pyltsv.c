#include "pyltsv.h"

static char*
rstip(char *str)
{
    size_t length = strlen(str);
    if (str[length - 1] == '\n' || str[length - 1] == '\r') {
      str[length - 1] = '\0';
    }

    return str;
}

static long
split(char *str, char *sep, char **output)
{
    // see http://hakobe932.hatenablog.com/entry/20060422/1145705391
    long last = 0;
    char *word = NULL;
    char *str_work = NULL;
    long str_len = strlen(str);
    str_work = (char*)PyMem_Malloc(sizeof(char) * (str_len + 1));
    strcpy(str_work, str);

    last = 0;
    for (word = strtok(str_work, sep); word; word = strtok(NULL, sep), ++last) {
        output[last] = word;
    }
    output[last] = NULL;

    return last;
}

static PyObject*
_parse_line(char *str)
{
    str = rstip(str);
    size_t str_len = strlen(str);
    char **tabs = (char**)PyMem_Malloc(sizeof(char*) * (str_len + 1));
    if (tabs == NULL) {
        PyErr_NoMemory();
        return NULL;
    }

    // Split tab.
    long tab_cnt = split(str, "\t", tabs);

    PyObject *dict = PyDict_New();
    if (dict == NULL) {
        return NULL;
    }
    Py_INCREF(dict);

    long i;
    for (i = 0; i < tab_cnt; ++ i) {
        size_t kv_len = strlen(tabs[i]);
        char *kv = (char*)PyMem_Malloc(sizeof(char*) * (kv_len + 1));
        strcpy(kv, tabs[i]);

        char *pos;
        pos = strstr(kv, ":");
        if (pos == NULL) {
            continue;
        }
        size_t value_len = strlen(pos);

        char *value = (char*)PyMem_Malloc(sizeof(char*) * (value_len + 1));
        strcpy(value, &pos[1]);

        size_t key_len = pos - kv;
        char *key = (char*)PyMem_Malloc(sizeof(char*) * (key_len + 1));
        key = strtok(kv, ":");

        // Create dict and add to list.
        PyObject *dict_value = PyString_FromString(value);
        PyDict_SetItemString(dict, key, dict_value);

        DEBUG("%ld: key is %s, val is %s\n-----------------\n", i, key, value);

        PyMem_Free((void*)key);
        PyMem_Free((void*)value);
    }

    return dict;
}

static PyObject*
parse_line(PyObject *self, PyObject *args)
{
    char *str;
    if (!PyArg_ParseTuple(args, "s", &str)) {
        return NULL;
    }
    return _parse_line(str);
}

static PyObject*
parse_file(PyObject *self, PyObject *args)
{
    const char *file_name;
    if (!PyArg_ParseTuple(args, "s", &file_name)) {
        return NULL;
    }

    FILE *fp = fopen(file_name, "r");
    long file_size;
    char *file_contents;
    if (!fp) {
        PyErr_SetString(PyExc_IOError, "LTSV file not found.");

        return NULL;
    }

    fseek(fp, 0L, SEEK_END);
    file_size = ftell(fp);
    rewind(fp);
    file_contents = (char*)PyMem_Malloc(sizeof(char) * (file_size + 1));
    if (file_contents == NULL) {
        fclose(fp);
        PyMem_Free((void*)file_contents);

        return NULL;
    }
    fread(file_contents, file_size, 1, fp);
    fclose(fp);
    file_contents[file_size] = '\0';

    char **lines = (char**)PyMem_Malloc(sizeof(char*) * (file_size + 1));
    if (lines == NULL) {
        PyErr_NoMemory();
        return NULL;
    }
    long line_cnt = split(file_contents, "\n", lines);

    PyObject *list = PyList_New(line_cnt);
    if (!list) {
        PyMem_Free((void*)file_contents);
        return NULL;
    }
    long i;
    for (i = 0; i < line_cnt; ++ i) {
        PyDict_New();
        PyObject *dict = PyDict_New();
        if (dict == NULL) {
            PyMem_Free((void*)file_contents);
            return NULL;
        }
        Py_INCREF(dict);
        dict = _parse_line(lines[i]);
        PyList_SET_ITEM(list, i, dict);
    }

    PyMem_Free((void*)file_contents);

    return list;
}

static PyMethodDef PyLtsvMethods[] =
{
     {"parse_file", parse_file, METH_VARARGS, "Parse ltsv file."},
     {"parse_line", parse_line, METH_VARARGS, "Parse ltsv line."},
     {NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC
initpyltsv(void)
{
    PyObject *m;
    m = Py_InitModule3("pyltsv", PyLtsvMethods, "Dead simple LTSV parser.");
    if (m == NULL){
        return;
    }
    PyModule_AddStringConstant(m, "__version__", VERSION);
}
