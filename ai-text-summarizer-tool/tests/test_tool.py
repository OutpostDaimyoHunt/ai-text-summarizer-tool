import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from summarizer import TextSummarizer
from analyzer import TextAnalyzer

def test_summarizer():
    summarizer = TextSummarizer()
    text = "Python is a powerful programming language. It is widely used for web development and data science."
    summary = summarizer.summarize(text, max_length=30, min_length=10)
    assert isinstance(summary, str)
    assert len(summary) > 0
    print("✓ test_summarizer passed")

def test_analyzer_word_count():
    analyzer = TextAnalyzer()
    assert analyzer.word_count("Hello world") == 2
    assert analyzer.word_count("") == 0
    print("✓ test_analyzer_word_count passed")

def test_analyzer_sentence_count():
    analyzer = TextAnalyzer()
    assert analyzer.sentence_count("Hi. How are you? I'm fine.") == 3
    assert analyzer.sentence_count("No punctuation") == 0
    print("✓ test_analyzer_sentence_count passed")

def test_analyzer_most_common_words():
    analyzer = TextAnalyzer()
    text = "apple banana apple cherry banana apple"
    result = analyzer.most_common_words(text, 2)
    assert result == [('apple', 3), ('banana', 2)]
    print("✓ test_analyzer_most_common_words passed")

def test_analyzer_average_word_length():
    analyzer = TextAnalyzer()
    assert analyzer.average_word_length("a bb ccc") == 2.0
    print("✓ test_analyzer_average_word_length passed")

if __name__ == "__main__":
    test_summarizer()
    test_analyzer_word_count()
    test_analyzer_sentence_count()
    test_analyzer_most_common_words()
    test_analyzer_average_word_length()
    print("\nAll tests passed!")