# app.py

import streamlit as st
import pandas as pd
import os
from recommender import ProductRecommender

# --- Setup ---
st.set_page_config(page_title="🛍️ E-Commerce Recommender", layout="wide")
st.title("🛍️ E-Commerce Product Recommender")

# --- Load Data ---
DATA_PATH = "products.csv"
IMAGE_FOLDER = "images"
df = pd.read_csv(DATA_PATH)
recommender = ProductRecommender(DATA_PATH)

# --- Product Selection ---
st.markdown("### 🔎 Choose a product to get recommendations")
product_names = df['title'].tolist()
product_id_map = dict(zip(df['title'], df['id']))
selected_product = st.selectbox("", product_names)

# --- Show Selected Product Info ---
if selected_product:
    product_id = product_id_map[selected_product]
    product_data = df[df['id'] == product_id].iloc[0]

    st.markdown("---")
    st.subheader("📦 Selected Product")
    col1, col2 = st.columns([1, 3])

    with col1:
        image_path = os.path.join(IMAGE_FOLDER, product_data['image'])
        if os.path.exists(image_path):
            st.image(image_path, width=200)
        else:
            st.warning(f"Image not found: {image_path}")

    with col2:
        st.markdown(f"**🛍️ Name:** {product_data['title']}")
        st.markdown(f"**📂 Category:** {product_data['category']}")
        st.markdown(f"**💬 Description:** {product_data['description']}")
        st.markdown(f"**💲 Price:** ${product_data['price']}")

    # --- Show Recommendations ---
    st.markdown("---")
    st.subheader("🧠 Recommended Products")

    recommended_products = recommender.recommend(product_id)

    for i, rec in recommended_products.iterrows():
        rec_image_path = os.path.join(IMAGE_FOLDER, rec['image'])
        rec_col1, rec_col2 = st.columns([1, 4])
        with rec_col1:
            if os.path.exists(rec_image_path):
                st.image(rec_image_path, width=100)
            else:
                st.warning(f"Image not found: {rec_image_path}")
        with rec_col2:
            st.markdown(f"**{rec['product_name']}**")
            st.markdown(f"💲 Price: ${rec['price']}")
            st.markdown("---")

# --- Footer ---
st.markdown("---")
st.markdown("🧾 Built with ❤️ by Anand using Streamlit | [GitHub Repo](#)")
