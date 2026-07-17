import sys
from database import cursor, connection


def add_note():
    note = input("Enter your note: ")
    cursor.execute("INSERT INTO notes (note) VALUES (?)", (note,))
    connection.commit()
    print("Note Added Successfully!")


def show_notes():
    cursor.execute("SELECT * FROM notes")
    notes = cursor.fetchall()

    if notes:
        for note_id, note in notes:
            print(f"{note_id}: {note}")
    else:
        print("No notes found.")

    print("===================================")


def search_notes():
    keyword = input("Please Enter The Keyword: ")

    cursor.execute(
        "SELECT id, note FROM notes WHERE note LIKE ?",
        (f"%{keyword}%",)
    )

    result = cursor.fetchall()

    if result:
        for note_id, note in result:
            print(f"{note_id}: {note}")
    else:
        print("No Notes Found!")

    print("===================================")


def edit_note():
    try:
        note_id = int(input("Enter The Note's ID: "))
    except ValueError:
        print("Invalid ID!")
        return

    result = cursor.execute(
        "SELECT id FROM notes WHERE id = ?",
        (note_id,)
    ).fetchone()

    if result is None:
        print("The Note Doesn't Exist!")
        return

    edited_note = input("Enter The Edited Note: ")

    cursor.execute(
        "UPDATE notes SET note = ? WHERE id = ?",
        (edited_note, note_id)
    )

    connection.commit()
    print("Note Edited Successfully!")


def delete_note():
    try:
        note_id = int(input("Enter The Note's ID: "))
    except ValueError:
        print("Invalid ID!")
        return

    result = cursor.execute(
        "SELECT id FROM notes WHERE id = ?",
        (note_id,)
    ).fetchone()

    if result is None:
        print("The Note Doesn't Exist!")
        return

    cursor.execute(
        "DELETE FROM notes WHERE id = ?",
        (note_id,)
    )

    connection.commit()
    print("Note Deleted Successfully!")


def run_notes():
    while True:
        try:
            print(
                "1. Add Note\n"
                "2. Show Notes\n"
                "3. Search Notes\n"
                "4. Edit Note\n"
                "5. Delete Note\n"
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
                add_note()
            elif choice == 2:
                show_notes()
            elif choice == 3:
                search_notes()
            elif choice == 4:
                edit_note()
            elif choice == 5:
                delete_note()
            elif choice == 6:
                return
            else:
                sys.exit()


if __name__ == "__main__":
    run_notes()
    cursor.close()
    connection.close()