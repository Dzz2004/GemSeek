# How to Download Yelp?
A guidance of downloading the Yelp dataset in Kaggle.

## 1. get a kaggle token
- **kaggle:** a community of Machine Learning and Data Science
- **get a token**: register, and follow the reference in offical website, then you will download a .json file named **kaggle.json**

## 2. config your token
- **library:** use conda or pip install  **kagglehub** in your python env. the exmaple:
    ```bash
    pip install kagglehub
    ```
- **position:** create a dir named **.kaggle**, and then move the **kaggle.json** under the path, the example: 
    ```
    your_project_path/.kaggle/kaggle.json
    ```
## 3. download by python
- **dataset_loading.py:** this code file gives a reference of how to downloading it. The core lines are:
    ```python
    import kagglehub

    # Download latest version
    path = kagglehub.dataset_download("yelp-dataset/yelp-dataset")

    print("Path to dataset files:", path) 
    ```
- **the path:** the dataset will be download in the default path. You will see the path after printing. If you want to download the dataset into where you want, add a param in ```kagglehub.dataset_download``` fuction.

## NOTICE

- The dataset is so large. Here are details about the sizes of the dataset.

    | **file** | **size** |
    | :--------: | :--------: |
    | bussiness.json | 113.36MB |
    | checkin.json | 273.67MB |
    | review.json | 4.98GB |
    | tip.json | 172.24MB |
    | user.json | 3.13GB |

- Because some files are so large, converting them directly to DataFrame can be disastrous. **It is better to work with a file and try to read it line by line.**
    


