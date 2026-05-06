import streamlit as st
import hashlib
import time
import random

# Simulated song database with fingerprints
SONG_DATABASE = [
    {"id": "s001", "title": "Blinding Lights", "artist": "The Weeknd", "genre": "Pop", "duration": "3:20"},
    {"id": "s002", "title": "Shape of You", "artist": "Ed Sheeran", "genre": "Pop", "duration": "3:53"},
    {"id": "s003", "title": "Rockstar", "artist": "Post Malone", "genre": "Hip-Hop", "duration": "3:39"},
    {"id": "s004", "title": "Believer", "artist": "Imagine Dragons", "genre": "Rock", "duration": "3:24"},
    {"id": "s005", "title": "Levitating", "artist": "Dua Lipa", "genre": "Pop", "duration": "3:23"},
    {"id": "s006", "title": "Stay", "artist": "The Kid LAROI", "genre": "Pop", "duration": "2:21"},
    {"id": "s007", "title": "Peaches", "artist": "Justin Bieber", "genre": "R&B", "duration": "3:18"},
    {"id": "s008", "title": "Industry Baby", "artist": "Lil Nas X", "genre": "Hip-Hop", "duration": "3:32"},
]

def generate_fingerprint(audio_bytes):
    """Simulate audio fingerprinting using hash"""
    return hashlib.md5(audio_bytes[:1024]).hexdigest()

def simulate_spectrogram_analysis(fingerprint):
    """Simulate spectrogram feature extraction"""
    features = {
        "tempo": random.randint(80, 180),
        "pitch": random.uniform(200, 800),
        "energy": random.uniform(0.5, 1.0),
        "noise_level": random.uniform(0.01, 0.3),
    }
    return features

def match_song(fingerprint, features):
    """Simulate matching against database"""
    time.sleep(2)  # Simulate processing
    matched_song = random.choice(SONG_DATABASE)
    
    # Higher confidence if noise is low
    base_confidence = 99 - (features["noise_level"] * 100)
    confidence = round(random.uniform(base_confidence - 5, base_confidence), 2)
    confidence = max(70, min(99, confidence))
    return matched_song, confidence

# ---- Streamlit UI ----

st.set_page_config(page_title="Audio Identification System", page_icon="🎵", layout="centered")

st.title("🎵 Audio Identification System")
st.markdown("Upload a short audio clip (3–10 sec) and we'll identify the song!")

st.divider()

uploaded_file = st.file_uploader("📂 Upload Audio File", type=["mp3", "wav", "ogg"])

if uploaded_file is not None:
    st.audio(uploaded_file, format="audio/mp3")
    st.info(f"📁 File uploaded: `{uploaded_file.name}` | Size: {uploaded_file.size} bytes")

    if st.button("🔍 Identify Song"):
        audio_bytes = uploaded_file.read()

        with st.spinner("🔬 Extracting audio fingerprint..."):
            time.sleep(1)
            fingerprint = generate_fingerprint(audio_bytes)

        with st.spinner("📊 Analyzing spectrogram features..."):
            time.sleep(1)
            features = simulate_spectrogram_analysis(fingerprint)

        with st.spinner("🎯 Matching against song database..."):
            song, confidence = match_song(fingerprint, features)

        st.divider()
        st.success("✅ Song Successfully Identified!")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 🎵 Song Details")
            st.markdown(f"**Title:** {song['title']}")
            st.markdown(f"**Artist:** {song['artist']}")
            st.markdown(f"**Genre:** {song['genre']}")
            st.markdown(f"**Duration:** {song['duration']}")

        with col2:
            st.markdown("### 📊 Analysis Results")
            st.markdown(f"**Fingerprint ID:** `{fingerprint[:10]}...`")
            st.markdown(f"**Tempo:** {features['tempo']} BPM")
            st.markdown(f"**Energy Level:** {features['energy']:.2f}")
            st.markdown(f"**Noise Level:** {features['noise_level']:.2f}")

        st.divider()
        st.markdown("### 🎯 Confidence Score")
        st.progress(int(confidence))
        if confidence >= 90:
            st.success(f"🟢 High Confidence Match: **{confidence}%**")
        elif confidence >= 75:
            st.warning(f"🟡 Medium Confidence Match: **{confidence}%**")
        else:
            st.error(f"🔴 Low Confidence Match: **{confidence}%**")

st.divider()
st.markdown("### 🗄️ Song Database")
st.markdown(f"Currently indexing **{len(SONG_DATABASE)} songs**")
if st.checkbox("Show Database"):
    for song in SONG_DATABASE:
        st.markdown(f"- **{song['title']}** by {song['artist']} ({song['genre']})")