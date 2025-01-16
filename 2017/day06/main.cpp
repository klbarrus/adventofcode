// karlb
// Advent of Code 2017, day 6

#include <algorithm>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

void readFile(const string &filename, vector<unsigned int> &puzz);
void printData(const vector<unsigned int> &puzz);
void bothParts(vector<unsigned int> &puzz);

int main(int argc, char *argv[]) {
  vector<string> args(argv + 1, argv + argc);

  for (auto filename : args) {
    cout << format("File {}\n", filename);

    vector<unsigned int> puzz;

    readFile(filename, puzz);
    // printData(puzz);

    bothParts(puzz);
  }

  return 0;
}

void readFile(const string &filename, vector<unsigned int> &puzz) {
  ifstream puzzle_in(filename);
  string line;

  while (getline(puzzle_in, line)) {
    unsigned int n;
    istringstream line_stream(line);

    while (line_stream >> n) {
      puzz.push_back(n);
    }
  }
}

void printData(const vector<unsigned int> &puzz) {
  for (auto const &x : puzz) {
    cout << format("{}\n", x);
  }
}

void bothParts(vector<unsigned int> &puzz) {
  size_t num_cycles = 0;
  bool seen_before = false;
  vector<vector<unsigned int>> state;

  while (!seen_before) {
    // find redistribution block
    auto max = max_element(puzz.begin(), puzz.end());
    auto index = max - puzz.begin();

    // redistribute
    unsigned int count = puzz[index];
    puzz[index] = 0;

    // circularly add blocks
    num_cycles++;
    while (count > 0) {
      index = (index + 1) % puzz.size();
      puzz[index] += 1;
      count--;
    }

    // if state has not been previously seen, save state
    auto it = find(state.begin(), state.end(), puzz);
    if (it != state.end()) {
      seen_before = true;
      auto dist = distance(it, state.end());

      cout << format("Part 1: {}\n", num_cycles);
      cout << format("Part 2: {}\n", dist);
    } else {
      state.push_back(puzz);
    }
  }
}