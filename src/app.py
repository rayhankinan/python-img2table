import streamlit as st

from convert import convert_pdf_to_dataframe

def main() -> None:
    st.title("PDF to CSV Converter")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    if uploaded_file is None:
        return

    converting = st.empty()

    if converting.button("Convert PDF to CSV", disabled=False, key="convert_button1"):
        converting.button("Converting...", disabled=True, key="convert_button2")

        for page, df_iter in convert_pdf_to_dataframe(uploaded_file):
            st.header(f"{uploaded_file.name} - Page {page}")

            for i, df in enumerate(df_iter):
                try:
                    st.subheader(f"Table {i + 1}")
                    st.dataframe(df)

                except Exception as e:
                    st.error(f"An error occurred: {e}")

        converting.button("Convert PDF to CSV", disabled=False, key="convert_button3")

if __name__ == "__main__":
    main()