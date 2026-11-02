#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include "Exoplanet.h"
#define NUM_FIELDS 9
#define TOSTRING_SIZE 1024
//struct defining all variables for exoplanets
struct ExoplanetStruct {
    char *name, *system, *method, *facility;
    int year, temperature;
    double radius, mass, habitability;
};

static char *copyString(const char *s) {
    char *c = malloc(strlen(s) + 1);
    if (c != NULL) strcpy(c, s);
    return c;
}
//removes whitespaces and new lines for nicer output
static void prettyPrint(char *s) {
    size_t n = strlen(s);
    while (n > 0 && isspace((unsigned char)s[n-1])) s[--n] = '\0';
}
//takes the next field from buffer and modifies it
static int nextField(char **cursor, char **out) {
    char *p = *cursor;
    while (*p == ' ' || *p == '\t') p++;
    if (*p == '"') {
        *out = ++p;
        p = strchr(p, '"');
        if (p == NULL) return -1;
        *p++ = '\0';
        while (*p == ' ' || *p == '\t') p++;
        if (*p == ',') {*cursor = p + 1; return 1;}
        if (*p == '\0') {*cursor = p; return 0;}
        return -1;
    }
    *out = p;
    while (*p != '\0' && *p != ',') p++;
    int more = *p == ',';
    *p = '\0';
    if (more) p++;
    prettyPrint(*out);
    *cursor = p;
    return more;
}

//function to convert values to int
static int toInt(const char *s, int *out) {
    char *end;
    //reference for strtol: https://www.tutorialspoint.com/c_standard_library/c_function_strtol.htm
    //used to convert the string value to a long int
    double value = strtol(s, &end, 10);
    if (end == s || *end != '\0') return 0;
    *out = value;
    return 1;
}

//function to convert values to double
static int toDouble(const char *s, double *out) {
    char *end;
    //reference for strtod: https://www.tutorialspoint.com/c_standard_library/c_function_strtod.htm
    //used to convert string value to a double
    double value = strtod(s, &end);
    if (end == s || *end != '\0') return 0;
    *out = value;
    return 1;
}

//function to parse values in txt file
Exoplanet *exoplanet_parse(const char *str) {
    if (str == NULL) return NULL;
    char *work = copyString(str);
    if (work == NULL) return NULL;
    prettyPrint(work);
    char *fields[NUM_FIELDS];
    char *cursor = work;
    int n = 0, more;
    do {
        if (n == NUM_FIELDS) {
            free(work);
            return NULL;
        }
        more = nextField(&cursor, &fields[n]);
        if (more < 0) {
            free(work);
            return NULL;
        }
        n++;
    }
    while (more);
    if (n != NUM_FIELDS) {
        free(work);
        return NULL;
    }
    Exoplanet *e = calloc(1, sizeof(Exoplanet));
    if (e == NULL) {
        free(work);
        return NULL;
    }
    e->name = copyString(fields[0]);
    e->system = copyString(fields[1]);
    e->method = copyString(fields[2]);
    e->facility = copyString(fields[4]);
    int ok = e->name && e->system && e->method
        && e->facility && toInt(fields[3], &e->year)
        && toDouble(fields[5], &e->radius)
        && toDouble(fields[6], &e->mass)
        && toInt(fields[7], &e->temperature)
        && toDouble(fields[8], &e->habitability);
    free(work);
    if (!ok) {
        exoplanet_free(e);
        return NULL;
    }
    return e;
}

void exoplanet_free(Exoplanet *planet) {
    if (planet == NULL) return;
    free(planet->name);
    free(planet->system);
    free(planet->method);
    free(planet->facility);
    free(planet);
}

const char *exoplanet_toString(const Exoplanet *p) {
    static char buffer[TOSTRING_SIZE];
    snprintf(buffer, sizeof buffer,
        "\"%s\", \"%s\", \"%s\", %d, \"%s\", %.3f, %.3f, %d, %.4f",
        p->name, p->system, p->method, p->year, p->facility,
        p->radius, p->mass, p->temperature, p->habitability);
    return buffer;
}

const char *exoplanet_getName(const Exoplanet *p) {
    return p->name;
}
const char *exoplanet_getSystem(const Exoplanet *p) {
    return p->system;
}
const char *exoplanet_getMethod(const Exoplanet *p) {
    return p->method;
}
int exoplanet_getYear(const Exoplanet *p) {
    return p->year;
}
const char *exoplanet_getFacility(const Exoplanet *p) {
    return p->facility;
}
double exoplanet_getRadius(const Exoplanet *p) {
    return p->radius;
}
double exoplanet_getMass(const Exoplanet *p) {
    return p->mass;
}
int exoplanet_getTemperature(const Exoplanet *p) {
    return p->temperature;
}
double exoplanet_getHabitability(const Exoplanet *p) {
    return p->habitability;
}

void exoplanet_setHabitability(Exoplanet *p, double habitability) {
    p->habitability = habitability;
}

//returns positive if a is more inhabitable than b, negative if less, 0 if same for ordering
int exoplanet_descendingByHabitability(const Exoplanet *a, const Exoplanet *b) {
    if (a->habitability < b->habitability) return 1;
    if (a->habitability > b->habitability) return -1;
    return 0;
}