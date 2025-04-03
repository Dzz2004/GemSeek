import kagglehub

# Download latest version
path = kagglehub.dataset_download("yelp-dataset/yelp-dataset")

print("Path to dataset files:", path) 
##  /home/dzz/.cache/kagglehub/datasets/yelp-dataset/yelp-dataset/versions/4

# Load the dataset
import pandas as pd
# open review.json file,and read it line by line 
review_path = path + "/yelp_academic_dataset_review.json"
open_file = open(review_path, "r", encoding="utf-8")
reviews = []
## read first 100 lines 
for i in range(100):
    line = open_file.readline()
    reviews.append(line)
open_file.close()

# convert to pandas dataframe
import json
def json_to_dataframe(json_lines):
    data = []
    for line in json_lines:
        data.append(json.loads(line))
    return pd.DataFrame(data)

# convert to pandas dataframe
df = json_to_dataframe(reviews)
df.to_csv("yelp_reviews_first100.csv", index=False)
print(df.head())
# print the columns
print(df.columns)


