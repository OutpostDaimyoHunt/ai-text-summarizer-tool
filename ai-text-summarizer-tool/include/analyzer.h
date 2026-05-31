#ifndef ANALYZER_H
#define ANALYZER_H

#include <string>
#include <map>

std::map<std::string, int> analyzeWordFrequency(const std::string& text);
int countSentences(const std::string& text);

#endif