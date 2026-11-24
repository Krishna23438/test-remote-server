
# from fastmcp import FastMCP
# import random
# import json

# # Create the FastMCP server instance
# mcp = FastMCP("Simple Calculate Server")


# # Tool: Add two numbers
# @mcp.tool
# def add(a: int, b: int) -> int:
#     """Add two numbers together.

#     Args:
#         a: First number
#         b: Second number

#     Returns:
#         The sum of a and b
#     """
#     return a + b


# # Tool: Generate a random number
# @mcp.tool
# def random_number(min_val: int = 1, max_val: int = 100) -> int:
#     """Generate a random number within a range.

#     Args:
#         min_val: Minimum value (default: 1)
#         max_val: Maximum value (default: 100)

#     Returns:
#         A random integer between min_val and max_val
#     """
#     if min_val > max_val:
#         raise ValueError("min_val cannot be greater than max_val")

#     return random.randint(min_val, max_val)


# # Resource: Server information
# @mcp.resource("info://server")
# def server_info() -> str:
#     """Get information about this server"""

#     info = {
#         "name": "Simple Calculator Server",
#         "version": "1.0.0",
#         "description": "A basic MCP server with math tools",
#         "tools": ["add", "random_number"],
#         "author": "Your Name"
#     }

#     return json.dumps(info, indent=2)

from fastmcp import FastMCP
import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(__file__),"expenses.db")

CATEGORIES_PATH = os.path.join(os.path.dirname(__file__),"categories.json")

mcp = FastMCP("ExpenseTracker")

def init_db():
  with sqlite3.connect(DB_PATH) as c:
    c.execute("""
        CREATE TABLE IF NOT EXISTS expenses(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          data TEXT NOT NULL,
          amount REAL NOT NULL,
          category TEXT NOT NULL,
          subcategory TEXT DEFAULT '',
          note TEXT DEFAULT ''
        )
    """)

init_db()

@mcp.tool
def add_expenses(date, amount, category , subcategory="",note=""):
  '''Add a new expense entry to the database.'''
  with sqlite3.connect(DB_PATH) as c:
    cur = c.execute(
      "INSERT INFO expenses(data, amount, category, subcategory, note) VALUES (?,?,?,?,?)",
      (date,amount,category,subcategory,note) 
    )
    return {"status":"ok","id":cur.lastrowid}

@mcp.tool
def list_expenses(start_date,end_date):
  '''List all the expense entry within an inclusive date range.'''
  with sqlite3.connect(DB_PATH) as c:
    cur = c.execute("""SELECT id, date, amount, category, subcategory, note FROM expenses 
    WHERE date BETWEEN ? AND ?
    ORDER BY id ASC

    """,
    (start_date,end_date))
    cols = [d[0] for d in cur.description]
    return [dict(zip(cols,r)) for r in cur.fetchall()]


  @mcp.tool
  def summarize(start_date,end_date, category=None):
    """Summarize expenses by category within an inclusive date range."""
    with sqlite3.connect(DB_PATH) as c:
      query = (
        """
          SELECT category, SUM(amount) AS total_amount
          From expenses
          WHERE date BETWEEN ? AND ?

        """
      )
      params = [start_date,end_date]

      if category:
        query += " AND category = ?"
        params.append(category)

      query += " GROUP BY category ORDER BY category ASC"

      cur = c.execute(query, params)
      cols = [d[0] for d in cur.description]
      return [dict(zip(cols ,r )) for r in cur.fetchall()]

@mcp.resource("expense:///categories", mime_type="application/json")  # Changed: expense:// → expense:///
def categories():
    try:
        # Provide default categories if file doesn't exist
        default_categories = {
            "categories": [
                "Food & Dining",
                "Transportation",
                "Shopping",
                "Entertainment",
                "Bills & Utilities",
                "Healthcare",
                "Travel",
                "Education",
                "Business",
                "Other"
            ]
        }
        
        try:
            with open(CATEGORIES_PATH, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            import json
            return json.dumps(default_categories, indent=2)
    except Exception as e:
        return f'{{"error": "Could not load categories: {str(e)}"}}'




# Start the server
if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=8000
    )
