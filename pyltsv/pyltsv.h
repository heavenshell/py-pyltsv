#include <Python.h>

#define VERSION "0.1"

#ifdef DEVELOP
#define DEBUG(...) \
    do { \
        printf("DEBUG %s %s %u:", __FILE__, __func__, __LINE__); \
        printf(__VA_ARGS__); \
        printf("\n"); \
    } while (0)
#else
#define DEBUG(...) do {} while (0)
#endif
