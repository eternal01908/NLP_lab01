import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.preprocessing.regex_tokenizer import RegexTokenizer
from src.core.interfaces import Tokenizer

def test_regex_tokenizer(text: str):
    tokenizer: Tokenizer = RegexTokenizer()
    tokens = tokenizer.tokenize(text)
    return tokens

if __name__ == "__main__":
    example = "Hello, world. This is a test"
    print(test_regex_tokenizer(example))