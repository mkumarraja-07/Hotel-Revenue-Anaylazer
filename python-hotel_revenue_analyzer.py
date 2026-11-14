import pandas as pd
import matplotlib.pyplot as plt
import os

FILE_NAME = "hotel_sales.csv"


def load_data():
    """Load and validate hotel sales data."""

    if not os.path.exists(FILE_NAME):
        print(f"Error: File '{FILE_NAME}' not found.")
        return None

    try:
        df = pd.read_csv(FILE_NAME)
    except Exception as e:
        print("Error reading CSV file:", e)
        return None

    required_columns = ["Date", "RoomType", "RoomsSold", "Rate"]

    for column in required_columns:
        if column not in df.columns:
            print(f"Error: Missing column '{column}'.")
            return None

    valid_rows = []
    skipped = 0

    for index, row in df.iterrows():
        row_number = index + 1

        try:
            rooms_sold = float(row["RoomsSold"])
            rate = float(row["Rate"])

            if rooms_sold < 0:
                print(
                    f"Warning: Row {row_number} skipped - "
                    f"RoomsSold must be 0 or more."
                )
                skipped += 1
                continue

            if rate < 0:
                print(
                    f"Warning: Row {row_number} skipped - "
                    f"Rate must be 0 or more."
                )
                skipped += 1
                continue

            if pd.isna(row["Date"]) or pd.isna(row["RoomType"]):
                print(f"Warning: Row {row_number} skipped - missing values.")
                skipped += 1
                continue

            valid_rows.append({
                "Date": str(row["Date"]),
                "RoomType": str(row["RoomType"]),
                "RoomsSold": rooms_sold,
                "Rate": rate
            })

        except (ValueError, TypeError):
            print(
                f"Warning: Row {row_number} skipped - "
                f"RoomsSold and Rate must be numeric."
            )
            skipped += 1

    valid_df = pd.DataFrame(valid_rows)

    if not valid_df.empty:
        valid_df["Revenue"] = valid_df["RoomsSold"] * valid_df["Rate"]

    print(f"\nValid records analysed: {len(valid_df)}")

    return valid_df


def daily_revenue(df):
    """Display daily revenue and best day."""

    if df is None or df.empty:
        print("No valid data available.")
        return

    daily = df.groupby("Date")["Revenue"].sum()

    print("\n--- Daily Revenue ---")

    for date, revenue in daily.items():
        print(f"{date} : Rs. {revenue:.0f}")

    total = daily.sum()

    print(f"\nTotal revenue: Rs. {total:.0f}")

    best_day = daily.idxmax()
    best_revenue = daily.max()

    print(
        f"Best day: {best_day} "
        f"(Rs. {best_revenue:.0f})"
    )

    # Chart
    plt.figure(figsize=(8, 5))
    daily.plot(kind="bar")
    plt.title("Daily Hotel Revenue")
    plt.xlabel("Date")
    plt.ylabel("Revenue (Rs.)")
    plt.tight_layout()
    plt.show()


def revenue_by_room_type(df):
    """Display revenue by room type."""

    if df is None or df.empty:
        print("No valid data available.")
        return

    room_revenue = df.groupby("RoomType")["Revenue"].sum()
    total = room_revenue.sum()

    print("\n--- Revenue by Room Type ---")

    for room_type, revenue in room_revenue.items():
        percentage = (revenue / total) * 100
        print(
            f"{room_type} : Rs. {revenue:.0f} "
            f"({percentage:.2f}%)"
        )

    print(f"Total revenue: Rs. {total:.0f}")

    # Chart
    plt.figure(figsize=(7, 5))
    room_revenue.plot(kind="bar")
    plt.title("Revenue by Room Type")
    plt.xlabel("Room Type")
    plt.ylabel("Revenue (Rs.)")
    plt.tight_layout()
    plt.show()


def show_all_data(df):
    """Display complete valid data."""

    if df is None or df.empty:
        print("No valid data available.")
        return

    print("\n--- Valid Hotel Sales Data ---")
    print(df.to_string(index=False))


def main():
    print("=" * 45)
    print("       HOTEL REVENUE ANALYZER")
    print("=" * 45)

    df = load_data()

    if df is None:
        return

    while True:
        print("\n========== MENU ==========")
        print("1. Daily revenue")
        print("2. Revenue by room type")
        print("3. Show valid records")
        print("4. Exit")
        print("==========================")

        choice = input("Enter your choice: ")

        if choice == "1":
            daily_revenue(df)

        elif choice == "2":
            revenue_by_room_type(df)

        elif choice == "3":
            show_all_data(df)

        elif choice == "4":
            print("\nThank you for using Hotel Revenue Analyzer.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()