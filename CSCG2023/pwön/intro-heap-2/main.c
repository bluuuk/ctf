// gcc -O0 -g main.c -o main
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#define MAX_TASKS 50
#define TASK_NAME 0x10
#define MAX_SUBTASKS 24
#define MAX_SUBTASK_LENGTH 0x100

typedef struct Subtask
{
    long length;
    char task[0];
} subtask_t;

typedef struct Task
{
    char name[TASK_NAME];
    subtask_t *subtasks[MAX_SUBTASKS];
} task_t;

task_t *tasks[MAX_TASKS];

long read_long()
{
    char buf[1024];
    char *end;
    long ret;

    if (!fgets(buf, sizeof(buf), stdin))
    {
        puts("error reading stdin");
        exit(1);
    }
    ret = strtol(buf, &end, 10);
    if (end == buf)
    {
        puts("not a number");
        exit(1);
    }
    return ret;
}

void add_task()
{
    char *last_n;

    for (int i = 0; i < MAX_TASKS; i++)
    {
        if (tasks[i])
        {
            continue;
        }
        tasks[i] = malloc(sizeof(task_t));
        memset(tasks[i], 0, sizeof(task_t));
        printf("name? ");
        read(0, tasks[i]->name, TASK_NAME);
        last_n = strrchr(tasks[i]->name, '\n');
        if (last_n)
        {
            *last_n = 0;
        }
        return;
    }
    puts("too many tasks :(");
}

void delete_task()
{
    long id;

    printf("id? ");
    id = read_long();
    if (id >= MAX_TASKS)
    {
        puts("invalid id");
        return;
    }
    if (!tasks[id])
    {
        puts("task does not exist");
        return;
    }

    free(tasks[id]);
    tasks[id] = NULL;
}

void list_tasks()
{
    for (int i = 0; i < MAX_TASKS; i++)
    {
        if (!tasks[i])
        {
            continue;
        }
        printf("[%02d] %s\n", i, tasks[i]->name);
    }
}

void delete_subtask()
{
    long id;
    long sid;

    printf("id? ");
    id = read_long();
    if (id >= MAX_TASKS)
    {
        puts("invalid id");
        return;
    }
    if (!tasks[id])
    {
        puts("task does not exist");
        return;
    }

    printf("sid? ");
    sid = read_long();
    if (sid >= MAX_TASKS)
    {
        puts("invalid sid");
        return;
    }
    if (!tasks[id]->subtasks[sid])
    {
        puts("subtask does not exist");
        return;
    }
    free(tasks[id]->subtasks[sid]);
    tasks[id]->subtasks[sid] = NULL;
}

void add_subtask()
{
    char *last_n;
    long id;
    long length;

    printf("id? ");
    id = read_long();
    if (id >= MAX_TASKS)
    {
        puts("invalid id");
        return;
    }
    if (!tasks[id])
    {
        puts("task does not exist");
        return;
    }
    for (int i = 0; i < MAX_SUBTASKS; i++)
    {
        if (tasks[id]->subtasks[i])
        {
            continue;
        }

        printf("length? ");
        length = read_long();
        if (length < 0 || length >= MAX_SUBTASK_LENGTH)
        {
            puts("invalid length");
            return;
        }

        tasks[id]->subtasks[i] = malloc(sizeof(subtask_t) + length);
        memset(tasks[id]->subtasks[i], 0, sizeof(subtask_t) + length);
        tasks[id]->subtasks[i]->length = length;
        printf("content? ");
        read(0, tasks[id]->subtasks[i]->task, length);
        last_n = strrchr(tasks[id]->subtasks[i]->task, '\n');
        if (last_n)
        {
            *last_n = 0;
        }
        return;
    }
    puts("too many sub tasks :(");
}

void list_subtasks()
{
    long id;
    printf("id? ");
    id = read_long();
    if (id < 0 || id >= MAX_TASKS)
    {
        puts("invalid id");
        return;
    }
    if (!tasks[id])
    {
        puts("task does not exist");
        return;
    }

    for (int i = 0; i < MAX_SUBTASKS; i++)
    {
        if (!tasks[id]->subtasks[i])
        {
            continue;
        }
        printf("[%02d] %s\n", i, tasks[id]->subtasks[i]->task);
    }
}

int menu()
{
    long choice;
    puts("---menu---");
    puts("[0] exit");
    puts("[1] add task");
    puts("[2] delete task");
    puts("[3] list tasks");
    puts("[4] add subtask");
    puts("[5] delete subtask");
    puts("[6] list subtasks");

    printf("choice? ");
    choice = read_long();
    return choice;
}

int main(int argc, char **argv)
{
    setvbuf(stdin, 0, _IONBF, 0);
    setvbuf(stdout, 0, _IONBF, 0);
    setvbuf(stderr, 0, _IONBF, 0);
    while (1)
    {
        switch (menu())
        {
        case 0:
            return 0;
        case 1:
            add_task();
            break;
        case 2:
            delete_task();
            break;
        case 3:
            list_tasks();
            break;
        case 4:
            add_subtask();
            break;
        case 5:
            delete_subtask();
            break;
        case 6:
            list_subtasks();
            break;
        default:
            puts("choose wisely");
        }
    }
}