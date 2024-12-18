// karlb
// Advent of Code 2024, day 3

#include <fstream>
#include <iostream>
#include <regex>
#include <vector>

using namespace std;

void readFile(const string &filename, vector<string> &vs);
void printData(vector<string> &vs);
void part1(const vector<string> &vs);
void part2(vector<string> &vs);
size_t convertAndMult(string x, string y);

int main(int argc, char *argv[]) {
  vector<string> args(argv + 1, argv + argc);

  for (auto filename : args) {
    cout << format("File {}\n", filename);

    vector<string> vs;
    readFile(filename, vs);
    //        printData(vs);

    part1(vs);
    part2(vs);
  }

  return 0;
}

void readFile(const string &filename, vector<string> &vs) {
  ifstream puzzle_in(filename);
  string line;

  while (getline(puzzle_in, line)) {
    vs.push_back(line);
  }
}

void printData(vector<string> &vs) {
  for (const auto &e : vs) {
    cout << format("{}\n", e);
  }
}

size_t convertAndMult(string x, string y) {
  int xi;
  int yi;
  from_chars(x.data(), x.data() + x.size(), xi);
  from_chars(y.data(), y.data() + y.size(), yi);

  return xi * yi;
}

void part1(const vector<string> &vs) {
  size_t total = 0;
  auto const rx = regex(R"(mul\((\d{1,3}),(\d{1,3})\))");

  for (const string &s : vs) {
    string e(s);
    for (smatch sm; regex_search(e, sm, rx);) {
      //            cout << format("{} - match size {}\n", sm.str(), sm.size());
      //            for (size_t i = 0; i < sm.size(); ++i) {
      //                cout << sm[i] << "\n";
      //            }

      // on a match, sm is size 3
      // 0 - entire "mul(x,y)" string
      // 1 - x
      // 2 - y

      total += convertAndMult(sm[1], sm[2]);

      e = sm.suffix();
    }
  }

  cout << format("Part 1: {}\n", total);
}

void part2(vector<string> &vs) {
  size_t total = 0;
  bool mul = true;
  auto const rx = regex(R"(mul\((\d{1,3}),(\d{1,3})\)|don\'t\(\)|do\(\))");

  for (string &e : vs) {
    for (smatch sm; regex_search(e, sm, rx);) {
      //            cout << format("{} - match size {}\n", sm.str(), sm.size());
      //            for (size_t i = 0; i < sm.size(); ++i) {
      //                cout << sm[i] << "\n";
      //            }

      string sm_str(sm.str());
      if (sm_str == "do()") {
        mul = true;
      } else if (sm_str == "don\'t()") {
        mul = false;
      } else {
        if (mul) {
          total += convertAndMult(sm[1], sm[2]);
        }
      }

      e = sm.suffix();
    }
  }

  cout << format("Part 2: {}\n", total);
}