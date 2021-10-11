
void read_notes(char *param_1)

{
    int retval;
    FILE *__stream;
    int counter;

    counter = 0;
    __stream = fopen("notes.txt", "r");
    while (counter < 10)
    {
        retval = __isoc99_fscanf(__stream, "%511[^\n]%*c", param_1 + counter * 0x204);
        if (retval == -1)
            break;
        *(param_1 + counter * 0x204 + 0x200) = 0;
        counter = counter + 1;
    }
    fclose(__stream);
    return;
}

void delete_note(char *param_1)

{
    long in_FS_OFFSET;
    int counter;
    long canary;

    canary = *(long *)(in_FS_OFFSET + 0x28);
    printf("Which note would you like to delete? ");
    __isoc99_scanf("%d", &counter);
    if (counter < 0xb) // 11 kann man noch löschen lol
    {
        *(param_1 + counter * 0x204 + 0x200) = 1;
        puts("Deleted.");
    }
    else
    {
        puts("Out of bounds. Try again.");
    }
    if (canary != *(long *)(in_FS_OFFSET + 0x28))
    {
        /* WARNING: Subroutine does not return */
        __stack_chk_fail();
    }
    return;
}

void add_note(long param_1)

{
    long offset;
    long in_FS_OFFSET;
    int number_of_notes;
    undefined8 local_38;
    long canary = *(long *)(in_FS_OFFSET + 0x28);
    local_38 = 0;
    number_of_notes = 0;

    // count the number of active notes
    while ((number_of_notes < 10 && (*(int *)(param_1 + (long)number_of_notes * 0x204 + 0x200) != 1)))
    {
        number_of_notes = number_of_notes + 1;
    }

    if (number_of_notes < 10)
    {
        printf("Note: ");
        snprintf((char *)&local_38, 0x1f, "%%%ds", 0x1ff); // LIT[%]%d => %511s
        offset = param_1 + (long)number_of_notes * 0x204;
        //__isoc99_scanf(&local_38, lVar1, lVar1);
        __isoc99_scanf("%511s", offset, offset); // why two times? but it will not just "repeat", but we can assume it is save

        *(param_1 + (long)number_of_notes * 0x204 + 0x200) = 0; // set to active?
    }
    else
    {
        puts("Sorry, there are no available slots. Please delete something");
    }
    if (canary != *(long *)(in_FS_OFFSET + 0x28))
    {
        /* WARNING: Subroutine does not return */
        __stack_chk_fail();
    }
    return;
}

void draft_note(void)
{
    long lVar1;
    undefined8 *puVar2;
    long in_FS_OFFSET;
    undefined8 local_238;
    undefined8 local_230;
    undefined8 local_228;
    undefined8 local_220;
    char local_218;
    undefined8 local_210;
    char buffer[63];
    long canary;

    canary = *(long *)(in_FS_OFFSET + 0x28);
    local_218 = 0;
    local_210 = 0;
    lVar1 = 0x3e;
    puVar2 = buffer;
    while (lVar1 != 0)
    {
        lVar1 = lVar1 + -1;
        *puVar2 = 0;
        puVar2 = puVar2 + 1;
    }
    local_238 = 0;
    local_230 = 0;
    local_228 = 0;
    local_220 = 0;
    printf("Quote: ");
    snprintf((char *)&local_238, 0x1f, "%%%ds", 0x1ff); // %512s
    __isoc99_scanf("%512s", &local_218, &local_218);
    catsay(&local_218);
    if (canary != *(long *)(in_FS_OFFSET + 0x28))
    {
        /* WARNING: Subroutine does not return */
        __stack_chk_fail();
    }
    return;
}

void list(long param_1)

{
    size_t sVar1;
    char *pcVar2;
    uint local_1c;

    puts("Here\'s a list of our notes:");
    local_1c = 0;
    while ((int)local_1c < 10)
    {
        if (*(int *)(param_1 + (long)(int)local_1c * 0x204 + 0x200) == 1)
        {
            pcVar2 = "DELETED";
        }
        else
        {
            pcVar2 = "LIVE";
        }
        sVar1 = strlen((char *)(param_1 + (long)(int)local_1c * 0x204));
        printf(" - %02d. length: %03d, state: %s\n", (ulong)local_1c, sVar1, pcVar2);
        local_1c = local_1c + 1;
    }
    return;
}

int main(void)

