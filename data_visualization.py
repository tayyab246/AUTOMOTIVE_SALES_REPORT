import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker

# Load the cleaned dataset
df = pd.read_csv('cleaned_car_sales.csv')

# Professional Styling Setup
sns.set_theme(style="whitegrid", rc={"axes.spines.top": False, "axes.spines.right": False})
colors = sns.color_palette("mako", 10)

# ==========================================
# 1. Top Selling Models (Bar Chart)
# ==========================================
plt.figure(figsize=(12, 6))

# Extract the top 10 selling models
top_models = df.nlargest(10, 'Sales')

ax1 = sns.barplot(data=top_models, x='Model', y='Sales', palette="crest")
plt.title('Top Selling Models by Volume', fontsize=16, pad=15, fontweight='bold')
plt.xlabel('Vehicle Model', fontsize=12, fontweight='bold')
plt.ylabel('Total Sales', fontsize=12, fontweight='bold')
plt.xticks(rotation=45, ha='right')

# Format y-axis to show "K" for thousands
ax1.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{int(x/1000)}K'))

# Add data labels on top of bars
for p in ax1.patches:
    ax1.annotate(f'{int(p.get_height()/1000)}K', 
                 (p.get_x() + p.get_width() / 2., p.get_height()), 
                 ha = 'center', va = 'center', 
                 xytext = (0, 9), 
                 textcoords = 'offset points',
                 fontsize=10, color='black')

plt.tight_layout()
plt.savefig('top_selling_models.png', dpi=300)
plt.show()

# ==========================================
# 2. Price vs. Resale Value (Scatter plot with Trendline)
# ==========================================
plt.figure(figsize=(10, 6))

# Drop NaNs for accurate regression
df_resale = df.dropna(subset=['Price', 'Resale_Value'])

ax2 = sns.regplot(data=df_resale, x='Price', y='Resale_Value', 
                  scatter_kws={'alpha':0.6, 'color': '#20B2AA'}, 
                  line_kws={'color': '#2F4F4F', 'linestyle': '--'})

plt.title('Price vs. Resale Value Analysis', fontsize=16, pad=15, fontweight='bold')
plt.xlabel('Original Vehicle Price ($)', fontsize=12, fontweight='bold')
plt.ylabel('Resale Value ($)', fontsize=12, fontweight='bold')

# Format axes with dollar signs and comma separators
ax2.xaxis.set_major_formatter(ticker.StrMethodFormatter('${x:,.0f}'))
ax2.yaxis.set_major_formatter(ticker.StrMethodFormatter('${x:,.0f}'))

plt.tight_layout()
plt.savefig('price_vs_resale.png', dpi=300)
plt.show()

# ==========================================
# 3. Engine Size vs. Horsepower 
# ==========================================
plt.figure(figsize=(10, 6))

ax3 = sns.scatterplot(data=df, x='Engine_size', y='Horsepower', 
                      s=70, alpha=0.7, color='#3CB371', edgecolor='black')

plt.title('Vehicle Performance: Engine Size vs. Horsepower', fontsize=16, pad=15, fontweight='bold')
plt.xlabel('Engine Size (Liters)', fontsize=12, fontweight='bold')
plt.ylabel('Horsepower', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig('engine_vs_horsepower.png', dpi=300)
plt.show()

# ==========================================
# 4. Top 10 Manufacturers by Resale Value
# ==========================================
plt.figure(figsize=(10, 6))

# Group by manufacturer and calculate average resale value
resale_by_mfg = df.groupby('Manufacturer')['Resale_Value'].mean().sort_values(ascending=False).head(10)

ax4 = sns.barplot(y=resale_by_mfg.index, x=resale_by_mfg.values, palette="viridis")
plt.title('Top 10 Manufacturers by Average Resale Value', fontsize=16, pad=15, fontweight='bold')
plt.xlabel('Average Resale Value ($)', fontsize=12, fontweight='bold')
plt.ylabel('Manufacturer', fontsize=12, fontweight='bold')

# Format x-axis with dollar signs
ax4.xaxis.set_major_formatter(ticker.StrMethodFormatter('${x:,.0f}'))

plt.tight_layout()
plt.savefig('top_mfg_resale_value.png', dpi=300)
plt.show()