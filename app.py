```python
import streamlit as st
from PIL import Image

from pet_analyzer import analyze_pet


st.set_page_config(
    page_title="PetSense AI",
    layout="wide"
)


st.title("PetSense AI")

st.subheader(
    "AI-Powered Pet Image Analysis"
)

st.write(
    "Upload a pet image and get basic information, "
    "health observations, and care suggestions."
)


uploaded_file = st.file_uploader(
    "Upload Pet Image",
    type=["jpg", "jpeg", "png"]
)


if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Pet Image",
        use_container_width=True
    )

    if st.button("Analyze Pet"):

        with st.spinner("Analyzing pet image..."):

            result = analyze_pet(image)

        st.success("Analysis completed")

        st.markdown("### Pet")

        st.write(
            result.get(
                "pet",
                "Pet detected"
            )
        )

        st.markdown("### Description")

        st.write(
            result.get(
                "description",
                "No description available."
            )
        )

        st.markdown("### Health Observation")

        st.write(
            result.get(
                "health",
                "No health observation available."
            )
        )

        st.markdown("### Care Suggestions")

        st.write(
            result.get(
                "care",
                "No care suggestions available."
            )
        )

else:

    st.info(
        "Please upload a JPG, JPEG, or PNG image of a pet."
    )
