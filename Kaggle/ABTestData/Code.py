import pandas as pd
from scipy.stats import ttest_ind


file_path = '/Users/youngseokkim/Desktop/AB Test/kaggle/AB_Test_Results.csv'
ab_test_data = pd.read_csv(file_path)

ab_test_data_info = ab_test_data.info()
ab_test_data_head = ab_test_data.head()

print("Data Information:")
ab_test_data.info()

#print("\nFirst Few Rows:")
#print(ab_test_data.head())

# Basic descriptive statistics for each group
descriptive_stats = ab_test_data.groupby('VARIANT_NAME')['REVENUE'].describe()
print("\nDescriptive statistics:")
print(descriptive_stats)

# Separate the data into control and variant groups
control_revenue = ab_test_data[ab_test_data['VARIANT_NAME'] == 'control']['REVENUE']
variant_revenue = ab_test_data[ab_test_data['VARIANT_NAME'] == 'variant']['REVENUE']

# Perform a t-test
t_stat, p_value = ttest_ind(control_revenue, variant_revenue, equal_var=False)

print("\nt-statistic:", t_stat)
print("p-value:", p_value)