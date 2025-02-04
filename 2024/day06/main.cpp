// karlb
// Advent of Code 2024, day 6

// TODO part 2 isn't correct

#include <algorithm>
#include <fstream>
#include <iostream>
#include <numeric>
#include <ranges>
#include <set>
#include <sstream>
#include <string>
#include <tuple>
#include <type_traits>
#include <utility>
#include <vector>

enum class Direction { up, right, down, left };
enum class Space { obstacle, empty };

using namespace std;
using enum Direction;

void readFile(const string &filename, set<pair<size_t, size_t>> &puzz,
              pair<size_t, size_t> &max, pair<size_t, size_t> &start);
void printData(const set<pair<size_t, size_t>> &puzz,
               const pair<size_t, size_t> &max,
               const pair<size_t, size_t> &start);
void part1(const set<pair<size_t, size_t>> &puzz,
           const pair<size_t, size_t> &max, const pair<size_t, size_t> &start);
void part2(const set<pair<size_t, size_t>> &puzz,
           const pair<size_t, size_t> &max, const pair<size_t, size_t> &start);
bool exit_maze(const pair<size_t, size_t> &max, const pair<size_t, size_t> &pos,
               Direction dir);
Space check_next_space(const set<pair<size_t, size_t>> &puzz,
                       const pair<size_t, size_t> &pos, Direction dir);
void rotate_direction(Direction &dir);
pair<size_t, size_t> move(const pair<size_t, size_t> &pos, Direction dir);

int main(int argc, char *argv[]) {
  vector<string> args(argv + 1, argv + argc);

  for (auto filename : args) {
    cout << format("File {}\n", filename);

    set<pair<size_t, size_t>> puzz;
    pair<size_t, size_t> max;   // max dimensions of
    pair<size_t, size_t> start; // starting coords

    readFile(filename, puzz, max, start);
    // printData(puzz, max, start);

    part1(puzz, max, start);
    part2(puzz, max, start);
  }

  return 0;
}

void readFile(const string &filename, set<pair<size_t, size_t>> &puzz,
              pair<size_t, size_t> &max, pair<size_t, size_t> &start) {
  ifstream puzzle_in(filename);
  string line_in;

  size_t row = 0;
  size_t col = 0;

  while (getline(puzzle_in, line_in)) {
    col = 0;
    for (const auto &ch : line_in) {
      if (ch == '#') {
        // found an obstacle
        puzz.insert({row, col});
      } else if (ch == '^') {
        // found start
        start = {row, col};
      }

      ++col;
    }

    ++row;
  }

  max = {row, col};
}

void printData(const set<pair<size_t, size_t>> &puzz,
               const pair<size_t, size_t> &max,
               const pair<size_t, size_t> &start) {
  cout << format("Obstacles:\n");
  for (auto const &x : puzz) {
    cout << format("({},{}); ", get<0>(x), get<1>(x));
  }
  cout << "\n";
  cout << format("Start coords: ({},{})\n", get<0>(start), get<1>(start));
  cout << format("Max coords: ({},{})\n", get<0>(max), get<1>(max));
}

void part1(const set<pair<size_t, size_t>> &puzz,
           const pair<size_t, size_t> &max, const pair<size_t, size_t> &start) {
  // cout << format("{} obstacles, starting at ({},{}\n", puzz.size(),
  //                get<0>(start), get<1>(start));

  // track which spaces were visited
  set<pair<size_t, size_t>> visited;

  auto dir = Direction::up;
  auto pos = start;

  visited.insert(pos);

  // exit loop when we exit the maze
  while (true) {
    if (exit_maze(max, pos, dir)) {
      break;
    }

    Space space = check_next_space(puzz, pos, dir);

    if (space == Space::obstacle) {
      rotate_direction(dir);
    } else {
      pos = move(pos, dir);
      visited.insert(pos);
    }
  }

  cout << format("Part 1: {}\n", visited.size());
}

