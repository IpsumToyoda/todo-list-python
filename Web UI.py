import streamlit as st
from todo_app_backend import load_tasks, save_tasks, add_task, delete_task, mark_done


def main():
    st.title("To-Do List")
    st.write("A simple Streamlit front end for your todo list.")

    if "tasks" not in st.session_state:
        st.session_state.tasks = load_tasks()

    with st.sidebar:
        st.header("Actions")
        new_task = st.text_input("New task")
        if st.button("Add task"):
            if new_task.strip():
                add_task(st.session_state.tasks, new_task.strip())
                save_tasks(st.session_state.tasks)
                st.success(f"Added: {new_task.strip()}")
                st.rerun()
            else:
                st.warning("Task cannot be empty.")

        if st.button("Reload tasks"):
            st.session_state.tasks = load_tasks()
            st.rerun()

    if not st.session_state.tasks:
        st.info("No tasks yet. Add one from the sidebar.")
    else:
        st.subheader(f"Tasks ({len(st.session_state.tasks)})")
        for index, task in enumerate(st.session_state.tasks):
            cols = st.columns([6, 1, 1])
            cols[0].write(f"{index + 1}. {task['text']}")
            status_text = "✓ Done" if task["done"] else "⏳ Pending"
            cols[1].write(status_text)

            if cols[2].button("Mark Done", key=f"done_{index}"):
                mark_done(st.session_state.tasks, index)
                save_tasks(st.session_state.tasks)
                st.rerun()

        st.markdown("---")
        st.subheader("Delete Task")
        delete_index = st.number_input(
            "Task number to delete",
            min_value=1,
            max_value=len(st.session_state.tasks),
            step=1,
        )
        if st.button("Delete task"):
            removed = delete_task(st.session_state.tasks, delete_index - 1)
            save_tasks(st.session_state.tasks)
            st.success(f"Removed: {removed['text']}")
            st.rerun()


if __name__ == "__main__":
    main()
