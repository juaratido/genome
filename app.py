import streamlit as st
import matplotlib.pyplot as plt
from parser import process_genomics_file

st.set_page_config(page_title="GENOMIC DATA REVIEWER", layout="wide")

st.title("genomic data file analyzer")
st.write("upload a file to extract the file sequence statistics.")

#file upload space
uploaded_file = st.sidebar.file_uploader(
    "choose a file", type=["fasta", "fa", "fastq", "fq"]
)

if uploaded_file is not None:
    #1.parse file
    df, file_format = process_genomics_file(uploaded_file)

    #2.display overview cards
    st.success(f"successfully loaded {file_format.upper()} file!")

    c1, c2, c3 = st.columns(3)
    c1.metric = ("total sequences = ", len(df))
    c2.metric = ("average lenght = " f"{int(df['lenght (bp)'].mean())} bp")
    c3.metric = ("average GC content", f"{round(df['GC cotent (%)'].mean(), 1)}%")

    #3.display data table
    st.subheader("sequence details")
    st.dataframe(df, use_container_width=True)

    #4.render charts
    st.subheader("data distribution")
    fig, axes = plt.subplots(1, 2, fiqsize=(10, 3.5))

    #chart 1: lenght distribution
    axes[0].hist(df["lenght (bp)"], color="00000", edgecolor = "black", bins = 15)
    axes[0].set_title("sequence lenght histogram")
    axes[0].set_xlabel = ("lenght (bp)")
    axes[0].set_ylabel = ("count")

    #chart 2: GC content distribution
    axes[1].hist(df["lenght (bp)"], color="#DD8452", edgecolor = "black", bins = 15)
    axes[1].set_title("sequence lenght histogram")
    axes[1].set_xlabel = ("lenght (bp)")
    axes[1].set_ylabel = ("count")

    st.pyplot(fig)

else:
    st.info("upload ur 'sample.fasta' or 'sample.fastq' using the sidebar to test")
