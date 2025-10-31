import plotly.express as px
import pandas as pd

# Load local CSV
df = pd.read_csv('ventes.csv')

# GRAPH 1: Sales by region
fig1 = px.pie(df, values='qte', names='region', title='Units sold by region')
fig1.write_html('ventes-par-region.html')
print('ventes-par-region.html created!')

# GRAPH 2: Sales by product
sales_by_product = df.groupby('produit')['qte'].sum().reset_index()
fig2 = px.bar(sales_by_product, x='produit', y='qte', title='Sales by product')
fig2.write_html('ventes-par-produit.html')
print('ventes-par-produit.html created!')

# GRAPH 3: Revenue by product
df['revenue'] = df['prix'] * df['qte']  # Use 'prix'
revenue_by_product = df.groupby('produit')['revenue'].sum().reset_index()
fig3 = px.bar(revenue_by_product, x='produit', y='revenue', title='Revenue by product')
fig3.write_html('ca-par-produit.html')
print('ca-par-produit.html created!')