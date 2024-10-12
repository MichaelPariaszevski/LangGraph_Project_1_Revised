from langgraph_project_1_dir.state import Custom_State

def change_iteration_counter_node(state: Custom_State): 
    return {"iteration_counter": state["iteration_counter"] - 1}