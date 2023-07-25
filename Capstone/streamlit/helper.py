from ultralytics import YOLO
import supervision as sv # Version 0.2.0
import streamlit as st
import cv2
import base64
import settings
import queue
import threading
import time

# Define the wdith & height of the video
frame_width = 1280
frame_height = 720

# bufferless VideoCapture
class VideoCapture:

    def __init__(self, name):
        self.cap = cv2.VideoCapture(name)
        self.q = queue.Queue()
        t = threading.Thread(target=self._reader)
        t.daemon = True
        t.start()

    # read frames as soon as they are available, keeping only the most recent one
    def _reader(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            if not self.q.empty():
                try:
                    self.q.get_nowait()  # discard previous (unprocessed) frame
                except queue.Empty:
                    pass
            self.q.put((ret, frame))

    def read(self):
        ret, frame = self.q.get()
        return ret, frame


def load_model(model_path):
    """
    Loads a YOLO object detection model from the specified model_path.

    Parameters:
        model_path (str): The path to the YOLO model file.

    Returns:
        A YOLO object detection model.
    """
    model = YOLO(model_path)
    return model


def display_tracker_option():
    """
    Create a selector to select if display tracker is required.

    Returns:
        Returns a bool, yes or no to display tracker
    """
    display_tracker = st.radio("Display Tracker", ('Yes', 'No'))
    is_display_tracker = True if display_tracker == 'Yes' else False
    return is_display_tracker


def display_warning (st_frame_text, st_frame_audio, alert_level):
    """
    Display a visual & audio warning if crowd number exceeds the alert level.

    Parameters:
        st_frame_text: The placholder streamlit object to display the warning text.
        st_frame_audio: The placeholder streamlit object to play the audio clip.
        alert_level: The total number of people to trigger the warning text & audio.

    Returns:
        None
    """
    st_frame_text.subheader(f'⚠️ WARNING!!! Crowd exceeded limit of {alert_level}! ⚠️')
    with open(settings.WARNING_AUDIO, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio controls autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st_frame_audio.markdown(
            md,
            unsafe_allow_html=True,
        )


def display_detected_frames(conf, model, st_frame_list, frame, is_display_tracker, alert_level, max_count):
    """
    Display the detected objects on a video frame using the YOLOv8 model.

    Parameters:
        conf (float): Confidence threshold for object detection.
        model (YoloV8): A YOLOv8 object detection model.
        st_frame_list (Streamlit object): A list of Streamlit object placeholders to display different objects in each location accordingly.
        frame (numpy array): A numpy array representing the video frame.
        is_display_tracker (bool): A flag indicating whether to display object tracking (default=None).
        alert_level (int): The total number of people to trigger the warning text & audio.
        max_count (int): Highest number of people detected.

    Returns:
        max_count: Maximum number of people detected.
    """

    # detect
    results = model(frame, conf=conf)[0]
    detections = sv.Detections.from_yolov8(results)
    count = len(results.boxes) # Count the number of detection
    if max_count < count:
        max_count = count
    # Display object tracking, if specified
    if is_display_tracker:
        box_annotator = sv.BoxAnnotator(thickness=4, text_thickness=4, text_scale=2)
        frame = box_annotator.annotate(scene=frame, detections=detections, skip_label=True)
    st_frame_list[0].image(frame[:, :, ::-1], caption='Detected Video', channels="RGB", use_column_width=True)
    st_frame_list[1].write(f'{count} people detected.')
    st_frame_list[2].write(f'Highest number of people detected: {max_count}')

    if count > alert_level:
         display_warning (st_frame_list[4], st_frame_list[3], alert_level)

    return max_count


# def play_youtube_video(conf, model):
#     """
#     Plays a yourube video.

#     Parameters:
#         conf: Confidence of YOLOv8 model.
#         model: An instance of the `YOLOv8` class containing the YOLOv8 model.

#     Returns:
#         None

#     Raises:
#         None
#     """
#     source_youtube = st.sidebar.text_input("YouTube Video url")

#     is_display_tracker = display_tracker_option()

#     if st.sidebar.button('Detect Objects'):
#         try:
#             video = pafy.new(source_youtube)
#             best = video.getbest(preftype="mp4")
#             vid_cap = cv2.VideoCapture(best.url)
#             st_frame = st.empty()
#             while (vid_cap.isOpened()):
#                 success, image = vid_cap.read()
#                 if success:
#                     _display_detected_frames(conf,
#                                              model,
#                                              st_frame,
#                                              image,
#                                              is_display_tracker
#                                              )
#                 else:
#                     vid_cap.release()
#                     break
#         except Exception as e:
#             st.sidebar.error("Error loading video: " + str(e))


def play_rtsp_stream(conf, model, alert_level):
    """
    Plays an rtsp stream. Detects Objects in real-time using the YOLOv8 object detection model.

    Parameters:
        conf: Confidence of YOLOv8 model.
        model: An instance of the `YOLOv8` class containing the YOLOv8 model.
        alert_level: The total number of people to trigger the warning text & audio.

    Returns:
        None

    Raises:
        None
    """
    source_rtsp = st.sidebar.text_input("RTSP stream url")
    is_display_tracker = display_tracker_option()
    st_frame_warning = st.empty()

    col1, col2 = st.columns(2)

    with col2:
        st_frame_2 = st.empty()
        st_frame_3 = st.empty()

    with col1:
        if st.sidebar.button('Detect Objects'):
            try:
                vid_cap = VideoCapture(source_rtsp)
                st_frame_1 = st.empty()
                st_frame_4 = st.empty()
                st_frame_list = [st_frame_1, st_frame_2, st_frame_3, st_frame_4, st_frame_warning]
                max_count=0
                while True:
                    time.sleep(0.5)  # simulate time between events
                    success, frame = vid_cap.read()  # Capture frame from VideoCapture
                    # if frame is not None:  # Check if frame is valid
                    if success:  # Check if frame is valid
                        max_count = display_detected_frames(conf, model, 
                                                            st_frame_list, 
                                                            frame, 
                                                            is_display_tracker,
                                                            alert_level, 
                                                            max_count)
                    else:
                        break

                # while (vid_cap.isOpened()):
                #     success, frame = vid_cap.read()
                #     if success:
                #         max_count = display_detected_frames(conf, 
                #                                             model, 
                #                                             st_frame_list, 
                #                                             frame, 
                #                                             is_display_tracker, 
                #                                             alert_level,
                #                                             max_count)
                #     else:
                #         vid_cap.release()
                #         break
            except Exception as e:
                st.sidebar.error("Error loading video: " + str(e))


def play_webcam(conf, model, alert_level):
    """
    Plays a webcam stream. Detects Objects in real-time using the YOLOv8 object detection model.

    Parameters:
        conf: Confidence of YOLOv8 model.
        model: An instance of the `YOLOv8` class containing the YOLOv8 model.
        alert_level: The total number of people to trigger the warning text & audio.

    Returns:
        None

    Raises:
        None
    """
    source_webcam = settings.WEBCAM_PATH
    is_display_tracker = display_tracker_option()
    st_frame_warning = st.empty()

    col1, col2 = st.columns(2)

    with col2:
        st_frame_2 = st.empty()
        st_frame_3 = st.empty()

    with col1:
        if st.sidebar.button('Detect Objects'):
            try:
                vid_cap = cv2.VideoCapture(source_webcam)
                st_frame_1 = st.empty()
                st_frame_4 = st.empty()
                st_frame_list = [st_frame_1, st_frame_2, st_frame_3, st_frame_4, st_frame_warning]
                max_count=0
                while (vid_cap.isOpened()):
                    success, frame = vid_cap.read()
                    if success:
                        max_count = display_detected_frames(conf, 
                                                            model, 
                                                            st_frame_list, 
                                                            frame, 
                                                            is_display_tracker, 
                                                            alert_level,
                                                            max_count)
                    else:
                        vid_cap.release()
                        break
            except Exception as e:
                st.sidebar.error("Error loading video: " + str(e))
    with col2:
        st.write(' ')


def play_stored_video(conf, model, alert_level):
    """
    Plays a stored video file. Tracks and detects objects in real-time using the YOLOv8 object detection model.

    Parameters:
        conf: Confidence of YOLOv8 model.
        model: An instance of the `YOLOv8` class containing the YOLOv8 model.
        alert_level: The total number of people to trigger the warning text & audio.

    Returns:
        None

    Raises:
        None
    """
    source_vid = st.sidebar.selectbox(
        "Choose a video...", settings.VIDEOS_DICT.keys())

    is_display_tracker = display_tracker_option()
    st_frame_warning = st.empty()

    col1, col2 = st.columns(2)

    with col1:

        with open(settings.VIDEOS_DICT.get(source_vid), 'rb') as video_file:
            video_bytes = video_file.read()
        if video_bytes:
            st.video(video_bytes)

    with col2:

        if st.sidebar.button('Detect Video Objects'):
            try:
                vid_cap = cv2.VideoCapture(str(settings.VIDEOS_DICT.get(source_vid)))
                # vid_cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
                # vid_cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)
                st_frame_1 = st.empty()
                st_frame_2 = st.empty()
                st_frame_3 = st.empty()
                st_frame_4 = st.empty()
                st_frame_list = [st_frame_1, st_frame_2, st_frame_3, st_frame_4, st_frame_warning]
                max_count=0
                while (vid_cap.isOpened()):
                    success, frame = vid_cap.read()
                    if success:
                        max_count = display_detected_frames(conf, 
                                                            model, 
                                                            st_frame_list, 
                                                            frame, 
                                                            is_display_tracker, 
                                                            alert_level,
                                                            max_count)
                    else:
                        vid_cap.release()
                        break
            except Exception as e:
                st.sidebar.error("Error loading video: " + str(e))
