Where we Addressed the Problem
1. City Filtering (CITY_FILTERING.md) 
You narrowed the dataset scope by selecting Indianapolis based on manageable size and representativeness.
Why it's aligned:

Reduces noise from overpopulated areas like Las Vegas or Phoenix.

Enables focused analysis on underrated businesses within a single city.

Cleaned city names helps improve data integrity—vital for reliable downstream analysis.

Key Progress:

Normalized city names to avoid duplicate entries.

Selected a target city with a balanced volume of businesses and reviews.

Filtered to 7,547 businesses and 360,000 reviews—feasible for modeling.

Sentiment Analysis (SENTIMENT_ANALYSIS.md) 
You conducted batch sentiment analysis on Indianapolis reviews using a sliding window model.

Why it's aligned:

Sentiment scores help distinguish businesses with genuinely positive feedback, not just high numerical ratings.

Enables deeper understanding of customer experiences, highlighting businesses with positive sentiment but few reviews—your "hidden gems."

Key Progress:

Used a multilingual model to rate review sentiment.

Saved results to reviews_Indianpolis_analyzed.csv.

Processed long reviews efficiently, ensuring all text was analyzed without truncation.
