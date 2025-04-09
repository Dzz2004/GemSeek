import kagglehub
import pandas as pd
import json
from tqdm import tqdm

# Load the business ids
business_ids_df = pd.read_csv("city_filter/business_ids_Indianapolis.csv")
business_ids_Indianapolis = set(business_ids_df["business_id"].tolist())  # ✅ 用 set 提升查找效率

# Load review data
path = kagglehub.dataset_download("yelp-dataset/yelp-dataset")
review_path = path + "/yelp_academic_dataset_review.json"

filtered_reviews = []

with open(review_path, "r", encoding="utf-8") as open_file:
    for line in tqdm(open_file, total=6990280):  # ✅ tqdm 直接包 open_file
        data = json.loads(line)
        if data["business_id"] in business_ids_Indianapolis:
            data["text"] = data["text"].replace("\n", " ")
            filtered_reviews.append({
                "review_id": data["review_id"],
                "user_id": data["user_id"],
                "business_id": data["business_id"],
                "stars": data["stars"],
                "useful": data["useful"],
                "funny": data["funny"],
                "cool": data["cool"],
                "text": data["text"],
                "date": data["date"]
            })

# ✅ 一次性转 DataFrame
reviews_Indianapolis = pd.DataFrame(filtered_reviews)

# Save to CSV
reviews_Indianapolis.to_csv("city_filter/reviews_Indianapolis.csv", index=False)
