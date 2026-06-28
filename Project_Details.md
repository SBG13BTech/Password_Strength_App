# Password Strength Checker (GUI)

## Overview

This project is a GUI-based Password Strength Checker built using Python and Tkinter. It evaluates the strength of a password based on multiple rules and provides feedback to help users create stronger passwords.

---

## Features

* Checks minimum password length (at least 12 characters)
* Detects common passwords using a dataset
* Identifies repeated characters (e.g., `aaa`, `111`)
* Detects sequential patterns (e.g., `abcd`, `1234`)
* Evaluates password strength using a scoring system (0–5)
* Displays multiple issues at once instead of stopping at the first error
* Simple and interactive GUI

---

## Technologies Used

* Python
* Tkinter (for GUI)

---

## How to Run

1. Make sure Python is installed on your system
2. Download or clone this repository
3. Ensure `Common_Passwords.txt` is in the same folder as the Python file
4. Run the program:

```bash
python main.py
```

---

## How It Works

The application:

1. Takes user input from the GUI
2. Checks for:

   * Length
   * Common passwords
   * Repetition
   * Sequences
3. Displays warnings for each issue
4. Calculates a strength score if the password is not common

---

## Scoring System

| Score | Strength        |
| ----- | --------------- |
| 0     | Very Weak       |
| 1     | Weak            |
| 2     | Slightly Weak   |
| 3     | Slightly Strong |
| 4     | Strong          |
| 5     | Very Strong     |

---

## Example Checks

* `123456` → Too short, common, sequence
* `aaaaaaa` → Repetition detected
* `Hello@123` → Medium strength
* `G7@kL9#pQ2!` → Strong password

---

## Future Improvements

* Add password suggestions
* Add strength meter (progress bar)
* Improve UI design
* Optimize common password lookup

---
