import sys
from database import cursor, connection


def add_task():
    task = input("Enter your task: ")
    due_time = input("Enter the task's time: ")

    cursor.execute(
        "INSERT INTO tasks (task, due_time) VALUES (?, ?)",
        (task, due_time)
    )

    connection.commit()
    print("Task Added Successfully!")


def show_tasks():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    if tasks:
        for task_id, task, due_time in tasks:
            print(f"Task No {task_id}: {task} at {due_time}")
    else:
        print("No tasks found!")

    print("===================================")


def search_tasks():
    keyword = input("Please Enter The Keyword: ")

    cursor.execute(
        "SELECT id, task, due_time FROM tasks WHERE task LIKE ?",
        (f"%{keyword}%",)
    )

    result = cursor.fetchall()

    if result:
        for task_id, task, due_time in result:
            print(f"{task_id}: {task} at {due_time}")
    else:
        print("No Tasks Found!")

    print("===================================")


def edit_task():
    try:
        task_id = int(input("Enter The Task's ID: "))
    except ValueError:
        print("Invalid ID!")
        return

    result = cursor.execute(
        "SELECT id FROM tasks WHERE id = ?",
        (task_id,)
    ).fetchone()

    if result is None:
        print("The Task Doesn't Exist!")
        return

    edited_task = input("Enter The Edited Task: ")
    edited_time = input("Enter The Edited Task Time: ")

    cursor.execute(
        "UPDATE tasks SET task = ?, due_time = ? WHERE id = ?",
        (edited_task, edited_time, task_id)
    )

    connection.commit()
    print("Task Edited Successfully!")


def delete_task():
    try:
        task_id = int(input("Enter The Task's ID: "))
    except ValueError:
        print("Invalid ID!")
        return

    result = cursor.execute(
        "SELECT id FROM tasks WHERE id = ?",
        (task_id,)
    ).fetchone()

    if result is None:
        print("The Task Doesn't Exist!")
        return

    cursor.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    connection.commit()
    print("Task Deleted Successfully!")


def run_tasks():
    while True:
        try:
            print(
                "1. Add Task\n"
                "2. Show Tasks\n"
                "3. Search Tasks\n"
                "4. Edit Task\n"
                "5. Delete Task\n"
                "6. Back To Main Menu\n"
                "7. Exit"
            )

            choice = int(input("Enter your choice: "))

            if choice not in [1, 2, 3, 4, 5, 6, 7]:
                raise ValueError("Invalid choice.")

        except ValueError:
            print("Invalid Choice!")

        else:
            if choice == 1:
                add_task()
            elif choice == 2:
                show_tasks()
            elif choice == 3:
                search_tasks()
            elif choice == 4:
                edit_task()
            elif choice == 5:
                delete_task()
            elif choice == 6:
                return
            else:
                sys.exit()


if __name__ == "__main__":
    run_tasks()
    cursor.close()
    connection.close()