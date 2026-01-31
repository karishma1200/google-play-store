
import pandas as pd
import re

# Load the extracted text file
def load_extracted_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

# Parse the extracted text into a DataFrame
def parse_text_to_dataframe(text):
    columns = ['App', 'Category', 'Rating', 'Reviews', 'Size', 'Installs', 'Type', 'Price', 'Content Rating', 'Genres', 'Last Updated', 'Current Ver', 'Android Ver']
    data = []
    buffer = ""
    for line in text.splitlines():
        # Skip empty lines and lines that are not part of the table
        if not line.strip():
            continue
        buffer += " " + line.strip()
        # Try to split the buffer into fields
        fields = re.split(r'\s{2,}|\t', buffer.strip())
        if len(fields) >= 13:
            data.append(fields[:13])
            buffer = ""  # Reset buffer for next row
    df = pd.DataFrame(data, columns=columns)
    # Data cleaning steps
    if not df.empty:
        df = df.dropna(subset=['App', 'Category'])
        df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
        df['Reviews'] = pd.to_numeric(df['Reviews'], errors='coerce')
        df['Installs'] = df['Installs'].str.replace(',', '', regex=False).str.replace('+', '', regex=False)
        df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')
        df['Price'] = df['Price'].str.replace('$', '', regex=False)
        df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
        df = df.drop_duplicates()
        if 'Rating' in df.columns:
            df['Rating'].fillna(df['Rating'].mean(), inplace=True)
    return df

if __name__ == "__main__":
    text = load_extracted_text("extracted_text.txt")
    df = parse_text_to_dataframe(text)
    if not df.empty:
        df.to_csv("apps_data.csv", index=False)
        print("Parsed data saved to apps_data.csv")
    else:
        print("No data parsed. Please check the extraction logic or the PDF structure.")
