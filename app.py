import streamlit as st
from core.state import init_state, go_to
from games.matematik import render_math_game
from games.turkce import render_turkce_game
from games.ingilizce import render_ingilizce_game

st.set_page_config(page_title="Roza'nın Dünyası", page_icon="🦄", layout="centered")

init_state()

# --- 🌟 GELİŞMİŞ GÖRSEL TASARIM (CSS VE ANİMASYONLAR) ---
st.markdown("""
<style>
    /* Arka planı canlandırıcı, yumuşak bir pembe-mor gradyan yapıyoruz */
    .stApp {
        background: linear-gradient(180deg, #FFF5F5 0%, #EBF8FF 50%, #FAF5FF 100%);
    }
    
    /* Ana Başlık Efekti (Gölgeli ve Canlı) */
    .main-title {
        font-family: 'Comic Sans MS', cursive, sans-serif;
        color: #4C51BF;
        text-align: center;
        font-size: 38px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 5px;
    }
    
    /* Butonları iPhone için dev ve yuvarlak yapma, üzerine gelince büyüme efekti */
    div.stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        font-size: 20px !important;
        font-weight: bold !important;
        padding: 18px 20px !important;
        border-radius: 20px !important;
        border: none !important;
        box-shadow: 0px 8px 15px rgba(118, 75, 162, 0.2) !important;
        transition: all 0.3s ease 0s !important;
    }
    
    /* Parmakla basıldığında veya fareyle gelindiğinde buton hafifçe büyüsün */
    div.stButton > button:hover {
        transform: translateY(-3px) scale(1.02) !important;
        box-shadow: 0px 15px 20px rgba(118, 75, 162, 0.4) !important;
    }
    
    /* Kategori alt başlıkları */
    .section-title {
        color: #2D3748;
        font-family: 'Comic Sans MS', sans-serif;
        text-align: center;
        margin-top: 10px;
        font-size: 22px;
    }
</style>
""", unsafe_allow_html=True)

# --- ÜST BAŞLIK ALANI ---
st.markdown('<h1 class="main-title">🦄 Roza\'nın Sihirli Dünyası 🎮</h1>', unsafe_allow_html=True)

# Gelişmiş 3D Efektli Skor Tablosu
st.markdown(f"""
<div style="
    background: linear-gradient(135deg, #FF416C 0%, #FF4B2B 100%);
    padding: 15px;
    border-radius: 25px;
    text-align: center;
    box-shadow: 0px 10px 20px rgba(255, 65, 108, 0.3);
    margin-bottom: 25px;
    border: 2px solid white;
">
    <span style="color: white; font-size: 18px; font-weight: bold; letter-spacing: 1px;">✨ TOPLAM YILDIZLARIN ✨</span>
    <h1 style="color: #FFF; margin: 5px 0 0 0; font-size: 42px; font-weight: 900; text-shadow: 2px 2px 0px #C53030;">⭐ {st.session_state.total_score} Puan</h1>
</div>
""", unsafe_allow_html=True)

# --- MİMARİ SAYFA YÖNLENDİRME ---
if st.session_state.current_page == "menu":
    
    # Müzik panelini daha şık gösterelim
    with st.expander("🎵 Arka Plan Müziğini Aç/Kapat", expanded=True):
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3")
    
    st.markdown('<p class="section-title">Bugün Hangi Maceraya Atılalım? 🥰</p>', unsafe_allow_html=True)
    st.write("")
    
    # Parlayan, iPhone uyumlu dev butonlar
    if st.button("🧮 Matematik Sihirbazı", use_container_width=True):
        go_to("matematik")
        
    st.write("") # Butonlar arası nefes alma boşluğu
    if st.button("📘 Türkçe Kelime Dünyası", use_container_width=True):
        go_to("turkce")
        
    st.write("")
    if st.button("🌍 İngilizce Dünyası", use_container_width=True):
        go_to("ingilizce")

elif st.session_state.current_page == "matematik":
    render_math_game()

elif st.session_state.current_page == "turkce":
    render_turkce_game()

elif st.session_state.current_page == "ingilizce":
    render_ingilizce_game()