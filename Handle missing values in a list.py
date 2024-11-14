data = [1, 2, None, 4, None, 6]
# Replace None with a default value(0)
cleaned_data = [x if x is not None else 0 for x in data]
print("Cleaned data:", cleaned_data)
