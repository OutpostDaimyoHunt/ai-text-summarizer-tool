#include "summarizer.h"
#include <cassert>

void testSummarizeText() {
    std::string text = "First sentence. Second sentence. Third sentence.";
    assert(summarizeText(text, 2) == "First sentence.Second sentence.");
}

void testSplitSentences() {
    std::string text = "One. Two! Three?";
    auto sentences = splitSentences(text);
    assert(sentences.size() == 3);
    assert(sentences[0] == "One.");
    assert(sentences[1] == " Two!");
}

int main() {
    testSummarizeText();
    testSplitSentences();
    return 0;
}