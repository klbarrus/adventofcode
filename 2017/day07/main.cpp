// karlb
// Advent of Code 2017, day 7

#include <algorithm>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <map>
#include <numeric>
#include <regex>
#include <set>
#include <string>
#include <vector>

using namespace std;

struct puzz_node {
  string name;
  int weight;
  vector<string> child;
  int children_total_weight;
  bool balanced;

  puzz_node(string &n, int w)
      : name{n}, weight{w}, child{}, children_total_weight{0}, balanced(false) {
  }

  void add_child(string &cn) { child.push_back(cn); }

  size_t num_children() const { return child.size(); }
};

struct balance_info {
  string name;
  int weight;
};

void readFile(const string &filename, vector<string> &puzz);
void printData(const vector<string> &puzz);
int fill_out_weights(map<string, puzz_node> &nodes, const string &sv);
void find_unbalanced_nodes(vector<string> &unbalanced,
                           const map<string, puzz_node> &nodes,
                           const string &sv);
int balance_tree(const vector<string> &unbalanced,
                 const map<string, puzz_node> &nodes);
string part1(const vector<string> &puzz);
void part2(const vector<string> &puzz, const string &bottom);

int main(int argc, char *argv[]) {
  vector<string> args(argv + 1, argv + argc);

  for (auto filename : args) {
    cout << format("File {}\n", filename);

    vector<string> puzz;

    readFile(filename, puzz);
    // printData(puzz);

    auto bottom = part1(puzz);
    part2(puzz, bottom);
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

string part1(const vector<string> &puzz) {
  // for part 1, the base tower will be the only one not listed on the rhs
  // add all names to a set for uniqueness, the remove names listed on the rhs

  set<string> names;
  regex towerInfo("(\\w+)");

  for (auto const &i : puzz) {
    auto info_begin = sregex_iterator(i.begin(), i.end(), towerInfo);
    // 1st entry in each line is a tower name
    smatch m = *info_begin;
    names.insert(m.str());
  }

  for (auto const &i : puzz) {
    auto info_begin = sregex_iterator(i.begin(), i.end(), towerInfo);
    auto info_end = sregex_iterator();
    // 3rd+ entry in each line are children/tower names
    auto info_third = info_begin;
    ++info_third;
    ++info_third;
    for (auto j = info_third; j != info_end; ++j) {
      smatch m = *j;
      names.erase(m.str());
    }
  }

  auto bottom = names.begin();
  cout << format("Part 1: {}\n", *bottom);
  // cout << "part 1: " << *bottom << '\n';

  return *bottom;
}

void part2(const vector<string> &puzz, const string &bottom) {
  // for part 2, build a graph of nodes (using a map)
  //   1st pass, add node name, weight, children
  //   2nd pass, total up children weight for each node
  //   3rd pass, find wrong weight

  map<string, puzz_node> nodes;
  regex towerInfo("(\\w+)");

  for (auto const &i : puzz) {
    auto info_begin = sregex_iterator(i.begin(), i.end(), towerInfo);
    // 1st entry in line is name, 2nd entry is weight
    auto info_name = info_begin;
    auto info_weight = ++info_begin;
    string node_name = (*info_name).str();
    int node_weight = stoi((*info_weight).str());
    puzz_node pn = puzz_node(node_name, node_weight);
    // 3rd+ entry are children (if present)
    auto info_children = ++info_begin;
    auto info_end = sregex_iterator();
    for (auto j = info_children; j != info_end; ++j) {
      string child_name = (*j).str();
      pn.add_child(child_name);
    }
    nodes.try_emplace(node_name, move(pn));
  }

  fill_out_weights(nodes, bottom);

  vector<string> unbalanced;
  find_unbalanced_nodes(unbalanced, nodes, bottom);
  auto part2 = balance_tree(unbalanced, nodes);

  cout << format("Part 2: {}\n", part2);
}

int fill_out_weights(map<string, puzz_node> &nodes, const string &sv) {
  auto pn = nodes.at(sv);
  if (pn.num_children() == 0)
    return pn.weight;

  vector<int> weights;

  for (const auto &i : pn.child) {
    auto child_weight = fill_out_weights(nodes, i);
    weights.push_back(child_weight);
  }
  if (all_of(weights.begin(), weights.end(),
             [=](auto i) { return i == weights[0]; }))
    pn.balanced = true;
  pn.children_total_weight = accumulate(weights.begin(), weights.end(), 0);

  auto total = pn.weight + pn.children_total_weight;
  auto [it, ins] = nodes.insert_or_assign(sv, move(pn));

  return total;
}

void find_unbalanced_nodes(vector<string> &unbalanced,
                           const map<string, puzz_node> &nodes,
                           const string &sv) {
  auto pn = nodes.at(sv);
  if (!pn.balanced && pn.num_children() != 0)
    unbalanced.push_back(pn.name);

  for (const auto &i : pn.child)
    find_unbalanced_nodes(unbalanced, nodes, i);
}

int balance_tree(const vector<string> &unbalanced,
                 const map<string, puzz_node> &nodes) {
  // the node that needs balancing is the highest one in the tree that is
  // unbalanced i.e. the last node added to the list of unbalanced nodes

  auto pn = nodes.at(unbalanced[unbalanced.size() - 1]);
  // cout << "balancing " << pn.name << ": ";

  vector<balance_info> balnodes;

  for (const auto &i : pn.child) {
    auto cn = nodes.at(i);
    balnodes.push_back(
        balance_info{cn.name, cn.weight + cn.children_total_weight});
  }

  int min = balnodes[0].weight;
  int max = balnodes[0].weight;

  for (const auto &i : balnodes) {
    if (i.weight > max)
      max = i.weight;
    if (i.weight < min)
      min = i.weight;
  }

  int count_min = 0;
  int count_max = 0;

  for (const auto &i : balnodes) {
    if (i.weight == min)
      count_min++;
    if (i.weight == max)
      count_max++;
  }

  int delta = 0;
  string balance;

  for (const auto &i : balnodes) {
    if (count_min > count_max) {
      // count_min is the mode; balance by subtracting from the node that weighs
      // max
      if (i.weight == max) {
        delta = min - max;
        balance = i.name;
        // cout << "subtract " << -delta << " from " << balance << "\n";
      }
    } else {
      // count_max is the mode; balance by adding to the node that weight min
      if (i.weight == min) {
        delta = max - min;
        balance = i.name;
        // cout << "add " << delta << " to " << balance << "\n";
      }
    }
  }

  auto bn = nodes.at(balance);
  // cout << "new weight of " << balance << ": " << bn.weight + delta << "\n";

  return (bn.weight + delta);
}
