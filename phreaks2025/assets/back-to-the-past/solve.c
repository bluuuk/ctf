#include <stdio.h> 
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

uint64_t seed = 0;

uint64_t my_srand(int32_t arg1)
{
    uint64_t result = (uint64_t)(arg1 - 1);
    seed = result;
    return result;
}


uint64_t my_rand()
{
    uint64_t rax_1 = 0x5851f42d4c957f2d * seed + 1;
    seed = rax_1;
    return rax_1 >> 0x21;
}

int main(){ 
    /*
        stime = "01/05/2024"
        etime = "31/05/2024"

        start = datetime.datetime.strptime(stime, "%d/%m/%Y").replace(tzinfo=datetime.timezone.utc).timestamp()
        end = datetime.datetime.strptime(etime, "%d/%m/%Y").replace(tzinfo=datetime.timezone.utc).timestamp()
    */
    uint64_t start = 1714521600;
    uint64_t end = 1717113600;

    FILE *file = fopen("flag.enc", "rb"); // Open file in binary read mode
    if (file == NULL) {
        puts("Failed to open file");
        exit(1);
    }

    fseek(file, 0, SEEK_END);
    long file_size = ftell(file);
    rewind(file);

    char *ciphertext = (char *)malloc((file_size + 1) * sizeof(char));
    if (ciphertext == NULL) {
        puts("Memory allocation failed");
        fclose(file);
        exit(1);
    }

    size_t bytes_read = fread(ciphertext, sizeof(char), file_size, file);
    if (bytes_read != file_size) {
        puts("Failed to read the complete file");
        free(ciphertext);
        fclose(file);
        exit(1);
    }

    ciphertext[file_size] = '\0'; 
    fclose(file);

    #define BUFFER_SIZE 6
    const char* plaintext = "PWNME{";

    
    unsigned char compare[BUFFER_SIZE] = {};
    for(uint64_t test_seed=start;test_seed<end;test_seed++){
        my_srand(test_seed);
        for(int i=0;i<BUFFER_SIZE;i++){
            int32_t rand = my_rand();
            int32_t rand2 = rand / 0x7f;
            compare[i] = (rand - ((int8_t)(rand2 << 7) - rand2)) ^ ciphertext[i];
        }
        if(strncmp(plaintext, compare, BUFFER_SIZE) == 0){
            printf("found %d\n",test_seed);
            my_srand(test_seed);
            for(int j=0;j<file_size;j++){
                int32_t rand = my_rand();
                int32_t rand2 = rand / 0x7f;
                printf("%c",(rand - ((int8_t)(rand2 << 7) - rand2)) ^ ciphertext[j]);
            }
            puts("\n");
        }
    }
    puts("done");
} 

