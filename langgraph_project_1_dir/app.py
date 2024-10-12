from langgraph_project_1_dir.graph import graph
from langchain_core.messages import HumanMessage
from pprint import pprint
from dotenv import load_dotenv, find_dotenv 

load_dotenv(find_dotenv(), override = True)

def invoke_graph(thesis: str, thread_id: int):  
    config ={"configurable": {"thread_id": thread_id}}
    thesis_message = [HumanMessage(content = thesis)]
    output = graph.invoke({"thesis": thesis_message}, config = config) 
    return output

if __name__ == "__main__": 
    example_thesis = "Social media has revolutionized communication and societal interactions, but it also presents significant challenges related to privacy, mental health, and misinformation."
    output = invoke_graph(thesis = example_thesis, thread_id = "thesis_agent_dir")
    print(output)
    print("\n" + ("#" * 100) + "\n") 
    print(output["final_response"])
    print("\n")