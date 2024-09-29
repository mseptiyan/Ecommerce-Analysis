import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
orders = pd.read_csv('data/orders_dataset.csv')
products = pd.read_csv('data/products_dataset.csv')
payments = pd.read_csv('data/order_payments_dataset.csv')
rfm_df = pd.read_csv('dashboard/main_data.csv')  # RFM analysis result

# Title of the dashboard
st.title("E-Commerce Data Analysis Dashboard")

# Section 1: RFM Analysis
st.header("RFM Analysis")

# Show RFM data
st.write(rfm_df)

# Visualize RFM
fig, ax = plt.subplots()
sns.histplot(rfm_df['monetary'], bins=30, kde=True, ax=ax)
ax.set_title("Distribution of Monetary Values")
ax.set_xlabel("Monetary")
ax.set_ylabel("Frequency")
st.pyplot(fig)

# Section 2: Product Categories
st.header("Product Categories")

# Count of products by category
category_counts = products['product_category_name'].value_counts().reset_index()
category_counts.columns = ['Category', 'Count']

# Bar chart
fig, ax = plt.subplots()
sns.barplot(x='Count', y='Category', data=category_counts.head(10), ax=ax)
ax.set_title("Top 10 Product Categories")
ax.set_xlabel("Count")
ax.set_ylabel("Category")
st.pyplot(fig)

# Section 3: Payment Methods
st.header("Payment Methods")

# Count of payment methods
payment_counts = payments['payment_type'].value_counts().reset_index()
payment_counts.columns = ['Payment Method', 'Count']

# Horizontal bar chart
fig, ax = plt.subplots(figsize=(10, 6))  # Ukuran figure lebih besar
ax.barh(payment_counts['Payment Method'], payment_counts['Count'], color='skyblue')

# Menambahkan label dan judul
ax.set_xlabel('Count')
ax.set_ylabel('Payment Method')
ax.set_title('Payment Method Distribution')

# Tampilkan diagram batang
st.pyplot(fig)


# Conclusion section
st.header("Conclusions")
st.write("""
- Kategori produk dengan total pembelian tertinggi adalah Cama Mesa Banho.
- Tren pembayaran yang paling sering digunakan oleh pelanggan adalah Credit Card.
""")