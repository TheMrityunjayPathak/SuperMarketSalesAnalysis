# Importing Libraries
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Light Mode
st.markdown(
    """
    <style>
        %s
    </style>
    """ % open("style.css").read(),
    unsafe_allow_html=True
)

# Page Configuration 
st.set_page_config(page_title="Exploratory Data Analysis",page_icon="🔍",layout="centered")

# Title and Sub-Title
st.markdown("<div style='background-color:#219C90; border-radius:50px;'><h1 style='text-align:center; color:white;'>Exploratory Data Analysis</h1></div>",unsafe_allow_html=True)

st.markdown("<h3 style='text-align:center; color:black;'>Super Market Sales Analysis</h3>",unsafe_allow_html=True)

# Image of Super Market
st.image("super-market.jpg",use_column_width=True)

# Data Pre-Processing 
df1 = pd.read_csv("super-market.csv")

df2 = df1.drop("Invoice ID",axis=1)

df2['Date'] = pd.to_datetime(df2['Date'])

df2['Year'] = df2['Date'].dt.year # Extracting Year from Date

df2['Month'] = df2['Date'].dt.month # Extracting Month from Date

df2['Day'] = df2['Date'].dt.day # Extracting Day from Date

# Problem Statement 
st.header("Problem Statement")

st.write("- The objective of this project is to analyze sales data to gain insights into customer purchasing behavior, product performance, and overall trends, of the supermarket business.")

data = st.toggle(label="Show Data")

if data:
    st.dataframe(df1,hide_index=True)

# Resources Link
st.header("Links to the Resources")

st.markdown("- [Link to the Dataset](https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales)")

st.markdown("- [Link to the Notebook](https://www.kaggle.com/code/themrityunjaypathak/super-market-sales-analysis)")

# About the Data Section
st.header("About the Data")

params = st.selectbox(label="Select any Parameter",options=["Shape","Columns","Description"],index=None)

if params == None:
    st.write("Please select an Option...")
elif params == "Shape":
    st.write("Shape of the Dataset :",df2.shape)
elif params == "Columns":
    st.write("Columns in the Dataset :")
    st.dataframe(df2.columns,use_container_width=True,hide_index=True)
else:
    st.write("Description of the Dataset :")
    st.dataframe(df1.describe(),use_container_width=True)

# Null Values and DataType of Columns
st.header("Null Values and DataType of Columns")

col_dtype_nulls = st.selectbox(label="Select any Column",options=df2.columns,index=None,placeholder="Pleaes select a Column...")

if col_dtype_nulls == None:
    st.write("Please select a Column...")
elif col_dtype_nulls == "Invoice ID":
    st.write(f"DataType of **{col_dtype_nulls}** Column is",df2[col_dtype_nulls].dtype)
    st.write(f"Null Values in **{col_dtype_nulls}** Column is",df2[col_dtype_nulls].isna().sum())
elif col_dtype_nulls == "Branch":
    st.write(f"DataType of **{col_dtype_nulls}** Column is",df2[col_dtype_nulls].dtype)
    st.write(f"Null Values in **{col_dtype_nulls}** Column is",df2[col_dtype_nulls].isna().sum())
elif col_dtype_nulls == "City":
    st.write(f"DataType of **{col_dtype_nulls}** Column is",df2[col_dtype_nulls].dtype)
    st.write(f"Null Values in **{col_dtype_nulls}** Column is",df2[col_dtype_nulls].isna().sum())
elif col_dtype_nulls == "Customer type":
    st.write(f"DataType of **{col_dtype_nulls}** Column is",df2[col_dtype_nulls].dtype)
    st.write(f"Null Values in **{col_dtype_nulls}** Column is",df2[col_dtype_nulls].isna().sum())
elif col_dtype_nulls == "Gender":
    st.write(f"DataType of **{col_dtype_nulls}** Column is",df2[col_dtype_nulls].dtype)
    st.write(f"Null Values in **{col_dtype_nulls}** Column is",df2[col_dtype_nulls].isna().sum())
elif col_dtype_nulls == "Product line":
    st.write(f"DataType of **{col_dtype_nulls}** Column is",df2[col_dtype_nulls].dtype)
    st.write(f"Null Values in **{col_dtype_nulls}** Column is",df2[col_dtype_nulls].isna().sum())
