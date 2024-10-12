from langchain_core.messages import SystemMessage
from langgraph_project_1_dir.state import Custom_State 
from langgraph_project_1_dir.llm_dir.llm_tools import llm_with_tools

sys_msg = SystemMessage(content = """
                        You are a helpful assistant tasked with pulling text gathered from the web in order to aid the user in completing their research paper based on their provided thesis statement.
                        Use the entire provided thesis as the input for your web search. 
                        Return all text/information gathered from the web search in a raw but human readable format. 
                        At the very end, include the url from the web search that was used to gather all of this text/information and include '----------------------------------------------------' on a new line after the url as a separator between different/unique web search results. 
                        ONLY SEARCH FROM trust-worthy sources from the web search such as Google Scholar, JSTOR, ScienceDirect, and other academic databases. 
                        If a source does not seem to be trustworthy, skip the source and execute the search again, for a maximum of 3 iterations.
                        DO NOT write the user's research paper for them. 
                        
                        -------------------------------------------------------------
                        
                        USE THE THESIS PART BELOW AS THE INPUT TO 'exa_search_node'
                        """)

# prompt = ChatPromptTemplate.from_template(template = """
#                         You are a helpful assistant tasked with pulling text gathered from the web in order to aid the user in completing their research paper based on their provided thesis statement.
#                         Use the entire provided thesis as the input for your web search. 
#                         Return all text/information gathered from the web search in a raw but human readable format. 
#                         At the very end, include the url from the web search that was used to gather all of this text/information and include '----------------------------------------------------' on a new line after the url as a separator between different/unique web search results. 
#                         ONLY SEARCH FROM trust-worthy sources from the web search such as Google Scholar, JSTOR, ScienceDirect, and other academic databases. 
#                         If a source does not seem to be trustworthy, skip the source and execute the search again, for a maximum of 3 iterations.
#                         DO NOT write the user's research paper for them. 
                        
#                         -------------------------------------------------------------
                        
#                         USE THE THESIS PART BELOW AS THE INPUT TO 'exa_search_node' 
                        
#                         recent_thesis_part: {recent_thesis_part}
#                         """)

def assistant_node(state: Custom_State): 
    # chain = prompt | llm_with_tools 
    # return {"context": [chain.invoke({"recent_thesis_part": state["recent_thesis_part"]})]}
    return {"context": [llm_with_tools.invoke([sys_msg] + [state["recent_thesis_part"]])]}