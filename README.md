![img](https://www.bee.id/wp-content/uploads/2023/04/telemarketing-adalah.jpg)

<center>

<h1>Potential Customer Classification to Increase Marketing Efficiency</h1>

---

</center>

<br />
<br />

## **Background**
Deposit is a banking investment product that allows customers to store their money for a specific period and withdraw it along with the interest (return) at an agreed time. Banks need the money stored in the form of deposits to maintain the company's liquidity and to increase profit, as the money deposited can be lent to other customers, allowing the bank to earn interest from loans. Therefore, banks are usually very active in seeking deposit investment customers, considering its nature as a win-win solution where both parties benefit.

The current limitation when bank marketing agents promote their deposit products is the lack of customer filtering beforehand, which often leads to contacting customers who are not potential (refusing to invest), making marketing activities less efficient and not yielding optimal results. Therefore, a special instrument is needed to filter customers. One of the instruments that can be used is a machine learning classification model that can predict how potential a customer is to accept a deposit investment offer. The advantage of using a machine learning model is that it can be continuously trained with new data, making this instrument more robust against the dynamics of customer characteristics.

## **Objective**
The objective of this project is to enhance the efficiency of the marketing team's activities by developing a model that can predict clients who are likely to invest in term deposits. A potential client is defined as one who, based on their characteristics (reflected by the values of various features), is highly likely to accept a term deposit investment offer after the telemarketing process. By using the developed model, the bank is expected to improve the efficiency of telemarketing activities by first filtering the client data so that the clients contacted by telemarketers/marketing agents are those who have a high potential (potential clients) to accept the term deposit investment offer.

## **About the dataset**

This dataset was taken from the UCI Machine Learning Repository. It was collected between May 2008 and November 2010 (2 years and 6 months) during telemarketing campaigns conducted by a bank in Portugal. The goal of these campaigns was to attract clients/customers to invest in term deposit instruments.

## **Conclusion**

1. The model was evaluated using the precision metric to avoid false positives, which occur when a client who is not actually potential is classified as potential. The selection of this metric is based on the project's objective, which is to improve the efficiency of marketing activities by creating a model that can predict clients who are likely to invest in term deposits. Incorrectly predicting a client as potential can harm the marketing team by reducing efficiency
   
2. Five models were tested in default mode, namely KNN, SVM, Decision Tree, Random Forest, and XGBoost. All models showed indications of overfitting (based on precision values), as the precision values from predictions on the training dataset were above 80%, while on the test dataset they were below 80%
   
3. In the evaluation of model predictions with default hyperparameters, the SVM model showed the lowest level of overfitting compared to other models, as it had the smallest difference in precision values between predictions on the training dataset and the test dataset. Simply put, the SVM model demonstrated better generalization ability compared to the other models
   
4. During the cross-validation process, the SVM model was selected as the best model to undergo hyperparameter tuning for several reasons:

   - It had the highest average precision from cross-validation results (80.6%) with a relatively small
     standard deviation (2.19%)
   - The difference between the average precision from cross-validation and the initial prediction
     precision was very small, only 0.537%
  These reasons indicate that the SVM model has good consistency in generalizing data, with very small differences in prediction results across different datasets
5. For predictions on both the training dataset and the test dataset, the SVM model with hyperparameter tuning had the highest precision values (82.2% on the training dataset and 80.2% on the test dataset) compared to the SVM model with default hyperparameters (81% on the training dataset and 78.6% on the test dataset)
   
6. In terms of overfitting (based on the precision metric) and data generalization, the SVM model with hyperparameter tuning was slightly better than the SVM model with default hyperparameters.

## **Business Recommendation**

1. Consider creating preventive measures such as **early intervention programs**, personalized payment plans, or targeted intensive communication for those predicted to default.
2. Provide customers with information at the beginning of the agreement about the consequences of defaulting and what they should do if they realize they are going to default

## **Model Improvement Recommendation**

1. Regularly update the model with new data to ensure its effectiveness over time. Periodic retraining and hyperparameter tuning can help maintain or improve the model's performance, ensuring that it adapts to any changes in customer behavior or economic conditions

