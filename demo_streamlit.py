import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("train.csv")

st.title("Trung tâm tin học")
st.header("Data Science")
menu = ["Display Text", "Display Data", "Display Chart", "Display Interactive Widget"]
choice = st.sidebar.selectbox('Menu', menu)
if choice == 'Display Text':
    st.subheader("Hành trang tốt nghiệp Data Science")
    st.text("Khóa học được thiết kế nhằm ôn tập và bổ sung kiến thức cho HV Data Science")
    st.markdown("### Có 5 chủ đề:")
    st.write("""
    - Chủ đề 1
    - Chủ đề 2
    - ...""")
    st.write("### Ngôn ngữ lập trình: Python")
    st.code("st.display_text_function('Nội dung')", language="python")
elif choice == 'Display Data':
    st.write("## Display Data")    
    st.dataframe(data.head(3))
    st.table(data.head(3))
    st.json(data.head(2).to_json())
elif choice == 'Display Chart':
    st.write("## Display Chart")
    count_Pclass = data[['PassengerId', 'Pclass']].groupby(['Pclass']).count()
    st.bar_chart(count_Pclass)
    fig, ax = plt.subplots()
    ax = sns.boxplot(x='Pclass', y='Fare', data=data)
    st.pyplot(fig)
else:
    st.write("## Display Interactive Widget")
    st.write("### Input your information")
    name = st.text_input("Name:")    
    sex = st.radio("Sex", options=['Male', 'Female'])    
    age = st.slider("Age", 1, 100,1)
    jobtime = st.selectbox("You have", options=['Part time job' , 'Full time job'])
    hobbies = st.multiselect("Hobbies", options=["Cooking", "Reading", "Writing", "Travel", "Others"])
    house = st.checkbox("Have house/ apartment")
    submit = st.button("Submit")
    if submit:
        st.write("#### Your Information:")
        st.write("Name:", name, 
        "- Sex:", sex, 
        "- Age:", age, 
        " - You have a", jobtime,
        "and a house/apartmnet" if house else "",
        "- Hobbies:", ', '.join(map(str, hobbies)))




# # Using menu
# menu = ["Home", "HTDS"]
# choice = st.sidebar.selectbox('Menu', menu)
# if choice == 'Home':    
#     st.subheader("[Trang chủ](https://csc.edu.vn)")  
# elif choice == 'HTDS':    
#     st.subheader("[Hành trang TN Data Science](https://csc.edu.vn/data-science-machine-learning/Hanh-trang-tot-nghiep-Data-Science_224)")
#     st.write("""### Có 5 chủ đề trong khóa học:
#     - Topic 1: Thu thập dữ liệu
#     - Topic 2: Trực quan hóa dữ liệu
#     - ...""")
