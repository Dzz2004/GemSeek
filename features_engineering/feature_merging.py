import pandas as pd

business_feature_path = 'features_engineering/business_features_engineering/businesses_Indianapolis_features.csv'
review_feature_path = 'features_engineering/review_features_engineering/business_review_Indianapolis_features.csv'
user_feature_path = 'features_engineering/user_features_engineering/businesses_user_Indianapolis_features.csv'
review_weighted_feature_path = 'features_engineering/user_features_engineering/business_review_Indianapolis_features_weighted.csv'


def merge_features(is_weighted=False):
    """
    Merge business, review, and user features into a single DataFrame.
    """
    # Load the features
    business_features = pd.read_csv(business_feature_path)
    review_features = pd.read_csv(review_feature_path) if not is_weighted else pd.read_csv(review_weighted_feature_path)
    user_features = pd.read_csv(user_feature_path)

    # Merge the features
    merged_features = business_features.merge(review_features, on='business_id', how='left')
    merged_features = merged_features.merge(user_features, on='business_id', how='left')

    # Save the merged features
    out_path = 'features_engineering/business_review_Indianapolis_features_weighted.csv' if is_weighted else 'features_engineering/business_review_Indianapolis_features.csv'
    merged_features.to_csv(out_path, index=False)
    print(f"Merged features saved to '{out_path}'")

if __name__ == "__main__":
    merge_features()
    merge_features(is_weighted=True)