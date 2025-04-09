import kagglehub
import pandas as pd
import json
from tqdm import tqdm

# Load the business_ids of Indianapolis
business_ids_df = pd.read_csv("city_filter/business_ids_Indianapolis.csv")
business_ids_Indianapolis = set(business_ids_df["business_id"].tolist())  # ✅ 用 set 提升查找效率

# load business data
path = kagglehub.dataset_download("yelp-dataset/yelp-dataset")
business_path = path + "/yelp_academic_dataset_business.json"
filtered_businesses = []

# columns:business_id,name,address,city,state,postal_code,latitude,longitude,stars,review_count,is_open,attributes,categories,hours

with open(business_path, "r", encoding="utf-8") as open_file:
    for line in tqdm(open_file, total=150346):  # ✅ tqdm 直接包 open_file
        data = json.loads(line)
        if data["business_id"] in business_ids_Indianapolis:
            filtered_businesses.append({
                "business_id": data["business_id"],
                "name": data["name"],
                "address": data["address"],
                "city": data["city"],
                "state": data["state"],
                "postal_code": data["postal_code"],
                "latitude": data["latitude"],
                "longitude": data["longitude"],
                "stars": data["stars"],
                "review_count": data["review_count"],
                "is_open": data["is_open"],
                "attributes": str(data["attributes"]),
                "categories": str(data["categories"]),
                "hours": str(data["hours"])
            })

# convert to pandas dataframe
businesses_Indianapolis = pd.DataFrame(filtered_businesses)
# Save to CSV
businesses_Indianapolis.to_csv("city_filter/businesses_Indianapolis.csv", index=False)
print("Filtered businesses saved to city_filter/businesses_Indianapolis.csv")
print(businesses_Indianapolis.head())
print("Total number of businesses in Indianapolis:", len(businesses_Indianapolis))



