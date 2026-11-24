from fastmcp import FastMCP
import random
import json

# Create the FastMCP server instance
mcp = FastMCP("Simple Calculate Server")

# Tool : Add two numbers
@mcp.tool
def add(a:int, b:int) -> int:
  """ Add two numbers together.
  
  Args:
     a: First number
     b: Second number
  Returns:
     The sum of a and b
  """

  return a+b


# Tool : Generate a random number 
@mcp.tool
def random_number(min_val: int = 1, max_val: int=100) -> int:
  """Generate a random number within a range.
  
  Args:

     min_val: Minimum value (default: 1)
  """
