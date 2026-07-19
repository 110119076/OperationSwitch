import json
import pandas as pd
import os
from tkinter import Tk, filedialog

# Hide the root tkinter window
root = Tk()
root.withdraw()

print("Select en.json file")
en_json_path = filedialog.askopenfilename(
    title="Select en.json",
    filetypes=[("JSON Files", "*.json")]
)

if not en_json_path:
    print("No en.json selected.")
    exit()

print("Select existing language file")
language_file_path = filedialog.askopenfilename(
    title="Select Language File",
    filetypes=[
        ("CSV Files", "*.csv"),
        ("Excel Files", "*.xlsx")
    ]
)

if not language_file_path:
    print("No language file selected.")
    exit()

# Read en.json
with open(en_json_path, "r", encoding="utf-8") as f:
    en = json.load(f)

# Read existing language file
df = pd.read_csv(language_file_path)

if "key" not in df.columns:
    raise ValueError("The selected language file must contain a 'key' column.")

# Only consider rows that belong to the IB channel
if "channel" in df.columns:
    df = df[df["channel"].astype(str).str.strip().eq("IB")].copy()

existing_rows_by_key = {}
for _, row in df.iterrows():
    key = row.get("key")
    if pd.notna(key):
        existing_rows_by_key[str(key)] = row.to_dict()

upserted_rows = []

for key, value in en.items():
    existing_row = existing_rows_by_key.get(key)
    value = value.replace("\n", " ").strip() if isinstance(value, str) else value
    if existing_row is None:
        upserted_rows.append({
            "id": "",
            "key": key,
            "English": value,
            "Hindi": value,
            "Tamil": value,
            "Gujarati": value,
            "Bengali": value,
            "Telugu": value,
            "Marathi": value,
            "Malayalam": value,
            "Kannada": value,
            "Channel": "IB",
            "Status": 1
        })
    else:
        current_english = existing_row.get("English", "")
        if str(current_english) != str(value):
            updated_row = existing_row.copy()
            updated_row["English"] = value
            upserted_rows.append(updated_row)

output_csv = "updated_language_file.csv"
result = pd.DataFrame(upserted_rows)
result.to_csv(output_csv, index=False, encoding="utf-8-sig")

print(f"Saved file: {output_csv}")

os.startfile(output_csv)