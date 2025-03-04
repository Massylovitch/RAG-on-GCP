import streamlit as st
import datetime as dt
import time
import vertexai

from lib.streaming import StreamHandler
from lib.chain import get_chain
from lib.source_retriever import list_top_k_sources, get_top_k_urls
from config import PROJECT_ID, REGION

STREAMING_MODE = True
vertexai.init(project=PROJECT_ID, location=REGION)

st.set_page_config(page_title="Chatbot", layout="centered")


def set_default_button_dict():
    buttons = {
        "docs_start_date": dt.date(2020, 1, 1),
        "docs_end_date": dt.date.today()
    }
    buttons["space_name"] = True
    return buttons


st.title("AI Assistant")
st.session_state["streaming_mode"] = st.checkbox(
    'Stream the answer', value=STREAMING_MODE)
st.text("I already read The documentation, so you don't have to !")

if "buttons" not in st.session_state:
    st.session_state["buttons"] = set_default_button_dict()

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "How may I help you?"}]

if "sources_md" not in st.session_state:
    st.session_state["sources_md"] = [""]


# Create sidebar
with st.sidebar:
    st.caption('Select the documents you want to search in:')

    button_dict = {}
    st.session_state["buttons"]["space_name"] = st.checkbox(
        "space_name", value=True)

    st.caption('Search in a specific time range:')
    st.session_state["buttons"]["docs_start_date"] = st.date_input(
        "Start date", dt.date(2020, 1, 1))
    st.session_state["buttons"]["docs_end_date"] = st.date_input(
        "End date", dt.date.today())


# Display the whole conversation in the UI
for n, message in enumerate(st.session_state.messages):
    if message["role"] == "assistant":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    else:
        with st.chat_message(message["role"], avatar="🧑‍💻"):
            st.markdown(message["content"])


if prompt := st.chat_input("How may I help you?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user", avatar="🧑‍💻").write(prompt)

    with st.chat_message("assistant"):
        with st.spinner(text='I am thinking...'):
            time_st = time.time()

            if st.session_state["streaming_mode"]:
                # Chain must be instanciated here because of st.empty behavior
                container = st.empty()
                handler = StreamHandler(container)
                chain = get_chain(
                    filters=st.session_state["buttons"], streaming=True, streaming_handler=[handler])
                print("prompt", prompt)
                result = chain({"query": prompt})
                answer = result["result"]
            else:
                result = st.session_state["qa_agent"]({"query": prompt})
                answer = result["result"]
                st.write(answer)

        time_end = time.time()
        sources = get_top_k_urls(result["source_documents"])
        sources_md = list_top_k_sources(result["source_documents"])

        # Save metadata
        st.session_state.runtime.append(float(round(time_end - time_st, 3)))
        st.session_state.sources.append(sources)
        st.session_state.sources_md.append(sources_md)

        # Write answer and sources
        if sources_md:
            st.markdown(sources_md)
        else:
            print(sources_md)

        st.session_state.messages.append(
            {"role": "assistant", "content": f"{answer}"})
