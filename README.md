import streamlit as st
import cv2
import mediapipe as mp

# إعداد Mediapipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

st.title("🤖 مترجم إشارات اليد")
st.write("هذا المشروع يلتقط حركة اليد من الكاميرا ويحاول التعرف على الإشارات.")

# تشغيل الكاميرا
run = st.checkbox('تشغيل الكاميرا')
FRAME
