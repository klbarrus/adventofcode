// karlb 
// Advent of Code 2024, day 3

#include <fstream>
#include <iostream>
#include <regex>
#include <vector>

using namespace std;

void readFile(const string& filename, vector<string>& vs);
void printData(vector<string>& vs);
void part1(vector<string>& vs);

int main(int argc, char* argv[]) {
    vector<string> args(argv + 1, argv + argc);

    for (auto filename : args) {
        cout << format("File {}\n", filename);

        vector<string> vs;
        readFile(filename, vs);
//        printData(vs);

        part1(vs);
    }

    return 0;
}

void readFile(const string& filename, vector<string>& vs) {
    ifstream puzzle_in(filename);
    string line;

    while (getline(puzzle_in, line)) {
        vs.push_back(line);
    }
}

void printData(vector<string>& vs) {
    for (const auto& e : vs) {
        cout << format("{}\n", e);
    }
}

void part1(vector<string>& vs) {
    size_t total = 0;
    auto const rx = regex(R"(mul\((\d{1,3}),(\d{1,3})\))");

    for (string& e : vs) {
        for (smatch sm; regex_search(e, sm, rx);) {
//            cout << format("{} - match size {}\n", sm.str(), sm.size());
//            for (size_t i = 0; i < sm.size(); ++i) {
//                cout << sm[i] << "\n";
//            }

            // on a match, sm is size 3
            // 0 - entire mul(x,y) string
            // 1 - x
            // 2 - y
            string x(sm[1]);
            string y(sm[2]);
            int xi;
            int yi;
            from_chars(x.data(), x.data() + x.size(), xi);
            from_chars(y.data(), y.data() + y.size(), yi);

            total += xi * yi;

            e = sm.suffix();
        }
    }

    cout << format("Part 1: {}\n", total);
}