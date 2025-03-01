import pprint

#Approach 1
task_list = [
    {
        "task_id": "001",
        "task_description": "Write a Python program",
        "task_points": 0,
        "completion": False
    },
    {
        "task_id": "002",
        "task_description": "Do my laundry",
        "task_points": 0,
        "completion": False
    },
    {
        "task_id": "003",
        "task_description": "Complete my assingment",
        "task_points": 10,
        "completion": True
    }
]

def mark_as_complete(task_id: str):
    for task in task_list:
        if task["task_id"] == task_id:
            task["completion"] = True
            task["task_points"] = 10
            return task
    return None


#Approach 2
class TaskList:
    """TaskList class to manage tasks"""
    def __init__(self):
        self.task_list = []
        pass
        
    def add_task(self, task_description: str)-> None:
        """Add a task to the task list
        Args:
            task_description (str): Task description
        Returns:
            None
        """   
        self.task_list.append({
            "task_id": str(len(self.task_list) + 1).zfill(3),
            "task_description": task_description,
            "task_points": 0,
            "completion": False
        })
    
    def mark_as_complete(self, task_id: str):
        """Mark a task as complete
        Args:
            task_id (str): Task ID
        Returns:
            dict: Task record
        """
        for task in self.task_list:
            if task["task_id"] == task_id:
                task["completion"] = True
                task["task_points"] = 10
                return task
        return None


if __name__ == "__main__":
    #Initialise the task list
    task_list = TaskList()

    #Add tasks to the task list
    task_list.add_task("Write a Python program")
    task_list.add_task("Do my laundry")
    task_list.add_task("Complete my assingment")

    pprint.pp(task_list.task_list)
    task_list.mark_as_complete("002")
    pprint.pp(task_list.task_list)
