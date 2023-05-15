import streamlit as st
from PIL import Image
import io

st.title("Image Resizer")


image_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if image_file is not None:
    
    image = Image.open(image_file)
    st.image(image, caption="Original Image", use_column_width=False)

    
    width = st.slider("Width", 1, 1000, 500)
    height = st.slider("Height", 1, 1000, 500)
    resized_image = image.resize((width, height))
    st.image(resized_image, caption="Resized Image", use_column_width=False)



    download_button = st.button("Download Resized Image")
    if download_button:
        
        bytes_io = io.BytesIO()
        resized_image.save(bytes_io, format="PNG")
        data = bytes_io.getvalue()

        st.download_button(
            label="Download",
            data=data,
            file_name="resized_image.png",
            mime="image/png",
        )
