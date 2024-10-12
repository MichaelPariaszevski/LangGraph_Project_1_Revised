from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import SystemMessage, HumanMessage
from langgraph_project_1_dir.state import Custom_State
from langgraph_project_1_dir.llm_dir.llm_structured import llm_structured

def query_parsing_node(state: Custom_State): 
    thesis = state["thesis"] 
    prompt_template = ChatPromptTemplate.from_template("""
                                                       The overall goal of this LLM application is to help a user in writing their research paper based on their thesis statement that they provide. 
                                                       However, this is the first step of the process in which you must parse the original, whole thesis into seperate sentences. 
                                                       This will require you to analyze the thesis statement, locate its main idea as well as its sub-arguemnts/reasonings, and finally, combine the main idea with ONE of the sub-arguemnts/reasonings in each sentence. 
                                                       Therefore, IF the original thesis statement included a main idea and 2 sub-arguments/reasonings, the final output must include 2 seperate sentences, each including the main idea and a unique sub-argument/reasoning. 
                                                       DO NOT INCLUDE quotation marks "" in the final output. 
                                                       
                                                       ---START OF EXAMPLES---
                                                       
                                                       For some guidance, consider the following examples: 
                                                       
                                                       Example 1:
                                                       
                                                       Original thesis statement: "Mandatory school uniforms should be implemented in educational institutions as they promote a sense of equality, reduce distractions, and foster a focused and professional learning environment." 
                                                       
                                                       Output: 
                                                            "Mandatory school uniforms should be implemented in educational institutions as they promote a sense of equality."
                                                            "Mandatory school uniforms should be implemented in educational institutions as they reduce distractions."
                                                            "Mandatory school uniforms should be implemented in educational institutions as they foster a focused and professional learning environment."
                                                            
                                                        Example 2: 
                                                        
                                                        Original thesis statement: "Globalization has created a world more interconnected than ever before, yet it also amplifies economic disparities and cultural homogenization."
                                                        
                                                        Output: 
                                                            "Globalization has created a world more interconnected than ever before, yet it also amplifies economic disparities."
                                                            "Globalization has created a world more interconnected than ever before, yet it also amplifies cultural homogenization."  
                                                            
                                                        Example 3: 
                                                        Original thesis statement: "Immigration enriches receiving countries culturally and economically, outweighing any perceived social or economic burdens." 
                                                        
                                                        Output: 
                                                            "Immigration enriches receiving countries culturally, outweighing any perceived social or economic burdens." 
                                                            "Immigration enriches receiving countries economically, outweighing any perceived social or economic burdens."
                                                            
                                                        ----END OF EXAMPLES---
                                                        
                                                        Original thesis statement: {thesis}
                                                       """)
    
    query_parsing_chain = prompt_template | llm_structured 
    parsed_thesis = query_parsing_chain.invoke({"thesis": thesis[0].content}) 
    return {"thesis_parts": [parsed_thesis.thesis_part_1, parsed_thesis.thesis_part_2, parsed_thesis.thesis_part_3], "iteration_counter": -1}