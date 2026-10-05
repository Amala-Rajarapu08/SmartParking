# Smart Parking Management System

## 1. Project Overview

The Smart Parking Management System is a Python-based application used to manage vehicle parking in a parking area.

The system provides five parking slots. Users can park vehicles, remove vehicles, view available slots, check parking summaries, and calculate parking fees.

## 2. Aim

To develop a Python-based parking management system that efficiently manages parking slots, tracks vehicles, calculates parking fees, and evaluates program performance.

## 3. Problem Decomposition

The main problem is divided into smaller tasks:

* **Parking slot management:** Check available slots and assign a slot to a vehicle.
* **Vehicle entry:** Store the vehicle number and entry time.
* **Vehicle removal:** Remove a parked vehicle and calculate its parking fee.
* **Parking summary:** Display total, occupied, and available slots.
* **Performance evaluation:** Measure the time taken to search for available slots.
* **Background reporting:** Generate a parking summary using a separate thread.

## 4. Computational Thinking

### 4.1 Abstraction

Abstraction hides unnecessary implementation details. The `ParkingSystem` class provides methods such as `park_vehicle()`, `remove_vehicle()`, and `summary()` so users can perform parking operations without knowing the internal implementation.

### 4.2 Pattern Recognition

The system repeatedly performs similar operations, such as checking parking slots and searching for a vehicle. These repeated tasks are handled using loops and reusable methods.

### 4.3 Algorithm Design

The system uses step-by-step algorithms to park vehicles, remove vehicles, and calculate parking fees.

### 4.4 Algorithm Paradigms

The project mainly uses a sequential search approach to find available parking slots. It does not currently implement advanced paradigms such as dynamic programming, backtracking, or branch-and-bound because they are not required for the current parking operations.

## 5. Data Structures

The project uses the following data structures:

* **Dictionary:** Stores parking slot numbers and vehicle numbers.
* **Dictionary:** Stores vehicle entry times.
* **Iterator:** Processes parking slots one by one.
* **Generator:** Produces available slot numbers when requested.
* **List comprehension:** Filters occupied parking slots in the advanced Python examples.

## 6. Algorithm and Complexity

### Available Slot Search

**Algorithm:**

1. Start from the first parking slot.
2. Check whether the slot is empty.
3. If it is empty, return that slot.
4. Otherwise, continue to the next slot.
5. If no empty slot is found, report that parking is full.

**Time complexity:** O(n), where n is the number of parking slots.

**Space complexity:** O(1) additional space for the search operation, excluding the stored parking data.

## 7. Object-Oriented Programming

The project uses the `ParkingSystem` class to organize parking-related data and operations.

* **Class:** `ParkingSystem` defines the parking system.
* **Object:** `parking` is an instance of the class.
* **Encapsulation:** Parking data and related methods are grouped inside the class.
* **Reusability:** Methods can be called multiple times without rewriting the same logic.

Inheritance and polymorphism are not implemented in the current version.

## 8. Advanced Python Features

The project demonstrates several Python features:

* **Functions:** Reusable operations for parking management.
* **Type hints:** Improve code readability and support static type checking.
* **Generator:** Produces available parking slots.
* **Decorator:** Measures the execution time of parking and vehicle removal methods.
* **Context manager:** Measures execution time in the advanced feature demonstration.
* **Higher-order function:** Demonstrated through a discount function.
* **Generic function:** Demonstrated using a type variable.
* **Comprehensions:** Create dictionaries and filter occupied slots.
* **Threading:** Runs a background parking summary report.
* **Lock:** Helps protect shared parking data during parking operations.

## 9. Functional Programming

The `calculate_fee()` function calculates the parking fee from its input values without modifying the parking system's data.

This demonstrates the use of a pure function.

The advanced Python demonstration also includes a higher-order function that accepts another function as an argument.

## 10. Testing and Code Quality

The project uses pytest for automated testing.

The tests cover:

* Parking a vehicle.
* Preventing duplicate vehicle entries.
* Handling a full parking area.
* Removing vehicles and calculating fees.
* Displaying parking summaries.
* Viewing parking slots.
* Handling invalid input.
* Testing advanced Python features and menu operations.

### Testing Results

* Total tests passed: 22
* Code coverage for `main.py`: 98%
* Formatting tool: Black
* Static type checker: mypy

All 22 tests passed in the latest test run. Black formatting and mypy checks also completed successfully.

## 11. Performance Evaluation

The project includes a performance evaluation function that searches for available slots 1,000 times.

It measures the total execution time and average time per operation.

The available-slot search uses a linear approach with O(n) time complexity, where n represents the number of parking slots.

## 12. AI-Assisted Development

AI assistance can support software development by helping with:

* Understanding project requirements.
* Generating initial code and test cases.
* Identifying errors and suggesting corrections.
* Improving code structure and readability.
* Preparing documentation.

AI-generated suggestions should be reviewed, tested, and validated before being included in the final project.

## 13. Conclusion

The Smart Parking Management System demonstrates how Python can be used to solve a practical parking management problem.

The project combines data structures, object-oriented programming, algorithms, advanced Python features, threading, automated testing, and performance measurement.

The current test results show that the main parking system has 98% test coverage, with all 22 automated tests passing.
