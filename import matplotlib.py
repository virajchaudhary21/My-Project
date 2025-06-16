import matplotlib.pyplot as plt

# Sample data
countries = ['India', 'China', 'USA', 'Indonesia', 'Pakistan', 'Brazil', 'Nigeria', 'Bangladesh', 'Russia', 'Mexico']
populations = [1380, 1440, 331, 273, 221, 213, 206, 166, 146, 128]

# Plotting the bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(countries, populations, color='skyblue')
plt.title('Total Population by Country (2020)', fontsize=16)
plt.xlabel('Country', fontsize=12)
plt.ylabel('Population (in millions)', fontsize=12)
plt.xticks(rotation=45)

# Adding population labels on top of each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval + 10, f'{yval}', ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()
