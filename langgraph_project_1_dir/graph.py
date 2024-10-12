from IPython.display import Image, display
from langgraph.prebuilt import ToolNode, tools_condition # tools_condition is not used here 
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph, START, END
from langgraph_project_1_dir.state import Custom_State
from langgraph_project_1_dir.nodes.query_parsing_node import query_parsing_node 
from langgraph_project_1_dir.nodes.assistant_node import assistant_node 
from langgraph_project_1_dir.nodes.exa_search_node import exa_search_node_new 
from langgraph_project_1_dir.nodes.change_iteration_counter_node import change_iteration_counter_node 
from langgraph_project_1_dir.nodes.text_and_quote_extractor_node import text_and_quote_extractor_node 
from langgraph_project_1_dir.nodes.load_thesis_part_node import load_thesis_part_node_new 
from langgraph_project_1_dir.graph_edges.thesis_part_conditional_edge import thesis_part_conditional_edge_new

builder = StateGraph(Custom_State) 

builder.add_node("query_parsing_node", query_parsing_node) 
builder.add_node("assistant_node", assistant_node)
builder.add_node("exa_search_node_new", exa_search_node_new) 
# builder.add_node("remove_one_thesis_part_node", remove_one_thesis_part_node)
builder.add_node("change_iteration_counter_node", change_iteration_counter_node)
builder.add_node("text_and_quote_extractor_node", text_and_quote_extractor_node)
builder.add_node("load_thesis_part_node_new", load_thesis_part_node_new)

builder.add_edge(START, "query_parsing_node") 
builder.add_edge("query_parsing_node", "load_thesis_part_node_new") 
builder.add_edge("load_thesis_part_node_new", "assistant_node")
builder.add_conditional_edges("assistant_node", thesis_part_conditional_edge_new)
builder.add_edge("exa_search_node_new", "change_iteration_counter_node")  
builder.add_edge("change_iteration_counter_node", "load_thesis_part_node_new")
builder.add_edge("text_and_quote_extractor_node", END)

graph = builder.compile(checkpointer = MemorySaver()) # interrupt_before = ["load_thesis_part_node"]

if __name__ == "__main__": 
    display(Image(graph.get_graph(xray = True).draw_mermaid_png(output_file_path = "./graph_png.png")))