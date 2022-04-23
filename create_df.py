# import pandas libraries
import pandas as pd

# create a list and dataframe 
column = ["Mariya", "Batman", "Spongebob"]
titled_columns = {"name": column,
                 "height": [1.67, 1.9, 0.25],
                 "weight": [54, 100, 1]}
data = pd.DataFrame(titled_columns)

# select the values from dataframe
select_column = data["weight"][1]
select_row = data.iloc[1]["weight"]

# calculate bmi of a person
bmi = []

# bmi calculation = weight/(height**2)
for i in range(len(data)):
    bmi_score = data["weight"][i]/(data["height"][i]**2)
    bmi.append(bmi_score)

# insert bmi calculated data into a new column
data["bmi"] = bmi

# save data to a csv file
data.to_csv("bmi.csv", index=False, sep="\t")

# print the data
print(data)



