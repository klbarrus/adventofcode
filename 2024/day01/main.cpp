// karlb
// Advent of Code 2024, day 1

#include <algorithm>
#include <fstream>
#include <iostream>
#include <ranges>
#include <sstream>
#include <tuple>
#include <vector>

using namespace std;

void readFile(const string &filename, vector<int> &v1, vector<int> &v2);
void printData(const vector<int> &v1, const vector<int> &v2);
void part1(const vector<int> &v1, const vector<int> &v2);
void part2(const vector<int> &v1, const vector<int> &v2);

int main(int argc, char *argv[]) {
  vector<string> args(argv + 1, argv + argc);

  for (auto arg : args) {
    cout << format("File {}\n", arg);

    vector<int> v1;
    vector<int> v2;

    readFile(arg, v1, v2);
    //        printData(v1, v2);

    sort(v1.begin(), v1.end());
    sort(v2.begin(), v2.end());

    part1(v1, v2);
    part2(v1, v2);
  }

  return 0;
}

void readFile(const string &filename, vector<int> &v1, vector<int> &v2) {
  ifstream puzzle_in(filename);
  string line;

  while (getline(puzzle_in, line)) {
    int n1;
    int n2;
    istringstream line_stream(line);

    line_stream >> n1;
    line_stream >> n2;
    v1.push_back(n1);
    v2.push_back(n2);
  }
}

void part1(const vector<int> &v1, const vector<int> &v2) {
  size_t distance = 0;
  for (const auto &[a, b] : views::zip(v1, v2)) {
    distance += abs(a - b);
  }

  cout << format("Part 1: {}\n", distance);
}

void part2(const vector<int> &v1, const vector<int> &v2) {
  size_t similarity = 0;

  for (const auto &a : v1) {
    auto num = ranges::count(v2.begin(), v2.end(), a);
    similarity += num * a;
  }

  cout << format("Part 2: {}\n", similarity);
}

void printData(const vector<int> &v1, const vector<int> &v2) {
  for (const auto &[a, b] : views::zip(v1, v2)) {
    cout << format("{} {}\n", a, b);
  }
}
