# %%
import pandas as pd

df = pd.read_csv("finbox_supported_metrics.csv")

# %%
def create_function_string(row):
    function_name = row["Metric Slug"]
    function_desc_short = row["Name"]
    function_desc_long = (
        row["Description"] if isinstance(row["Description"], str) else None
    )
    function_periods = row["Periods"] if isinstance(row["Periods"], str) else None
    if function_periods:
        function_default_period = row["Default Period"]
    file_name = row["Category"].lower().replace(" ", "_") + "_metrics.py"
    function_string = (
        f"def {function_name}("
        + (f"period: str = '{function_default_period}'" if function_periods else "")
        + f'):\n    """{function_desc_short}'
        + (f"\n\n    {function_desc_long}" if function_desc_long else "")
        + (
            f"\n\n    Args:\n        period: str, default='{function_default_period}'\n            {function_periods}"
            if function_periods
            else ""
        )
        + f"""\n    \"\"\"\n    pass\n\n"""
    )
    # return function_string
    with open(file_name, "a") as f:
        f.write(function_string)


# %%
df.apply(create_function_string, axis=1)
