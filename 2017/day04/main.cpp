// karlb
// Advent of Code 2017, day 4

#include <algorithm>
#include <fstream>
#include <iostream>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

void readFile(const string &filename, vector<string> &puzz);
void printData(const vector<string> &puzz);
void part1(const vector<string> &puzz);

int main(int argc, char *argv[]) {
  vector<string> args(argv + 1, argv + argc);

  for (auto filename : args) {
    cout << format("File {}\n", filename);

    vector<string> puzz;

    readFile(filename, puzz);
    // printData(puzz);

    part1(puzz);
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

void part1(const vector<string> &puzz) {
  size_t part1 = 0;

  for (auto const &x : puzz) {
    string word;
    stringstream line_stream(x);
    vector<string> line_data;

    while (line_stream >> word) {
      line_data.push_back(word);
    }

    // insert into set: if word already present (no insertion) - invalid
    bool valid = true;
    set<string> ss;

    for (auto const &w : line_data) {
      auto res = ss.insert(w);
      if (!res.second) {
        valid = false;
      }
    }

    if (valid) {
      part1++;
    }
  }

  cout << format("Part 1: {}\n", part1);
}