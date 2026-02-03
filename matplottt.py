import matplotlib.pyplot as plt
import numpy as np
from sqlalchemy import values  
import pandas as pd

# plotting a line graph using matplotlib.....

# print(plt.__version__)

# x = np.array([2023, 2024, 2025, 2026])
# y  = np.array([10, 15, 13, 17])
# y1  = np.array([17, 25, 73, 67])
# y2 = np.array([19, 25, 33, 37])

# line_style = dict(marker='.', markersize=10, markeredgecolor='red', markerfacecolor='blue', linestyle='dashed', linewidth=2, alpha=0.5)
# plt.plot(x,y)
# plt.plot(y)
# plt.plot(x,y, color = 'red', **line_style)
# plt.plot(x,y1, color = 'purple', **line_style)
# plt.plot(x,y2, color = 'orange', **line_style)

# plt.title("Aditya's Line Graph", fontsize=20, fontfamily='serif', color='blue')

# plt.xlabel('Year', fontsize=14, fontfamily='serif', color='green')
# plt.ylabel('Value', fontsize=14, fontfamily='serif', color='green')

# x = np.array([2023, 2024, 2025, 2026])
# y  = np.array([10, 15, 13, 17])
# y1  = np.array([17, 25, 73, 67])
# y2 = np.array([19, 25, 33, 37])

# plt.tick_params(axis="both", direction="in", length=10, width=2, colors='red', grid_color='blue', grid_alpha=0.5)

# plt.plot(x,y, label = 'Line 1')
# plt.plot(x,y1, label = 'Line 2')
# plt.plot(x,y2, label = 'Line 3')    


# plt.xticks(x)

# plt.show()

# grid lines in matplotlib.....

# x = [1, 2, 3, 4, 5]
# y = [5, 10, 15, 20, 25]

# plt.grid(axis="both", linewidth = 2, color = 'lightgray', linestyle = "dashed") # Add grid lines to the plot

# plt.plot(x,y)

# plt.show()

# barchart in matplotlib.....

# categories = ['Grains', 'Fruit', 'Vegetables', 'Protein', 'Dairy', 'Sweets']
# values = np.array([4, 3, 2, 5, 3, 1])

# plt.bar(categories, values, color = 'skyblue')
# plt.barh(categories, values, color = 'skyblue')

# plt.title("Aditya's Bar Chart", fontsize=20, fontfamily='serif', color='blue')

# plt.xlabel('Food Categories', fontsize=14, fontfamily='calibri', color='green')
# plt.ylabel('Quantity', fontsize=14, fontfamily='calibri', color='green')
# plt.show()

# Pie chart in matplotlib.....

# categories = ['Freshmen', 'Sophomore', 'Junior', 'Senior']
# values = np.array([100, 150, 120, 80])
# colors = ['lightcoral', 'lightskyblue', 'lightgreen', 'gold']
# plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=140, colors=colors, explode=(0.1, 0, 0, 0), shadow=True)

# plt.show()

# Scatter plot in matplotlib.....

# x1 = np.array([0, 1, 1, 2, 3, 4, 5, 6, 7, 7, 8]) # hours studied
# y1 = np.array([55, 60, 65, 70, 75, 80, 85, 90, 92, 95, 100]) # exam scores

# x2 = np.array([0, 1, 1, 2, 3, 4, 5, 6, 7, 7, 8]) # hours studied
# y2 = np.array([50, 55, 60, 65, 70, 75, 80, 85, 90, 92, 95]) # exam scores
# plt.scatter(x1, y1, color =  'skyblue', marker='o', s=100, edgecolor='black', alpha=0.7)
# plt.scatter(x2, y2, color =  'lightcoral', marker='s', s=100, edgecolor='black', alpha=0.7)
# plt.xlabel('Hours Studied')
# plt.ylabel('Exam Scores')
# plt.title('Scatter Plot of Hours Studied vs Exam Scores')

# plt.legend(['Group 1', 'Group 2'])
# plt.show()

# Histogram in matplotlib.....

# scores = np.random.normal(loc= 80, scale= 10, size= 1000)
# scores = np.clip(scores, 0, 100)
# plt.hist(scores, bins=30, color='skyblue', edgecolor='black')
# plt.xlabel('Scores')
# plt.ylabel('Frequency')
# plt.title('Distribution of Scores')
# plt.show()

# Subplots in matplotlib.....

# x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# figure, axes = plt.subplots(2, 2)

# axes[0, 0].bar(x, x*2, color='red')
# axes[0, 1].plot(x, x**3, color='blue')
# axes[1, 0].plot(x, x**4, color='green')
# axes[1, 1].plot(x, x**5, color='orange')

# axes[0, 0].set_title('Plot 1')
# axes[0, 1].set_title('Plot 2')
# axes[1, 0].set_title('Plot 3')
# axes[1, 1].set_title('Plot 4')
    
# plt.show()
 
 
# Pandas with matplotlib.....
 
# df = pd.read_csv("pokemon1.csv")
# print(df["Type 1"].value_counts(ascending=True))

# type_counts = df["Type 1"].value_counts()
# plt.bar(type_counts.index, type_counts.values, color='skyblue', edgecolor='black')
# plt.title("Number of Pokemon by Type", fontsize=20, fontfamily='serif', color='blue')
# plt.xlabel('Pokemon Type', fontsize=14, fontfamily='calibri', color='green')
# plt.ylabel('Count', fontsize=14, fontfamily='calibri', color='green')   
# plt.tight_layout()

# plt.show()