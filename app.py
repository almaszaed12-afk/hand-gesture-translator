import streamlit as st
import cv2
import mediapipe as mp

# تهيئة Mediapipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

st.title("🤚 مترجم إشارات اليد")
st.write("هذا المشروع يتعرف على حركة اليد من الكاميرا ويحولها للنصوص على Streamlit.")

# تشغيل الكاميرا
run = st.checkbox("تشغيل الكاميرا")

FRAME_WINDOW = st.image([])

cap = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while run:
        ret, frame = cap.read()
        if not ret:
            st.write("لم يتم العثور على الكاميرا.")
            break

        # تحويل الألوان من BGR إلى RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # معالجة اليد
        results = hands.process(frame)

        # رسم العلامات إذا تم اكتشاف اليد
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        FRAME_WINDOW.image(frame)

cap.release()
