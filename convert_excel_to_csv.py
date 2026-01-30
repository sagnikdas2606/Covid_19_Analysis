import pandas as pd

# Load all sheets
sheets = pd.read_excel("C:/Users/SAGNIK/Downloads/Covid_19_Analysis/Covid_19_Analysis/data/raw/covid_19_dataset-1718175635.xlsx", sheet_name=None)

# Merge all sheets into one dataframe
merged_df = pd.concat(sheets.values(), ignore_index=True)

# Save as CSV
merged_df.to_csv("C:/Users/SAGNIK/Downloads/Covid_19_Analysis/Covid_19_Analysis/data/processed/merged_data.csv", index=False)

print("CSV created successfully!")