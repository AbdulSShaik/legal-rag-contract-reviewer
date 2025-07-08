import streamlit as st
from preprocess import extract_text, chunk_text
from embeddings import embed_chunks
from llm import ask_llm
from prompts import get_analysis_prompt
from clause_classifier import classify_clause

st.title("📄 AI Contract Clause Analyzer")

uploaded_file = st.file_uploader("Upload Contract", type=["pdf", "docx"])

if uploaded_file:
    st.success("Contract Uploaded.")
    content = extract_text(uploaded_file)
    chunks = chunk_text(content)
    index, vectors = embed_chunks(chunks)

    for chunk in chunks[:3]:
        st.subheader("Clause")
        st.write(chunk)

        with st.expander("Analysis"):
            prompt = get_analysis_prompt(chunk)
            response = ask_llm(prompt)
           # st.text_area("LLM Output", response, height=200)

        with st.expander("Recommended Clause Modifications"):
            if response and "add" in response.lower():
                st.markdown("### ➕ Suggested Additions")
                for line in response.split("\n"):
                    if "add" in line.lower():
                        st.write("- " + line.strip())
            if response and "remove" in response.lower():
                st.markdown("### ➖ Suggested Removals")
                for line in response.split("\n"):
                    if "remove" in line.lower():
                        st.write("- " + line.strip())

        if response and "recommend" in response.lower():
            st.markdown("### ✅ Recommendation")
            st.write(response.split("3. Recommend changes and justify:")[-1].strip())

        if "risk" in response.lower() or "compliance" in response.lower() or "concern" in response.lower():
          st.markdown("### ⚠️ Observations (Risks)")
    risk_lines = [line.strip() for line in response.splitlines() 
                  if any(word in line.lower() for word in ["risk", "compliance", "concern"])]
    if risk_lines:
        for line in risk_lines:
            st.write("- " + line)
    else:
        st.write("No specific risk-related lines found.")


        with st.expander("Clause Type"):
            label, score = classify_clause(chunk)
            st.markdown(f"**Predicted Type**: {label} (Confidence: {score:.2f})")