// karlb
// Advent of Code 2017, day 3

#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

void readFile(const string &filename, vector<size_t> &puzz);
void printData(const vector<size_t> &puzz);
void part1(const vector<size_t>& puzz);
void part2(void);

int main(int argc, char *argv[]) {
  vector<string> args(argv + 1, argv + argc);

  for (auto filename : args) {
    cout << format("File {}\n", filename);

    vector<size_t> puzz;

    readFile(filename, puzz);
    //prsize_tData(puzz);

    part1(puzz);
    part2();
  }

  return 0;
}

void readFile(const string &filename, vector<size_t> &puzz) {
  ifstream puzzle_in(filename);
  string line;

  while (getline(puzzle_in, line)) {
    size_t n;
    istringstream line_stream(line);

    line_stream >> n;
    puzz.push_back(n);
  }
}

void printData(const vector<size_t> &puzz) {
  for (auto const &x : puzz) {
    cout << format("{}\n", x);
  }
}

void part1(const vector<size_t>& puzz) {
  for (auto const& n : puzz) {
    size_t res = 0;
    size_t oddsq = 3;
    while (oddsq * oddsq < n)
        oddsq += 2;

    size_t fs = (oddsq * oddsq - n) % (oddsq - 1);
    if (fs > (oddsq - 1) / 2)
        res = fs;
    else
        res = oddsq - 1 - fs;

    cout << format("Part 1: {}\n", res);
  }
}

void part2(void) {
  cout << format("Part 2: see OEIS sequence 141481 (https://oeis.org/A141481)\n");
}