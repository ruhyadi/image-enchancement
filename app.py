"""Apps for image enhancement"""
import streamlit as st
import os
import json
import matplotlib.pyplot as plt

from thresholding import process, save_configs

def app():
    """stramlit app"""
    st.header("Image Enhancement")
    st.subheader("Enhancement with opencv")

    col0 = st.columns(2)
    with col0[0]:
        input_image = st.file_uploader("Upload input image", type=["jpg", "png"])
    with col0[1]:
        output_image = st.file_uploader("Upload ground-truth image", type=["jpg", "png"])

    # TODO: implement configs loader from json
    # with col0[2]:
    #     load_config = st.file_uploader("Load config", type=["json"])

    # if load_config is not None:
    #     with open("results/configs.json", "wb") as f:
    #             f.write(load_config.getbuffer())
    #     with open("results/configs.json", "r") as f:
    #         config = json.load(f)

    col1 = st.columns(3)
    with col1[0]:
        st.write("_")
        ksize = st.slider("Smoothing", 1, 101, 5, 2)
    with col1[1]:
        st.write("Sharpening")
        alpha = st.slider("Alpha", 0.0, 2.0, 1.5, 0.001)
    with col1[2]:
        st.write("_")
        beta = st.slider("Beta", -1.0, 0.0, -0.5, 0.01)

    threshold = st.slider("Threshold value", 0, 255, 127)

    col2 = st.columns([1, 1, 3])
    with col2[0]:
        equalizer = st.checkbox("Equalizer")
    with col2[1]:
        clahe = st.checkbox("CLAHE")
    with col2[2]:
        clahe_slider = st.slider("CLAHE clipLimit", 0.0, 5.0, 1.0, 0.1)

    input_save_path = os.path.join("results", input_image.name)
    output_save_path = os.path.join("results", output_image.name)
    intermediate_path = os.path.join("results", "inter_" + input_image.name)
    processed_path = os.path.join("results", "thresholded_" + input_image.name)

    col3 = st.columns([5, 1])
    with col3[1]:
        save_configs_btn = st.button("Save configs")

    if save_configs_btn:
        with st.spinner("Saving configs..."):
            save_configs(
                configs={
                    "equalizer": equalizer,
                    "clahe": clahe,
                    "clahe_cliplimit": clahe_slider,
                    "ksize": ksize,
                    "alpha": alpha,
                    "beta": beta,
                    "threshold": threshold
                },
                output_path="results"
            )
        st.success("Configs saved")

    if input_image is not None and output_image is not None:
        with open(input_save_path, "wb") as f:
                f.write(input_image.getbuffer())
        with open(output_save_path, "wb") as f:
                f.write(output_image.getbuffer())      

        # process image, return histogram
        hist = process(
            img_path=input_save_path,
            inter_path=intermediate_path,
            output_path=processed_path,
            equalizer=equalizer,
            clahe=clahe,
            clahe_cliplimit=clahe_slider,
            ksize=ksize,
            alpha=alpha,
            beta=beta,
            threshold=threshold
        )

        col = st.columns(4)
        with col[0]:
            st.write("Input image")
            st.image(input_save_path, use_column_width=True)
        with col[1]:
            st.write("Intermediate image")
            st.image(intermediate_path, use_column_width=True)
        with col[2]:
            st.write("Output image")
            st.image(processed_path, use_column_width=True)
        with col[3]:
            st.write("Grount truth image")
            st.image(output_save_path, use_column_width=True)

        # plot histogram
        col3 = st.columns([2, 5, 2])
        with col3[1]:
            st.write("Histogram")
            fig, ax = plt.subplots()
            ax.plot(hist)
            st.pyplot(fig)

if __name__ == "__main__":
    app()

