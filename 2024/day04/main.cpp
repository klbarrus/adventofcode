// karlb
// Advent of Code 2024, day 4

#include <fstream>
#include <iostream>
#include <ranges>
#include <span>
#include <sstream>
#include <string>
#include <tuple>
#include <vector>

using namespace std;

void readFile(const string &filename, vector<string> &puzz);
void printData(const vector<string> &puzz);
void part1(const vector<string> &puzz);
void part2(const vector<string> &puzz);
string getRow(size_t row, const vector<string> &puzz);
string getCol(size_t col, const vector<string> &puzz);
string getDiagUp(size_t diag, const vector<string> &puzz);
string getDiagDown(size_t diag, const vector<string> &puzz);
size_t search(const string &line);
bool search3x3(string &a, string &b, string &c);

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

void part2(const vector<string> &puzz) {
  size_t numRows = puzz.size();
  size_t total = 0;

  // slide a 3x3 view over the puzzle

  for (size_t i = 0; i < numRows - 2; ++i) {
    auto window1 = puzz[i] | views::slide(3);
    auto window2 = puzz[i + 1] | views::slide(3);
    auto window3 = puzz[i + 2] | views::slide(3);

    for (const auto &elem : views::zip(window1, window2, window3)) {
      auto a = get<0>(elem) | ranges::to<string>();
      auto b = get<1>(elem) | ranges::to<string>();
      auto c = get<2>(elem) | ranges::to<string>();
      //      cout << format("sliding view: \n");
      //      cout << format("{}\n", a);
      //      cout << format("{}\n", b);
      //      cout << format("{}\n", c);
      if (search3x3(a, b, c)) {
        //        cout << "found x-mas\n";
        total++;
      }
      //        cout << "\n";
    }
  }

  cout << format("Part 2: {}\n", total);
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

bool search3x3(string &a, string &b, string &c) {
  if (b[1] != 'A') {
    return false;
  }

  string corners(4, ' ');
  corners[0] = a[0];
  corners[1] = a[2];
  corners[2] = c[0];
  corners[3] = c[2];

  if (corners == "MMSS" || corners == "SMSM" || corners == "SSMM" ||
      corners == "MSMS") {
    return true;
  }

  return false;
}