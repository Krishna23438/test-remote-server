Steps to made a remote server 

Install uv
Create new folder 
Open the folder in vs code
Uv init
Uv add fastmcp 
Create a simple server
Run the server uv run main.py
Test the server using mcp inspector 
Create a Github repo 
Git init
git add
git commit -m "Initial commit:Simple MCP server"
Git remote add origin

Git push -u origin main
Create an account on FastMCP cloud 
Deploy on FastMCP 


https://krishnagupta.fastmcp.app/mcp

💰 Expense Tracker MCP Server

An Expense Tracker MCP Server built using FastMCP that enables AI assistants to interact with expense data through the Model Context Protocol (MCP).

The server provides tools to add expenses, retrieve expense records within a specified date range, and generate category-wise expense summaries. It uses an SQLite database for persistent data storage and asynchronous database operations with aiosqlite.

🚀 Features

Add Expenses: Store expense records with date, amount, category, subcategory, and notes.

List Expenses: Retrieve expenses within an inclusive date range.

Expense Summarization: Calculate total spending and transaction counts grouped by category.

Category Resource: Expose predefined expense categories through an MCP resource in JSON format.

SQLite Database: Store expense records in a lightweight SQLite database.

Asynchronous Operations: Use aiosqlite for asynchronous database queries.

HTTP Transport: Run the MCP server using HTTP transport, making it suitable for local or remote MCP client connections.

Error Handling: Handle database errors and return meaningful error messages.

🛠️ Tech Stack

Technology

Purpose

Python

Core programming language

FastMCP

MCP server development

Model Context Protocol (MCP)

Communication between AI clients and tools

SQLite

Expense data storage

aiosqlite

Asynchronous database operations

JSON

Category resource format

HTTP

Server communication transport

📂 Project Structure

expense-tracker-mcp-server/
│
├── main.py              # FastMCP server and MCP tools
├── categories.json      # Optional custom expense categories
├── expenses.db          # SQLite database (created at runtime)
├── pyproject.toml       # Project dependencies and configuration
├── uv.lock              # Dependency lock file (if generated)
└── README.md            # Project documentation

⚙️ Installation and Setup

1. Clone the Repository

git clone YOUR_GITHUB_REPOSITORY_URL
cd expense-tracker-mcp-server

2. Create a Virtual Environment

uv venv

Activate it on Windows PowerShell:

.venv\Scripts\Activate.ps1

3. Install Dependencies

uv add fastmcp aiosqlite

4. Run the MCP Server

uv run python main.py

The server starts using HTTP transport on port 8000.

MCP endpoint:

http://localhost:8000/mcp

🔧 Available MCP Tools

The server currently exposes three MCP tools.

1. add_expense

Adds a new expense record to the SQLite database.

Parameters:

Parameter

Description

date

Date of the expense

amount

Expense amount

category

Expense category

subcategory

Optional subcategory

note

Optional expense description

Example input:

{
  "date": "2026-11-25",
  "amount": 500,
  "category": "Food & Dining",
  "subcategory": "Restaurant",
  "note": "Dinner"
}

2. list_expenses

Retrieves expense records between two dates, including both the start and end dates.

Parameters:

Parameter

Description

start_date

Starting date

end_date

Ending date

Example input:

{
  "start_date": "2026-11-01",
  "end_date": "2026-11-30"
}

3. summarize

Generates a category-wise expense summary for a specified date range.

Parameters:

Parameter

Description

start_date

Starting date

end_date

Ending date

category

Optional category filter

Example input:

{
  "start_date": "2026-11-01",
  "end_date": "2026-11-30",
  "category": "Food & Dining"
}

The tool returns the total amount spent and the number of transactions for each matching category.

📚 Available MCP Resource

expense:///categories

Provides expense categories in JSON format.

Default categories include:

Food & Dining

Transportation

Shopping

Entertainment

Bills & Utilities

Healthcare

Travel

Education

Business

Other

If categories.json exists, the server reads its contents. Otherwise, it returns the predefined default categories.

🌐 Transport Configuration

This project uses HTTP transport through FastMCP.

mcp.run(
    transport="http",
    host="0.0.0.0",
    port=8000
)

Transport: HTTP (Streamable HTTP)

Host: 0.0.0.0

Port: 8000

Endpoint: /mcp

Binding to 0.0.0.0 allows the server to listen on available network interfaces. Public internet access requires additional deployment and network configuration.

🧪 Testing with MCP Inspector

You can test the MCP server using the FastMCP development Inspector.

uv run fastmcp dev inspector main.py

For an HTTP connection test, start the server separately:

uv run python main.py

Then connect the Inspector to:

http://localhost:8000/mcp

Select the HTTP transport/connection option when configuring the Inspector.

🗄️ Database Schema

The project uses an SQLite table named expenses.

Column

Data Type

Description

id

INTEGER

Primary key

date

TEXT

Expense date

amount

REAL

Expense amount

category

TEXT

Expense category

subcategory

TEXT

Optional subcategory

note

TEXT

Optional expense note

The database is initialized automatically when the server module loads.

🔮 Future Improvements

AI-powered spending analysis and personalized financial insights.

Monthly and yearly expense reports.

Budget creation and tracking.

Spending alerts and budget notifications.

Integration with visualization dashboards.

Export expense reports to CSV and PDF.

Authentication and user-specific expense records.

🤝 Contributing

Contributions, suggestions, and improvements are welcome!

Fork the repository.

Create a new feature branch.

Commit your changes.

Push your branch.

Open a Pull Request.

📄 License

This project is open-source. Add a license file (such as MIT) if you want to distribute it under that license.

Developed using Python, FastMCP, SQLite, and the Model Context Protocol (MCP).