elif col_dtype_nulls == "Unit price":
    st.write(f"DataType of **{col_dtype_nulls}** Column is",df2[col_dtype_nulls].dtype)
    st.write(f"Null Values in **{col_dtype_nulls}** Column is",df2[col_dtype_nulls].isna().sum())
elif col_dtype_nulls == "Quantity":
    st.write(f"DataType of **{col_dtype_nulls}** Column is",df2[col_dtype_nulls].dtype)
    st.write(f"Null Values in **{col_dtype_nulls}** Column is",df2[col_dtype_nulls].isna().sum())
elif col_dtype_nulls == "Tax 5%":
    st.write(f"DataType of **{col_dtype_nulls}** Column is",df2[col_dtype_nulls].dtype)
    st.write(f"Null Values in **{col_dtype_nulls}** Column is",df2[col_dtype_nulls].isna().sum())
elif col_dtype_nulls == "Total":
    st.write(f"DataType of **{col_dtype_nulls}** Column is",df2[col_dtype_nulls].dtype)
    st.write(f"Null Values in **{col_dtype_nulls}** Column is",df2[col_dtype_nulls].isna().sum())
elif col_dtype_nulls == "Date":
    st.write(f"DataType of **{col_dtype_nulls}** Column is",df2[col_dtype_nulls].dtype)
    st.write(f"Null Values in **{col_dtype_nulls}** Column is",df2[col_dtype_nulls].isna().sum())
elif col_dtype_nulls == "Time":
    st.write(f"DataType of **{col_dtype_nulls}** Column is",df2[col_dtype_nulls].dtype)
    st.write(f"Null Values in **{col_dtype_nulls}** Column is",df2[col_dtype_nulls].isna().sum())
elif col_dtype_nulls == "Payment":
    st.write(f"DataType of **{col_dtype_nulls}** Column is",df2[col_dtype_nulls].dtype)
    st.write(f"Null Values in **{col_dtype_nulls}** Column is",df2[col_dtype_nulls].isna().sum())
elif col_dtype_nulls == "cogs":
    st.write(f"DataType of **{col_dtype_nulls}** Column is",df2[col_dtype_nulls].dtype)
    st.write(f"Null Values in **{col_dtype_nulls}** Column is",df2[col_dtype_nulls].isna().sum())
elif col_dtype_nulls == "gross margin percentage":
    st.write(f"DataType of **{col_dtype_nulls}** Column is",df2[col_dtype_nulls].dtype)
    st.write(f"Null Values in **{col_dtype_nulls}** Column is",df2[col_dtype_nulls].isna().sum())
elif col_dtype_nulls == "gross income":
    st.write(f"DataType of **{col_dtype_nulls}** Column is",df2[col_dtype_nulls].dtype)
    st.write(f"Null Values in **{col_dtype_nulls}** Column is",df2[col_dtype_nulls].isna().sum())
else:
    st.write(f"DataType of **{col_dtype_nulls}** Column is",df2[col_dtype_nulls].dtype)
    st.write(f"Null Values in **{col_dtype_nulls}** Column is",df2[col_dtype_nulls].isna().sum())

# Examine Categorical Columns
st.header("Examine Categorical Columns")

cat_col = st.selectbox(label="Select any Categorical Column",options=["Branch","City","Customer type","Gender","Payment","Product line","Quantity"],index=None)

if cat_col == None:
    st.write("Please select a Column...")
elif cat_col == "Branch":
    st.write(f"Count of every unique value in **{cat_col}** column ↓")
    st.dataframe(df2[cat_col].value_counts(),use_container_width=True)
elif cat_col == "City":
    st.write(f"Count of every unique value in **{cat_col}** column ↓")
    st.dataframe(df2[cat_col].value_counts(),use_container_width=True)
elif cat_col == "Customer type":
    st.write(f"Count of every unique value in **{cat_col}** column ↓")
    st.dataframe(df2[cat_col].value_counts(),use_container_width=True)
elif cat_col == "Gender":
    st.write(f"Count of every unique value in **{cat_col}** column ↓")
    st.dataframe(df2[cat_col].value_counts(),use_container_width=True)
elif cat_col == "Payment":
    st.write(f"Count of every unique value in **{cat_col}** column ↓")
    st.dataframe(df2[cat_col].value_counts(),use_container_width=True)
elif cat_col == "Product line":
    st.write(f"Count of every unique value in **{cat_col}** column ↓")
    st.dataframe(df2[cat_col].value_counts(),use_container_width=True)
