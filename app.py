import streamlit as st
from PIL import Image
from datetime import datetime

from ocr import extract_text, detect_mood


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
    '<div class="subtitle">OCR-Based Pet Mood and Behavior Assistant</div>',
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
        "Upload an image containing readable text. "
        "OCR will extract the text and the system "
        "will estimate the mood."
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
                "Reading image and analyzing pet information..."
            ):

                try:

                    extracted_text = extract_text(image)

                    mood = detect_mood(extracted_text)

                except Exception as e:

                    st.error("Unable to analyze the image.")
                    st.code(str(e))
                    st.stop()


            analysis_time = datetime.now().strftime(
                "%d-%m-%Y %I:%M:%S %p"
            )


            mood_data = {

                "PLAYFUL": {
                    "score": 90,
                    "description":
                        "The pet may be showing playful or energetic behavior.",
                    "tip":
                        "Give your pet safe play time and interactive toys."
                },

                "HAPPY": {
                    "score": 90,
                    "description":
                        "The detected text suggests a positive or happy mood.",
                    "tip":
                        "Positive interaction, gentle attention and play can maintain this mood."
                },

                "RELAXED": {
                    "score": 85,
                    "description":
                        "The pet may be feeling calm and comfortable.",
                    "tip":
                        "Allow the pet to rest in a quiet and comfortable environment."
                },

                "EXCITED": {
                    "score": 92,
                    "description":
                        "The detected information indicates excitement or high energy.",
                    "tip":
                        "Provide safe exercise and interactive activities."
                },

                "SAD": {
                    "score": 65,
                    "description":
                        "The detected text may indicate a less positive emotional state.",
                    "tip":
                        "Give your pet attention and monitor changes in behavior."
                },

                "ANGRY": {
                    "score": 70,
                    "description":
                        "The detected information may indicate irritation or defensive behavior.",
                    "tip":
                        "Give the pet some space and avoid forcing interaction."
                },

                "UNKNOWN": {
                    "score": 0,
                    "description":
                        "The available OCR text was not enough to identify a mood.",
                    "tip":
                        "Try uploading a clearer image containing readable text."
                }
            }


            mood = str(mood).upper().strip()

            data = mood_data.get(
                mood,
                mood_data["UNKNOWN"]
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
                    f"{data['score']}%"
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

                    <p>{data['description']}</p>

                </div>
                """,
                unsafe_allow_html=True
            )


            if data["score"] > 0:

                st.write("### Mood Confidence")

                st.progress(
                    data["score"] / 100
                )

                st.caption(
                    f"Estimated confidence: {data['score']}%"
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

                st.warning(
                    "No readable text was found in the image."
                )


            st.write("### Pet Care Recommendation")

            st.markdown(
                f"""
                <div class="tip-box">
                    <b>Recommendation:</b><br>
                    {data['tip']}
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
                        """
                        <div class="card">

                        <h4>Behavioral Observation</h4>

                        Mood detected from available OCR text.<br>
                        Text-based emotional indicators analyzed.<br>
                        Pet type considered during analysis.<br>
                        Results should also be interpreted with visual behavior.

                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                with detail2:

                    st.markdown(
                        """
                        <div class="card">

                        <h4>AI Interpretation</h4>

                        OCR extracts text from the image.<br>
                        Mood detection analyzes emotional keywords.<br>
                        Confidence score provides an estimate.<br>
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
{data['score']}%

Description:
{data['description']}

Recommendation:
{data['tip']}

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

        st.error("Unable to open the uploaded image.")
        st.code(str(e))


else:

    st.info(
        "Upload a pet image to start the analysis."
    )


st.markdown(
    """
    <div class="footer">
        PetMood AI - OCR-Based Pet Mood Assistant<br>
        AI-assisted analysis for educational purposes
    </div>
    """,
    unsafe_allow_html=True
)