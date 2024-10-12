from pydantic import BaseModel, Field 
from typing import Optional

class parsed_query(BaseModel): 
    """The original thesis statement split into its parts.""" 
    thesis_part_1: str = Field(description = "Thesis that has been split into its main idea/main argument and first sub-argument/reasoning.") 
    thesis_part_2: str = Field(description = "Thesis that has been split into its main idea/main argument and second sub-argument/reasoning.")
    thesis_part_3: Optional[str] = Field(description = "Thesis that has been split into its main idea/main argument and third sub-argument/reasoning.")