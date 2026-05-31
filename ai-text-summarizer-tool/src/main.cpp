#include <iostream>
#include "summarizer.h"
#include "analyzer.h"

int main() {
    std::string text = "Artificial intelligence is transforming industries. It enables automation and data analysis. "
                       "Many companies are adopting AI solutions. This trend will continue in the future.";

    std::cout << "Summary:\n" << summarizeText(text, 2) << "\n\n";
    std::cout << "Word Frequency:\n";
    for (const auto& [word, count] : analyzeWordFrequency(text)) {
        std::cout << word << ": " << count << "\n";
    }
    std::cout << "\nSentence Count: " << countSentences(text) << "\n";
    return 0;
}