#include "summarizer.h"
#include <algorithm>
#include <sstream>
#include <cctype>

std::vector<std::string> splitSentences(const std::string& text) {
    std::vector<std::string> sentences;
    std::string sentence;
    for (char c : text) {
        sentence += c;
        if (c == '.' || c == '!' || c == '?') {
            sentences.push_back(sentence);
            sentence.clear();
        }
    }
    if (!sentence.empty()) sentences.push_back(sentence);
    return sentences;
}

std::string summarizeText(const std::string& text, int sentenceCount) {
    auto sentences = splitSentences(text);
    if (sentences.size() <= sentenceCount) return text;

    std::vector<std::string> summary;
    for (int i = 0; i < sentenceCount; ++i) {
        summary.push_back(sentences[i]);
    }
    return std::accumulate(summary.begin(), summary.end(), std::string());
}