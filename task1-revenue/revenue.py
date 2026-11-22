"""
1. Calculate the total revenue.
2. Convert revenue IDs into human-readable names.
3. Display revenue values in a bar chart."""


import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

data = {
'cash': 942.498,
'todayCash': 9053.299,
'Rev00016': 348.8300000005,
'Rev00013': 31.99993,
'Rev00015': 92.36,
'Rev00017': 287.34,
'Rev00020': 296.1,
'Rev00018': 47.54,
'Rev00045': 77.00,
}
revTypes = {
'Rev00016': {'name': 'Petty cash', 'connectedTo': 'Physical'},
'Rev00013': {'name': 'Debit card', 'connectedTo': 'HDFC'},
'Rev00015': {'name': 'PhonePe', 'connectedTo': 'ICICI'},
'Rev00017': {'name': 'Google pay', 'connectedTo': 'SBI'},
'Rev00020': {'name': 'UPI', 'connectedTo': 'ICICI'},
'Rev00018': {'name': 'Credit card', 'connectedTo': 'SBI'},
}

# Function to get revenue name
def get_rev_name(revId) -> str:
    return revTypes.get(revId, {}).get('name', 'Unknown')


# Calculate total and collect revenue details
total_revenue = 0
revenue_names = []
revenue_values = []
revenue_mapping = {}

for key, value in data.items():
    if key.startswith('Rev'):
        total_revenue += value

        name = get_rev_name(key)
        revenue_mapping[key] = name

        revenue_names.append(name)
        revenue_values.append(value)

# Print total and mapping
print(f"Total Revenue: {total_revenue:.3f}")
print(revenue_mapping)

# Plot bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(revenue_names, revenue_values)

plt.title('Revenue Analysis')
plt.xlabel('Revenue Names')
plt.ylabel('Revenue Values')

# Format y-axis
plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.3f'))

# Display values on bars
for bar in bars:
    height = bar.get_height()
    plt.annotate(
        f'{height:.3f}',
        (bar.get_x() + bar.get_width() / 2, height),
        ha='center',
        va='bottom'
    )

plt.tight_layout()
plt.show()
