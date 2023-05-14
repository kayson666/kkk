# Import pandas
import pandas as pd

# Load the data
zhengzhuang1 = pd.read_excel('症状标准化术语表1.xlsx')
zhengzhuang2 = pd.read_excel('症状标准化术语表2.xlsx')

# Extract the required columns from the dataframes
zhengzhuang1_extracted = zhengzhuang1[['症状', '同义词']]
zhengzhuang2_extracted = zhengzhuang2[['症状', '同义词']]

# Replace NaN values with empty strings
zhengzhuang1_extracted = zhengzhuang1_extracted.fillna('')
zhengzhuang2_extracted = zhengzhuang2_extracted.fillna('')

# Create dictionaries from the dataframes
dict1 = dict(zip(zhengzhuang1_extracted.症状, zhengzhuang1_extracted.同义词.str.split('，|、|,')))
dict2 = dict(zip(zhengzhuang2_extracted.症状, zhengzhuang2_extracted.同义词.str.split('，|、|,')))

# Merge the dictionaries
merged_dict = {**dict1, **dict2}

# Remove duplicates from the lists in the dictionary
for key, value in merged_dict.items():
    merged_dict[key] = list(set(value))

# Convert the dictionary back into a DataFrame
merged_df = pd.DataFrame(list(merged_dict.items()), columns=['症状', '同义词'])

# Convert the lists in the '同义词' column back into strings
merged_df['同义词'] = merged_df['同义词'].apply(lambda x: '，'.join(x))

# Merge the new dataframe with the original zhengzhuang2 dataframe
zhengzhuang2_final = pd.merge(zhengzhuang2.drop('同义词', axis=1), merged_df, on='症状', how='left')

# Save the DataFrame as an Excel file
zhengzhuang2_final.to_excel('症状标准化术语表.xlsx', index=False)