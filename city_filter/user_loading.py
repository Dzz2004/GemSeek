import kagglehub
import pandas as pd
import json
from tqdm import tqdm

# Download latest version
path = kagglehub.dataset_download("yelp-dataset/yelp-dataset")

print("Path to dataset files:", path) 
##  /home/dzz/.cache/kagglehub/datasets/yelp-dataset/yelp-dataset/versions/4

# Load the dataset
import pandas as pd
# open user.json file,and read it line by line 
user_path = path + "/yelp_academic_dataset_user.json"
print("Path to user file:", user_path)
open_file = open(user_path, "r", encoding="utf-8")
users = []
## read first 100 lines 
# # columns:'user_id', 'name', 'review_count', 'yelping_since', 'useful', 'funny',
#        'cool', 'elite', 'friends', 'fans', 'average_stars', 'compliment_hot',
#        'compliment_more', 'compliment_profile', 'compliment_cute',
#        'compliment_list', 'compliment_note', 'compliment_plain',
#        'compliment_cool', 'compliment_funny', 'compliment_writer',
#        'compliment_photos'

for i in tqdm(range(100), desc="Loading users", unit="user"):
    line = json.loads(open_file.readline())
    users.append({        
        'user_id':line['user_id'],
        'name':line['name'],
        'review_count':line['review_count'],
        'yelping_since':line['yelping_since'],
        'useful':line['useful'],
        'funny':line['funny'],
        'cool':line['cool'],
        'elite':line['elite'],
        'friends':line['friends'],
        'fans':line['fans'],
        'average_stars':line['average_stars'],
        'compliment_hot':line['compliment_hot'],
        'compliment_more':line['compliment_more'],
        'compliment_profile':line['compliment_profile'],
        'compliment_cute':line['compliment_cute'],
        'compliment_list':line['compliment_list'],
        'compliment_note':line['compliment_note'],
        'compliment_plain':line['compliment_plain'],
        'compliment_cool':line['compliment_cool'],
        'compliment_funny':line['compliment_funny'],
        'compliment_writer':line['compliment_writer'],
        'compliment_photos':line['compliment_photos']
    })
open_file.close()



# convert to pandas dataframe
df = pd.DataFrame(users)
df.to_csv("yelp_users_first100.csv", index=False)
print(df.head())
# print the columns
print(df.columns)