void part2(const set<pair<size_t, size_t>> &puzz,
           const pair<size_t, size_t> &max, const pair<size_t, size_t> &start) {
  // get grid dimensions
  size_t max_row = get<0>(max);
  size_t max_col = get<1>(max);

  // record positions that create a loop/paradox
  set<pair<size_t, size_t>> paradox;

  // loop over grid
  for (size_t row = 0; row < max_row; row++) {
    for (size_t col = 0; col < max_col; col++) {
      // add obstacle at (row,col)
      auto puzz_copy = puzz;
      auto res = puzz_copy.insert({row, col});
      if (!res.second) {
        // no insertion, so obstacle already present
        // therefore we can skip this (row, col)
        continue;
      }

      // track which positions are visited
      // include direction - if tuple already exists in the set, we're in a loop
      set<tuple<size_t, size_t, Direction>> visited;

      bool loop = false;
      auto dir = Direction::up;
      auto pos = start;

      visited.insert({get<0>(pos), get<1>(pos), dir});

      while (true) {
        if (exit_maze(max, pos, dir)) {
          break;
        }

        Space space = check_next_space(puzz_copy, pos, dir);

        if (space == Space::obstacle) {
          rotate_direction(dir);
        } else {
          pos = move(pos, dir);
        }
        auto res = visited.insert({get<0>(pos), get<1>(pos), dir});
        if (!res.second) {
          // no insertion
          // this <pos, dir> has already been visited
          // this is a loop, so exit
          loop = true;
          break;
        }
      } // while simulating guard movement

      //      cout << format("Part 2, ({},{}) - {}\n", row, col, loop);

      if (loop) {
        // cout << format("Part 2, ({},{})\n", row, col);
        //  path loops, add (row,col) to paradox set
        paradox.insert({row, col});
      }
    } // col
  } // row

  cout << format("Part 2: {}\n", paradox.size());
}

// given the current position and maze dimensions
// the next step in the direction indicated would exit the maze
bool exit_maze(const pair<size_t, size_t> &max, const pair<size_t, size_t> &pos,
               Direction dir) {
  //  cout << format("exit_maze\n");

  bool exit = false;

  size_t current_row = get<0>(pos);
  size_t current_col = get<1>(pos);
  size_t max_row = get<0>(max);
  size_t max_col = get<1>(max);

  switch (dir) {
  case Direction::up:
    if (current_row == 0) {
      exit = true;
    }
    break;
  case Direction::right:
    if (current_col == max_col - 1) {
      exit = true;
    }
    break;
  case Direction::down:
    if (current_row == max_row - 1) {
      exit = true;
    }
    break;
  case Direction::left:
    if (current_col == 0) {
      exit = true;
    }
    break;
  default:
    cout << format("exit_maze() direction {}?\n", to_underlying(dir));
    break;
  }

  return exit;
}

// given the current position and direction
// check if the next step in the direction indicated hits an obstacle
Space check_next_space(const set<pair<size_t, size_t>> &puzz,
                       const pair<size_t, size_t> &pos, Direction dir) {
  //  cout << format("check_next_space\n");
  Space rv = Space::empty;
  size_t row = get<0>(pos);
  size_t col = get<1>(pos);

  switch (dir) {
  case Direction::up:
    --row;
    break;
  case Direction::right:
    ++col;
    break;
  case Direction::down:
    ++row;
    break;
  case Direction::left:
    --col;
    break;
  default:
    cout << format("check_next_space() direction {}?\n", to_underlying(dir));
    break;
  }

  if (puzz.contains({row, col})) {
    rv = Space::obstacle;
  }

  return rv;
}

void rotate_direction(Direction &dir) {
  //  cout << format("rotate_direction\n");
  switch (dir) {
  case Direction::up:
    dir = Direction::right;
    break;
  case Direction::right:
    dir = Direction::down;
    break;
  case Direction::down:
    dir = Direction::left;
    break;
  case Direction::left:
    dir = Direction::up;
    break;
  default:
    cout << format("rotate_direction() direction {}?\n", to_underlying(dir));
    break;
  }
}

pair<size_t, size_t> move(const pair<size_t, size_t> &pos, Direction dir) {
  size_t row = get<0>(pos);
  size_t col = get<1>(pos);

  // cout << format("move ({},{}) to ", row, col);
  switch (dir) {
  case Direction::up:
    --row;
    break;
  case Direction::right:
    ++col;
    break;
  case Direction::down:
    ++row;
    break;
  case Direction::left:
    --col;
    break;
  default:
    cout << format("move() direction {}?\n", to_underlying(dir));
    break;
  }
  // cout << format("({},{})\n", row, col);

  return {row, col};
}
