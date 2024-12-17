// karlb 
// Advent of Code 2024, day 1

#include <algorithm>
#include <fstream>
#include <iostream>
#include <ranges>
#include <sstream>
#include <tuple>
#include <vector>

void readFile(const std::string& filename, std::vector<int>& v1, std::vector<int>& v2);
void printData(const std::vector<int>& v1, const std::vector<int>& v2);
void part1(const std::vector<int>& v1, const std::vector<int>& v2);
void part2(const std::vector<int>& v1, const std::vector<int>& v2);

int main(int argc, char* argv[]) {
    std::vector<std::string> args(argv + 1, argv + argc);

    for (auto arg : args) {
        std::cout << "File " << arg << "\n";

        std::vector<int> v1;
        std::vector<int> v2;

        readFile(arg, v1, v2);
//        printData(v1, v2);

        std::sort(v1.begin(), v1.end());
        std::sort(v2.begin(), v2.end());

        part1(v1, v2);
        part2(v1, v2);
    }


    return 0;
}

void readFile(const std::string& filename, std::vector<int>& v1, std::vector<int>& v2) {
    std::ifstream puzzle_in(filename);
    std::string line;

    while (std::getline(puzzle_in, line)) {
        int n1;
        int n2;
        std::istringstream line_stream(line);

        line_stream >> n1;
        line_stream >> n2;
        v1.push_back(n1);
        v2.push_back(n2);
    }
}

void part1(const std::vector<int>& v1, const std::vector<int>& v2) {
    size_t distance = 0;
    for (const auto& [a,b] : std::views::zip(v1, v2)) {
        distance += std::abs(a - b);
    }

    std::cout << std::format("Part 1: {}\n", distance);
}

void part2(const std::vector<int>& v1, const std::vector<int>& v2) {
    size_t similarity = 0;

    for (const auto& a : v1) {
        auto num = std::ranges::count(v2.begin(), v2.end(), a);
        similarity += num * a;
    }

    std::cout << std::format("Part 2: {}\n", similarity);
}

void printData(const std::vector<int>& v1, const std::vector<int>& v2) {
    for (const auto& [a,b] : std::views::zip(v1, v2)) {
        std::cout << std::format("{} {}\n", a, b);
    }
}
