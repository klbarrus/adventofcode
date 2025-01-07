// karlb
// Advent of Code 2017, day 1

#include <algorithm>
#include <fstream>
#include <iostream>
#include <ranges>
#include <sstream>
#include <vector>

using namespace std;

void readFile(const string &filename, vector<string> &puzz);
void printData(const vector<string> &puzz);
void part1(const vector<string>& puzz);
void part2(const vector<string>& puzz);
size_t captcha(const string& orig, size_t offset);

int main(int argc, char *argv[]) {
  vector<string> args(argv + 1, argv + argc);

  for (auto filename : args) {
    cout << format("File {}\n", filename);

    vector<string> puzz;

    readFile(filename, puzz);
    // printData(puzz);

    part1(puzz);
    part2(puzz);
  }

  return 0;
}

void readFile(const string &filename, vector<string> &puzz) {
  ifstream puzzle_in(filename);
  string line;

  while (getline(puzzle_in, line)) {
    puzz.push_back(line);
  }
}

void printData(const vector<string> &puzz) {
  for (auto const &x : puzz) {
    cout << format("{}\n", x);
  }
}

void part1(const vector<string>& puzz) {
  for (auto const &x : puzz) {
    size_t res = captcha(x, 1);
    cout << format("Part 1: {}\n", res);
  }
}

void part2(const vector<string>& puzz) {
  for (auto const &x : puzz) {
    size_t res = captcha(x, x.length() / 2);
    cout << format("Part 2: {}\n", res);
  }
}

size_t captcha(const string& orig, size_t offset) {
  string copy = orig;
  size_t res = 0;

  rotate(copy.begin(), copy.begin() + offset, copy.end());

  for (const auto &[a, b] : views::zip(orig, copy)) {
    if (a == b) {
      res += static_cast<size_t>(a) - '0';
    }
  }

  return res;
}