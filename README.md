# To-Do App (Console + Streamlit)

This repository contains a small To-Do application with two user interfaces that share a common backend.

Files:
- `todo_app_backend.py` — core logic: `load_tasks`, `save_tasks`, `add_task`, `delete_task`, `mark_done`.
- `todo.py` — console UI that calls the backend functions.
- `Web UI.py` — Streamlit web UI that calls the backend functions.
- `tasks.json` — data file (ignored by git; contains user tasks).

Quick start

Console UI:

```bash
cd c:\STUDY\Python\TO-Do
python todo.py
```

Streamlit UI:

```bash
cd c:\STUDY\Python\TO-Do
c:/STUDY/Python/venv/Scripts/python.exe -m streamlit run "Web UI.py"
```

Notes

- `tasks.json` is in `.gitignore` to avoid committing user data.
- The backend is UI-agnostic; you can add another UI (API, mobile client) and reuse `todo_app_backend.py`.
