import streamlit as st
import pandas as pd
import numpy as np


st.header("2024 AHI 507 Streamlit Example")
st.subheader("We are going to go through a couple different examples of loading and visualization information into this dashboard")

st.text("""In this streamlit dashboard, we are going to focus on some recently released school learning modalities data from the NCES, for the years of 2021.""")

## https://healthdata.gov/National/School-Learning-Modalities-2020-2021/a8v3-a3m3/about_data
df = pd.read_csv("https://healthdata.gov/resource/a8v3-a3m3.csv?$limit=50000") ## first 1k 

## data cleaning 
df['week_recoded'] = pd.to_datetime(df['week'])
df['zip_code'] = df['zip_code'].astype(str)

df['week'].value_counts()

## box to show how many rows and columns of data we have: 
col1, col2, col3 = st.columns(3)
col1.metric("Columns", df.shape[1]) 
col2.metric("Rows", len(df))
col3.metric("Number of unique districts/schools:", df['district_name'].nunique())

## exposing first 1k of NCES 20-21 data
st.dataframe(df)



table = pd.pivot_table(df, values='student_count', index=['week'],
                       columns=['learning_modality'], aggfunc="sum")

table = table.reset_index()
table.columns

## bar chart by week 
st.bar_chart(
    table,
    x="week",
    y="Hybrid",
)

st.bar_chart(
    table,
    x="week",
    y="In Person",
)

st.bar_chart(
    table,
    x="week",
    y="Remote",
)

st.header("*********************************************")

st.header("Enhanced Streamlit Dashboards")

## widget 1 for link to original dataset in button form
st.page_link("https://healthdata.gov/National/School-Learning-Modalities-2020-2021/a8v3-a3m3/about_data", label="Original Dataset", icon="🏫")


## area chart for learning modalities

st.subheader("Data for AL")
short_frame = df.head(134)
st.dataframe(df.head (134))

st.subheader("Trends in Learning Modalities Over Time")
st.line_chart(
    df,
    x="week",
    y="learning_modality",
    width= 400,
    height= 500,
    color=["#0000FF"]
)
st.text("""This chart is to show how the proportion of in-person, remote, and hybrid learning modalities changed week by week throughout the school year.""")


## map chart by zipcode

st.subheader("Operational Schools by Zip Code in Alabama")
st.map(
    short_frame,

)
st.text("""To visualize how the distribution of operational schools varied by zip code. 
This could show if urban or rural areas had more operational schools during a given period """)


## line chart

st.subheader("Operational Schools and Student Count Over Time")
st.line_chart(
    df,
    x="week",
    y="operational_schools", 

)
st.text("""To see if there is a correlation between the number of schools open and the number of students attending
 You might observe a drop in student count in certain weeks (possibly due to shifts to remote learning or other disruptions).""")

## widget 2 to rate visualizations
st.text("""Rate these data visualizations!""")
sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")

