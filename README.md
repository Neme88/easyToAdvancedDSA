Big O Notation - Time Complexity Guide

📌 Overview

This repository contains a comprehensive guide to Big O Notation, including time complexities for various algorithms and data structures. The goal is to help developers understand how different operations scale as input size increases.

📊 What is Big O Notation?

Big O Notation describes the efficiency of an algorithm in terms of time complexity (how fast it runs) and space complexity (how much memory it uses). It represents the upper bound of an algorithm's growth rate as input size increases.

⏳ Common Time Complexities

Below are the most common time complexities in order of best to worst performance:

Notation

Complexity Name

Example Algorithm

O(1)

Constant Time

Hash table lookup

O(log n)

Logarithmic Time

Binary Search

O(n)

Linear Time

Iterating over an array

O(n log n)

Linearithmic Time

Merge Sort, Quick Sort (best/average case)

O(n²)

Quadratic Time

Bubble Sort, Selection Sort

O(2ⁿ)

Exponential Time

Fibonacci (naïve recursion)

O(n!)

Factorial Time

Traveling Salesman Problem (brute-force)

📂 Repository Structure

This repository is structured as follows:

📂 easyToAdvancedDSA
│── 📁 Big-O Notation      # Code implementations of algorithms
│── 📁 data-structures  # Time complexities of common data structures
│── 📁 functions  # Summary table of Big O complexities
│── 📄 README.md        # Overview and explanations


🔥 Algorithms Covered

This repository includes Big O analysis for:

Sorting Algorithms (Bubble Sort, Merge Sort, Quick Sort, etc.)

Searching Algorithms (Binary Search, Linear Search)

Graph Algorithms (DFS, BFS, Dijkstra's Algorithm)

Recursion & Dynamic Programming (Fibonacci, Memoization, Tabulation)


📌 Data Structures & Their Complexities

1️⃣ Arrays

Operation

Time Complexity

Access

O(1)

Search

O(n)

Insert (end)

O(1)

Insert (middle)

O(n)

Delete

O(n)

2️⃣ Linked Lists

Operation

Time Complexity

Access

O(n)

Search

O(n)

Insert

O(1) (at head)

Delete

O(1) (at head)

3️⃣ Hash Tables

Operation

Time Complexity (Avg)

Time Complexity (Worst)

Insert

O(1)

O(n)

Search

O(1)

O(n)

Delete

O(1)

O(n)

More data structures (Stacks, Queues, Trees, Graphs) are included in the data-structures/ folder.

🚀 How to Use This Repository

Clone the repository:

git clone https://github.com/Neme88/easyToAdvancedDSA.git

Navigate into the directory:

cd big-o-notation-guide

Explore the different algorithms and data structures with their time complexity analysis.

📖 References

Big O Cheat Sheet

Introduction to Algorithms (Cormen, Leiserson, Rivest, Stein)

Cracking the Coding Interview (Gayle Laakmann McDowell)

💡 Contributions

Contributions are welcome! Feel free to fork this repo, create a new branch, and submit a pull request (PR) with improvements.

🛠 Maintainers

This repository is maintained by Your Name. If you have any questions, feel free to reach out or open an issue.

⭐ Support

If you find this repository helpful, please star it ⭐ on GitHub!

