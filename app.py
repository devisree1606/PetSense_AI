
import streamlit as st
from PIL import Image
from datetime import datetime

from ocr import extract_text
from pet_analyzer import analyze_pet


st.set_page_config(
    page_title="PetMood AI",
    page_icon="P",
    layout="wide"
)


st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #fff0f6, #eef8ff);
    }

    .title {
        text-align: center;
        font-size: 52px;
        font-weight: 800;
        color: #7b2cbf;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 20px;
        color: #555;
        margin-bottom: 30px;
    }

    .card {
        background: white;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0px 5px 20px rgba(0,0,0,0.10);
        margin-bottom: 20px;
    }

    .mood-card {
        background: linear-gradient(135deg, #fff0f6, #f3e8ff);
        padding: 30px;
        border-radius: 25px;
        text-align: center;
        box-shadow: 0px 5px 20px rgba(0,0,0,0.12);
    }

    .mood {
        font-size: 42px;
        font-weight: bold;
        color: #ff4d6d;
    }

    .section-title {
        font-size: 25px;
        font-weight: 700;
        color: #7b2cbf;
        margin-bottom: 10px;
    }

    .text-box {
        padding: 18px;
        border-radius: 15px;
        background: #f3e8ff;
        color: #333;
        font-size: 16px;
        line-height: 1.6;
    }

    .tip-box {
        padding: 18px;
        border-radius: 15px;
        background: #e8f7ff;
        color: #333;
        line-height: 1.6;
    }

    .warning-box {
        padding: 18px;
        border-radius: 15px;
        background: #fff4e5;
        color: #663c00;
        line-height: 1.6;
    }

    .footer {
        text-align: center;
        color: #777;
        padding: 30px;
        font-size: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown(
    '<div class="title">PetMood AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-Assisted Pet Mood and Behavior Assistant</div>',
    unsafe_allow_html=True
)


with st.sidebar:

    st.header("Pet Settings")

    pet_type = st.selectbox(
        "Select Pet Type",
        ["Dog", "Cat", "Other"]
    )

    analysis_mode = st.selectbox(
        "Analysis Mode",
        [
            "Basic Mood Analysis",
            "Detailed Pet Analysis"
        ]
    )

    st.divider()

    st.info(
        "Upload a clear dog or cat image. "
        "The system will analyze the selected pet type "
        "and provide an estimated mood."
    )

    st.divider()

    st.caption("PetMood AI")
    st.caption("AI-assisted pet mood analysis")


st.markdown(
    '<div class="card">',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">Upload Pet Image</div>',
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader(
    "Choose a JPG, JPEG or PNG image",
    type=["jpg", "jpeg", "png"]
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


if uploaded_file is not None:

    try:

        image = Image.open(uploaded_file)

        col1, col2 = st.columns([1.2, 1])

        with col1:

            st.markdown(
                '<div class="card">',
                unsafe_allow_html=True
            )

            st.image(
                image,
                caption="Uploaded Pet Image",
                use_container_width=True
            )

            st.markdown(
                '</div>',
                unsafe_allow_html=True
            )

        with col2:

            st.markdown(
                '<div class="card">',
                unsafe_allow_html=True
            )

            st.markdown(
                '<div class="section-title">Image Information</div>',
                unsafe_allow_html=True
            )

            st.write(f"Pet Type: {pet_type}")
            st.write(f"Image Size: {image.width} x {image.height}")
            st.write(f"Image Format: {image.format}")
            st.write(f"Analysis Mode: {analysis_mode}")

            st.markdown(
                '</div>',
                unsafe_allow_html=True
            )


        if st.button(
            "Analyze Pet Mood",
            use_container_width=True
        ):

            with st.spinner(
                "Analyzing pet image..."
            ):

                try:

                    # OCR is still used to extract any available text
                    extracted_text = extract_text(image)

                    # Pet image analysis
                    result = analyze_pet(
                        image,
                        pet_type
                    )

                    mood = str(
                        result.get("mood", "UNKNOWN")
                    ).upper().strip()

                    score = int(
                        result.get("score", 0)
                    )

                    description = result.get(
                        "description",
                        "The pet mood could not be estimated."
                    )

                    recommendation = result.get(
                        "recommendation",
                        "Observe your pet's behavior carefully."
                    )

                except Exception as e:

                    st.error(
                        "Unable to analyze the pet image."
                    )

                    st.code(str(e))

                    st.stop()


            analysis_time = datetime.now().strftime(
                "%d-%m-%Y %I:%M:%S %p"
            )


            st.divider()

            st.markdown(
                '<div class="section-title">Analysis Result</div>',
                unsafe_allow_html=True
            )


            result_col1, result_col2, result_col3 = st.columns(3)

            with result_col1:

                st.metric(
                    "Detected Mood",
                    mood
                )

            with result_col2:

                st.metric(
                    "Mood Score",
                    f"{score}%"
                )

            with result_col3:

                st.metric(
                    "Pet",
                    pet_type
                )


            st.markdown(
                f"""
                <div class="mood-card">
                    <div class="mood">
                        {mood}
                    </div>
                    <p>{description}</p>
                </div>
                """,
                unsafe_allow_html=True
            )


            if score > 0:

                st.write("### Mood Confidence")

                st.progress(
                    min(score, 100) / 100
                )

                st.caption(
                    f"Estimated confidence: {score}%"
                )


            st.write("### Extracted OCR Text")

            if extracted_text:

                st.markdown(
                    f"""
                    <div class="text-box">
                        {extracted_text}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:

                st.info(
                    "No readable text was found in the image. "
                    "Mood analysis was performed using the pet image."
                )


            st.write("### Pet Care Recommendation")

            st.markdown(
                f"""
                <div class="tip-box">
                    <b>Recommendation:</b><br>
                    {recommendation}
                </div>
                """,
                unsafe_allow_html=True
            )


            st.write("### Safety Reminder")

            st.markdown(
                """
                <div class="warning-box">
                Mood detection is an AI-assisted estimate.
                It should not be treated as a veterinary diagnosis.
                If your pet shows sudden behavioral changes,
                aggression, unusual movement, loss of appetite,
                or signs of pain, consult a qualified veterinarian.
                </div>
                """,
                unsafe_allow_html=True
            )


            if analysis_mode == "Detailed Pet Analysis":

                st.divider()

                st.write("### Detailed Analysis")

                detail1, detail2 = st.columns(2)

                with detail1:

                    st.markdown(
                        f"""
                        <div class="card">
                        <h4>Behavioral Observation</h4>
                        Pet type selected: {pet_type}.<br>
                        Image-based analysis was performed.<br>
                        Detected mood: {mood}.<br>
                        Confidence score: {score}%.
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                with detail2:

                    st.markdown(
                        f"""
                        <div class="card">
                        <h4>AI Interpretation</h4>
                        The uploaded image was analyzed.<br>
                        The system estimated the pet's mood.<br>
                        Mood result: {mood}.<br>
                        Results are intended for assistance only.
                        </div>
                        """,
                        unsafe_allow_html=True
                    )


            report = f"""
PETMOOD AI ANALYSIS REPORT

Analysis Date:
{analysis_time}

Pet Type:
{pet_type}

Analysis Mode:
{analysis_mode}

Detected Mood:
{mood}

Mood Score:
{score}%

Description:
{description}

Recommendation:
{recommendation}

Extracted OCR Text:
{extracted_text if extracted_text else "No readable text found."}

Disclaimer:
This is an AI-assisted estimate and is not a veterinary diagnosis.
"""


            st.divider()

            st.download_button(
                "Download Analysis Report",
                data=report,
                file_name="PetMood_AI_Report.txt",
                mime="text/plain",
                use_container_width=True
            )

            st.caption(
                f"Analysis completed on {analysis_time}"
            )


    except Exception as e:

        st.error(
            "Unable to open the uploaded image."
        )

        st.code(str(e))


else:

    st.info(
        "Upload a pet image to start the analysis."
    )


st.markdown(
    """
    <div class="footer">
        PetMood AI - AI-Assisted Pet Mood Assistant<br>
        AI-assisted analysis for educational purposes
    </div>
    """,
    unsafe_allow_html=True
)

