from summarizer import TextSummarizer
from analyzer import TextAnalyzer

def main():
    sample_text = (
        "Artificial intelligence is transforming the modern world. "
        "From healthcare to finance, AI systems are automating complex tasks. "
        "Machine learning models can now diagnose diseases, drive cars, and "
        "generate creative content. However, ethical concerns remain about "
        "privacy and job displacement. Researchers continue to work on "
        "making AI more transparent and fair for everyone."
    )

    summarizer = TextSummarizer()
    analyzer = TextAnalyzer()

    print("=== AI Text Summarizer & Analyzer ===")
    print("\nOriginal Text:")
    print(sample_text)

    print("\n--- Summary ---")
    summary = summarizer.summarize(sample_text)
    print(summary)

    print("\n--- Analysis ---")
    print(f"Word count: {analyzer.word_count(sample_text)}")
    print(f"Sentence count: {analyzer.sentence_count(sample_text)}")
    print(f"Average word length: {analyzer.average_word_length(sample_text):.2f}")
    print("Most common words:", analyzer.most_common_words(sample_text, 3))

if __name__ == "__main__":
    main()