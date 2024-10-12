from langgraph_project_1_dir.state import Custom_State

def load_thesis_part_node_new(state: Custom_State):
    if abs(state["iteration_counter"]) <= len(state["thesis_parts"]):
        return {"recent_thesis_part": state["thesis_parts"][state["iteration_counter"]]}
    else: 
        pass