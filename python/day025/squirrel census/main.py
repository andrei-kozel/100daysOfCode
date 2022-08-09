import pandas

data = pandas.read_csv("data.csv")
colors = data["Primary Fur Color"].dropna().to_list()

unique_colors = []

for color in colors:
    if color not in unique_colors:
        unique_colors.append(color)


output_data = {"Fur Color": [], "Count": []}

for color in unique_colors:
    output_data["Fur Color"].append(color)
    output_data["Count"].append(colors.count(color))

output_csv = pandas.DataFrame(output_data)
output_csv.to_csv("squirrel_count.csv")
