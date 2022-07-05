# Data-Science-Projects
This repo has almost all the projects that I have done during my Data Science learning duration. I have used various kinds of algorithms of Machine Learning to do the predictions and after the predictions, I have calculated the accuracy of each model.
Each Project is using a different dataset and solves a different problem that can be found along with the code. And each project is having the following steps.
1) Data Understanding
2) Data Cleaning
3) Data Analysis (Descriptive, Statistic, EDA)
4) Feature Engineering
5) Model Building
6) Model Evaluation

Let's discuss each of the projects briefly.
## 1) Breast Cancer Prediction
Breast cancer is the most frequent form of cancer in women worldwide. It accounts for 25% of all cancer cases and afflicted more than 2,1,000,000 persons in 2015 alone. So, I used an open-source dataset from Kaggle that was having the BIO details of the patient along with the target feature. So, I preprocessed the data and check the relationship of features with the target and get the following heatmap.
![image](https://user-images.githubusercontent.com/53445779/175564908-96dae2fc-ae81-4e3d-850f-00e190f0a2cb.png)

I used all of the features and built the following two models.
- Logistic Regression
- K Nearest Neighbour

KNN was performing well so I tried to get the optimal value of K for KNN.
![image](https://user-images.githubusercontent.com/53445779/175565282-8380246a-ce3d-4746-a469-f8a15bc4488d.png)

From this image K=4 or 5 is performing well so I selected K=5 and did hyperparameter tuning using GridSearchCV and get the optimal values for hyperparameters of the model and the final accuracy that I achieved was *88%*.

## Car Spead Prediction (Simple Linear VS Polynomial Regression)

The second project that I made in this repository was to check the difference between Simple Linear Regression and the Polynomial Regression model. Car ID was the input feature and Spead of the car is the target feature. First, I made Simple regression and for that plot is given below.

![image](https://user-images.githubusercontent.com/53445779/175906895-e1eb6cd6-1548-4045-a776-266c4e99f039.png)

Then I applied the Polynomial Regression model and that plot is given below.

![image](https://user-images.githubusercontent.com/53445779/175906977-d0c9d3b9-76c5-4dd2-82a2-14489ff98b9c.png)

From this, you can see that Polynomial is performing very well than the Simple Linear Regression model because that data is Non-Linear.

## Heart Data Analysis
