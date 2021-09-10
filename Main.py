from pywebio.input  import *
from pywebio.output import *
from functools import partial # call any function


def completed(buttonName, task , tasks): # remove the todo
    if buttonName == 'Click to complete':
        tasks.remove(task)
    clear('tasks')

    if tasks:
        put_table([
            [todo , put_buttons(['Click to complete'],onclick=partial(completed,task = todo, tasks = tasks))] for todo in tasks
        ],
            scope = 'tasks',
        )

def priority(buttonName,task,tasks):
    pass


def todo():
    tasks = [] # to append tasks
    with use_scope('tasks'):
        while True:
            todo = input("Hey! Write your To Do : ")
            tasks.append(todo)
            clear('tasks')
            put_table([
                [todo , put_buttons(['Click to complete'],onclick=partial(completed,task = todo, tasks = tasks)),put_buttons(['Priority'],onclick=partial(priority,task = todo, tasks = tasks))] for todo in tasks
            ])



# List comprehension..
# a = [i for i in range(0,100,3) if i % 2 == 0]
# print(a)
todo()
# test
# pyweb