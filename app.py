import streamlit
import streamlit as st
import pandas as pd
import  seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import jinja2  as jin
import folium
import numpy as np
from streamlit_folium import folium_static
import plotly.figure_factory as ff
from numerize import numerize



#df = pd.read_excel('C:/Users/Pal/WHO Covid-19-global dataset.xlsx')

#data1=df.dropna()

#data1.rename(columns={"Name":"Countries_Name"},inplace =True)

data1=pd.read_excel('C:/Users/Pal/New_Data.xlsx')
#data1.drop(("Unnamed: 0"), axis=1, inplace=True)
st.sidebar.title("World Covid -19 Cases Data Analysis")

st.sidebar.image('https://voxeu.org/sites/default/files/cover_images/blog_review/AdobeStock_376071772.jpeg')

streamlit.title("World Covid -19 Report ")

Menu =st.sidebar.radio(" Select the given option ",
                       ("Overall Analysis", "Continents_Base_Analysis","Country_Wise_Statisic","World_Map",
                        "Country_Map")
                       )

if Menu=="Overall Analysis":
    #Total_Cases = data1["Cases - cumulative total"].sum()
    Case=numerize.numerize(203294406)

    #Total_Deaths = data1["Deaths - cumulative total"].sum()
    Deaths=numerize.numerize(4303502)
    #Total_new_case_in_7_day = data1["Cases - newly reported in last 7 days"].sum()
    c=numerize.numerize(4337573)

    st.header(" World Covid-19 main statisic ")
    col1, col2,col3=st.columns(3)
    with col1:
        st.header("Total_Cases")
        st.title(Case)

    with col2:
        st.header("Total_Deaths")
        st.title(Deaths)

    with col3:
        st.header("New_Case_in_7_day")
        st.title(c)


    fig, ax = plt.subplots(figsize=(15, 15))
    st.header(" Overall Covid- 19 Situation in the World")

    fig = px.treemap(data1, path=["WHO Region"], values='Cases - cumulative total', color_continuous_scale='rdpu'
                     , color='Cases - cumulative total', title=" Covid-19 Case details with Contients_Name")
    fig.update_layout(width=900, height=600)

    st.plotly_chart(fig)

    fig, ax = plt.subplots(figsize=(15, 15))
    fig = px.pie(data1, values='Cases - cumulative total', names='WHO Region',
                 title="Distribution of Cases Percentage in Continents")
    fig.update_layout(width=800, height=600)

    st.plotly_chart(fig)

    fig = px.treemap(data1, path=["WHO Region"], values='Deaths - cumulative total', color_continuous_scale='reds'
                     , color='Deaths - cumulative total', title=" Covid-19 Deaths details with Contients_Name ")

    fig.update_layout(width=900, height=600)

    st.plotly_chart(fig)

    fig, ax = plt.subplots(figsize=(15, 15))
    fig = px.pie(data1, values='Deaths - cumulative total', names='WHO Region',
                 title="Distribution of Deaths Percentage  in Continents")
    fig.update_layout(width=800, height=500)
    st.plotly_chart(fig)



    Top10_Cases = data1.sort_values(by="Cases - cumulative total", ascending=False).head(10)

    fig= px.bar(Top10_Cases, x=Top10_Cases["Countries_Name"], y=Top10_Cases["Cases - cumulative total"],
           title="Top 10 Nations in the world with highest number of Covid-19 Cases")
    fig.update_layout(width=1000, height=600)
    st.plotly_chart(fig)

    Top10_deaths = data1.sort_values(by="Deaths - cumulative total", ascending=False).head(10)

    fig=px.bar(Top10_deaths,x=Top10_deaths["Countries_Name"],y=Top10_deaths["Deaths - cumulative total"],
               title="Top 10 Nations in the world highest number of Deaths with Covid-19")
    fig.update_layout(width=1000, height=600)
    st.plotly_chart(fig)




    #st.dataframe(data1)


