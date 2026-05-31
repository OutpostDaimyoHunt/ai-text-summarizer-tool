from collections import Counter
import re

class TextAnalyzer:
    def word_count(self, text: str) -> int:
        return len(text.split())

    def sentence_count(self, text: str) -> int:
        return len(re.findall(r'[.!?]+', text))

    def most_common_words(self, text: str, n: int = 5) -> list:
        words = re.findall(r'\b\w+\b', text.lower())
        return Counter(words).most_common(n)

    def average_word_length(self, text: str) -> float:
        words = text.split()
        if not words:
            return 0.0
        return sum(len(w) for w in words) / len(words)