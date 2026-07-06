import streamlit as st

def init_state():
    """Oyunun ilk andaki hafıza kayıtlarını ve müzik ayarlarını hazırlar."""
    if "current_page" not in st.session_state:
        st.session_state.current_page = "menu"
        
    if "total_score" not in st.session_state:
        st.session_state.total_score = 0

    # Varsayılan müzik durumu (İlk başta açık olsun)
    if "music_on" not in st.session_state:
        st.session_state.music_on = True

def go_to(page_name):
    """Sayfalar arası geçişi sağlayan ana motor."""
    st.session_state.current_page = page_name
    st.rerun()