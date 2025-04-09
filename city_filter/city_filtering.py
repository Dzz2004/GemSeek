import kagglehub
import pandas as pd
import json
from tqdm import tqdm

business_ids_Indianapolis = []

# Download latest version
path = kagglehub.dataset_download("yelp-dataset/yelp-dataset")
# Load the dataset
business_path = path + "/yelp_academic_dataset_business.json"
open_file = open(business_path, "r", encoding="utf-8")

# Load the alias: columns:alias_name,canonical_name
alias_df = pd.read_csv("city_filter/alias_dict.csv")
alias_dict = {}
for index, row in alias_df.iterrows():
    alias_dict[row["alias_name"]] = row["canonical_name"]


# Create a function to get canonical name
def get_canonical_name(alias_name):
    return alias_dict.get(alias_name, alias_name)

while True:
    line = open_file.readline()
    if not line:
        break
    # convert to pandas dataframe
    data = json.loads(line)
    # check if the city is Indianapolis
    if get_canonical_name(data['city']) == "Indianapolis":
        business_ids_Indianapolis.append(data["business_id"])
open_file.close()
# convert business_ids_Indianapolis to pandas dataframe
df = pd.DataFrame(business_ids_Indianapolis, columns=["business_id"])
# save to csv
df.to_csv("city_filter/business_ids_Indianapolis.csv", index=False)
    