else:
    st.write(f"Count of every unique value in **{cat_col}** column ↓")
    st.dataframe(df2[cat_col].value_counts(),use_container_width=True)

# Data Visualization 
st.header("Data Visualization")

data_col = st.selectbox(label="Select any Chart Type",options=["Distribution Plot","Bar Chart","Line Plot","Count Plot"],index=None)

if data_col == None:
    st.write("Please select any Chart Type...")
elif data_col == "Bar Chart":
    select_bar_one = st.checkbox(label="Gross Income from Different Product Lines in Different Cities")
    if select_bar_one:
        sns.set_style('darkgrid')
        fig, ax = plt.subplots()
        ax = sns.barplot(x=df2['Product line'],y=df2['gross income'],data=df2,hue=df2['City'])
        ax.set_xticklabels(ax.get_xticklabels(),rotation=90)
        plt.xlabel('Product Line')
        plt.title('Gross Income from Different Product Lines in Different Cities')
        plt.legend(title='Cities',loc='upper right')
        st.pyplot(fig)
    
    select_bar_two = st.checkbox(label="Taxes on Different Product Lines")
    if select_bar_two:
        fig, ax = plt.subplots()
        sns.set_style('darkgrid')
        ax = sns.barplot(x=df2['Product line'],data=df2,y=df2['Tax 5%'])
        ax.set_xticklabels(ax.get_xticklabels(),rotation=90)
        plt.title('Taxes on Different Product Lines')
        st.pyplot(fig)
        
    select_bar_three = st.checkbox(label="Total Gross Income from Different Branches by Different Genders")
    if select_bar_three:
        sns.set_style('darkgrid')
        fig, ax = plt.subplots()
        ax = sns.barplot(x=df2['Branch'],y=df2['gross income'],data=df2,hue=df2['Gender'])
        plt.title('Total Gross Income from Different Branches by Different Genders')
        plt.legend(title='Gender',loc='upper right')
        st.pyplot(fig)
elif data_col == "Distribution Plot":
    select_dist_one = st.checkbox(label="Subplots of Distribution of Unit Price, Ratings and Gross Income")
    if select_dist_one:
        sns.set_style('darkgrid')
        fig, ax = plt.subplots(1, 3, figsize=(12,5)) 
        sns.histplot(data=df2['Rating'],kde=True,ax=ax[0])
        ax[0].set_title('Distribution of Rating of Products')
        sns.histplot(data=df2['Unit price'],kde=True,ax=ax[1])
        ax[1].set_title('Distribution of Unit Price of Products')
        sns.histplot(data=df2['gross income'],kde=True,ax=ax[2])
        ax[2].set_title('Distribution of Gross Income from Sales')
        fig.tight_layout()
        st.pyplot(fig)
elif data_col == "Line Plot":
    select_line_one = st.checkbox(label="Per Unit Price of Each Product Lines")
    if select_line_one:
        sns.set_style('darkgrid')
        fig, ax = plt.subplots()
        ax = sns.lineplot(x=df2['Product line'],y=df2['Unit price'],data=df2)
        ax.set_xticklabels(ax.get_xticklabels(),rotation=90)
        plt.xlabel('Product Line')
        plt.title('Per Unit Price of Each Product Lines')
        st.pyplot(fig)

    select_line_two = st.checkbox(label="Quantity of Products Sold from Each Product Line")
    if select_line_two:
        sns.set_style('darkgrid')
        fig, ax = plt.subplots()
        ax = sns.lineplot(x=df2['Product line'],y=df2['Quantity'],data=df2)
        ax.set_xticklabels(ax.get_xticklabels(),rotation=90)
        plt.title('Quantity of Products Sold from Each Product Line')
        st.pyplot(fig)

    select_line_three = st.checkbox(label="Total Amount Spend on Different Product Lines by Different Genders")
    if select_line_three:
        sns.set_style('darkgrid')
        fig, ax = plt.subplots()
        ax = sns.lineplot(x=df2['Product line'],y=df2['Total'],data=df2,hue=df2['Gender'],err_style=None)
        ax.set_xticklabels(ax.get_xticklabels(),rotation=90)
        plt.title('Total Amount Spend on Different Product Lines by Different Genders')
        plt.legend(title='Gender',loc='upper right')
        st.pyplot(fig)

    select_line_four = st.checkbox(label="Rating of Different Product Lines by Different Genders")
    if select_line_four:
        sns.set_style('darkgrid')
        fig, ax = plt.subplots()
        ax = sns.lineplot(x=df2['Product line'],y=df2['Rating'],data=df2,hue=df2['Gender'],err_style=None)
        ax.set_xticklabels(ax.get_xticklabels(),rotation=90)
        plt.xlabel('Product Line')
        plt.title('Rating of Different Product Lines by Different Genders')
        plt.legend(title='Gender',loc='upper right')
        st.pyplot(fig)

    select_line_five = st.checkbox(label="Total Sale on Each Day for All Months")
    if select_line_five:
        sns.set_style('darkgrid')
        fig, ax = plt.subplots()
        ax = sns.lineplot(x=df2['Day'],y=df2['Total'],hue=df2['Month'],err_style=None,palette='crest')
        plt.legend(title='Month',loc='upper right')
        plt.title('Total Sale on Each Day for All Months')
        st.pyplot(fig)

    select_line_six = st.checkbox(label="Number of Products bought by Different Genders from Different Product Lines")
    if select_line_six:
        sns.set_style('darkgrid')
        fig, ax = plt.subplots()
        ax = sns.lineplot(x=df2['Product line'],y=df2['Quantity'],data=df2,hue=df2['Gender'],err_style=None)
        ax.set_xticklabels(ax.get_xticklabels(),rotation=90)
        plt.title('Number of Products bought by Different Genders from Different Product Lines')
        plt.legend(title='Gender',loc='upper right')
        st.pyplot(fig)

