import streamlit as st
from agent import run_agent
from memory import get_weak_topics

st.set_page_config(page_title="Agentic DSA Assistant", layout="centered")

st.title("🤖 Agentic DSA Assistant")
st.write("Ask DSA questions, get hints, explanations, or code analysis.")

# Initialize chat history in UI
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input (chat box)
user_input = st.chat_input("Type your question or paste code...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = run_agent(user_input)
            st.markdown(response)

    # Save assistant response
    st.session_state.messages.append({"role": "assistant", "content": response})

# Sidebar (extra features)
st.sidebar.title("📊 User Insights")

if st.sidebar.button("Show Weak Topics"):
    weak = get_weak_topics("user1")
    if weak:
        st.sidebar.write(weak)
    else:
        st.sidebar.write("No data yet.")