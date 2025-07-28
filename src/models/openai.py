from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional, Union, Literal


class OpenAIContentBlockTextCacheControl(BaseModel):
    "works for openrouter"

    type: Literal["ephemeral"]


class ClaudeContentBlockImage(BaseModel):
    type: Literal["image"]
    source: Dict[str, Any]


# class OpenAISystemMessage(BaseModel):


class OpenAIContentBlockText(BaseModel):
    type: Literal["text"]
    text: str
    cache_control: Optional[OpenAIContentBlockTextCacheControl] = None


class OpenAIContentBlockImage(BaseModel):
    type: Literal["input_image"]
    image_url: str
    detail: Literal["low", "high", "auto"] = "auto"


class OpenAIMessage(BaseModel):
    role: Literal["developer", "system", "user", "assistant", "tool"]
    content: Union[
        str,
        List[
            Union[
                OpenAIContentBlockText,
                ClaudeContentBlockImage,
                ClaudeContentBlockToolUse,
                ClaudeContentBlockToolResult,
            ]
        ],
    ]
