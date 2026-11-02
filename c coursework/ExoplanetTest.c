#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include "Exoplanet.h"

static bool check(bool cond, const char *what) {
    if (!cond) fprintf(stderr, "Fail: %s\n", what);
    return cond;
}

bool testExoplanet(void) {
    bool ok = true;

    // test 1: parse a line from the txt file and check every field
    Exoplanet *a = exoplanet_parse(
        "\"PDS 70 b\", \"PDS 70\", \"Imaging\", 2018, \"Paranal Observatory\", ""30.488, 953.490, 1204, 0.0000\n");
    if (!check(a != NULL, "valid line")) return false;
    //reference for strcmp: https://www.w3schools.com/c/ref_string_strcmp.php
    //strcmp used to verify that values of the strings are identical, returning 0
    ok &= check(strcmp(exoplanet_getName(a), "PDS 70 b") == 0, "name");
    ok &= check(strcmp(exoplanet_getSystem(a), "PDS 70") == 0, "system");
    ok &= check(strcmp(exoplanet_getMethod(a), "Imaging") == 0, "method");
    ok &= check(exoplanet_getYear(a) == 2018, "year");
    ok &= check(strcmp(exoplanet_getFacility(a), "Paranal Observatory") == 0, "facility");
    ok &= check(fabs(exoplanet_getRadius(a) - 30.488) < 1e-9, "radius");
    ok &= check(fabs(exoplanet_getMass(a) - 953.490) < 1e-9, "mass");
    ok &= check(exoplanet_getTemperature(a) == 1204, "temperature");
    ok &= check(exoplanet_getHabitability(a) == 0.0, "habitability");

    // test 2: a comma must not split the field
    Exoplanet *c = exoplanet_parse(
        "\"WASP-148, b\", \"WASP-148\", \"Transit\", 2020, \"SuperWASP-North\", "
        "8.093, 92.489, 940, 0.5000");
    ok &= check(c != NULL && strcmp(exoplanet_getName(c), "WASP-148, b") == 0
                && fabs(exoplanet_getHabitability(c) - 0.5) < 1e-9,
                "comma in name");

    // test 3: set and get
    exoplanet_setHabitability(a, 0.8);
    ok &= check(fabs(exoplanet_getHabitability(a) - 0.8) < 1e-12, "set habitability");

    // test 4: toString matches the txt format and parsse
    exoplanet_setHabitability(a, 0.1234);
    const char *s = exoplanet_toString(a);
    ok &= check(strcmp(s, "\"PDS 70 b\", \"PDS 70\", \"Imaging\", 2018, ""\"Paranal Observatory\", 30.488, 953.490, 1204, 0.1234") == 0,
                "toString format");
    Exoplanet *b = exoplanet_parse(s);
    ok &= check(b != NULL && strcmp(exoplanet_getName(b), "PDS 70 b") == 0
                && exoplanet_getTemperature(b) == 1204
                && fabs(exoplanet_getHabitability(b) - 0.1234) < 1e-9,
                "round trip");

    // test 5: descending comparator test
    exoplanet_setHabitability(a, 0.3);
    if (b != NULL) exoplanet_setHabitability(b, 0.7);
    ok &= check(b != NULL && exoplanet_descendingByHabitability(a, b) > 0,
                "descending comparator a < b");
    ok &= check(b != NULL && exoplanet_descendingByHabitability(b, a) < 0,
                "descending comparator a > b");
    ok &= check(exoplanet_descendingByHabitability(a, a) == 0,
                "descending comparator equal");

    // test 6: invalid input test
    ok &= check(exoplanet_parse(NULL) == NULL, "parse null");
    ok &= check(exoplanet_parse("") == NULL, "parse empty");
    ok &= check(exoplanet_parse("\"a\", \"b\", \"c\"") == NULL, "too few fields");
    ok &= check(exoplanet_parse("\"a\", \"b\", \"c\", 1, \"d\", 1, 1, 1, 0, 9") == NULL,
                "too many fields");
    ok &= check(exoplanet_parse("\"a\", \"b\", \"c\", xx, \"d\", 1, 1, 1, 0") == NULL,
                "invalid year format");
    ok &= check(exoplanet_parse("\"a, \"b\", \"c\", 1, \"d\", 1, 1, 1, 0") == NULL,
                "unbalanced quotes");

    // free memory
    exoplanet_free(a);
    exoplanet_free(b);
    exoplanet_free(c);
    exoplanet_free(NULL);

    return ok;
}