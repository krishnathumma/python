import streamlit as st
import functions

todos = functions.get_todos()
st.set_page_config(layout="wide")
def add_todo():
    todo = st.session_state["new_todo"]+"\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo List")
st.subheader("This is my todo app")
st.write("Nice <b>write</b>", unsafe_allow_html=True)

st.text_input(label="", placeholder="Enter todo here ...",
                          on_change=add_todo, key="new_todo")

for index, todo in enumerate(todos):
    checked = st.checkbox(todo, key=todo)
    if checked:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()




# //st.session_state