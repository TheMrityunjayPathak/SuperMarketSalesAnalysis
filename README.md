## Super Market Sales Analysis

Hello Everyone,

Here is My EDA Project based on Super Market Sales Dataset where I analyzed the Data by using Matplotlib and Seaborn.

## Dataset

I used Super Market Sales Dataset from Kaggle recorded for 3 Different Cities for 3 Months.

**Link to the Dataset :** [Super Market Sales Dataset](https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales)

## Problem Statement

- The objective of the supermarket sales project is to analyze sales data to gain insights into customer purchasing behavior, product performance, and overall trends, enabling data-driven decision-making for the supermarket business.

## Table of Contents

- [Setting up the Enviroment](#setting-up-the-enviroment)
- [Libraries required for the Project](#libraries-required-for-the-project)
- [Getting started with Repository](#getting-started)
- [Steps involved in the Project](#steps-involved-in-the-project)
- [Conclusion](#conclusion)
- [Link to the Notebook](#link-to-the-notebook)

## Setting up the Enviroment

Jupyter Notebook is required for this project and you can install and set it up in the terminal.

- Install the Notebook - `pip install notebook`

- Run the Notebook - `jupyter notebook`

## Libraries required for the Project

**NumPy**

- Go to Terminal and run this code - `pip install numpy`

- Go to Jupyter Notebook and run this code from a cell - `!pip install numpy`

**Pandas**

- Go to Terminal and run this code - `pip install pandas`

- Go to Jupyter Notebook and run this code from a cell - `!pip install pandas`

**Matplotlib**

- Go to Terminal and run this code - `pip install matplotlib`

- Go to Jupyter Notebook and run this code from a cell - `!pip install matplotlib`

**Seaborn**

- Go to Terminal and run this code - `pip install seaborn`

- Go to Jupyter Notebook and run this code from a cell - `!pip install seaborn`

**Sklearn**

- Go to Terminal and run this code - `pip install sklearn`

- Go to Jupyter Notebook and run this code from a cell - `!pip install sklearn`

## Getting Started

- Clone the repository to your local machine using the following command :
```
git clone https://github.com/TheMrityunjayPathak/SuperMarketSalesAnalysis.git
```

## Steps involved in the Project

**Reading the Data**

- First I installed all the necessary libraries required for this Project.

- Then I imported the Data by reading csv file using `read.csv()` Method.

- Then I dropped the `Invoice ID` Column because we don't need it in analysis.

- After that I listed down all the columns in the Dataset by `df.columns` Method.

- Then I used `df.shape` Method to look for the rows and columns in the Data.

- Then I look for the Info of the Dataset by using `df.info()` Method.

**Cleaning the Data**

- First I start by describing the Data by using `df.describe()` Method.

- Then I converted Date Column to Pandas Date and Time DataType.

- And After that I extracted Year, Month, Day from the Date.

- Then I listed down all the unique values of categorical columns.

- And Finally I verified the null values in the Dataset by using `df.isna().sum()`

**Visualizing the Data**

- Per Unit Price of Each Product Lines

![4dda0fb4-2fe9-461c-877f-6d309d329bea](https://github.com/TheMrityunjayPathak/SuperMarketSalesAnalysis/assets/123563634/ec10388d-9019-4e82-91b4-8cc4af67067e)

- Count of Different Types of Customers from Different Cities

![59566abe-8e0a-4347-8ee9-fb8f5608ddb0](https://github.com/TheMrityunjayPathak/SuperMarketSalesAnalysis/assets/123563634/2e57f8b1-4c3a-4dd8-a727-aa30b5e82acb)

- Count of Different Types of Products in Super Market

![9f65905c-ff13-4ecd-abfa-3f780508e363](https://github.com/TheMrityunjayPathak/SuperMarketSalesAnalysis/assets/123563634/c1b32b30-345d-4322-90e2-8136ee4305e6)

- Count of Different Gender Visitors at Different Branches

![ab391fa6-b095-4134-9cca-9d0aa26db3d0](https://github.com/TheMrityunjayPathak/SuperMarketSalesAnalysis/assets/123563634/c5b8a7dc-b019-409f-a19a-094b2f237b7c)

- Count of Different Types of Payment Methods used by Different Genders

![1cec281b-96e2-42eb-8e4c-7ef76eaeb497](https://github.com/TheMrityunjayPathak/SuperMarketSalesAnalysis/assets/123563634/c112815d-9f15-4569-8f23-b23f5c8bb3c1)

- Count of Different Gender Visitors from Different Cities

![69ab4d7f-a7a3-4af6-ad73-55422d57e381](https://github.com/TheMrityunjayPathak/SuperMarketSalesAnalysis/assets/123563634/bf804002-0553-4a6e-94da-92299ff4109d)

- Quantity of Products Sold from Each Product Line

![b5d54ca5-3d22-4eec-b21d-392e91dfa6d7](https://github.com/TheMrityunjayPathak/SuperMarketSalesAnalysis/assets/123563634/f564c16b-2bbc-46f8-b244-46412949a702)

- Different Payment Methods Used by Different Cities

![73eaa774-43ac-4728-9c6d-16462bcddfc6](https://github.com/TheMrityunjayPathak/SuperMarketSalesAnalysis/assets/123563634/ac310f2c-943d-4d24-82cb-d9f4b302b2ce)

- Total Amount Spend on Different Product Lines by Different Genders

![f016e947-d8ca-48ca-8094-030e53cdd1a4](https://github.com/TheMrityunjayPathak/SuperMarketSalesAnalysis/assets/123563634/40cf5aa8-705b-49c3-94a2-9e1ada613654)

- Rating of Different Product Lines by Different Genders

![07944ecc-262b-4c34-9011-28d2fa8730aa](https://github.com/TheMrityunjayPathak/SuperMarketSalesAnalysis/assets/123563634/bb5d3c8e-d440-4675-92d6-ff40d7df678e)

- Gross Income from Different Product Lines in Different Cities

![download](https://github.com/TheMrityunjayPathak/SuperMarketSalesAnalysis/assets/123563634/2a1a88fe-38c5-44e0-a73c-d12f62787de4)

- Total Sale on Each Day for All Months

![download](https://github.com/TheMrityunjayPathak/SuperMarketSalesAnalysis/assets/123563634/a6a72f27-d5a4-4a28-ac85-ce501fd68ad3)

- Rating of Different Products in Each Month

![download](https://github.com/TheMrityunjayPathak/SuperMarketSalesAnalysis/assets/123563634/05f98763-f7f1-4e75-976f-0902f4b79103)

- Taxes on Different Product Lines

![download](https://github.com/TheMrityunjayPathak/SuperMarketSalesAnalysis/assets/123563634/9a8e2178-0468-4ad6-b249-1889480dbddf)

- Number of Products bought by Different Genders from Different Product Lines

![download](https://github.com/TheMrityunjayPathak/SuperMarketSalesAnalysis/assets/123563634/6d6152fe-f3c4-496d-8aa7-0fab163d9179)

- Total Gross Income from Different Branches by Different Genders

![download](https://github.com/TheMrityunjayPathak/SuperMarketSalesAnalysis/assets/123563634/8f22c567-caa7-46eb-b38e-d21fa3ea488a)

## Conclusion

- In conclusion, Super Market Sales Project revealed valuable insights into customer purchasing behavior and product performance, providing opportunities for data-driven strategies to enhance profitability and customer satisfaction.

## Link to the Notebook
