import numpy as np
from collections import defaultdict

class RecommendationSystem:
    def __init__(self):
        self.user_ratings = {}
        self.item_similarity = {}
    
    def add_user_ratings(self, user_id, ratings):
        self.user_ratings[user_id] = ratings
    
    def collaborative_filtering(self, target_user, k=3):
        similarities = {}
        target_ratings = self.user_ratings.get(target_user, {})
        
        for user, ratings in self.user_ratings.items():
            if user != target_user:
                similarity = self._cosine_similarity(target_ratings, ratings)
                similarities[user] = similarity
        
        top_users = sorted(similarities.items(), key=lambda x: x[1], reverse=True)[:k]
        
        recommendations = {}
        for user, similarity in top_users:
            for item, rating in self.user_ratings[user].items():
                if item not in target_ratings:
                    if item not in recommendations:
                        recommendations[item] = 0
                    recommendations[item] += similarity * rating
        
        return sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    
    def _cosine_similarity(self, ratings1, ratings2):
        common_items = set(ratings1.keys()) & set(ratings2.keys())
        if not common_items:
            return 0
        
        dot_product = sum(ratings1[item] * ratings2[item] for item in common_items)
        norm1 = sum(ratings1[item]**2 for item in common_items) ** 0.5
        norm2 = sum(ratings2[item]**2 for item in common_items) ** 0.5
        
        if norm1 == 0 or norm2 == 0:
            return 0
        
        return dot_product / (norm1 * norm2)

if __name__ == "__main__":
    rs = RecommendationSystem()
    
    rs.add_user_ratings("user1", {"item1": 5, "item2": 3, "item3": 4})
    rs.add_user_ratings("user2", {"item1": 4, "item2": 2, "item4": 5})
    rs.add_user_ratings("user3", {"item3": 3, "item4": 4, "item5": 5})
    
    recommendations = rs.collaborative_filtering("user1")
    print("推荐结果:", recommendations)
