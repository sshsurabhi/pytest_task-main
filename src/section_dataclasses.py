from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=False)
class Person:
    name: str
    age: int
    hobbies: List[str]
    nickname: Optional[str] = None
