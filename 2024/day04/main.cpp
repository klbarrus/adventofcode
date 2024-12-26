// karlb
// Advent of Code 2024, day 4

#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

void readFile(const string &filename, vector<string> &puzz);
void printData(const vector<string> &puzz);

int main(int argc, char *argv[]) {
  vector<string> args(argv + 1, argv + argc);

  for (auto filename : args) {
    cout << format("File {}\n", filename);

    vector<string> puzz;

    readFile(filename, puzz);
    printData(puzz);
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
