
#include <stdlib.h>
#include <stdio.h>

int main()
{
    ssize_t read_bytes;

    char inputbuffer[40];

    puts("Give me your password: ");
    read_bytes = read(0, inputbuffer, 0x1f);
    inputbuffer[(int)read_bytes + -1] = '\0';
    int index = 0;

    
    for(int i=0;i<read_bytes -1 ;i++){
        printf("%c\t",inputbuffer[i]);
    }
    puts("\n");
    while (index < (int)read_bytes + -1) {
        inputbuffer[index] = (inputbuffer[index] ^ (char)index + 10U) - 2;
        index = index + 1;
    }
  // lp`7a<qLw\x1ekHopt(f-f*,o}V\x0f\x15J
    for(int i=0;i<read_bytes -1 ;i++){
        printf("%d|%c\t",inputbuffer[i],inputbuffer[i]);
    }
    return 0;
}