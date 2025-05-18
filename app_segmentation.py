import streamlit as st
from ultralytics import YOLO
import tempfile
from PIL import Image
import os

# Load YOLOv8 model
MODEL_PATH = "models/best_yolov8_model_segmentation.pt"
model = YOLO(MODEL_PATH)

class_id_to_name = {
    0: "Class A",
    1: "Class B",
    2: "Class C",
    3: "Class D",
    4: "Class F"
}

st.set_page_config(page_title="Fire Segmentation App", layout="centered")
st.title("🔥 Fire Classification System with Suppression Guidance for Segmentation Task - CPE 313 Project")
st.markdown("You can upload an image to detect and segment fire instances. The app will also provide suppression guidance.")

# Image upload
uploaded_file = st.file_uploader("Upload an image.", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
        image.save(temp_file.name)
        image_path = temp_file.name

    results = model(image_path)

    # Show segmentation result image
    result_img = results[0].plot()
    st.image(result_img, caption="Segmentation Result", use_column_width=True)

    # Get detected class IDs from results
    detected_class_ids = list(set([int(c) for c in results[0].boxes.cls.cpu().numpy()]))

    if detected_class_ids:
        st.subheader("Detected Fire Classes:")
        for class_id in detected_class_ids:
            class_name = class_id_to_name.get(class_id, "Unknown Class")
            st.write(class_name)

        st.subheader("Suppression Guidance:")
        for class_id in detected_class_ids:
            if class_id == 0:
                st.info("Class A (Ordinary combustibles): Use water, foam, or multipurpose dry chemical extinguishers for wood, paper, cloth, and plastics fires.")
            elif class_id == 1:
                st.warning("Class B (Flammable liquids): Use foam, CO2, or dry chemical extinguishers; avoid water for fires involving gasoline, oil, or solvents.")
            elif class_id == 2:
                st.error("Class C (Electrical): Use CO2 or dry chemical agents for extinguishing; avoid water or foam to prevent electrical shock; shut off power safely.")
            elif class_id == 3:
                st.warning("Class D (Metals): Use specialized dry powder extinguishers for metal fires; avoid water or common extinguishers to prevent explosions.")
            elif class_id == 4:
                st.error("Class F (Cooking oils): Use wet chemical extinguishers for kitchen fires; avoid water to prevent splattering and fire spread.")
    else:
        st.write("✅ No fire detected.")

    os.remove(image_path)
