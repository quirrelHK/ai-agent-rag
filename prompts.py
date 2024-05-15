from llama_index.core import PromptTemplate
# instruction_str = (
#     "1. Convert the query to executable Python code using Pandas.\n"
#     "2. The final line of code should be a Python expression that can be called with the `eval()` function.\n"
#     "3. The code should represent a solution to the query.\n"
#     "4. PRINT ONLY THE EXPRESSION.\n"
#     "5. Do not quote the expression.\n"
# )

# pandas_prompt_str = (
#     "You are working with a pandas dataframe in Python.\n"
#     "The name of the dataframe is `df`.\n"
#     "This is the result of `print(df.head())`:\n"
#     "{df_str}\n\n"
#     "Follow these instructions:\n"
#     "{instruction_str}\n"
#     "Query: {query_str}\n\n"
#     "Expression:"
# )
# response_synthesis_prompt_str = (
#     "Given an input question, synthesize a response from the query results.\n"
#     "Query: {query_str}\n\n"
#     "Pandas Instructions (optional):\n{pandas_instructions}\n\n"
#     "Pandas Output: {pandas_output}\n\n"
#     "Response: "
# )




instruction_str = """\
    1. Convert the query to executable Python code using Pandas.
    2. The final line of code should be a Python expression that can be called with the `eval()` function.
    3. The code should represent a solution to the query.
    4. PRINT ONLY THE EXPRESSION.
    5. Do not quote the expression."""

new_prompt = PromptTemplate(
    """\
    You are working with a pandas dataframe in Python.
    The name of the dataframe is `df`.
    This is the result of `print(df.head())`:
    {df_str}

    Follow these instructions:
    {instruction_str}
    Query: {query_str}

    Expression: """
)

context = """Purpose: The primary role of this agent is to assist users by providing accurate 
            information about world population statistics and details about a country. """