{
    long in_FS_OFFSET;
    char data[512];
    char auStack4664[1162];
    long canary;

    int option = 0;
    int counter = 0;

    while (counter < 10)
    {
        auStack4664[(long)counter * 0x81] = 1; // set bytes *129 to 1
        data[(long)counter * 0x204] = 0;       // set bytes *516 to 0
        counter = counter + 1;
    }
    read_notes(data);

    auStack4664[387] = 1;
    option = 0;

    puts("This is your confidential notebook.");
    puts("This should get you through the next mission!");
    puts("Good luck!\n");
    do
    {
        if (option == 9)
        {
            catsay("Byezzz!!!");
            return 0;
        }
        scanf("%d", &option);
        switch (option)
        {
        default:
            printf("Unknown option. Please choose again.");
            break;
        case 1:
            list(data);
            break;
        case 2:
            print_note(data);
            break;
        case 3:
            draft_note();
            break;
        case 4:
            add_note(data);
            break;
        case 5:
            delete_note(data);
            break;
        case 9:
            break;
        }
    } while (1);
}

void catsay(char *param_1)

{
    int iVar1;
    long lVar2;
    undefined8 *puVar3;
    long in_FS_OFFSET;
    int local_230;
    uint local_22c;
    int local_228;
    int local_224;
    int local_220;
    int local_21c;
    undefined8 local_218;
    undefined8 local_210;
    undefined8 local_208[63];
    long canary;

    canary = *(long *)(in_FS_OFFSET + 0x28);
    local_218 = 0;
    local_210 = 0;
    lVar2 = 0x3e;
    puVar3 = local_208;
    while (lVar2 != 0)
    {
        lVar2 = lVar2 + -1;
        *puVar3 = 0;
        puVar3 = puVar3 + 1;
    }
    strncpy((char *)&local_218, param_1, 0x1ff);
    prepare(&local_218);
    get_dimensions(&local_218, &local_230, &local_22c, &local_230);
    if (local_230 != 0)
    {
        putchar(0x20);
        local_228 = 0;
        while (local_228 <= (int)(local_22c + 1))
        {
            putchar(0x5f);
            local_228 = local_228 + 1;
        }
        putchar(10);
        if (local_230 == 1)
        {
            print_line(&DAT_0010300b, &local_218, &DAT_00103008, (ulong)local_22c);
        }
        else
        {
            local_224 = print_line(&DAT_00103011, &local_218, &DAT_0010300e, (ulong)local_22c);
            local_220 = 1;
            while (local_220 < local_230 + -1)
            {
                iVar1 = print_line(&DAT_00103017, (long)&local_218 + (long)local_224, &DAT_00103014,
                                   (ulong)local_22c);
                local_224 = local_224 + iVar1;
                local_220 = local_220 + 1;
            }
            print_line(&DAT_0010301d, (long)&local_218 + (long)local_224, &DAT_0010301a, (ulong)local_22c);
        }
        putchar(0x20);
        local_21c = 0;
        while (local_21c <= (int)(local_22c + 1))
        {
            putchar(0x2d);
            local_21c = local_21c + 1;
        }
        putchar(10);
        puts("   \\    /\\_/\\  ");
        puts("    \\  ( o.o ) ");
        puts("        > ^ <  ");
    }
    if (canary != *(long *)(in_FS_OFFSET + 0x28))
    {
        /* WARNING: Subroutine does not return */
        __stack_chk_fail();
    }
    return;
}

void get_dimensions(long param_1, int *param_2, int *param_3)

{
    int iVar1;
    int local_10;

    local_10 = 0;
    *param_2 = 0;
    *param_3 = 0;
    while (*(char *)(param_1 + local_10) != '\0')
    {
        iVar1 = next_line_len(param_1 + local_10);
        if (*param_3 < iVar1)
        {
            *param_3 = iVar1;
        }
        local_10 = local_10 + iVar1;
        if (*(char *)(param_1 + local_10) == ' ')
        {
            local_10 = local_10 + 1;
        }
        *param_2 = *param_2 + 1;
    }
    return;
}

void print_note(long param_1)

{
    char *pcVar1;
    long in_FS_OFFSET;
    int local_14;
    long local_10;

    local_10 = *(long *)(in_FS_OFFSET + 0x28);
    printf("Which note would you like to print out? ");
    __isoc99_scanf("%d", &local_14);
    if (local_14 < 10)
    {
        if (*(int *)(param_1 + (long)local_14 * 0x204 + 0x200) == 1)
        {
            pcVar1 = "DELETED";
        }
        else
        {
            pcVar1 = (char *)(param_1 + (long)local_14 * 0x204);
        }
        catsay(pcVar1);
    }
    else
    {
        puts("This note doesn\'t exist. Try again. ");
    }
    if (local_10 != *(long *)(in_FS_OFFSET + 0x28))
    {
        /* WARNING: Subroutine does not return */
        __stack_chk_fail();
    }
    return;
}