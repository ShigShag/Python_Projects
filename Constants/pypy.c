#include <stdlib.h>
size_t str_len(char *string)
{
    size_t length = 0;
    while (*string != '\0')
    {
        length++;
        string++;
    }
    return length;
}

char* append(char *string, char *value)
{
    size_t len_string = str_len(string) + 1;
    size_t len_value = str_len(value) + 1;


    char* result = (char *) malloc((len_string + len_value - 1) * sizeof(char));
    if(result == NULL)
    {
        free(result);
        return NULL;
    }

    int i = 0;

    while(i < len_string - 1)
    {
        *result = string[i];
        result++;
        i++;
    }
    i = 0;
    while(i < len_value)
    {
        *result = value[i];
        result++;
        i++;
    }

    return result - (len_string + len_value - 1);
}

int main(int argc, char *argv[])
{

    if (argc > 1)
    {
        char *executable_path = "F:\\pypy3.6-v7.3.1-win32\\pypy3.exe ";
		for(int i = 1;i < argc;i++)
		{
			char *command = append(executable_path, argv[i]);
			system(command);
		}
    }
    return 0;
}