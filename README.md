# Customer_churn.io
This repository contains the customer churn project I worked on during the data scientist job simulation at BCG last November.

## Project structure

```text
Customer_churn.io/
├── README.md
├── requirements.txt
├── scripts/
│   ├── 01_load_data.py
│   ├── 02_eda.py
│   ├── 03_feature_engineering.py
│   ├── 04_modeling.py
│   ├── 05_evaluation.py
│   └── 06_train_pipeline.py
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── eda.py
│   ├── feature_engineering.py
│   ├── modeling.py
│   ├── evaluation.py
│   └── train_pipeline.py
├── data/
│   └── README.md
├── models/
│   └── .gitkeep
├── reports/
│   └── .gitkeep
├── Task 2 - Model Answer - EDA (2).ipynb
├── Task 3 - Model Answer - Feature Engineering.ipynb
├── Task 4 - Model Answer - Modeling.ipynb
└── .gitignore
```

This project follows a standard machine learning workflow: data loading, exploratory analysis, feature engineering, model training, evaluation, and business recommendations.


Executive summary
Host Organisation : BCG X
Client : PowerCo

1)	Setting the business situation and background

The Energy Market has experienced a lot change in recent years and there are more options than ever for customers to choose from. A major gas and electricity supplier called PowerCo that supplies energy to millions of clients is seeing an increase in customer churn in its customer base. This trend is concerning because churn can significantly impact revenue and market share.

The company operates in a highly competitive environment and is looking for ways to better understand customer behavior. In such a context, churn prediction becomes a strategic priority, as retaining existing customers is typically more cost-effective than acquiring new ones.

2)	Problem

After the data science team investigated the business situation, we believed that the main concern of our client is that PowerCo is experiencing churn and wants to know what are the key indicators causing customers to leave. The business need is not only to predict churn, but also to identify the drivers behind it so that the company can take targeted action.

4)	Hypothesis and data

As a data science team, after looking at the business problem through the lens of a data scientist, we came to a hypothesis such as: customer churning may be caused by customer price sensitivity, customer tenure, consumption patterns, and other customer-specific variables.

In order to test whether churn is driven by customer price sensitivity, we modeled churn probabilities of customers. To build this model, the data science team required the following data from PowerCo:

a) Customer historical data which includes characteristics of each client, for example industry, historical electricity and gas consumption, date joined as a customer, etc.

b) Churn data which should indicate if a customer has churned.

c) Historical price data which includes the price the company charges for both electricity and gas at granular time intervals.

4)	Our findings

After careful exploration of the data, we found some insights that we believe may be of interest to PowerCo stakeholders.

![image](https://github.com/user-attachments/assets/513bd9c7-282c-4192-9045-797cbb84fd45)

This graph above is simply showing us the churning status of the company.
We found that nearly 10% of PowerCo's clients have churned.

![image](https://github.com/user-attachments/assets/1d0ce88e-4391-4153-bb2f-d1f46d7414b2)

This graph above shows the churning rates across the type of contract of a customer, meaning whether or not they have signed for gas service at PowerCo. What we found is that nearly 10% of customers with gas service churned, while the churn rate differed significantly depending on contract type and customer profile.

![image](https://github.com/user-attachments/assets/d4df2ffe-146b-41b3-9e50-4270b6187525)

This chart above shows how customer tenure could influence their decision to leave. We see that clients with only 1 year of tenure do not churn, whereas after 2 years of being a PowerCo customer, churn begins to become more evident.

Note on key metrics
In order to make sure that our model performs well and informs business decision-making for our client, the data science team managed to build some key metrics to increase the predictive power of the model.
The metrics that we thought were relevant and that improved the predictive power of the model are the following:
1) Difference between off-peak prices in December and the preceding January

2) The average price changes across individual periods

3) Maximum price change between months and time periods

4) Customer tenure, which captures the number of months a company has been a client of PowerCo

5) Consumption, net margin, and other customer-level business indicators.

![image](https://github.com/user-attachments/assets/33db1714-d162-4bae-ae66-4aed6301f529)

This table above shows the tenures and the corresponding churning rates. For instance, 12% of companies with 4 months of tenure churned against 8% of companies with 5 months of tenure. The key insight from the table is that the highest churning rates occur at specific tenure intervals, suggesting that customer lifecycle stage matters.

Note on metrics importance: After evaluating our metrics, we found that the metrics that drive the prediction power of our model are not primarily price metrics, but rather consumption, customer tenure, and customer profitability indicators.

Model summary

Within the data, as we saw earlier, 10% of companies churned. Out of 3286 non-churning companies, our model accurately predicted 3282. Within the churning companies, our model accurately predicted the majority of cases, showing that the predictive signal was strong enough to guide business action.

Recommendations

PowerCo stakeholders should focus more on client retention rather than on customer churn because of the predictive power of our model regarding customer retention rates. By targeting at-risk customers earlier, the business can reduce churn and protect revenue while improving overall customer satisfaction.
