#include <stdio.h>
#include <stdlib.h>

char *short_input = "1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet";

char *read_file(const char *filename)
{
    FILE *file = fopen(filename, "r");
    if (file == NULL)
    {
        printf("Failed to open file\n");
        return NULL;
    }

    fseek(file, 0, SEEK_END);
    long file_size = ftell(file);
    fseek(file, 0, SEEK_SET);

    char *buffer = (char *)malloc(file_size + 1);
    if (buffer == NULL)
    {
        printf("Failed to allocate memory\n");
        fclose(file);
        return NULL;
    }

    fread(buffer, 1, file_size, file);
    buffer[file_size] = '\0';

    fclose(file);
    return buffer;
}

int sum(char *s)
{
    int sum = 0;
    int first_digit = -1;
    int last_digit = -1;
    while (*s != '\0')
    {
        // printf("Cur char: %c\n", *s);
        if (*s >= '0' && *s <= '9')
        {
            // this is a number
            if (first_digit == -1)
            {
                first_digit = *s - '0';
            }
            last_digit = *s - '0';
        }
        else if (*s == '\n')
        {
            printf("Sum %d, first_digit %d, last_digit %d\n", sum, first_digit, last_digit);
            sum += first_digit * 10 + last_digit;
            first_digit = -1;
            last_digit = -1;
        }
        s++;
    }
    sum += first_digit * 10 + last_digit;
    return sum;
}

int main(void)
{
    printf("Sum: %d\n", sum(short_input));
    char *input = read_file("01.txt");
    printf("Sum: %d\n", sum(input));
    return 0;
}