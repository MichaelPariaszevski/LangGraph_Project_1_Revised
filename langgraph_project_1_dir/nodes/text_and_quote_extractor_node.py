from langgraph_project_1_dir.state import Custom_State 
from langgraph_project_1_dir.llm_dir.llm import llm 
from langchain.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser

def text_and_quote_extractor_node(state: Custom_State): 
    context = state["context"] 
    original_thesis = state["thesis"] 
    system_message_template = ChatPromptTemplate.from_template(template = """
                                   Given the original thesis statement below and all of the provided context, return reasoning as to why the websites, articles, or academic papers found through the web searchs assist the user in writing their research paper. 
                                   You must return SPECIFIC QUOTATIONS from the websites, articles, or academic papers themselves that the user can utilize within their own research paper. 
                                   Display all reasoning in a numbered list format with the urls for each piece of reasoning at the end of the line. 
                                   DO NOT write the user's research paper for them.
                                   VERY IMPORTANT, USE ONLY THE PROVIDED ORIGINAL THESIS AND CONTEXT, DO NOT RETRIEVE INFORMATION FROM YOUR OWN INTERNAL DATABASE
                                   
                                   -------------------------------------------------
                                   
                                   Original Thesis Statement: {original_thesis} 
                                   
                                   Given Context: {context}
                                   
                                   """)
    text_and_quote_extractor_chain = system_message_template | llm | StrOutputParser()
    return {"final_response": text_and_quote_extractor_chain.invoke({"original_thesis": original_thesis[0].content, "context": context})}