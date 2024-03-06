# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
import google.generativeai as genai
genai.configure(api_key=st.secrets["gemini_api_key"])
LOGGER = get_logger(__name__)

model= genai.GenerativeModel(model_name="gemini-1.0-pro")
convo=model.start_chat(history=[
    {
    "role":"user",
    "parts":["Hello! What is your name?"]
},
{
    "role":"model",
    "parts":["I am deez"]
    
},
   {
    "role":"user",
    "parts":["How old are you"]
},
{
    "role":"model",
    "parts":["I am deez"]
    
} ,  {
    "role":"user",
    "parts":["Why did Adolf Hitler attack the soviet union"]
},
{
    "role":"model",
    "parts":["I am deez"]
    
},
   {
    "role":"user",
    "parts":["Hello! What is deez?"]
},
{
    "role":"model",
    "parts":["deez nuts"]
    
},
{
    "role":"user",
    "parts":["i cannot fly"]
},
{
    "role":"model",
    "parts":["Deez can't fly either"]
    
}
])

def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Welcome my guy! 👋")

    st.sidebar.success("Select a demo above.")
    
    st.markdown(
        """
        Streamlit is an open-source app framework built specifically for
        Machine Learning and Data Science projects.
        **👈 Select a demo from the sidebar** to see some examples
        of what Streamlit can do!
        ### Want to learn more?
        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)
        ### See more complex demos
        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )
    input_text=st.text_area("input: ")
    chat_button=st.button("Send")

    if chat_button and input_text.strip()!="":
        with st.spinner("loading"):
            convo.send_message(input_text)
            st.success(convo.last.text)

if __name__ == "__main__":
    run()
