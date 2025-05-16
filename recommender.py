# recommender.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class ProductRecommender:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self.vectorizer.fit_transform(self.df['description'])

    def recommend(self, product_id, top_n=5):
        try:
            index = self.df[self.df['id'] == product_id].index[0]
        except IndexError:
            return pd.DataFrame()

        cosine_similarities = cosine_similarity(self.tfidf_matrix[index], self.tfidf_matrix).flatten()
        similar_indices = cosine_similarities.argsort()[-(top_n + 1):][::-1]
        similar_indices = [i for i in similar_indices if i != index]

        columns_to_show = ['id', 'title', 'category', 'description', 'image']
        if 'price' in self.df.columns:
            columns_to_show.append('price')

        return self.df.iloc[similar_indices][columns_to_show].rename(columns={'title': 'product_name'})
