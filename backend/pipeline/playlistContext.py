from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

@dataclass
class PlaylistContext:
    user_id: str
    user_query: str

    intent: Optional[str] = None
    is_safe: bool = True
    rag_context: Optional[str] = None
    user_preferences: Dict[str, Any] = field(default_factory=dict)

    songs: List[Any] = field(default_factory=list)
    playlist_url: Optional[str] = None
