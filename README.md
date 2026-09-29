# Personal Finance Tracker

A small desktop application for tracking personal income and expenses.

The project demonstrates a simple CRUD-style workflow with a graphical interface, local data persistence, SQL queries, input validation, and basic financial summaries.

## Features

- Add income and expense transactions
- Choose a category for each transaction
- Store data locally in SQLite
- View transaction history
- Calculate total income, total expenses, and current balance
- Automatically create the database and default categories on first launch
- Validate transaction amounts before saving

## Tech Stack

- **Python 3**
- **Tkinter** — graphical user interface
- **SQLite** — local database
- **Python standard library** — no third-party dependencies

## Project Structure

```text
personal-finance-tracker/
├── main.py           # Tkinter application and UI
├── helper.py           # Tkinter application and UI
├── db/
│   └── .gitkeep     # Keeps the data directory in Git
    └── database.db 
├── .gitignore
└── requirements.txt
```

The actual SQLite database is generated automatically at `data/finance.db` when the application starts. It is intentionally excluded from Git so that personal financial data is not published.

## How to Run

Clone the repository and run:

```bash
python main.py
```

No external packages are required.

## Notes

This is a portfolio/educational project. The application is designed for local use and does not include authentication, cloud synchronization, encryption, or multi-user support.

## Possible Improvements

- Monthly and category-based analytics
- Charts for income and expenses
- Edit and delete transactions
- Export to CSV
- Custom categories
- Automated tests
- Packaging as a standalone desktop application
