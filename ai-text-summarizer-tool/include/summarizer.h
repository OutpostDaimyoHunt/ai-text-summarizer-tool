#ifndef SUMMARIZER_H
#define SUMMARIZER_H

#include <string>
#include <vector>

std::string summarizeText(const std::string& text, int sentenceCount = 3);
std::vector<std::string> splitSentences(const std::string& text);

#endif