import koreanize_matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns
import streamlit as st

st.set_page_config(
    page_title="Likelion AI School 자동차 연비 App",
    page_icon="🚗",
    layout="wide",
)

st.markdown("# 자동차 연비 🚗")
st.sidebar.markdown("# 자동차 연비 🚗")

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv"

@st.cache
def load_data(url):
    data = pd.read_csv(url)
    return data

data_load_state = st.text('Loading data...')
data = load_data(url)
data_load_state.text("Done! (using st.cache)")

st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year',
    list(reversed(range(data.model_year.min(), data.model_year.max())))
    )

if selected_year > 0 :
    data = data[data.model_year == selected_year]

sorted_unique_origin = sorted(data.origin.unique())
selected_origin = st.sidebar.multiselect('origin', sorted_unique_origin, sorted_unique_origin)

if len(selected_origin) > 0:
    data = data[data.origin.isin(selected_origin)]

st.dataframe(data)

st.line_chart(data["mpg"])

st.bar_chart(data["mpg"])

pxh = px.histogram(data, x="origin")
st.plotly_chart(pxh)

fig, ax = plt.subplots(figsize=(10, 3))
sns.boxenplot(data=data, x="origin", y="mpg").set_title("지역별 MPG")
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(10, 3))
sns.countplot(data=data, x="origin").set_title("지역별 자동차 연비 데이터 수")
st.pyplot(fig)
