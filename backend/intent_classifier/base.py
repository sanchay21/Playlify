from abc import ABC, abstractmethod

class BaseLLM(ABC):
    """
    Contract for any LLM provider.
    """

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """Generate a response for a given prompt"""
        pass
