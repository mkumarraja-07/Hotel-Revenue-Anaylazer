# Project Summary: Hotel Revenue Analyzer

**Language:** Python 3

**Concepts:** Functions, Loops, Conditions, File Handling, Pandas, Matplotlib

**Code file:** `hotel_revenue_analyzer.py`

**Data file:** `hotel_sales.csv`

---

## 1. Project Overview

This project is a console-based hotel sales analyzer. It reads room sales data from a CSV file (`hotel_sales.csv`) with the columns `Date`, `RoomType`, `RoomsSold` and `Rate`. Each row is checked, and wrong rows are skipped with a warning. For every valid row, the program calculates `Revenue = RoomsSold × Rate`. A menu then lets the user see the daily revenue (with the best day and a bar chart), the revenue by room type (with percentage share and a bar chart), or all the valid records. The program keeps running until the user chooses `4. Exit`.

## 2. What I Have Done

- Used `pandas` to read the CSV file with `pd.read_csv()`, and `matplotlib` to draw the charts.
- Put the file loading and checking in a function named `load_data()`, and made one more function for each menu option: `daily_revenue()`, `revenue_by_room_type()` and `show_all_data()`.
- Checked that the file exists using `os.path.exists()`, and used `try/except` so a bad CSV file does not crash the program.
- Checked that all 4 required columns (`Date`, `RoomType`, `RoomsSold`, `Rate`) are present. If one is missing, the program shows an error and stops.
- Used a **`for` loop** with `iterrows()` to check every row one by one.
- Skipped a row with a warning when `RoomsSold` or `Rate` is negative, when `Date` or `RoomType` is empty, or when `RoomsSold` or `Rate` is not a number.
- Added a new `Revenue` column by multiplying `RoomsSold` and `Rate`.
- Used `groupby()` and `sum()` to get the revenue for each date and for each room type.
- Used `idxmax()` and `max()` to find the best day.
- Calculated the percentage share of each room type, shown with 2 decimal places.
- Drew a bar chart for the daily revenue and another for the room type revenue.
- Used a **`while True` loop** with `if`, `elif` and `else` to show the menu again and again, and `break` to exit.
- Added a message for wrong menu choices: `Invalid choice. Please enter 1, 2, 3 or 4.`
- Handled the case when there is no valid data, by showing `No valid data available.`
- Tested the program with the test cases given below.

## 3. Test Cases and Screenshots

### Test Case 1:
<img width="1917" height="1030" alt="Screenshot 2026-11-13 192249" src="https://github.com/user-attachments/assets/c6515626-1d36-4e70-a5d7-421cde17f3ac" />




### Test Case 2:
<img width="1917" height="1010" alt="Screenshot 2026-11-13 192304" src="https://github.com/user-attachments/assets/6b5eda52-6b45-41d6-b50d-3fdb1980c945" />




### Test Case 3:
<img width="1917" height="1016" alt="Screenshot 2026-11-13 192326" src="https://github.com/user-attachments/assets/f8e3de64-8bb2-46b0-8ca1-fcc115b3a7bc" />




### Test Case 4:
<img width="1915" height="1018" alt="Screenshot 2026-11-13 192340" src="https://github.com/user-attachments/assets/943ffcfd-367f-4e20-a209-066ca6a15315" />


### Graph OLf Test Case 1:
<img width="800" height="500" alt="graph_project" src="https://github.com/user-attachments/assets/2363ef36-cd7a-4897-ba2a-35ba0cf7dd02" />

### Graph OLf Test Case 2:
<img width="700" height="500" alt="graph_proj" src="https://github.com/user-attachments/assets/cdaa4658-9b9e-4955-916e-9832d3e83c8f" />







## 4. Hardships Faced and How I Overcame Them

| Hardship | How I Overcame It |
|---|---|
| **Program crashed when the file was missing.** Running the code without the CSV file gave a `FileNotFoundError`. | I used `os.path.exists()` to check the file first. If it is not found, the program prints an error and returns safely. |
| **Bad values in the data.** Text like `abc` in `RoomsSold` stopped the program with a `ValueError`. | I put the conversion `float()` inside a `try/except` block. A bad row now gives a warning and is skipped. |
| **Negative numbers were accepted.** A rate or rooms sold below 0 gave a wrong revenue. | I added an `if` check for `rooms_sold < 0` and `rate < 0`, and skipped those rows with a clear warning. |
| **Row numbers in warnings were confusing.** Pandas starts the index at 0, but a person counts rows from 1. | I used `row_number = index + 1` so the warning shows the row number the way the user sees it. |
| **Missing values were not caught.** Empty `Date` or `RoomType` cells became `NaN` and gave strange output. | I used `pd.isna()` to find empty cells and skipped those rows with a `missing values` warning. |
| **Revenue column did not exist at first.** I tried to group by revenue before it was calculated. | I created `Revenue = RoomsSold * Rate` right after the valid rows were collected, so every later function can use it. |
| **Empty data crashed the analysis.** If all rows were wrong, `idxmax()` gave an error. | I checked `df is None or df.empty` at the start of every function and print `No valid data available.` |
| **Percentage did not look right.** The values had many decimal places. | I used the format `:.2f` for percentage and `:.0f` for revenue so the output is neat. |
| **Chart labels were cut off.** The date labels on the bar chart overlapped the edges of the window. | I added `plt.tight_layout()` before `plt.show()`, so everything fits inside the figure. |
| **Menu kept asking after a wrong choice.** I was not sure how to handle numbers outside 1 to 4. | I added an `else` branch that shows an error message, and the `while True` loop shows the menu again. |

## 5. What I Learned

- How to read a CSV file using `pandas` and check that the needed columns are there.
- How to clean data by checking each row and skipping the wrong ones with a warning.
- How to use `groupby()` and `sum()` to total values by date and by category.
- How to draw bar charts using `matplotlib`.
- How to use `try/except` so the program does not crash on bad input or a bad file.
- How to build a menu-driven program using a `while` loop and functions.
- How to test a program against different cases and find the reason for a difference in output.

## 6. How to Run

Install the required libraries (only once):

```bash
pip install pandas matplotlib
```

Keep `hotel_revenue_analyzer.py` and `hotel_sales.csv` in the same folder, and then run:

```bash
python hotel_revenue_analyzer.py
```

## 7. Files in This Project

```
Python-Projects/
├── hotel_revenue_analyzer.py   # main program
├── hotel_sales.csv             # hotel sales data
├── images/                     # screenshots of the test cases
├── README.md                   # project description
└── Summary.md                  # this summary
```
