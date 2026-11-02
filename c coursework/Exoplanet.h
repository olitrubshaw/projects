//header file for adt representing exoplanets
#ifndef EXOPLANET_H
#define EXOPLANET_H

typedef struct ExoplanetStruct Exoplanet;
//initialise fields from txt file
Exoplanet* exoplanet_parse(const char *str);
//de-initialises field from the heap
void exoplanet_free(Exoplanet* planet);
//to_string to convert all data from txt file to string
const char* exoplanet_toString(const Exoplanet *planet);
//accessors
const char* exoplanet_getName(const Exoplanet *planet);
const char* exoplanet_getSystem(const Exoplanet *planet);
const char* exoplanet_getMethod(const Exoplanet *planet);
int exoplanet_getYear(const Exoplanet* planet);
const char* exoplanet_getFacility(const Exoplanet *planet);
double exoplanet_getRadius(const Exoplanet *planet);
double exoplanet_getMass(const Exoplanet *planet);
int exoplanet_getTemperature(const Exoplanet *planet);
double exoplanet_getHabitability(const Exoplanet *planet);
//function to set the habitability of an exoplanet
void exoplanet_setHabitability(Exoplanet *planet, double habitability);
//comparator for list_sort, printing in descending order of habitability
int exoplanet_descendingByHabitability(const Exoplanet *a, const Exoplanet *b);
#endif