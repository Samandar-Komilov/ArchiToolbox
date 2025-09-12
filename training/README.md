# 🧠 DSA Mastery Plan (Builder-Focused)

**Duration:** May – December 2025
**Reference Book:** *Data Structures and Algorithms in Python* by Goodrich
**Supporting Resources:**

* *Recursive Book of Recursion* by Al Sweigart
* Udemy Course: *Python Data Structures and Algorithms + Leetcode*

**Focus:** Master DSA via implementation and integration in real-world systems (Nginx, Redis, SQLite)

---

## 🌟 Goals

* Move from paper-level knowledge to deep implementation and real-world application.
* Master DSA not for interviews, but for system building as a future software architect.
* Learn to integrate DSA directly into full systems (Redis, SQLite).

---

## 🗓️ Phase 1: Foundation & Core Structures (May)

### Subphases and Learning Strategy:

Each week focuses on a core theme with deep integration between Book, Udemy, and Recursion Book.

#### ✅ Week 1: Recursion Intuition + Array Fundamentals

* Read Ch. 1–3 from *Recursive Book of Recursion*
* Study recursion basics from Goodrich (Ch. 4)
* Solve recursive problems on strings & arrays

**GitHub Issues:**

* \[Read] Recursion Book Ch. 1–3
* \[Implement] Factorial, Fibonacci (Recursive and Iterative)
* \[Practice] Reverse string, Palindrome check, Sum of array recursively
* \[Read] Goodrich Ch. 4: Recursion
* \[Write] Recursive intuition notes

#### ✅ Week 2: Array-Based Sequences & Techniques

* Study Goodrich Ch. 5: Array-based structures
* Implement dynamic array, Python list behavior
* Techniques: Two Pointers, Sliding Window, Prefix Sum, Difference Array, Binary Search

**GitHub Issues:**

* \[Read] Goodrich Ch. 5
* \[Implement] DynamicArray class in Python
* \[Implement] Two Pointers, Sliding Window examples
* \[Implement] Prefix Sum, Difference Array (1D, 2D)
* \[Practice] Binary Search and variants (lower bound, upper bound)
* \[Write] Note: When to use which technique

#### ✅ Week 3: Stacks & Queues

* Study Goodrich Ch. 6
* Implement Stack and Queue via lists and linked lists
* Concepts: Balanced Parentheses, Infix to Postfix, Min Stack
* Include recursion-based stack uses (call stack, backtracking basics)

**GitHub Issues:**

* \[Read] Goodrich Ch. 6
* \[Implement] Stack using list and LL
* \[Implement] Queue using list and LL
* \[Project] Balanced Parentheses Checker
* \[Implement] Reverse Stack using Recursion
* \[Practice] Implement Infix to Postfix converter

#### ✅ Week 4: Linked Lists Deep Dive

* Study Goodrich Ch. 7 + Udemy LL section
* Implement Singly, Doubly, and Circular Linked Lists
* Techniques: Fast/Slow Pointers, Cycle Detection, LL Reversal (iterative and recursive)

**GitHub Issues:**

* \[Read] Goodrich Ch. 7
* \[Follow] Udemy: Linked List implementation
* \[Implement] Singly Linked List
* \[Implement] Doubly Linked List
* \[Implement] Circular Linked List
* \[Practice] Detect cycle (Floyd’s), Reverse LL, Find middle node

#### ✅ Week 5: Recap and Reimplementation

* Re-implement major structures in C (if relevant to Cserver)
* Combine data structures in small CLI apps
* Review recursion and connections

---

## 🎡 Mini Projects (Phase 1)

* Text Buffer using Gap Buffer (array-based insert/delete)
* CLI Stack/Queue Visualizer
* Recursion Problems CLI (prompt user for recursive task)

---

## 🗓️ Phase 2: Sorting & Recursion Patterns (June)

### Topics:

* Sorting algorithms: Selection, Insertion, Merge, Quick, Heap Sort
* Divide & conquer recursion
* Sorting technique patterns (stable sort, in-place, recursion trees)
* Binary tree intro

### Subphases and Learning Strategy:

#### ✅ Week 1: Basic Sorts & Concepts

* 📖 Goodrich: Ch. 12.1–12.2 (Selection, Insertion Sort)
* 🎥 Udemy: Sorting section intro
* Practice: Stability, in-place sorting, selection/insertion analysis
* ✅ GitHub Issues:

  * [ ] Implement selection + insertion sort
  * [ ] Markdown note on time complexity, stable vs unstable sort
  * [ ] Build CLI sorter for numeric data files

#### ✅ Week 2: Merge & Quick Sort

* 📖 Goodrich: Ch. 12.3–12.4
* 🎥 Udemy: Merge sort & quick sort section
* Practice: Recursion trees, memory analysis, divide-and-conquer recursion
* ✅ GitHub Issues:

  * [ ] Implement merge sort (recursive + in-place)
  * [ ] Implement quick sort (with pivot strategy comparison)
  * [ ] Markdown note: recursion depth + memory

#### ✅ Week 3: Heap Sort & Binary Tree Basics

* 📖 Goodrich: Ch. 9.1–9.3 (Binary trees), 10.1 (Heaps)
* 🎥 Udemy: Heap implementation
* 🔹 Recursive Book: Tree recursion preview (skip Ch. 4 full deep dive)
* ✅ GitHub Issues:

  * [ ] Implement heap sort using min/max heap
  * [ ] Build CLI priority queue simulator
  * [ ] Markdown note: tree-based sorting vs linear-based

#### ✅ Week 4: Sorting Use Cases

* Apply sorting in real systems: log parsing, file systems, etc.
* Practice: k-sorted arrays, external sort design, stable sort importance
* Mini Project:

  * CLI file sorter (by size/date)
  * Markdown note: real-world sorting decisions
  * Add optional: Recursive merge sort implementation in C


---

## 🗓️ Phase 3: Trees Deep Dive (July)

### Subphases and Learning Strategy:


---

## 🗓️ Phase 4: Graphs & Heaps (August)

### Subphases and Learning Strategy:


---

## 🗓️ Phase 5: Real-World System Models (September)

### Subphases and Learning Strategy:


---

## 🗓️ Phase 6: Redis & SQLite Integration (October–December)

### Subphases and Learning Strategy:

---

## 📃 Weekly Schedule

| Day     | Focus                         |
| ------- | ----------------------------- |
| Mon     | Read book + implement concept |
| Tue     | Solve 2 real-world problems   |
| Wed     | Build mini component          |
| Thu     | Reimplement in C if relevant  |
| Fri     | Review & refactor             |
| Weekend | Project integration           |

---

## ✅ Tracking Progress

Create a GitHub repo:

* `/implementations/` — DSA from scratch in Python & C
* `/projects/` — Real-world use mini systems
* `/notes/` — Markdown notes, diagrams, learnings
* Use **Issues** for each task, assigned to **Milestone: Phase 1**
* Use **Labels** like `recursion`, `python`, `c-impl`, `project`, `book` to track categories

---

## Final Goal by December 2025

You should be able to:

* Build Redis and SQLite-like systems from scratch
* Implement all major DSA components in Python and C
* Make architectural decisions based on algorithmic tradeoffs
* Interview confidently and build real-world systems with DSA mastery
