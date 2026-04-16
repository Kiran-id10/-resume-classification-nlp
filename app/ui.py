import streamlit as st
import requests

st.title("📄 Resume Classification")

text = st.text_area("Paste Resume Text")

if st.button("Predict"):

    if text.strip() == "":
        st.warning("Enter resume text")
    else:
        try:
            res = requests.post(
                "http://127.0.0.1:8000/predict",
                json={"resume": text}
            )

            result = res.json()

            if "prediction" in result:
                st.success(f"Category: {result['prediction']}")
            else:
                st.error(result)

        except Exception as e:
            st.error(e)
