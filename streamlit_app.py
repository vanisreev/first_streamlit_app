import streamlit
streamlit.title('My Parents New Healthy Diner, yummy!')
streamlit.header("Menu😊")
streamlit.text("sandwich🧇 ")
streamlit.header("build your own smpothie 🍹")
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("pick soe fruits",list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
streamlit.multiselect("pick soe fruits",list(my_fruit_list.index),['Avocado','Grapes'])
