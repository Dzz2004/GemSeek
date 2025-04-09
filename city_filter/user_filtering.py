import kagglehub
import pandas as pd
import json
from tqdm import tqdm

# Load the reviews of Indianapolis
reviews_Indianapolis = pd.read_csv("city_filter/reviews_Indianapolis.csv")

# extract user_id
user_ids_Indianapolis = set(reviews_Indianapolis["user_id"].tolist())  # ✅ 用 set 提升查找效率

# Load users data
path = kagglehub.dataset_download("yelp-dataset/yelp-dataset")
user_path = path + "/yelp_academic_dataset_user.json"

filtered_users = []
## read first 100 lines 
# # columns:'user_id', 'name', 'review_count', 'yelping_since', 'useful', 'funny',
#        'cool', 'elite', 'friends', 'fans', 'average_stars', 'compliment_hot',
#        'compliment_more', 'compliment_profile', 'compliment_cute',
#        'compliment_list', 'compliment_note', 'compliment_plain',
#        'compliment_cool', 'compliment_funny', 'compliment_writer',
#        'compliment_photos'

with open(user_path, "r", encoding="utf-8") as open_file:
    for line in tqdm(open_file, total=1987897):  # ✅ tqdm 直接包 open_file
        data = json.loads(line)
        if data["user_id"] in user_ids_Indianapolis:
            filtered_users.append({
                'user_id':data['user_id'],
                'name':data['name'],
                'review_count':data['review_count'],
                'yelping_since':data['yelping_since'],
                'useful':data['useful'],
                'funny':data['funny'],
                'cool':data['cool'],
                'elite':data['elite'],
                'friends':data['friends'],
                'fans':data['fans'],
                'average_stars':data['average_stars'],
                'compliment_hot':data['compliment_hot'],
                'compliment_more':data['compliment_more'],
                'compliment_profile':data['compliment_profile'],
                'compliment_cute':data['compliment_cute'],
                'compliment_list':data['compliment_list'],
                'compliment_note':data['compliment_note'],
                'compliment_plain':data['compliment_plain'],
                'compliment_cool':data['compliment_cool'],
                'compliment_funny':data['compliment_funny'],
                'compliment_writer':data['compliment_writer'],
                'compliment_photos':data['compliment_photos']
            })
# convert to pandas dataframe
users_Indianapolis = pd.DataFrame(filtered_users)
# Save to CSV
users_Indianapolis.to_csv("city_filter/users_Indianapolis.csv", index=False)
print("Filtered users saved to city_filter/users_Indianapolis.csv")
print(users_Indianapolis.head())

