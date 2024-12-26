// karlb
// Advent of Code 2024, day 5

#include <algorithm>
#include <fstream>
#include <iostream>
#include <map>
#include <ranges>
#include <sstream>
#include <tuple>
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
bool isValid(const multimap<int, int> &pof, const multimap<int, int> &por,
             const vector<int> &v);
bool lookup(const multimap<int, int> &mm, const int key, const int item);
void printVec(const vector<int> &v);

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

bool lookup(const multimap<int, int> &mm, const int key, const int item) {
  auto key_range = mm.equal_range(key);
  auto res = find_if(key_range.first, key_range.second,
                     [item](const auto &pair) { return pair.second == item; });

  bool found = false;

  if (res != key_range.second) {
    found = true;
  }

  return found;
}

bool isValid(const multimap<int, int> &pof, const multimap<int, int> &por,
             const vector<int> &v) {
  auto numl = 0;
  auto numr = v.size() - 1;

  for (const auto &e : v) {
    auto vl = v | views::take(numl++);
    auto vr = v | views::reverse | views::take(numr--) | views::reverse;

    for (const auto &x : vl) {
      if (lookup(pof, e, x)) {
        return false;
      }
    }

    for (const auto &x : vr) {
      if (lookup(por, e, x)) {
        return false;
      }
    }
  }

  return true;
}

void part1(const multimap<int, int> &pof, const multimap<int, int> &por,
           const vector<vector<int>> &pn, vector<vector<int>> &pne) {
  size_t page_num = 0;
  for (const auto &v : pn) {
    if (isValid(pof, por, v)) {
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
  // cout << format("{} page numbers in error\n", pne.size());
  size_t page_num = 0;
  for (auto &v : pne) {
    auto vc = v;
    bool done = false;

    while (!done) {
      // repeatedly swap pages until no more swaps done
      done = true;

      for (tuple t : vc | views::adjacent<2>) {
        auto [t1, t2] = t;
        //        cout << format("({},{}) ", t1, t2);
        if (lookup(por, t1, t2)) {
          //          cout << " swap "; // need to swap
          auto i1 = find(vc.begin(), vc.end(), t1);
          auto i2 = find(vc.begin(), vc.end(), t2);
          iter_swap(i1, i2);
          done = false;
          break;
        }
      }
    }

    // pages now in order
    int mid = vc.size() / 2;
    page_num += vc[mid];
  }

  cout << format("Part 2: {}\n", page_num);
}

void printVec(const vector<int> &v) {
  for (const auto &e : v) {
    cout << format("{} ", e);
  }
  cout << "\n";
}
