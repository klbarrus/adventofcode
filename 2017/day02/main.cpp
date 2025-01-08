// karlb
// Advent of Code 2017, day 2

#include <algorithm>
#include <fstream>
#include <iostream>
#include <ranges>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

void readFile(const string &filename, vector<vector<int>> &puzz);
void printData(const vector<vector<int>> &puzz);
void part1(const vector<vector<int>> &puzz);
void part2(const vector<vector<int>> &puzz);

int main(int argc, char *argv[]) {
  vector<string> args(argv + 1, argv + argc);

  for (auto filename : args) {
    cout << format("File {}\n", filename);

    vector<vector<int>> puzz;

    readFile(filename, puzz);
    // printData(puzz);

    part1(puzz);
    part2(puzz);
  }

  return 0;
}

void readFile(const string &filename, vector<vector<int>> &puzz) {
  ifstream puzzle_in(filename);
  string line;

  while (getline(puzzle_in, line)) {
    int num;
    vector<int> line_data;
    std::stringstream line_stream(line);
    while (line_stream >> num) {
      line_data.push_back(num);
    }

    puzz.push_back(line_data);
  }
}

void printData(const vector<vector<int>> &puzz) {
  for (auto const &v : puzz) {
    for (auto const &i : v) {
      cout << format("{} ", i);
    }
    cout << "\n";
  }
}

void part1(const vector<vector<int>> &puzz) {
  size_t sum = 0;

  for (auto const &v : puzz) {
    auto [min_elem, max_elem] = minmax_element(v.begin(), v.end());
    sum += (*max_elem - *min_elem);
  }

  cout << format("Part 1: {}\n", sum);
}

void part2(const vector<vector<int>> &puzz) {
  size_t sum = 0;

  for (auto const &v : puzz) {
    for (auto const &[a, b] : views::cartesian_product(v, v)) {
      if (a != b && a % b == 0) {
        sum += a / b;
        break;
      }
    }
  }

  cout << format("Part 2: {}\n", sum);
}
