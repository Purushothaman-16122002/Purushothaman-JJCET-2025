"""Luke is daydreaming in Math class. He has a sheet of graph paper with  rows and  columns, and he imagines that there is an army base in each cell for a total of  bases. 
He wants to drop supplies at strategic points on the sheet, marking each drop point with a red dot.
If a base contains at least one package inside or on top of its border fence, then it's considered to be supplied. For example:

image

Given n and m, what's the minimum number of packages that Luke must drop to supply all of his bases?

Example
n=2
m=3
Packages can be dropped at the corner between cells (0, 0), (0, 1), (1, 0) and (1, 1) to supply 4 bases.
Another package can be dropped at a border between (0, 2) and (1, 2). This supplies all bases using 2 packages.

Function Description

Complete the gameWithCells function in the editor below.

gameWithCells has the following parameters:

int n: the number of rows in the game
int m: the number of columns in the game
Returns

int: the minimum number of packages required
Input Format

Two space-separated integers describing the respective values of n and m.

Constraints
0<n,m<=1000

Sample Input 0

2 2
Sample Output 0

1
Explanation 0

Luke has four bases in a 2*2 grid. If he drops a single package where the walls of all four bases intersect, then those four cells can access the package:

image

Because he managed to supply all four bases with a single supply drop, we print 1 as our answer.
"""

#include <assert.h>
#include <ctype.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* readline();
char* ltrim(char*);
char* rtrim(char*);
char** split_string(char*);

int parse_int(char*);

/*
 * Complete the 'gameWithCells' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER m
 */

int gameWithCells(int n, int m) {

}

int main()
{
    FILE* fptr = fopen(getenv("OUTPUT_PATH"), "w");

    char** first_multiple_input = split_string(rtrim(readline()));

    int n = parse_int(*(first_multiple_input + 0));

    int m = parse_int(*(first_multiple_input + 1));

    int result = gameWithCells(n, m);

    fprintf(fptr, "%d\n", result);

    fclose(fptr);

    return 0;
}

char* readline() {
    size_t alloc_length = 1024;
    size_t data_length = 0;

    char* data = malloc(alloc_length);

    while (true) {
        char* cursor = data + data_length;
        char* line = fgets(cursor, alloc_length - data_length, stdin);

        if (!line) {
            break;
        }

        data_length += strlen(cursor);

        if (data_length < alloc_length - 1 || data[data_length - 1] == '\n') {
            break;
        }

        alloc_length <<= 1;

        data = realloc(data, alloc_length);

        if (!data) {
            data = '\0';

            break;
        }
    }

    if (data[data_length - 1] == '\n') {
        data[data_length - 1] = '\0';

        data = realloc(data, data_length);

        if (!data) {
            data = '\0';
        }
    } else {
        data = realloc(data, data_length + 1);

        if (!data) {
            data = '\0';
        } else {
            data[data_length] = '\0';
        }
    }

    return data;
}

char* ltrim(char* str) {
    if (!str) {
        return '\0';
    }

    if (!*str) {
        return str;
    }

    while (*str != '\0' && isspace(*str)) {
        str++;
    }

    return str;
}

char* rtrim(char* str) {
    if (!str) {
        return '\0';
    }

    if (!*str) {
        return str;
    }

    char* end = str + strlen(str) - 1;

    while (end >= str && isspace(*end)) {
        end--;
    }

    *(end + 1) = '\0';

    return str;
}

char** split_string(char* str) {
    char** splits = NULL;
    char* token = strtok(str, " ");

    int spaces = 0;

    while (token) {
        splits = realloc(splits, sizeof(char*) * ++spaces);

        if (!splits) {
            return splits;
        }

        splits[spaces - 1] = token;

        token = strtok(NULL, " ");
    }

    return splits;
}

int parse_int(char* str) {
    char* endptr;
    int value = strtol(str, &endptr, 10);

    if (endptr == str || *endptr != '\0') {
        exit(EXIT_FAILURE);
    }

    return value;
}
