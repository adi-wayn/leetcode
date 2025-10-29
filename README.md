🧩 LeetCode Solutions by Adi Wayn

A collection of LeetCode problem solutions — written in various programming languages — focused on improving algorithmic thinking, data structure mastery, and problem-solving efficiency.
Each solution emphasizes clarity, performance, and scalability.

📂 Project Structure
📁 leetcode/
 ├── arrays/
 │    ├── RemoveElement.java
 │    ├── TwoSum.py
 │    └── ...
 ├── strings/
 │    ├── ReverseString.cpp
 │    └── PalindromeCheck.js
 ├── linkedlist/
 │    ├── MergeTwoLists.java
 │    └── RemoveDuplicates.py
 ├── README.md
 └── ...


Each folder represents a topic category (Arrays, Strings, Linked Lists, etc.)

Each file contains a complete, well-documented solution with examples and comments.

🚀 How to Run

Open the file in your preferred IDE or editor (e.g., IntelliJ, VS Code, PyCharm, etc.).

Ensure you have the proper environment for the file’s language (Java, Python, C++, etc.).

Run the program’s entry point (main, function call, or test block).

Some problems include example test cases for validation.

🧠 Example Problem
Remove Element

Given an array nums and a value val, remove all instances of val in-place and return the new length.

def removeElement(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k


Explanation:
We don’t delete elements — we overwrite them.
Everything beyond the new length can be ignored.

🧩 Topics Covered

Arrays & Strings

Linked Lists

Stacks & Queues

Recursion & Backtracking

Binary Trees

HashMaps & Sets

Sliding Window

Dynamic Programming

Greedy Algorithms

🎯 Purpose

💡 A personal learning space for building strong algorithmic foundations and preparing for technical interviews.
All solutions are written with a focus on readability, efficiency, and modularity.

🧰 Tools & Technologies

Any programming language supported on LeetCode (Java, Python, C++, JavaScript, etc.)

Git & GitHub for version control

Optional unit testing (JUnit, pytest, etc.)

📬 Contact

Author: Adi Wayn
📧 adiwayn@gmail.com

🌐 LeetCode Profile

💻 GitHub Profile

📄 License

This repository is distributed under the MIT License.
Feel free to use, share, or modify the code for learning and educational purposes.
