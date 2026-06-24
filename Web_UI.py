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
        priority = st.selectbox("Priority", ["Low", "Normal", "High"], index=1)
        category = st.text_input("Category", value="General")

        if st.button("Add task"):
            if new_task.strip():
                add_task(st.session_state.tasks, new_task.strip(), priority, category.strip() or "General")
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
            created_date = task.get("created_at", "")
            if "T" in created_date:
                created_date = created_date.split("T")[0]

            cols = st.columns([4, 1, 1, 1])
            cols[0].markdown(
                f"**{index + 1}. {task['text']}**  \n"
                f"Priority: {task.get('priority', 'Normal')}  \n"
                f"Category: {task.get('category', 'General')}  \n"
                f"Created: {created_date}"
            )
            status_text = "✓ Done" if task["done"] else "⏳ Pending"
            cols[1].write(status_text)

            if not task["done"]:
                if cols[2].button("Mark Done", key=f"done_{index}"):
                    mark_done(st.session_state.tasks, index)
                    save_tasks(st.session_state.tasks)
                    st.rerun()
            else:
                cols[2].write("")

            if cols[3].button("Delete", key=f"delete_{index}"):
                removed = delete_task(st.session_state.tasks, index)
                save_tasks(st.session_state.tasks)
                st.success(f"Removed: {removed['text']}")
                st.rerun()


if __name__ == "__main__":
    main()
