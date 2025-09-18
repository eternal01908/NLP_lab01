from typing import List
from src.core.interfaces import Tokenizer

class SimpleTokenizer(Tokenizer):
    def tokenize(self, text: str) -> list[str]:
        tokens = []
        current = []

        def flush_current():
            if current:
                tokens.append("".join(current).lower())
                current.clear()

        for ch in text:
            if ch.isalnum() or ch == "_":  # cho phép _ trong từ
                current.append(ch)
            elif ch.isspace():
                flush_current()
            else:
                flush_current()
                tokens.append(ch)  # các ký tự khác tách riêng

        flush_current()
        return tokens