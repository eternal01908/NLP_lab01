import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.preprocessing.simple_tokenizer import SimpleTokenizer
from src.core.interfaces import Tokenizer

def test_simple_tokenizer(text: str):
    tokenizer: Tokenizer = SimpleTokenizer()
    tokens = tokenizer.tokenize(text)
    return tokens

if __name__ == "__main__":
    example = "Hello, world. This is a test?"
    print(test_simple_tokenizer(example))