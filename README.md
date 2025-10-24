# My DSA Solutions - ZTM Course

Personal solutions and implementations for the Zero to Mastery (ZTM) Data Structures and Algorithms Masterclass using C++.

## About

This repository contains my personal implementations and solutions while working through the ZTM DSA Masterclass on Udemy. All solutions are written in C++ and compiled/tested on OMARCHY Linux (Arch-based distribution).

## Setup

### Prerequisites

- C++ compiler (g++ or clang++)
- Linux/Unix environment (OMARCHY/Arch Linux)
- Git for version control

### Verify Your Environment

```bash
g++ --version
# Ensure C++17 or later is supported
```

### Compilation

Standard compilation command for most solutions:

```bash
g++ -std=c++17 -o output_name filename.cpp
./output_name
```

For debugging with additional flags:

```bash
g++ -std=c++17 -Wall -Wextra -g -o output_name filename.cpp
./output_name
```

## Repository Structure

```
.
├── Arrays/
│   ├── two_sum.cpp
│   ├── reverse_array.cpp
│   └── ...
├── LinkedLists/
│   ├── reverse_linked_list.cpp
│   ├── detect_cycle.cpp
│   └── ...
├── Stacks/
│   ├── valid_parentheses.cpp
│   └── ...
├── Queues/
├── Trees/
│   ├── binary_tree_traversal.cpp
│   ├── bst_operations.cpp
│   └── ...
├── Graphs/
│   ├── bfs.cpp
│   ├── dfs.cpp
│   └── ...
├── Sorting/
│   ├── bubble_sort.cpp
│   ├── merge_sort.cpp
│   ├── quick_sort.cpp
│   └── ...
├── Searching/
│   ├── binary_search.cpp
│   └── ...
├── DynamicProgramming/
│   ├── fibonacci.cpp
│   ├── knapsack.cpp
│   └── ...
└── README.md
```

## Learning Resources

- **Course**: [ZTM - Master the Coding Interview: Data Structures + Algorithms](https://zerotomastery.io/courses/learn-data-structures-and-algorithms/)
- **Reference Repository**: [shree1999/Data-Structures-and-Algorithms](https://github.com/shree1999/Data-Structures-and-Algorithms)
- **Editor**: Neovim with LazyVim configuration
- **Terminal**: Kitty

## Progress Tracking

| Topic | Status | Problems Solved |
|-------|--------|-----------------|
| Arrays & Strings | 🔄 In Progress | 0/20 |
| Linked Lists | ⏳ Not Started | 0/15 |
| Stacks & Queues | ⏳ Not Started | 0/10 |
| Trees & Graphs | ⏳ Not Started | 0/25 |
| Sorting Algorithms | ⏳ Not Started | 0/8 |
| Searching | ⏳ Not Started | 0/5 |
| Dynamic Programming | ⏳ Not Started | 0/20 |
| Recursion | ⏳ Not Started | 0/12 |
| Hash Tables | ⏳ Not Started | 0/10 |

Legend:
- ✅ Completed
- 🔄 In Progress
- ⏳ Not Started

## Notes

- All solutions are personal implementations created while following the course
- Reference solutions are checked against the official repository only when stuck
- Focus is on understanding concepts rather than memorizing solutions
- Code is compiled and tested on OMARCHY Linux with g++ compiler

## Workflow

1. Watch course lecture on specific topic
2. Attempt to solve problem independently
3. Compile and test solution locally
4. If stuck, reference the official repository
5. Refactor and optimize solution
6. Document learnings and edge cases

## Common Commands

```bash
# Compile a single file
g++ -std=c++17 -o solution problem.cpp && ./solution

# Compile with all warnings
g++ -std=c++17 -Wall -Wextra -pedantic -o solution problem.cpp

# Compile with debugging symbols
g++ -std=c++17 -g -o solution problem.cpp

# Run with valgrind for memory checks
valgrind --leak-check=full ./solution
```

## License

Personal learning repository - not intended for commercial use.

## Contact

Created while learning DSA for interview preparation and competitive programming practice.

---

**Last Updated**: October 24, 2025