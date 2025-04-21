# Entry 4
##### 3/17/25

My tool is flask and my freedom project on a to-do list. I have been learning my tool using online documentations and watching online videos. Also I learn to use python in w3schools as Flask makes it easier to build web stuff using Python so I also have to learn how to write in python to work. The goal is to build a simple website that allows users to manage tasks efficiently.I have been learning the tool using W3Schools and [videos](https://www.youtube.com/watch?v=45P3xQPaYx).

One of features that I added to my To-Do List app is a point system that rewards people for doing the tasks. This point system can help me add a game on the side for people to play on the app and makes the expierence of a to-do  more rewarding.

Some code snippet:
```python
task = tasks[task_id]
if not task["completed"]:
    points = task["points"]
    tasks.pop(task_id)
    total_points += points
```
the basically check if the task is done and if it dont have complete, it'll delete the task and give you the point

another one is:
``` python
<form method="POST">
       <input type="text" name="task" placeholder="Enter new task" required>
       <input type="number" name="points" placeholder="Enter points" required min="1">
       <button type="submit">Add Task</button>
   </form>
```

this code is asking for a task name and # of points you want to assigned to it. POST a form where you will enter the things in the input boxx to get a result.


[Previous](entry03.md) | [Next](entry05.md)

[Home](../README.md)