else:
    select_count_one = st.checkbox(label="Count of Different Types of Customers from Different Cities")
    if select_count_one:
        sns.set_style('darkgrid')
        fig, ax = plt.subplots()
        ax = sns.countplot(x=df2['Customer type'],data=df2,hue=df2['City'])
        plt.xlabel('Customer Type')
        plt.title('Count of Different Types of Customers from Different Cities')
        plt.legend(title='City',loc='upper right')
        st.pyplot(fig)

    select_count_two = st.checkbox(label="Count of Different Types of Products in Super Market")
    if select_count_two:
        sns.set_style('darkgrid')
        fig, ax = plt.subplots()
        ax = sns.countplot(x=df2['Product line'],data=df2,order=df2['Product line'].value_counts().index)
        ax.set_xticklabels(ax.get_xticklabels(),rotation=90)
        plt.xlabel('Product Line')
        plt.title('Count of Different Types of Products in Super Market')
        st.pyplot(fig)

    select_count_three = st.checkbox(label="Count of Different Gender Visitors at Different Branches")
    if select_count_three:
        sns.set_style('darkgrid')
        fig, ax = plt.subplots()
        ax = sns.countplot(x=df2['Gender'],data=df2,hue=df2['Branch'])
        plt.xlabel('Gender')
        plt.title('Count of Different Gender Visitors at Different Branches')
        plt.legend(title='Branch',loc='upper right')
        st.pyplot(fig)

    select_count_four = st.checkbox(label="Count of Different Types of Payment Methods used by Different Genders")
    if select_count_four:
        sns.set_style('darkgrid')
        fig, ax = plt.subplots()
        ax = sns.countplot(x=df2['Payment'],data=df2,hue=df2['Gender'])
        plt.xlabel('Payment')
        plt.title('Count of Different Types of Payment Methods used by Different Genders')
        plt.legend(title='Gender',loc='upper right')
        st.pyplot(fig)

    select_count_five = st.checkbox(label="Count of Different Gender Visitors from Different Cities")
    if select_count_five:
        sns.set_style('darkgrid')
        fig, ax = plt.subplots()
        ax = sns.countplot(x=df2['City'],data=df2,order=df2['City'].value_counts().index,hue=df2['Gender'])
        plt.xlabel('City')
        plt.title('Count of Different Gender Visitors from Different Cities')
        plt.legend(title='Gender',loc='upper right')
        st.pyplot(fig)

    select_count_six = st.checkbox(label="Different Payment Methods Used by Different Cities")
    if select_count_six:
        sns.set_style('darkgrid')
        fig, ax = plt.subplots()
        ax = sns.countplot(x=df2['City'],data=df2,hue=df2['Payment'])
        plt.legend(title='Payment Method',loc='upper right')
        plt.title('Different Payment Methods Used by Different Cities')
        st.pyplot(fig)

# Footer Section
st.write("")
st.markdown("<h3 style='text-align:center; color:black;'>Thanks 👏 for Visiting!</h3>",unsafe_allow_html=True)
