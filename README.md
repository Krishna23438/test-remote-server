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

# 💰 Expense Tracker MCP Server

An **Expense Tracker MCP Server** built using [FastMCP](https://github.com/jlowin/fastmcp) that enables AI assistants to interact with expense data through the **Model Context Protocol (MCP)**.

The server provides tools to add expenses, retrieve expense records within a specified date range, and generate category-wise expense summaries. It uses an SQLite database for persistent data storage and asynchronous database operations with `aiosqlite`.

## 🚀 Features

- **Add Expenses:** Store expense records with date, amount, category, subcategory, and notes.
- **List Expenses:** Retrieve expenses within an inclusive date range.
- **Expense Summarization:** Calculate total spending and transaction counts grouped by category.
- **Category Resource:** Expose predefined expense categories through an MCP resource in JSON format.
- **SQLite Database:** Store expense records in a lightweight SQLite database.
- **Asynchronous Operations:** Use `aiosqlite` for asynchronous database queries.
- **HTTP Transport:** Run the MCP server using HTTP transport, making it suitable for local or remote MCP client connections.
- **Error Handling:** Handle database errors and return meaningful error messages.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| FastMCP | MCP server development |
| Model Context Protocol (MCP) | Communication between AI clients and tools |
| SQLite | Expense data storage |
| aiosqlite | Asynchronous database operations |
| JSON | Category resource format |
| HTTP | Server communication transport |

## 📂 Project Structure

```text
expense-tracker-mcp-server/
│
├── main.py              # FastMCP server and MCP tools
├── categories.json      # Optional custom expense categories
├── expenses.db          # SQLite database (created at runtime)
├── pyproject.toml       # Project dependencies and configuration
├── uv.lock              # Dependency lock file (if generated)
└── README.md            # Project documentation
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd expense-tracker-mcp-server
```

### 2. Create a Virtual Environment

```bash
uv venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
uv add fastmcp aiosqlite
```

### 4. Run the MCP Server

```bash
uv run python main.py
```

The server starts using HTTP transport on port `8000`.

**MCP endpoint:**

```text
http://localhost:8000/mcp
```

## 🔧 Available MCP Tools

The server currently exposes three MCP tools.

### 1. `add_expense`

Adds a new expense record to the SQLite database.

**Parameters:**

| Parameter | Description |
|---|---|
| `date` | Date of the expense |
| `amount` | Expense amount |
| `category` | Expense category |
| `subcategory` | Optional subcategory |
| `note` | Optional expense description |

**Example