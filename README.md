# 🛍️ E-Commerce Product Recommender System
This is an intelligent product recommendation system for an e-commerce platform. Built using **Python**, **Pandas**, **Scikit-learn**, and **Streamlit**, it suggests similar products based on the user's selection using NLP and cosine similarity.

> 🔗 Developed as part of the Micro IT Internship Project.

---

## 🚀 Features

- ✅ View detailed information of selected products
- 🤖 Get intelligent product recommendations
- 🖼️ Display product images dynamically
- 📦 User-friendly web interface built with Streamlit
- 📊 Content-based filtering using product metadata
- 💾 Runs locally in a browser

---

## 📂 Project Structure
ecommerce_recommender/
├── app.py # Streamlit App
├── recommender.py # Recommendation Engine Logic
├── products.csv # Product Dataset
├── images/ # Product Images
├── requirements.txt # Required Python Libraries
├── LICENSE
└── README.md


---

## 🧠 How It Works

The recommendation engine uses **content-based filtering** by vectorizing product metadata (title, description, category) using **TF-IDF** and calculates similarity using **cosine similarity**.

---

## 🔧 Installation & Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/ecommerce-recommender.git
   cd ecommerce-recommender

pip install -r requirements.txt
streamlit run app.py

✅ Requirements

    Python 3.8+

    Streamlit

    Pandas

    Scikit-learn

    Install with:
    pip install -r requirements.txt

📄 License

This project is licensed under the MIT License. See the LICENSE file for details.
🙋‍♂️ Author

Bhooma Anand
B.Tech CSE (AI), UTD CSVTU Bhilai
💼 Internship @ Micro IT
📬 razzanand97@gmail.com
⭐️ Show Your Support

If you like this project, give it a ⭐️ on GitHub — it helps others discover it!
