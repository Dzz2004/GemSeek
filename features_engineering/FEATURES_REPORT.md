

# Yelp 商家用户评论特征提取报告  
**Yelp Business, User, and Review Feature Extraction Report**

## 🧾 项目概述 | Project Overview

本项目旨在从 Yelp 数据集中提取高质量的结构化特征，构建适用于后续分析和建模的商家、用户和评论多维度数据集。  
This project aims to extract high-quality structured features from the Yelp dataset, building a multi-dimensional dataset of businesses, users, and reviews for downstream analysis and modeling.

## 📁 源代码与输出 | Code & Outputs

- **三种特征的文件夹 / folders**: `business_features_engineering`,`review_features_engineering`,`user_features_engineering`
- **合并和补充代码 / merge and supplement**: `feature_merging.py`
- **最终输出 / Final Output**:  `features.csv`,`features_weighted.csv`
- **包含字段 / contains**:
  ```txt
  business_id,stars,review_count,attr_score,cat_score,avg_review_stars,std_review_stars_scaled,pos_review_ratio,neg_review_ratio,neu_review_ratio,long_review_ratio,avg_review_length_scaled,avg_word_count_scaled,avg_useful_scaled,avg_funny_scaled,avg_cool_scaled,interact_score_mean_scaled,sentiment_score_mean_scaled,first_review_date,last_review_date,recent_review_ratio,review_timespan_days_scaled,review_density_per_day_scaled,review_burst_score_scaled,avg_user_avg_stars,elite_user_ratio,avg_user_account_age_days,avg_user_review_count_log_scaled,avg_user_useful_log_scaled,avg_user_funny_log_scaled,avg_user_cool_log_scaled,avg_user_fans_log_scaled,avg_user_compliments_log_scaled
  ```

## 🏪 商家特征 | Business Features

- **源文件**：`business_feature.ipynb`  
  **Source**: `business_feature.ipynb`

- **最终输出**：`business_Indianapolis_features.csv`  
  **Final Output**: `business_Indianapolis_features.csv`

- **中间数据**：
  - `business_Indianapolis_cleaned.csv`：原始数据清洗与统一格式  
  - `business_Indianapolis_top_attributes.csv`：前30高频属性与值  
  - `business_Indianapolis_categories.csv`：前50高频类别与值  

- **特征内容**：
  - `stars`, `review_count`：商家评分与评论数  
  - `attr_score`, `cat_score`：属性得分与类别得分（未加权）  
  - 可视化图：`business_scores_distribution.png`

- **说明**：属性与类别得分作为两个独立变量保留。  
  **Note**: `attr_score` and `cat_score` are retained as separate features.



## 👤 用户特征 | User Features

- **源文件**：`user_feature.ipynb`  
  **Source**: `user_feature.ipynb`

- **最终输出**：`businesses_user_Indianapolis_features.csv`  
  **Final Output**: `businesses_user_Indianapolis_features.csv`

- **特征内容**（聚合到商家维度）：
  - `avg_user_review_count`：用户平均评论数  
  - `avg_user_useful`, `avg_user_funny`, `avg_user_cool`：互动类均值  
  - `avg_user_stars`：用户平均评分  
  - `avg_user_fans`：平均粉丝数  
  - `avg_user_elite_flag`：精英用户占比  
  - `avg_user_compliment_sum`：赞赏数总和均值  
  - `avg_user_account_age_days`：用户账号平均存在时长（天）



## 💬 评论特征 | Review Features

- **源文件**：`user_quality.ipynb`(在`user_features_engineering`目录下), `review_feature.ipynb`  
  **Source**: `user_quality.ipynb`(under `user_features_engineering`), `review_feature.ipynb`

- **最终输出**：  
  - `business_review_Indianapolis_features.csv`：基础评论特征  
  - `business_review_Indianapolis_features_weighted.csv`：包含加权特征的版本(在`user_features_engineering`目录下)

- **基础特征**：
  - 平均评分、方差、情感比例（正/负/中性）  
  - 长文本比例、平均长度、词数、互动性（useful, funny, cool）  
  - 评论时间密度、活跃度、新近评论比例、爆发程度等  

- **加权特征**（使用交互性和时间加权）：
  - `weighted_stars`：加权评分  
  - `weighted_sentiment_score_scaled`：加权情感得分  
  - `weighted_useful_scaled`，`weighted_funny_scaled`，`weighted_cool_scaled`：加权互动特征  
  - `weighted_interact_score_scaled`：整体交互性加权得分  
  - `std_weighted_stars_scaled`：加权评分的标准差（衡量稳定性）



## ✅ 总结 | Conclusion

本阶段已成功构建了以**商家为中心**的三类高质量结构化特征，包括：

1. 商家属性和类别特征  
2. 用户群体画像特征  
3. 评论文本行为和情感特征（含加权处理）

这些特征为后续的异常商家识别、评分预测、GNN建图等任务提供了坚实的数据基础。  
These features provide a solid foundation for downstream tasks such as identifying underrated businesses, score prediction, and graph construction using GNNs.