if Menu=="Continents_Base_Analysis":
    def Select_cont(data1):
        Contients = data1["WHO Region"].unique()
        Contients.tolist()
        return Contients


    Contients= Select_cont(data1)
    Contients_Select= st.sidebar.selectbox("Select the Contient", Contients)


    def data_cont(data1, Contients):

        if Contients == "Americas":
            st.header("Covid-19 Report of: Americas")
            data_sort = data1[data1["WHO Region"] == "Americas"]
            st.dataframe(data_sort)

            parameter = ["Cases - cumulative total", "Deaths - cumulative total",
                         "Cases - cumulative total per 100000 population"
                , "Deaths - cumulative total per 100000 population"]
            fig = parameter.sort()
            for i in parameter:
                fig, ax = plt.subplots(figsize=(15, 15))
                data_sort1 = data_sort.sort_values(by=i, ascending=False).head(10)
                fig = px.bar(data_sort1, x=data_sort1['Countries_Name'], y=data_sort1[i], color=data_sort1[i],
                             log_y=True,title=" Top 10 Americas Countries Vs "+ ""+ i)
                fig.update_layout(width=1000, height=600)
                st.plotly_chart(fig)

        if Contients == "South-East Asia":
            st.header("Covid-19 Report of: South-East Asia")
            data_sort = data1[data1["WHO Region"] == "South-East Asia"]
            st.dataframe(data_sort)
            parameter = ["Cases - cumulative total", "Deaths - cumulative total",
                         "Cases - cumulative total per 100000 population"
                , "Deaths - cumulative total per 100000 population"]
            fig = parameter.sort()
            for i in parameter:
                data_sort1 = data_sort.sort_values(by=i, ascending=False).head(10)
                fig = px.bar(data_sort1, x=data_sort1['Countries_Name'], y=data_sort1[i], color=data_sort1[i],
                             log_y=True,title=" Top 10 South-East Asia Countries Vs"+  ""+ i)
                fig.update_layout(width=1000, height=600)
                st.plotly_chart(fig)

        if Contients == "Europe":
            st.header("Covid-19 Report of: Europe")
            data_sort = data1[data1["WHO Region"] == "Europe"]
            st.dataframe(data_sort)
            parameter = ["Cases - cumulative total", "Deaths - cumulative total",
                         "Cases - cumulative total per 100000 population"
                , "Deaths - cumulative total per 100000 population"]
            fig = parameter.sort()
            for i in parameter:
                data_sort1 = data_sort.sort_values(by=i, ascending=False).head(10)
                fig = px.bar(data_sort1, x=data_sort1['Countries_Name'], y=data_sort1[i], color=data_sort1[i],
                             log_y=True,title="Top 10 Europe Countries Vs"+  ""+ i)
                fig.update_layout(width=1000, height=600)
                st.plotly_chart(fig)

        if Contients == "Eastern Mediterranean":
            st.header("Covid-19 Report of: Eastern Mediterranean")
            data_sort = data1[data1["WHO Region"] == "Eastern Mediterranean"]
            st.dataframe(data_sort)
            parameter = ["Cases - cumulative total", "Deaths - cumulative total",
                         "Cases - cumulative total per 100000 population"
                , "Deaths - cumulative total per 100000 population"]
            fig = parameter.sort()
            for i in parameter:
                data_sort1 = data_sort.sort_values(by=i, ascending=False).head(10)
                fig = px.bar(data_sort1, x=data_sort1['Countries_Name'], y=data_sort1[i], color=data_sort1[i],
                             log_y=True,title="Top 10 Eastern Mediterranean Countries Vs"+  ""+ i)
                fig.update_layout(width=1000, height=600)
                st.plotly_chart(fig)

        if Contients == "Africa":
            st.header("Covid-19 Report of: Africa")
            data_sort = data1[data1["WHO Region"] == "Africa"]
            st.dataframe(data_sort)
            parameter = ["Cases - cumulative total", "Deaths - cumulative total",
                         "Cases - cumulative total per 100000 population"
                , "Deaths - cumulative total per 100000 population"]
            fig = parameter.sort()
            for i in parameter:
                data_sort1 = data_sort.sort_values(by=i, ascending=False).head(10)
                fig = px.bar(data_sort1, x=data_sort1['Countries_Name'], y=data_sort1[i], color = data_sort1[i],
                             title="Top 10 Africa Countries Vs"+  ""+ i)

                fig.update_layout(width=1000, height=600)
                st.plotly_chart(fig)

        if Contients == "Western Pacific":
            st.header("Covid-19 Report of: Western Pacific")
            data_sort = data1[data1["WHO Region"] == "Western Pacific"]
            st.dataframe(data_sort)
            parameter = ["Cases - cumulative total", "Deaths - cumulative total",
                         "Cases - cumulative total per 100000 population"
                , "Deaths - cumulative total per 100000 population"]
            fig = parameter.sort()
            for i in parameter:
                data_sort1 = data_sort.sort_values(by=i, ascending=False).head(10)
                fig = px.bar(data_sort1, x=data_sort1['Countries_Name'], y=data_sort1[i], color = data_sort1[i],
                             log_y=True,title="Top 10 Western Pacific Countries Vs"+  ""+ i)
                fig.update_layout(width=1000, height=600)
                st.plotly_chart(fig)
        return data_sort1



    conts = data_cont(data1,Contients_Select)

