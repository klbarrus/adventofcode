// karlb
// Advent of Code 2017, day 5 

#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

void readFile(const string &filename, vector<int> &puzz);
void printData(const vector<int> &puzz);
size_t do_jumps(vector<int>& table, int (* fn)(int));
int calc_off1(int off);
int calc_off2(int off);
void part1(const vector<int>& table);
void part2(const vector<int>& table);

int main(int argc, char *argv[]) {
  vector<string> args(argv + 1, argv + argc);

  for (auto filename : args) {
    cout << format("File {}\n", filename);

    vector<int> puzz;

    readFile(filename, puzz);
    // printData(puzz);

    part1(puzz);
    part2(puzz);
  }

  return 0;
}

void readFile(const string &filename, vector<int> &puzz) {
  ifstream puzzle_in(filename);
  string line;

  while (getline(puzzle_in, line)) {
    int n;
    istringstream line_stream(line);

    line_stream >> n;
    puzz.push_back(n);
  }
}

void printData(const vector<int> &puzz) {
  for (auto const &x : puzz) {
    cout << format("{}\n", x);
  }
}

size_t do_jumps(vector<int>& table, int (* fn)(int)) {
    size_t pos = 0;
    size_t count = 0;
    while (pos < table.size()) {
        int offset = table[pos];
        table[pos] += fn(offset);
        pos += offset;
        count++;
    }
    return count;
}

int calc_off1(int off) {
    return 1;
}

int calc_off2(int off) {
    if (off >= 3)
        return -1;
    else
        return 1;
}

void part1(const vector<int>& table) {
  vector<int> jt = table;
  size_t numJumps = do_jumps(jt, calc_off1);

  cout << format("Part 1: {}\n", numJumps);
}

void part2(const vector<int>& table) {
  vector<int> jt = table;
  size_t numJumps = do_jumps(jt, calc_off2);

  cout << format("Part 2: {}\n", numJumps);
}