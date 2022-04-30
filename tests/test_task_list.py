import unittest

from app.task_list import TaskList
from xml.dom import NotFoundErr

class TestTaskList(unittest.TestCase):
    
    def return_raise_not_found_err(self):
       return NotFoundErr("Task not found")
    def test_init_empty_tasklist(self):
        tasklist = TaskList()
        self.assertEqual(
            tasklist.tasks, 
            []
        )

    def test_initialization_task(self):
        tasklist = TaskList(
            [
                {
                    "task_name": "TASK_1",
                    "task_description": ["Mysql", "MongoDB", "Postgres"]
                },
                {
                    "task_name": "TASK_2",
                    "task_description": ["Python", "Django", "Flask"]
                },
                {
                    "task_name": "TASK_3",
                    "task_description": ["NodeJS", "ExpressJS", "ReactJS"]
                },
            ]
        )
        self.assertEqual(
            tasklist.tasks,
            [
                {
                    "task_name": "TASK_1",
                    "task_description": ["Mysql", "MongoDB", "Postgres"]
                },
                {
                    "task_name": "TASK_2",
                    "task_description": ["Python", "Django", "Flask"]
                },
                {
                    "task_name": "TASK_3",
                    "task_description": ["NodeJS", "ExpressJS", "ReactJS"]
                },
            ]
        )

    def test_add_task(self):
        tasklist = TaskList(
            [
                {
                    "task_name": "TASK_1",
                    "task_description": ["Mysql", "MongoDB", "Postgres"]
                },
                {
                    "task_name": "TASK_2",
                    "task_description": ["Python", "Django", "Flask"]
                },
                {
                    "task_name": "TASK_3",
                    "task_description": ["NodeJS", "ExpressJS", "ReactJS"]
                },
            ]
        )
        new_task_list = tasklist + {"task_name": "TASK_4", "task_description": ["C++", "C#", "Java"]}
        self.assertEqual(
            new_task_list.tasks,
            [
                {
                    "task_name": "TASK_1",
                    "task_description": ["Mysql", "MongoDB", "Postgres"]
                },
                {
                    "task_name": "TASK_2",
                    "task_description": ["Python", "Django", "Flask"]
                },
                {
                    "task_name": "TASK_3",
                    "task_description": ["NodeJS", "ExpressJS", "ReactJS"]
                },
                {
                    "task_name": "TASK_4",
                    "task_description": ["C++", "C#", "Java"]
                },
            ]
        )

    def test_remove_task(self):
        tasklist = TaskList(
            [
                {
                    "task_name": "TASK_1",
                    "task_description": ["Mysql", "MongoDB", "Postgres"]
                },
                {
                    "task_name": "TASK_2",
                    "task_description": ["Python", "Django", "Flask"]
                },
                {
                    "task_name": "TASK_3",
                    "task_description": ["NodeJS", "ExpressJS", "ReactJS"]
                },
            ]
        )
        new_task_list = tasklist.remove_task({"task_name": "TASK_2"})
        self.assertEqual(
            new_task_list.tasks,
            [
                {
                    "task_name": "TASK_1",
                    "task_description": ["Mysql", "MongoDB", "Postgres"]
                },
                {
                    "task_name": "TASK_3",
                    "task_description": ["NodeJS", "ExpressJS", "ReactJS"]
                },
            ]
        )

    def test_remove_task_not_found(self):
        tasklist = TaskList(
            [
                {
                    "task_name": "TASK_1",
                    "task_description": ["Mysql", "MongoDB", "Postgres"]
                },
                {
                    "task_name": "TASK_2",
                    "task_description": ["Python", "Django", "Flask"]
                },
                {
                    "task_name": "TASK_3",
                    "task_description": ["NodeJS", "ExpressJS", "ReactJS"]
                },
            ]
        )
        new_task_list = tasklist.remove_task({"task_name": "TASK_4"}),

        self.assertEqual(
            new_task_list[0],
            {"error": "Task not found"}
        )