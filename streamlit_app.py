import streamlit
streamlit.title('My Parents New Healthy Diner, yummy!')
streamlit.header("Menu😊")
streamlit.text("sandwich🧇 ")
streamlit.header("build your own smpothie 🍹")
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("pick some fruits",list(my_fruit_list.index)['Avocado','Grapes'])
---streamlit.dataframe(my_fruit_list)
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
