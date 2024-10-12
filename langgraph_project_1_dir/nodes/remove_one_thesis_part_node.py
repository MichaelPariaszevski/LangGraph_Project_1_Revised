from langgraph_project_1_dir.state import Custom_State

def remove_one_thesis_part_node(state: Custom_State): 
    return {"thesis_parts": state["thesis_parts"][0: -1]}