// karlb
// Advent of Code 2024, day 5

#include <fstream>
#include <iostream>
#include <map>
#include <ranges>
#include <sstream>
#include <vector>

using namespace std;

void readFile(const string &filename, multimap<int, int> &pof,
              multimap<int, int> &por, vector<vector<int>> &pn);
void printData(const multimap<int, int> &pof, const multimap<int, int> &por,
               const vector<vector<int>> &pn);
void part1(const multimap<int, int> &pof, const multimap<int, int> &por,
           const vector<vector<int>> &pn, vector<vector<int>> &pne);
void part2(const multimap<int, int> &pof, const multimap<int, int> &por,
           const vector<vector<int>> &pne);

int main(int argc, char *argv[]) {
  vector<string> args(argv + 1, argv + argc);

  for (auto filename : args) {
    cout << format("File {}\n", filename);

    multimap<int, int> pof;  // page rules, forward map
    multimap<int, int> por;  // page rules, reverse map
    vector<vector<int>> pn;  // page numbers
    vector<vector<int>> pne; // page numbers that are in error

    readFile(filename, pof, por, pn);
    // printData(pof, por, pn);

    part1(pof, por, pn, pne);
    part2(pof, por, pne);
  }

  return 0;
}

void readFile(const string &filename, multimap<int, int> &pof,
              multimap<int, int> &por, vector<vector<int>> &pn) {
  ifstream puzzle_in(filename);
  string line;
  bool order = true;

  while (getline(puzzle_in, line)) {
    if (line.empty()) {
      order = false;
      continue;
    }

    if (order) {
      // first half of input, reading page order rules
      int x;
      char sep;
      int y;
      istringstream line_stream(line);
      line_stream >> x;
      line_stream >> sep;
      line_stream >> y;

      pof.insert({x, y});
      por.insert({y, x});
    } else {
      // second half of input, reading page numbers to print
      int x;
      char comma;
      istringstream line_stream(line);
      vector<int> temp;

      // read first number
      line_stream >> x;
      temp.push_back(x);

      // read rest of numbers
      while (line_stream >> comma >> x) {
        temp.push_back(x);
      }

      pn.push_back(temp);
    }
  }
}

void printData(const multimap<int, int> &pof, const multimap<int, int> &por,
               const vector<vector<int>> &pn) {
  cout << format("Page order rules (forward):\n");
  for (const auto &e : pof) {
    cout << format("{} {}\n", e.first, e.second);
  }

  cout << format("Page order rules (reverse):\n");
  for (const auto &e : por) {
    cout << format("{} {}\n", e.first, e.second);
  }

  cout << format("Page numbers:\n");
  for (const auto &v : pn) {
    for (const auto &e : v) {
      cout << format("{} ", e);
    }
    cout << format("\n");
  }
}

void part1(const multimap<int, int> &pof, const multimap<int, int> &por,
           const vector<vector<int>> &pn, vector<vector<int>> &pne) {
  size_t page_num = 0;
  for (const auto &v : pn) {
    auto numl = 0;
    auto numr = v.size() - 1;
    // process this vector, checking against rules
    bool correct = true;
    for (const auto &e : v) {
      auto vl = v | views::take(numl++);
      auto vr = v | views::reverse | views::take(numr--) | views::reverse;

      //      cout << format("Processing {}: ", e);
      for (const auto &x : vl) {
        // lookup in pof, if present - error
        //      cout << format("{} ", x);
        auto rkey = pof.equal_range(e);
        auto res = find_if(rkey.first, rkey.second,
                           [x](const auto &pair) { return pair.second == x; });
        if (res != rkey.second) {
          correct = false;
        }
      }
      //    cout << format(" | ");
      for (const auto &x : vr) {
        // lookup in por, if present - error
        //      cout << format("{} ", x);
        auto rkey = por.equal_range(e);
        auto res = find_if(rkey.first, rkey.second,
                           [x](const auto &pair) { return pair.second == x; });
        if (res != rkey.second) {
          correct = false;
        }
      }
      //      cout << "\n";
    }

    if (correct) {
      int mid = v.size() / 2;
      page_num += v[mid];
    } else {
      pne.push_back(v);
    }
  }

  cout << format("Part 1: {}\n", page_num);
}

void part2(const multimap<int, int> &pof, const multimap<int, int> &por,
           const vector<vector<int>> &pne) {
  cout << format("{} page numbers in error\n", pne.size());
}
