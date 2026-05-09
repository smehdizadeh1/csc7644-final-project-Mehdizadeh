import json
import os
import pandas as pd
import re


def ensure_output_dir(output_dir="outputs"):
    """Create outputs directory if it does not exist."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)


def clean_excel_string(value):
    """
    Remove illegal characters that Excel cannot handle.
    """

    if isinstance(value, str):
        value = re.sub(r'[\x00-\x1F\x7F]', '', value)
    return value


def save_jsonl(data, file):
    """
    Save data in JSONL format.
    """

    ensure_output_dir()
    file_path = os.path.join("outputs", file)

    with open(file_path, "w", encoding="utf-8") as f:
        for item in data:
            f.write(json.dumps(item) + "\n")

    print(f"\nSaved JSONL: {file_path}")


def save_excel(data, file):
    """
    Save data in Excel format with cleaning.
    """

    ensure_output_dir()
    file_path = os.path.join("outputs", file)

    # Clean data before writing
    cleaned_data = []
    for row in data:
        cleaned_row = {
            key: clean_excel_string(value)
            for key, value in row.items()
        }
        cleaned_data.append(cleaned_row)

    df = pd.DataFrame(cleaned_data)

    try:
        df.to_excel(file_path, index=False)
        print(f"Saved Excel: {file_path}")

    except PermissionError:
        print("Excel file is open. Please close it and try again.")