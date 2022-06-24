# Data-Science-Projects
This repo have almost all projects that I have done during my Data Science learning duration. I have used various kinds of algorithms of Machine Learning to do the predictions and after predictions, I have calculated the accuracy of each model.
Each Project is using a different dataset and solving a different problem that can be found along with the code. And each project is having the following steps.
1) Data Understanding
2) Data Cleaning
3) Data Analysis (Descriptive, Statistic, EDA)
4) Feature Engineering
5) Model Building
6) Model Evalution

Let's discuss each of the project briefly.
## Breast Cancer Prediction
Breast cancer is the most frequent form of cancer in women worldwide. It accounts for 25% of all cancer cases and afflicted more than 2,1,000,000 persons in 2015 alone. So, I used an open-source dataset from kaggle that was having the BIO details of patient along with target feature. So, I preprocessed the data and check the relationship of features with target and get the following heatmap.
![image](https://user-images.githubusercontent.com/53445779/175564908-96dae2fc-ae81-4e3d-850f-00e190f0a2cb.png)
I used all of the features and built following two models.
- Logistic Regression
- K Nearest Neighbour
KNN was performing well so I tried to get the optimal value of K for KNN.
![image](https://user-images.githubusercontent.com/53445779/175565282-8380246a-ce3d-4746-a469-f8a15bc4488d.png)
From this image K=4 or 5 is performing well so I selected K=5 and did hyperparameter tuning using GridSearchCV and get the optimal values for hyperparameters of model and the final accuracy that I achieved was **88%**.
