from langchain_exa import ExaSearchRetriever

exa_search_retriever = ExaSearchRetriever(k = 1, highlights = False, type = "autotype")

def exa_search_node(recent_thesis_part: str):
    """Search for context from online sources. 
    This search should use the entire recent_thesis_part 
    This tool should return context for the question that was asked and the accompanying url for the context. 
    Include the url at the end of the context on a new line.
    
    Args: 
        recent_thesis_part: recent_thesis_part
    """
    # exa_search_retriever = ExaSearchRetriever(k = 1, highlights = False, type = "autotype") 
    output = exa_search_retriever.invoke(recent_thesis_part) 
    return output[0].page_content + output[0].metadata["url"]