import openpyxl

def extract_urls_from_excel(file_path, sheet_name, column_index):
    try:
        urls = []
        # Load the Excel workbook
        workbook = openpyxl.load_workbook(file_path)
        # Access the specified sheet
        sheet = workbook[sheet_name]
        # Iterate over rows in the specified column
        for row in sheet.iter_rows(min_row=2, min_col=column_index, max_col=column_index, values_only=True):
            # Add non-empty URLs to the list
            if row[0] is not None:
                urls.append(row[0])
        return urls
    except Exception as e:
        print("Error:", e)
        return []

# Example usage:
file_path = "Assignment/Input.xlsx"
sheet_name = "Sheet1"
column_index = 1  # Assuming URLs are in the first column (A)
url_id = extract_urls_from_excel(file_path, sheet_name, column_index)
print("Extracted URLs:")
for id in url_id:
    print(id)

column_index = 2
urls = extract_urls_from_excel(file_path,sheet_name,column_index)
print('Extracted URLs:')
for url in urls:
    print(url)
