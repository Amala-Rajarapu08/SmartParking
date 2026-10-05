# Smart Parking Management System

## 1. Introduction

The Smart Parking Management System is a Python-based application that manages vehicle parking using a simple menu-driven interface. It helps users park vehicles, view available slots, remove vehicles, and calculate parking fees.

## 2. Objectives

* Manage parking slots efficiently.
* Check parking slot availability.
* Record vehicle entry times.
* Calculate parking fees based on parking duration.
* Display parking summaries.

## 3. Technologies Used

* **Programming Language:** Python 3.9
* **Concepts:** Object-Oriented Programming, dictionaries, functions, loops, and conditional statements
* **Testing:** Pytest
* **Code Coverage:** Pytest-cov
* **Static Type Checking:** Mypy

## 4. Main Features

1. View parking slots.
2. Park a vehicle in the first available slot.
3. Prevent duplicate vehicle entries.
4. Remove a parked vehicle.
5. Calculate parking fees at ₹20 per hour, with a minimum charge of ₹20.
6. Display total, occupied, and available slots.

## 5. Data Structures

Dictionaries are used to store parking slot information and vehicle entry times. This allows the system to organize and retrieve parking information.

## 6. Testing and Results

Eight automated tests were executed using Pytest.

**Test result:** 8 passed.

**Code coverage:** 68% of statements in `main.py` were covered by the tests.

**Static type checking:** Mypy reported no issues in `main.py`.

## 7. Conclusion

The Smart Parking Management System successfully performs basic parking operations, calculates parking fees, and displays parking summaries. Automated testing and static type checking were used to verify the program.
## 8. Algorithm Design

### Vehicle Parking Algorithm

1. Start the parking system.
2. Read the vehicle number from the user.
3. Convert the vehicle number to uppercase and remove extra spaces.
4. Check whether the vehicle is already parked.
5. Search for the first available parking slot.
6. Assign the vehicle to that slot and record its entry time.
7. Display a success message.
8. If no slot is available, display a parking-full message.

### Vehicle Removal Algorithm

1. Read the vehicle number.
2. Check whether the vehicle is currently parked.
3. Calculate the parking duration using the recorded entry time.
4. Calculate the parking fee.
5. Free the occupied slot and remove the vehicle's entry record.
6. Display the parking duration and fee.

## 9. Time and Space Complexity

Let **n** represent the number of parking slots.

| Operation          | Time Complexity |
| ------------------ | --------------- |
| View parking slots | O(n)            |
| Park a vehicle     | O(n)            |
| Remove a vehicle   | O(n)            |
| Parking summary    | O(n)            |

The parking system uses dictionaries to store slot details and entry times. The overall space complexity is **O(n)** because storage grows with the number of parking slots and parked vehicles.

## 10. AI-Assisted Development

AI assistance was used to help understand the project requirements, develop Python code, identify errors, and prepare automated tests.

The generated code was reviewed and tested before being used in the project. Pytest was used to validate the main parking operations, and Mypy was used to check type annotations.
## Performance Evaluation

The Smart Parking Management System was evaluated using 1,000 available-slot search operations.

**Measured results:**

* Total execution time: 0.000924 seconds
* Average execution time: 0.00000092 seconds
* Number of operations: 1,000
* Time complexity: O(n), where n is the number of parking slots

The performance test demonstrates the execution time of the available-slot search with five parking slots. The measured time may vary depending on the computer and system load.

## Testing Results

The application was tested using pytest.

* Total test cases: 8
* Passed: 8
* Failed: 0
* Code coverage: 73%
* Static type checking: Passed
* Code formatting: Passed

All eight existing test cases passed successfully after the performance evaluation feature was added.


