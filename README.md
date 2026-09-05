# CodeAlpha_StockPortfolioTracker
# 📈 Stock Portfolio Tracker – CodeAlpha Internship Project

## 📌 Project Overview

This project is a **simple Stock Portfolio Tracker developed in Python** as part of my **CodeAlpha Internship**.

The program allows users to select stocks from a predefined list, enter the quantity they own, and calculate the total investment value. The final result is also saved in a text file called `portfolio.txt`.

## 🎯 Objective

The main objective of this project is to create a simple program that can:

* Display a list of available stocks.
* Accept stock names and quantities from the user.
* Calculate the value of each selected stock.
* Calculate the total investment value.
* Save the final result to a text file.

## ✨ Features

* 📊 Displays available stocks and their prices.
* 💰 Calculates individual stock values.
* 📈 Calculates the total investment value.
* 🔤 Accepts stock names without worrying about uppercase/lowercase input.
* ❌ Handles stocks that are not available in the predefined list.
* 📄 Saves the final portfolio value to `portfolio.txt`.

## 💵 Available Stocks

The program uses a hardcoded dictionary containing the following stock prices:

| Stock | Price |
| ----- | ----: |
| AAPL  |  $180 |
| TSLA  |  $250 |
| GOOGL |  $150 |
| MSFT  |  $420 |
| AMZN  |  $180 |

> **Note:** These prices are hardcoded for educational purposes and do not represent live market prices.

## 🛠️ Technologies Used

* **Python 3**
* Dictionary
* Loops
* Conditional statements
* User input
* File handling

## 📚 Python Concepts Used

This project helped me practice:

* Dictionaries
* Variables
* `for` loops
* `if-else` statements
* User input using `input()`
* String methods such as `.upper()`
* Arithmetic operations
* Formatted strings using f-strings
* File handling using `open()`

## ▶️ How to Run the Project

### Step 1: Install Python

Make sure Python 3 is installed on your computer.

Check the installation using:

```bash
python --version
```

### Step 2: Clone the Repository

```bash
git clone https://github.com/your-username/stock-portfolio-tracker.git
```

### Step 3: Navigate to the Project Folder

```bash
cd stock-portfolio-tracker
```

### Step 4: Run the Program

```bash
python portfolio.py
```

No external Python libraries are required to run this project.

## 💻 Sample Output

```text
----- Stock Portfolio Tracker -----
Available stocks: AAPL, TSLA, GOOGL, MSFT, AMZN

How many stocks do you want to add? 2

Enter stock name: AAPL
Enter quantity: 5
AAPL: $180 × 5 = $900

Enter stock name: TSLA
Enter quantity: 2
TSLA: $250 × 2 = $500

-------------------------------
Total Investment Value: $1400
-------------------------------
Result saved to portfolio.txt
```

## 📄 Output File

After running the program, a file named:

```text
portfolio.txt
```

is automatically created.

It contains the total investment value, for example:

```text
Stock Portfolio Tracker
------------------------
Total Investment Value: $1400
```

## 📂 Project Structure

```text
stock-portfolio-tracker/
│
├── portfolio.py
├── portfolio.txt
└── README.md
```

## 🚀 Future Improvements

The project can be improved by adding:

* Live stock market prices using an API.
* More stocks and companies.
* Portfolio performance tracking.
* Profit and loss calculations.
* CSV file support.
* Better input validation.
* A graphical user interface (GUI).

## 🎓 Internship Information

**Internship:** CodeAlpha Internship
**Project:** Python Development
**Project Type:** Console-Based Python Application
**Task:** Stock Portfolio Tracker

This project was developed as part of my **CodeAlpha Internship** to gain practical experience with Python dictionaries, calculations, loops, and file handling.

## 👨‍💻 Author

**Akash**

---

⭐ *This project was created as part of my CodeAlpha Internship to strengthen my Python programming, problem-solving, and practical development skills.*
