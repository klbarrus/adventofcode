FROM gcc:latest
COPY . /usr/src/aoc
WORKDIR /usr/src/aoc
RUN g++ --std=c++23 -lstdc++ -o aoc main.cpp
CMD ["./aoc", "test-1.txt", "test-2.txt", "data.txt"]
