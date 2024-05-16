from langchain.llms import CTransformers
from langchain.prompts import PromptTemplate
import streamlit as st
import base64
import time 

def get_llama_response(input_text, blog_style):
    llm = CTransformers(
        model='C:/Users/HP/Downloads/Llama-2-Article-Generation-App-main/llama-2-7b.ggmlv3.q8_0.bin',
        model_type='llama',
        config={'max_new_tokens': 256, 'temperature': 0.01}  # Adjust max_new_tokens as needed
    )

    template = "Write a blog for a {blog_style} profile about {input_text}."
    prompt = PromptTemplate(
        input_variables=["blog_style", "input_text"],
        template=template
    )

    response = llm(prompt.format(blog_style=blog_style, input_text=input_text))
    return response

def get_download_link(text, filename="blog_post.txt"):
    b64 = base64.b64encode(text.encode()).decode()
    href = f'<a href="data:file/txt;base64,{b64}" download="{filename}">Download Blog Post</a>'
    return href

st.set_page_config(page_title="Blog Generator by M M AKHTAR & PRANJAL MITTAL", page_icon='🤖', layout='centered', initial_sidebar_state='collapsed')
st.header("Blog Generator by M M AKHTAR & PRANJAL MITTAL 🤖")

# st.set_page_config(page_title="Blog Generator using LARGE LANGUAGE MODEL", page_icon='🤖', layout='centered', initial_sidebar_state='collapsed')
# st.header("Blog Generator using Large Language Model LLAMA2🤖")

input_text = st.text_input("Enter the Blog Topic")
blog_style = st.selectbox('Writing the blog for', ('Researchers', 'Data Scientist', 'Common People'), index=0)

if st.button("Generate"):
    with st.spinner('Generating the blog post...'):
        # Progress bar logic
        progress_bar = st.progress(0)
        for i in range(100):
            # Update progress bar
            time.sleep(0.01)
            progress_bar.progress(i + 1)
        blog_content = get_llama_response(input_text, blog_style)
        progress_bar.empty()  # Clear progress bar after completion
        
        st.write(blog_content)
        # Download link
        download_link = get_download_link(blog_content)
        st.markdown(download_link, unsafe_allow_html=True)