if Menu=="Country_Wise_Statisic":
    def Select_Country(data1):
        Country_name = data1['Countries_Name'].unique().tolist()

        Country_name.sort()
        Country_name.insert(0,"Overall")
        return Country_name


    Country_name = Select_Country(data1)

    selected_country_name=st.sidebar.selectbox("Select the Country",Country_name)


    def Select_Country_data(data1, Country_name):

        if Country_name == "Overall":
            data4 = data1
            st.header(" Overall Covid-19_Report")
            st.dataframe(data4)

        if Country_name != "Overall":
            st.header("Covid-19_report of :")
            st.header( Country_name)

            temp_df = data1[data1["Countries_Name"] == Country_name]

            a = temp_df.iloc[:, 1].values.tolist()
            b = temp_df.iloc[:, 2].values.tolist()
            c = temp_df.iloc[:, 3].values.tolist()
            d = temp_df.iloc[:, 4].values.tolist()
            e = temp_df.iloc[:, 5].values.tolist()
            f = temp_df.iloc[:, 6].values.tolist()
            g = temp_df.iloc[:, 7].values.tolist()
            h = temp_df.iloc[:, 8].values.tolist()
            i = temp_df.iloc[:, 9].values.tolist()
            j = temp_df.iloc[:, 10].values.tolist()
            k = temp_df.iloc[:, 11].values.tolist()
            l = temp_df.iloc[:, 12].values.tolist()

            for m, n, o, p, q, r, s, t, u, v, w, x in zip(a, b, c, d, e, f, g, h, i, j, k, l):
                data_matrix = [['Covid_Details', 'Covid-19_report'],
                               ['Countries_Name', m],
                               ['WHO Region', n],
                               ['Cases - cumulative total', o],
                               ['Cases - cumulative total per 100000 population', p],
                               ['Cases - newly reported in last 7 days', q],
                               ['Cases - newly reported in last 7 days per 100000 population', r],
                               ['Cases - newly reported in last 24 hours', s],
                               ['Deaths - cumulative total', t],
                               ['Deaths - cumulative total per 100000 population', u],
                               ['Deaths - newly reported in last 7 days', v],
                               ['Deaths - newly reported in last 7 days per 100000 population', w],
                               ['Deaths - newly reported in last 24 hours', x],
                               ]
                fig = ff.create_table(data_matrix)

                st.plotly_chart(fig)

            #st.table(data4)

        return ("")


    Country_wise = Select_Country_data(data1,selected_country_name)


