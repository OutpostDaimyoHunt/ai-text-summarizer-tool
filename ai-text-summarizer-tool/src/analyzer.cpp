#include "analyzer.h"
#include <sstream>
#include <cctype>
#include <algorithm>

std::map<std::string, int> analyzeWordFrequency(const std::string& text) {
    std::map<std::string, int> freq;
    std::istringstream iss(text);
    std::string word;

    while (iss >> word) {
        word.erase(std::remove_if(word.begin(), word.end(), [](char c) {
            return !isalpha(c);
        }), word.end());
        if (!word.empty()) {
            std::transform(word.begin(), word.end(), word.begin(), ::tolower);
            freq[word]++;
        }
    }
    return freq;
}

int countSentences(const std::string& text) {
    return splitSentences(text).size();
}