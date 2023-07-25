# Python In-built packages
from pathlib import Path
import PIL

# External packages
import streamlit as st

# Local Modules
import settings
import helper

# Setting page layout
st.set_page_config(
    page_title="CrowdSenseAI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)   

# Main page heading
st.title("CrowdSenseAI: Detection & Early Warning System")

# Sidebar
st.sidebar.header("🤖 ML Model Config")

# # Model Options
# model_type = st.sidebar.radio(
#     "Select Task", ['Detection', 'Segmentation'])

confidence = float(st.sidebar.slider(
    "Select Model Confidence", 20, 100, 40)) / 100

st_frame_warning_header = st.sidebar.empty()
st_frame_warning_slider = st.sidebar.empty()

model_path = Path(settings.MODEL)

# Load Pre-trained ML Model
try:
    model = helper.load_model(model_path)
except Exception as ex:
    st.error(f"Unable to load model. Check the specified path: {model_path}")
    st.error(ex)

st.sidebar.header("Input Options")
source_radio = st.sidebar.radio(
    "Select Source", settings.SOURCES_LIST)

if source_radio != settings.IMAGE:
    st_frame_warning_header.header("🚨 Warning Threshold")
    alert_level = st_frame_warning_slider.slider(
    "Alert Level", 100, 1000, 400)
                      
source_img = None
# If image is selected
if source_radio == settings.IMAGE:
    source_img = st.sidebar.file_uploader(
        "Choose an image...", type=("jpg", "jpeg", "png", 'bmp', 'webp'))

    col1, col2 = st.columns(2)

    with col1:
        try:
            if source_img is None:
                default_image_path = str(settings.DEFAULT_IMAGE)
                default_image = PIL.Image.open(default_image_path)
                st.image(default_image_path, caption="Default Image",
                         use_column_width=True)
            else:
                uploaded_image = PIL.Image.open(source_img)
                st.image(source_img, caption="Uploaded Image",
                         use_column_width=True)
        except Exception as ex:
            st.error("Error occurred while opening the image.")
            st.error(ex)

    with col2:
        if source_img is None:
            default_detected_image_path = str(settings.DEFAULT_DETECT_IMAGE)
            default_detected_image = PIL.Image.open(
                default_detected_image_path)
            st.image(default_detected_image_path, caption='Detected Image',
                     use_column_width=True)
        else:
            if st.sidebar.button('Detect Objects'):
                
                res = model.predict(uploaded_image,
                                    conf=confidence,
                                    show_labels = False,
                                    show_conf = False,
                                    augment=True
                                    )
                boxes = res[0].boxes
                res_plotted = res[0].plot()[:, :, ::-1]
                st.image(res_plotted, caption='Detected Image',
                         use_column_width=True)
                st_frame_people_count = st.empty()
                count=0
                try:
                    with st.expander("Detection Results"):
                        for box in boxes:
                            st.write(box.data)
                            count+=1
                except Exception as ex:
                    # st.write(ex)
                    st.write("No image is uploaded yet!")
                st_frame_people_count.write(f'{count} people detected.')

elif source_radio == settings.VIDEO:
    helper.play_stored_video(confidence, model, alert_level)

elif source_radio == settings.WEBCAM:
    helper.play_webcam(confidence, model, alert_level)

elif source_radio == settings.RTSP:
    helper.play_rtsp_stream(confidence, model, alert_level)

else:
    st.error("Please select a valid source type!")
