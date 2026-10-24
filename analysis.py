import pandas as pd

# 1. Create the IT Salaries dataset
data = {
    'Job_Title': ['Data Analyst', 'Software Engineer', 'Data Scientist', 'Data Analyst', 'Software Engineer', 'DevOps Engineer', 'Data Scientist', 'Data Analyst'],
    'Experience_Years': [1, 3, 4, 2, 5, 6, 2, 3],
    'Salary_USD': [45000, 75000, 90000, 48000, 85000, 95000, 88000, 47000],
    'Remote': ['Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No']
}
df = pd.DataFrame(data)

print("--- Original Dataset ---")
display(df.head())

# 2. Data Cleaning
df = df.drop_duplicates()
df['Salary_USD'] = df['Salary_USD'].fillna(df['Salary_USD'].mean())

# 3. Create a clean, perfectly aligned column summary table instead of df.info()
info_df = pd.DataFrame({
    'Column_Name': df.columns,
    'Non_Null_Count': df.notnull().sum().values,
    'Null_Count': df.isnull().sum().values,
    'Data_Type': df.dtypes.values
})
print("\n--- Clean Column Summary Table ---")
display(info_df)

# 4. Exploratory Data Analysis: Average Salary by Job Title (Rounded to Nearest Dollar)
avg_salary_by_job = df.groupby('Job_Title')['Salary_USD'].mean().round(0).astype(int).reset_index()
print("\n--- Average Salary by Job Title ---")
display(avg_salary_by_job)