import streamlit as st 
from langgraph_project_1_dir.app import invoke_graph
from dotenv import load_dotenv, find_dotenv 

load_dotenv(find_dotenv(), override = True) 

st.set_page_config(page_title = "Research Paper Searcher") 

st.subheader("Research Paper Thesis Analyzer")

with st.sidebar: 
    thesis = st.text_input(label = "Input your full thesis statement") 
    thread_id = st.text_input(label = "Input a thread id")
    
    run_button = st.button("Run Research Paper Searcher")
    
if run_button and thesis and thread_id: 
    with st.spinner("Running Research Paper Searcher"): 
        output = invoke_graph(thesis = thesis, thread_id = thread_id)
    st.write(format(output["final_response"]))