if Menu=="World_Map":
    st.header("Covid-19_Cases and Deaths Footprint in the World ")
    fig = px.density_mapbox(data1, lat='latitude', lon='longitude', z=data1['Log_Cases - cumulative total'],
                            radius=6, zoom=1,
                            hover_name="Countries_Name", width=1100, height=600,

                            hover_data=data1[["Deaths - cumulative total", "Cases - cumulative total"]])

    fig.update_layout(mapbox_style="stamen-toner", mapbox_center_lon=180)
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    st.plotly_chart(fig)




if Menu == "Country_Map":
    data1['latitude'] = data1['latitude'].astype(str)
    data1['longitude'] = data1['longitude'].astype(str)

    def Select_Country_1(data1):

        Country_name_1 = data1['Countries_Name'].unique().tolist()
        #Country_name_1 =data1.index
        #Country_name_1.tolist()
        Country_name_1.sort()
        Country_name_1.insert(0,"Overall")
        return Country_name_1


    Country_name_1 = Select_Country_1(data1)

    selected_country_name_1=st.sidebar.selectbox("Select the Country",Country_name_1)


    def Map_select(data1, Country_name_1):
        if Country_name_1 == 'Overall':
            st.header("Overall Covid-19 impact visualization on Globally")
            map = folium.Map(location=[10, -20], zoom_start=2.3, tiles='Stamen Toner')

            for lat, lon, value, name in zip(data1['latitude'], data1['longitude'], data1['Cases - cumulative total'],
                                             data1['Countries_Name']):
                folium.CircleMarker([lat, lon],
                                    radius=10,
                                    popup=('<strong>Country</strong>: ' + str(name).capitalize() + '<br>' +
                                           '<strong>Confirmed Cases</strong>: ' + str(value) + '<br>'),

                                    color='red',

                                    fill_color='red',
                                    fill_opacity=0.7).add_to(map)
            folium_static(map)


            #for (p, q) in data1.iterrows():
                #folium.Marker(location=[q.loc["latitude"], q.loc["longitude"]],
                              #popup=q.loc[["Countries_Name", "Cases - cumulative total"]]
                              #, icon=folium.Icon(color='red', icon='fa-ambulance', prefix='fa', )).add_to(map)
            #folium_static(map)

        if Country_name_1 != 'Overall':
            for cont in data1['Countries_Name']:
                if Country_name_1 == cont:
                    st.header("Country wise visualization and information :")
                    st.header(cont)

                    temp_df = data1[data1['Countries_Name'] == cont]
                    a = temp_df.iloc[:, 1].values.tolist()
                    b = temp_df.iloc[:, 2].values.tolist()
                    c = temp_df.iloc[:, 3].values.tolist()
                    h = temp_df.iloc[:, 8].values.tolist()
                    l = temp_df.iloc[:, 12].values.tolist()
                    m = temp_df.iloc[:, 14].values.tolist()
                    n = temp_df.iloc[:, 15].values.tolist()

                    for i, j in zip(m, n):

                        map = folium.Map(location=[i, j], zoom_start=5, tiles='OpenStreetMap')

                        for o, p, q, r, s, t, u in zip(a, b, c, h, l, m, n):
                            if Country_name_1 == cont:
                                popup = ('<strong>Country</strong>:' + str(
                                    o) + '<br>' + '<strong>WHO Region</strong>:' + str(p)
                                         + '<br>' + '<strong>Confirmed Cases</strong>: ' + str(q) + '<br>' +
                                         '<strong>Confirmed Deaths</strong>:' + str(
                                            r) + '<br>' + '<strong>Deaths reported in last 24 hours</strong>:' + str(
                                            s) + '<br>')

                                folium.Marker(location=[t, u], popup=popup,
                                              icon=folium.Icon(color='red', icon='fa-info', prefix='fa', )).add_to(map)

                    folium_static(map)

                    return data1


    Country_wise_1 = Map_select(data1, selected_country_name_1)
















