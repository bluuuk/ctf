
#include <stdlib.h>
#include <stdio.h>

int main()
{
    ssize_t read_bytes;
    int loop;
    char inputbuffer[40];

    puts("Give me your password: ");
    read_bytes = read(0, inputbuffer, 0x1f);
    inputbuffer[(int)read_bytes + -1] = '\0';
    loop = 0;

    
    for(int i=0;i<read_bytes -1 ;i++){
        printf("%c\t",inputbuffer[i]);
    }
    puts("\n");
    while (loop < (int)read_bytes + -1)
    {
        inputbuffer[loop] =  inputbuffer[loop] + -119;
        loop = loop + 1;
    }
    for(int i=0;i<read_bytes -1 ;i++){
        printf("%d|%c\t",inputbuffer[i],inputbuffer[i]);
    }
    return 0;
}