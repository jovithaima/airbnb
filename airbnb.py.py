# -*- coding: utf-8 -*-
"""Untitled23.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1k866WJ3TcfD4XL5i7qqWE2xjBhva-4X1
"""

import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import warnings
from streamlit_extras.dataframe_explorer import dataframe_explorer
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#:PAGE STEPUP:
warnings.filterwarnings('ignore')
#warnings.filterwarnings('ignore')

st.set_page_config(page_title="AIRBNB.Inc DATA ANALYSIS",
                   layout="wide",
@@ -40,13 +40,37 @@
selected
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#:HOME:
df=pd.read_csv("D:\DTM9\CAP-4\Airbnb_data_analysis\AirBnB01.csv")
@st.cache_resource
def df_airbnb():
    df=pd.read_csv("D:\DTM9\CAP-4\Airbnb_data_analysis\AirBnB01.csv")
    return df

df=df_airbnb()

#Hide the streamlit hambuger Icon,footer note and header
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

if selected=="Home":
    st.subheader(":red[AIRBNB.Inc Data Analysis]")
    st.write("---")

    st.write("### Airbnb In Different Countries")
    df=df.rename(columns={"lati":"lat","longi":"lon"})
    st.map(df)
    st.write("---")

    st.write("### Explore the Airbnb dataset")
    ex=pd.read_csv("D:\DTM9\CAP-4\Airbnb_data_analysis\AirBnB01.csv")
    ex=ex[['host_name','Country','Room_type','Property_type','price','Minimum_nights','maximum_nights','cancellation_policy','bedrooms']]
    ft_df=dataframe_explorer(ex)
    st.dataframe(ft_df,use_container_width=True)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#:Data Exploration:
if selected=="Data Exploration":
@@ -90,28 +114,71 @@
        fig.update_layout(width=500,height=450)
        st.plotly_chart(fig)

    price_Df=df3.groupby(['Country','Property_type','Room_type']).price.mean()
    price_Df=price_Df.reset_index()
    price_Df=price_Df.sort_values('price',ascending=False)
    p=price_Df.sort_values(by='price')
    fig=px.bar(p,x='price',y='Country',title='Average Price distribution in Room type and Corresponding Countries',
            color='Room_type')
    st.plotly_chart(fig)

    on=st.toggle("Average Price for Room_type and Property_type & Corresponding Countries")
    if on:
        price_Df=df3.groupby(['Country','Property_type','Room_type']).price.mean()
        price_Df=price_Df.reset_index()
        price_Df=price_Df.sort_values('price',ascending=False)
        fig=px.bar(price_Df,x='price',y='Country',title='Average Price distribution in Room type and Corresponding Countries',
            color='Room_type')
    cl4,cl5=st.columns([1,1])
    with cl4:
        Roomdf=df3.groupby('Property_type').Id.count()
        Roomdf=Roomdf.reset_index()
        Roomdf=Roomdf.rename(columns={'Id':'Total_listed'})
        fig=px.bar(Roomdf,x="Total_listed",y="Property_type",title="Property_type Distribution",color_discrete_sequence=px.colors.sequential.Blackbody_r)
        fig.update_layout(width=600,height=450)
        st.plotly_chart(fig)

        fig=px.bar(price_Df,x='Property_type',y='price',title='Average Price distribution in Property type and Corresponding Countries',
            color='Country')
        fig.update_layout(width=900,height=600)
    with cl5:
        cal_df=df3.groupby('cancellation_policy').Id.count()
        cal_df=cal_df.reset_index()
        cal_df=cal_df.rename(columns={'Id':'Total_listed'})
        label=cal_df['cancellation_policy']
        values=cal_df['Total_listed']
        fig=go.Figure(data=[go.Pie(labels=label,values=values,hole=.5,title="Cancellation_policy Distribution")])
        fig.update_layout(width=600,height=450)
        st.plotly_chart(fig)


    st.markdown("##")
    tab1,tab2=st.tabs(["**Price Analysis**","**Host Analysis By Review**"])
    with tab1:
        on=st.toggle("Pricing Analysis")
        if on:
            #Average Price by Room Type
            price_Df=df3.groupby(['Country','Property_type','Room_type']).price.mean()
            price_Df=price_Df.reset_index()
            price_Df=price_Df.sort_values('price',ascending=False)
            fig=px.bar(price_Df,x='price',y='Country',title='Average Price distribution in Room type and Corresponding Countries',
                color='Room_type')
            st.plotly_chart(fig)

            #Average Price by Property Type
            fig=px.bar(price_Df,x='Property_type',y='price',title='Average Price distribution in Property type and Corresponding Countries',
                color='Country')
            fig.update_layout(width=900,height=600)
            st.plotly_chart(fig)

            #Pricing has High Number of Reviews
            price_review=df3[['Review_scores','price',"host_name"]].sort_values(by='price')
            fig=px.scatter(price_review,x='price',y='Review_scores',color='host_name',title='Price Distribution by Review Score')
            st.plotly_chart(fig)

            #Pricing has High Number of Reviews
            price_review=df3[['number_of_reviews','price',"host_name"]].sort_values(by='price')
            fig=px.scatter(price_review,x='price',y='number_of_reviews',color='host_name',title='Price Distribution by Number of Review ')
            st.plotly_chart(fig)

    with tab2:
        on=st.toggle("Host Analysis")
        if on:
            #Review Scores by Host and Country
            re_sc=df3[['host_name','Review_scores','Country']]
            review_sc=re_sc.sort_values('Review_scores',ascending=False)
            fig = px.scatter(review_sc, x='Review_scores', y='host_name', color='Country', title='Review Scores by Host and Country',
                            labels={'Review_scores': 'Review Scores'})
            fig.update_layout(xaxis=dict(tickangle=45))
            st.plotly_chart(fig)

            #Review Scores by Host number of review and Country
            re_100=df3[['host_name','number_of_reviews','Country']]
            review_100=re_100.sort_values('number_of_reviews',ascending=False)
            review_100=review_100[review_100['number_of_reviews']>=250].sort_values('number_of_reviews',ascending=False)
            fig=px.bar(review_100,x='number_of_reviews',y='host_name',color='Country',title="High Number(>250) of Reviews by Host and Country")
            st.plotly_chart(fig)

    st.write("#### Geo-Visualization")
    fig = px.scatter_mapbox(df3, lat='lati', lon='longi', color='price', size='accommodates',
                            color_continuous_scale=px.colors.cyclical.Edge_r,hover_name='Name', mapbox_style="carto-positron", zoom=0)