import streamlit as st
from langchain_community.tools import ArxivQueryRun,WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper,ArxivAPIWrapper
from langchain_community.tools import DuckDuckGoSearchRun
## Custom Tools 
from langchain_groq import ChatGroq
from langchain.agents import initialize_agent, AgentType
from langchain.agents import AgentExecutor
from langchain.callbacks import StreamlitCallbackHandler
## Run all these tools with an agent
import os 
from dotenv import load_dotenv

load_dotenv()

# Configure page
st.set_page_config(page_title="Search Engine With Langchain", page_icon="🔍")
st.title("Search Engine With Langchain")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "How can I help you? ."}]

# Sidebar configuration
with st.sidebar:
    st.title("Settings")
    api_key = st.text_input("Enter your Groq API Key", type="password")
    
    if not api_key:
        st.warning("Please enter your Groq API key to continue.")
        st.stop()

# Initialize tools and LLM
try:
    llm = ChatGroq(groq_api_key=api_key, model_name="llama3-8b-8192")
    
    wikipedia = WikipediaAPIWrapper(top_k_results=1, doc_content_window=250)
    wiki = WikipediaQueryRun(api_wrapper=wikipedia)
    
    arxiv = ArxivAPIWrapper(top_k_results=1, doc_content_window=250)
    arxiv_tool = ArxivQueryRun(api_wrapper=arxiv)
    
    duckduckgo = DuckDuckGoSearchRun(name="search")
    tools = [wiki, arxiv_tool, duckduckgo]
    
except Exception as e:
    st.error(f"Error initializing tools: {str(e)}")
    st.stop()

# Display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Handle user input
if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    try:
        agent = initialize_agent(
            tools,
            llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            handle_parsing_errors=True
        )
        
        with st.chat_message("assistant"):
            st_callback = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
            response = agent.run(prompt, callbacks=[st_callback])  # Changed from st.session_state.messages to just prompt
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.write(response)
            
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")







