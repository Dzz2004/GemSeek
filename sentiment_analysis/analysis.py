# Use a pipeline as a high-level helper
from transformers import pipeline
import pandas as pd


pipe = pipeline("text-classification", model="tabularisai/multilingual-sentiment-analysis")

df = pd.read_csv("yelp_reviews_first100.csv")
df = df.dropna(subset=["text"]) # drop rows with NaN in the text column
df = df[df["text"].str.len() < 512] # drop rows with text longer than 512 characters

df = df[df["text"].str.strip() != ""] # drop rows with empty strings in the text column

results = pd.DataFrame()
## add id column to results
results["review_id"] = df["review_id"]
results["bussiness_id"] = df["business_id"]
results["user_id"] = df["user_id"]
results["sentiment"] = ""
results["confident_score"] = ""

for i, row in df.iterrows():
    # print(i)
    # print(row["text"])
    # print(row["review_id"])
    # print(row["business_id"])
    # print(row["user_id"])
    result = pipe(row["text"])[0]
    results.at[i, "sentiment"] = result["label"]
    results.at[i, "confident_score"] = result["score"]
    print(f"Processed {i} rows, {row['review_id']}, {row['business_id']}, {row['user_id']}, {result['label']}, {result['score']}")
results.to_csv("sentiment_analysis/sentiment_analysis_results.csv", index=False)