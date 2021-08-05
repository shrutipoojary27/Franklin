#include <stdio.h>

int hammingDist(char *str1, char *str2)
{
    int i = 0, count = 0;
    while (str1[i] != '\0')
    {
        if (str1[i] != str2[i])
            count++;
        i++;
    }
    return count;
}

int main()
{char name[20] = "Edward Lampoh";
 char email[30] = "dredielam@gmail.com";
 char slack[20] = "@Eddie";
 char biostack[20] = "Software Development";
 char twitter[20] = "@edd_guardiola";
 int d;
 d = hammingDist(slack, twitter);
 printf("%s, %s, %s, %s, %s, %d", name, email, slack, biostack, twitter, d);

 return (0);
}

