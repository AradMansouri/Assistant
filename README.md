# Assistant

A modular command-line assistant built with Python. This project combines several useful utilities into a single application, including note management, task management, weather lookup, and password generation.

## Features

### 📝 Notes
- Add notes
- View all notes
- Search notes by keyword
- Edit notes
- Delete notes

### ✅ Tasks
- Add tasks
- View all tasks
- Search tasks by keyword
- Edit tasks
- Delete tasks
- Set a due time for each task

### 🌤 Weather
- Get the current weather for any city using the wttr.in service.

### 🔐 Password Generator
- Generate secure random passwords with a custom length.

## Technologies Used

- Python 3
- SQLite
- Requests
- password-generator

## Project Structure

```
Assistant/
│
├── main.py
├── database.py
├── notes.py
├── tasks.py
├── weather.py
├── passwordGenerator.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

Clone the repository:

```bash
git clone git@github.com:AradMansouri/Assistant.git
```

Move into the project directory:

```bash
cd Assistant
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

## Database

The application automatically creates an SQLite database (`assistant.db`) on the first run.

## Future Improvements

- User authentication
- Task reminders
- Better weather information using a dedicated API
- Export notes and tasks
- GUI version
- Unit tests

## Author

**Arad Mansouri**

GitHub: https://github.com/AradMansouri
