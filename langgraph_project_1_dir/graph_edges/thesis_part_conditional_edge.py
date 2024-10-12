from typing import Literal 
from langgraph_project_1_dir.state import Custom_State

def thesis_part_conditional_edge_new(state: Custom_State) -> Literal["exa_search_node_new", "text_and_quote_extractor_node"]: 
    if len(state["thesis_parts"]) > 0 and state["thesis_parts"][-1] != None and abs(state["iteration_counter"]) <= len(state["thesis_parts"]): 
        return "exa_search_node_new" 
    else: 
        return "text_and_quote_extractor_node"