import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title='Dataframes',layout='wide')

st.title("Dataframes")

input=st.text_input("enter path")

if st.button("run"):
    if not os.path.exists(input):
        st.exception(FileNotFoundError())
    else:
        for foldername,subfolders,filenames in os.walk(input):
            for filename in filenames:
                if "test" not in filename:
                    st.exception(FileExistsError())
                else:
                    df=pd.read_csv("%s\%s" % (foldername,filename),index_col=0)
                    st.dataframe(df)                   