class TaskList():
    def __init__(self, tasks=None):
        if tasks is None:
            tasks = []
        self.tasks = tasks

    def __add__(self, task: dict):
        return TaskList(self.tasks + [task])

    def remove_task(self, task):
        if task['task_name']:
            task_to_remove = next((x for x in self.tasks if x['task_name'] == task['task_name']), None)
        if not task_to_remove:
            return {"error": "Task not found"}
        self.tasks.remove(task_to_remove)
        return TaskList(self.tasks)
