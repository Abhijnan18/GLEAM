from gleam import Gleam, Panel
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')  # Use TkAgg backend

# Sample data
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [23, 45, 56, 78]
}

df = pd.DataFrame(data)

# Create a plot using matplotlib
plt.figure(figsize=(10, 6))
plt.bar(df['Category'], df['Values'])
plt.xlabel('Category')
plt.ylabel('Values')
plt.title('Sample Bar Chart')

# Save the plot
plt.savefig('bar_chart.png')

# Create a Gleam app
app = Gleam()

# Add the plot to the app
app.add_panel(Panel.from_file('bar_chart.png'))

# Run the app
app.run()
