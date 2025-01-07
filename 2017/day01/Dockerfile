FROM gcc:latest
COPY . /usr/src/aoc
WORKDIR /usr/src/aoc
RUN g++ --std=c++23 -lstdc++ -o aoc main.cpp
CMD ["./aoc", "test.txt", "data.txt"]
