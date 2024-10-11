from typing_extensions import TypedDict 
from typing import Annotated 
from operator import add 

class Custom_State(TypedDict): 
    thesis: str 
    thesis_parts: Annotated[list[str], add]
    context: Annotated[list[str], add] 
    recent_thesis_part: str
    iteration_counter: int
    final_response: str