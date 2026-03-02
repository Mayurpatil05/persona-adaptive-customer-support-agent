import streamlit as st
import requests

st.title("Persona-Adaptive Customer Support Agent")

query = st.text_area("Describe your issue:")

if st.button("Submit"):

    response = requests.post(
        "http://localhost:8000/support",
        json={"message": query}
    )

    data = response.json()

    st.write("Detected Persona:", data["persona"])

    if data["escalated"]:
        st.error("Escalated to Human Agent")
        st.write(data["summary"])
    else:
        st.success("AI Response")
        st.write(data["response"])