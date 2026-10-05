import streamlit as st
from PIL import Image
from pet_analyzer import analyze_pet


st.set_page_config(
    page_title="PetSense AI",
    layout="wide"
)

st.title("PetSense AI")
st.subheader("Visual Pet Behavior & Safety Assistant")

st.write(
    "Upload a dog or cat image and explore its possible "
    "mood, activity, body language, safety and interaction."
)

st.divider()

uploaded_file = st.file_uploader(
    "Upload Pet Image",
    type=["jpg", "jpeg", "png"]
)


if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Uploaded Pet Image",
        width=500
    )

    if st.button("Analyze Image", type="primary"):

        with st.spinner("Analyzing the uploaded image..."):

            try:
                result = analyze_pet(image)

                st.session_state["result"] = result
                st.session_state["section"] = "overall"

            except Exception as e:

                st.error("Unable to analyze the image.")

                st.write(str(e))


if "result" in st.session_state:

    result = st.session_state["result"]

    st.divider()

    st.subheader("Analysis Options")

    col1, col2, col3 = st.columns(3)

    with col1:

        if st.button(
            "Mood",
            use_container_width=True
        ):
            st.session_state["section"] = "mood"

        if st.button(
            "Activity",
            use_container_width=True
        ):
            st.session_state["section"] = "activity"

    with col2:

        if st.button(
            "Body Language",
            use_container_width=True
        ):
            st.session_state["section"] = "body"

        if st.button(
            "Safety",
            use_container_width=True
        ):
            st.session_state["section"] = "safety"

    with col3:

        if st.button(
            "Interaction",
            use_container_width=True
        ):
            st.session_state["section"] = "interaction"

        if st.button(
            "Overall Report",
            use_container_width=True
        ):
            st.session_state["section"] = "overall"


    st.divider()

    section = st.session_state.get(
        "section",
        "overall"
    )


    if section == "mood":

        st.subheader("Possible Mood")

        st.info(result["mood"])

        st.write("Visible Clues")

        st.write(result["visible_clues"])


    elif section == "activity":

        st.subheader("Activity")

        st.info(result["activity"])


    elif section == "body":

        st.subheader("Body Language")

        st.info(result["body_language"])


    elif section == "safety":

        st.subheader("Safety Check")

        st.info(result["safety"])


    elif section == "interaction":

        st.subheader("Recommended Interaction")

        st.info(result["interaction"])


    elif section == "overall":

        st.subheader("PetSense AI Report")

        st.write(
            f"Possible Mood: {result['mood']}"
        )

        st.write(
            f"Activity: {result['activity']}"
        )

        st.write(
            f"Body Language: {result['body_language']}"
        )

        st.write(
            f"Safety: {result['safety']}"
        )

        st.write(
            f"Interaction: {result['interaction']}"
        )

        st.divider()

        st.caption(
            "Results are based only on visible information "
            "in the uploaded image. Possible mood is an "
            "interpretation of visible behavior and is not "
            "a veterinary diagnosis."
        )