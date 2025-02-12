import pandas as pd  

df = pd.read_csv("students.csv") 

for column_name in df.columns:
    column_df = df[[column_name]]
    
    print(f"{column_name}:")
    
    for value in column_df[column_name]:
        print(value)
    
    print("\n" + "-"*30 + "\n")
    
    column_df.to_csv(f"{column_name}.csv", index=False)

print("CSV files created successfully!")
