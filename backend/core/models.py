from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class StoryOptionLLM(BaseModel):
    text: str = Field(description="The text of the option that the user can choose.")
    nextNode: Dict[str, Any] = Field(description="The next node in the story that this option leads to.") 
    
class StoryNodeLLM(BaseModel):
    content: str = Field(description="The content of the story at this node.")
    isEnding: bool = Field(description="Whether this node is an ending.")
    isWinningEnding: bool = Field(description="Whether this node is a winning ending.")
    options: Optional[List[StoryOptionLLM]] = Field(default=None, description="The options available at this node. Should be None for ending nodes.")
    
class StoryLLMResponse(BaseModel):
    title: str = Field(description="The title of the story.")
    rootNode: StoryNodeLLM = Field(description="The root node of the story, which contains the starting situation and options.")