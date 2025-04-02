# 12-Day Detailed Parallel Action Plan

## Core Parallel Points:
- **Development of traditional models (K-means/Random Forest) and GNN can proceed in parallel after data preprocessing**
- **Data annotation, visualization, and model training are conducted simultaneously**
- **LLM text processing and structured feature engineering are carried out concurrently**

### Days 1-2: Data Preprocessing and Basic Feature Engineering

| Task                                   | Lead Official  | Deliverable               | Parallelism Description        |
| -------------------------------------- | -------------- | ------------------------- | ------------------------------ |
| Data cleaning (conditional filtering or sampling) | KAIZEN         | Cleaned `business.json`    | Synchronized with LLM processing |
| Sentiment analysis of reviews using LLM | Dong Zhuangzhi | Sentiment score file      | Independent task               |
| User social relationship analysis      | Zhong Guangshen| `user-user_edge_list.csv` | Independent task               |

### Days 3-4: Feature Fusion and Graph Construction

| Task                                   | Lead Official  | Deliverable               | Parallelism Description        |
| -------------------------------------- | -------------- | ------------------------- | ------------------------------ |
| Merchant feature merging (value + sentiment) | Dong Zhuangzhi | `business_features.pkl`   | Input for traditional models   |
| Heterogeneous graph construction (DGL) | Zhong Guangshen| `business_user_graph.bin` | Input for GNN                  |
| Manually annotate 100 merchant labels  | KAIZEN         | `labeled_business.csv`    | Independent task               |

### Days 5-8: Model Development (Fully Parallel)

**Traditional Model Branch**

| Task                                   | Lead Official  | Deliverable               | Parallel Tools                 |
| -------------------------------------- | -------------- | ------------------------- | ------------------------------ |
| K-means cluster analysis               | Dong Zhuangzhi | `cluster_results.csv`     | Jupyter Notebook               |
| Random forest training and parameter tuning | Dong Zhuangzhi | `RF_model.pkl`           | Scikit-learn                   |

**GNN Branch**

| Task                                   | Lead Official  | Deliverable               | Parallel Tools                 |
| -------------------------------------- | -------------- | ------------------------- | ------------------------------ |
| Lightweight GNN model design           | Zhong Guangshen| `GNN_model.pt`           | PyTorch + DGL                  |
| GNN training (supervised learning)     | Zhong Guangshen| `business_potential_score.csv` | CUDA acceleration (optional) |

### Days 9-10: Comparison and Visualization of Results

| Task                                   | Lead Official         | Deliverable               | Collaborative Approach         |
| -------------------------------------- | --------------------- | ------------------------- | ------------------------------ |
| Model performance comparison (AUC/F1)  | Dong Zhuangzhi & Zhong Guangshen | `comparison_report.md` | Joint analysis                 |
| Results visualization                  | Liza                  | `comparison.png`          | Template code reuse            |
| GNN attention weight visualization     | Zhong Guangshen       | `attention_heatmap.png`   | PyVis library                  |

### Days 11-12: Report Integration and Rehearsal

| Task                                   | Lead Official  | Deliverable               | Division of Labor Logic        |
| -------------------------------------- | -------------- | ------------------------- | ------------------------------ |
| PPT production (model comparison storyline) | Liza          | `final_presentation.pptx` | Use template for quick filling |
| Technical report writing (methodology + results) | Dong Zhuangzhi | `technical_report.pdf` | LaTeX template                 |
| Rehearsal and Q&A preparation          | Zhong Guangshen| `QA_notes.txt`           | Mock judge questions           |

## NOTICE
it is just a reference.

The contant is may not enough mature. with the development of this project, it may be changed. 
