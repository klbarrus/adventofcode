// karlb
// Advent of Code 2024, day 4

#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

void readFile(const string &filename, vector<string> &puzz);
void printData(const vector<string> &puzz);
void part1(const vector<string> &puzz);
string getRow(size_t row, const vector<string> &puzz);
string getCol(size_t col, const vector<string> &puzz);
string getDiagUp(size_t diag, const vector<string> &puzz);
string getDiagDown(size_t diag, const vector<string> &puzz);
size_t search(const string &line);

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
  size_t numRows = puzz.size();
  size_t numCols = puzz[0].length();
  size_t numDiags = numRows + numCols - 1;
  size_t count = 0;
  size_t total = 0;

  for (size_t i = 0; i < numRows; ++i) {
    string row = getRow(i, puzz);
    count = search(row);
    // if (count) {
    //   cout << format("row {}, found {}\n", i, count);
    // }
    total += count;
  }

  for (size_t i = 0; i < numCols; ++i) {
    string col = getCol(i, puzz);
    count = search(col);
    // if (count) {
    //   cout << format("col {}, found {}\n", i, count);
    // }
    total += count;
  }

  for (size_t i = 0; i < numDiags; ++i) {
    string diag = getDiagUp(i, puzz);
    count = search(diag);
    // if (count) {
    //   cout << format("diag up {}, found {}\n", i, count);
    // }
    total += count;
  }

  for (size_t i = 0; i < numDiags; ++i) {
    string diag = getDiagDown(i, puzz);
    count = search(diag);
    // if (count) {
    //   cout << format("diag down {}, found {}\n", i, count);
    // }
    total += count;
  }

  cout << format("Part 1: {}\n", total);
}

string getRow(size_t row, const vector<string> &puzz) { return puzz[row]; }

string getCol(size_t col, const vector<string> &puzz) {
  size_t rows = puzz.size();
  string retVal(rows, ' ');

  for (size_t i = 0; i < rows; ++i) {
    retVal[i] = puzz[i].at(col);
  }

  return retVal;
}

string getDiagUp(size_t diag, const vector<string> &puzz) {
  size_t rows = puzz.size();
  size_t cols = puzz[0].length();
  size_t dsize = min(rows, cols);
  string retVal(dsize, ' ');

  size_t r, c;

  // get indices of diagonal start
  if (diag < rows) {
    r = diag;
    c = 0;
  } else {
    r = rows - 1;
    c = diag - rows + 1;
  }

  dsize = 0;
  do {
    retVal[dsize] = puzz[r].at(c);
    ++dsize;
    --r;
    ++c;
  } while (r < rows && c < cols);

  // cout << format("diag {}: {}\n", diag, retVal);

  return retVal;
}

string getDiagDown(size_t diag, const vector<string> &puzz) {
  size_t rows = puzz.size();
  size_t cols = puzz[0].length();
  size_t dsize = min(rows, cols);
  string retVal(dsize, ' ');

  size_t r, c;

  // get indices of diagonal start
  if (diag < rows) {
    r = rows - diag - 1;
    c = 0;
  } else {
    r = 0;
    c = diag - rows + 1;
  }

  dsize = 0;
  do {
    retVal[dsize] = puzz[r].at(c);
    ++dsize;
    ++r;
    ++c;
  } while (r < rows && c < cols);

  // cout << format("diag {}: {}\n", diag, retVal);

  return retVal;
}

size_t search(const string &line) {
  size_t count = 0;
  size_t pos;

  pos = line.find("XMAS", 0);
  while (pos != string::npos) {
    count++;
    pos = line.find("XMAS", pos + 1);
  }

  pos = line.find("SAMX", 0);
  while (pos != string::npos) {
    count++;
    pos = line.find("SAMX", pos + 1);
  }

  return count;
}