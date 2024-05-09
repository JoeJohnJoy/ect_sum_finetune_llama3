# create a streamlit app to show the UI for loading a csv file
import streamlit as st
import pandas as pd
from pathlib import Path

main_path = Path(__file__).parent.parent
df = pd.read_csv(main_path/'UI_data/final_result.csv')

st.title('Earning Calls Text Summarization Tool using Fine tuned Llama 3 Model')

# create a drop down to select the column file
column = st.selectbox('Select the column to view', df['file'].unique())
#

# filter the dataframe based on the selected column
filtered_df = df[df['file'] == column][['input_llm','output_llm','instruction_llm','fine_tune_result_llm','fine_tune_result_fine_tune']]

# display each cell as a text area
# wrap the text in text area
for i in range(filtered_df.shape[0]):
    st.text_area('Input', filtered_df.iloc[i]['input_llm'])
    st.text_area('Expected Result', filtered_df.iloc[i]['output_llm'])
    st.text_area('Instruction', filtered_df.iloc[i]['instruction_llm'])
    st.text_area('Before Fine tuning', filtered_df.iloc[i]['fine_tune_result_llm'])
    st.text_area('After Fine tuning', filtered_df.iloc[i]['fine_tune_result_fine_tune'])