import todo_app_backend as backend


def test_add_delete_mark():
    tasks = []
    backend.add_task(tasks, "a")
    assert tasks == [{"text": "a", "done": False}]

    backend.mark_done(tasks, 0)
    assert tasks[0]["done"] is True

    removed = backend.delete_task(tasks, 0)
    assert removed["text"] == "a"
    assert tasks == []


def test_save_load(tmp_path, monkeypatch):
    # point backend TASKS_FILE to a temp file
    tmpfile = tmp_path / "t.json"
    monkeypatch.setattr(backend, "TASKS_FILE", str(tmpfile))

    tasks = []
    backend.add_task(tasks, "b")
    backend.save_tasks(tasks)

    loaded = backend.load_tasks()
    assert loaded == [{"text": "b", "done": False}]
