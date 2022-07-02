"""Apps for image thresholding"""
import streamlit as st
import os

from thresholding import process

def app():
    """stramlit app"""
    st.header("Image Thresholding")
    st.subheader("Thresholding with opencv")

    col0 = st.columns(2)
    with col0[0]:
        input_image = st.file_uploader("Upload input image", type=["jpg", "png"])
    with col0[1]:
        output_image = st.file_uploader("Upload output image", type=["jpg", "png"])

    slider = st.slider("Threshold value", 0, 255, 127)

    input_save_path = os.path.join("results", input_image.name)
    output_save_path = os.path.join("results", output_image.name)
    output_path = os.path.join("results", "thresholded_" + input_image.name)

    if input_image is not None and output_image is not None:
        with open(input_save_path, "wb") as f:
                f.write(input_image.getbuffer())
        with open(output_save_path, "wb") as f:
                f.write(output_image.getbuffer())      

        process(input_save_path, output_path, slider)

        col = st.columns(3)
        with col[0]:
            st.write("Input image")
            st.image(input_save_path, use_column_width=True)
        with col[1]:
            st.write("Output image")
            st.image(output_save_path, use_column_width=True)
        with col[2]:
            st.write("Output image")
            st.image(output_path, use_column_width=True)

if __name__ == "__main__":
    app()

