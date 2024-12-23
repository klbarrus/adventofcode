// karlb
// Advent of Code 2024, day 2

#include <algorithm>
#include <fstream>
#include <iostream>
#include <numeric>
#include <ranges>
#include <sstream>
#include <tuple>
#include <vector>

using namespace std;

void readFile(const string &filename, vector<vector<int>> &v);
void printData(const vector<vector<int>> &vov);
void printVec(const vector<int> &v);
void part1(const vector<vector<int>> &vov);
void part2(const vector<vector<int>> &vov);
bool isSafe(const vector<int> &v);

int main(int argc, char *argv[]) {
  vector<string> args(argv + 1, argv + argc);

  for (auto filename : args) {
    cout << format("File {}\n", filename);

    vector<vector<int>> vov;

    readFile(filename, vov);
    //        printData(vov);

    part1(vov);
    part2(vov);
  }

  return 0;
}

void readFile(const string &filename, vector<vector<int>> &v) {
  ifstream puzzle_in(filename);
  string line;

  while (getline(puzzle_in, line)) {
    int n;
    vector<int> temp;
    istringstream line_stream(line);

    while (line_stream >> n) {
      temp.push_back(n);
    }

    v.push_back(temp);
  }
}

bool isSafe(const vector<int> &v) {
  vector<int> diff(v.size());
  adjacent_difference(v.begin(), v.end(), diff.begin());

  bool safe_increase = ranges::all_of(diff.begin() + 1, diff.end(),
                                      [](int i) { return 0 < i && i <= 3; });
  bool safe_decrease = ranges::all_of(diff.begin() + 1, diff.end(),
                                      [](int i) { return 0 > i && i >= -3; });

  return safe_increase || safe_decrease;
}

void part1(const vector<vector<int>> &vov) {
  size_t num_safe = 0;

  for (const auto &v : vov) {
    if (isSafe(v)) {
      num_safe++;
    }
  }

  cout << format("Part 1: {}\n", num_safe);
}

void part2(const vector<vector<int>> &vov) {
  size_t num_safe = 0;

  for (const auto &v : vov) {
    if (isSafe(v)) {
      num_safe++;
    } else {
      for (size_t i = 0; i < v.size(); ++i) {
        vector<int> temp = v;
        temp.erase(temp.begin() + i);
        if (isSafe(temp)) {
          num_safe++;
          break;
        }
      }
    }
  }

  cout << format("Part 2: {}\n", num_safe);
}

void printData(const vector<vector<int>> &vov) {
  for (const auto &v : vov) {
    for (const auto &e : v) {
      cout << format("{} ", e);
    }
    cout << "\n";
  }
}

void printVec(const vector<int> &v) {
  for (const int &e : v) {
    cout << format("{} ", e);
  }
}
