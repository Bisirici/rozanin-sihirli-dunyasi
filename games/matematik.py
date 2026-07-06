
import streamlit as st
import random
from core.state import go_to

# =========================================================================
# 4. SINIF MEB MATEMATİK MÜFREDATINA UYGUN SAYI ARALIKLARI
# =========================================================================
# Kaynak: MEB 4. sınıf matematik kazanımları
#   - Toplama/Çıkarma : en çok 4 basamaklı doğal sayılarla işlem
#   - Çarpma          : 2 basamaklı sayı ile 2 basamaklı sayının çarpımı
#   - Bölme           : en çok 3 basamaklı sayıyı en çok 2 basamaklı sayıya
#                        kalansız bölme
#
# Seviye eşikleri: puan arttıkça sayılar kademeli olarak büyür.
LEVEL_1_SCORE_LIMIT = 40   # Bu puana kadar: Kolay
LEVEL_2_SCORE_LIMIT = 80   # Bu puana kadar: Orta / sonrası: Zor

LEVEL_NAMES = {1: "Kolay 🌱", 2: "Orta 🌟", 3: "Zor 🔥"}

# Her doğru cevapta kazanılan puan
PUAN_KAZANC = 10
# Şampiyonluk için hedef puan
HEDEF_PUAN = 100

OPERATIONS = {
    "carpma": {"symbol": "✖️", "label": "Çarpma"},
    "bolme": {"symbol": "➗", "label": "Bölme"},
    "toplama": {"symbol": "➕", "label": "Toplama"},
    "cikarma": {"symbol": "➖", "label": "Çıkarma"},
}


def get_difficulty_level() -> int:
    """Toplam puana göre 1 (kolay) - 3 (zor) arası seviye döndürür."""
    score = st.session_state.get("total_score", 0)
    if score < LEVEL_1_SCORE_LIMIT:
        return 1
    elif score < LEVEL_2_SCORE_LIMIT:
        return 2
    return 3


def generate_multiplication(level: int) -> tuple[str, int]:
    """Seviyeye göre çarpma sorusu üretir (çarpım tablosu -> 2 haneli x 2 haneli)."""
    if level == 1:
        n1, n2 = random.randint(1, 10), random.randint(1, 10)
    elif level == 2:
        n1, n2 = random.randint(10, 50), random.randint(2, 9)
    else:
        n1, n2 = random.randint(10, 30), random.randint(10, 20)
    correct = n1 * n2
    question = f"{n1} × {n2}"
    return question, correct


def generate_division(level: int) -> tuple[str, int]:
    """Seviyeye göre bölme sorusu üretir. Her zaman kalansız (tam bölünen) sayılar seçilir."""
    if level == 1:
        divisor = random.randint(1, 5)
        quotient = random.randint(1, 10)
    elif level == 2:
        divisor = random.randint(2, 9)
        quotient = random.randint(2, 15)
    else:
        divisor = random.randint(2, 12)
        quotient = random.randint(5, 25)
    dividend = divisor * quotient
    question = f"{dividend} ÷ {divisor}"
    return question, quotient


def generate_addition(level: int) -> tuple[str, int]:
    """Seviyeye göre toplama sorusu üretir (2 haneli -> 4 haneli sayılar)."""
    if level == 1:
        n1, n2 = random.randint(10, 99), random.randint(10, 99)
    elif level == 2:
        n1, n2 = random.randint(100, 999), random.randint(10, 999)
    else:
        n1, n2 = random.randint(1000, 9999), random.randint(100, 9999)
    correct = n1 + n2
    question = f"{n1} + {n2}"
    return question, correct


def generate_subtraction(level: int) -> tuple[str, int]:
    """Seviyeye göre çıkarma sorusu üretir. Sonuç her zaman pozitif olacak şekilde kurgulanır."""
    if level == 1:
        n2 = random.randint(10, 99)
        n1 = n2 + random.randint(1, 99)
    elif level == 2:
        n2 = random.randint(100, 999)
        n1 = n2 + random.randint(1, 999)
    else:
        n2 = random.randint(1000, 9999)
        n1 = n2 + random.randint(1, 9999)
    correct = n1 - n2
    question = f"{n1} - {n2}"
    return question, correct


QUESTION_GENERATORS = {
    "carpma": generate_multiplication,
    "bolme": generate_division,
    "toplama": generate_addition,
    "cikarma": generate_subtraction,
}


def generate_wrong_options(correct_answer: int) -> list[int]:
    """Doğru cevaba yakın, mantıklı ve tekrarsız 3 yanlış şık üretir."""
    wrong_answers = set()
    spread = max(3, int(correct_answer * 0.15)) if correct_answer > 20 else 10
    attempts = 0
    while len(wrong_answers) < 3 and attempts < 50:
        wrong_ans = correct_answer + random.randint(-spread, spread)
        if wrong_ans != correct_answer and wrong_ans >= 0:
            wrong_answers.add(wrong_ans)
        attempts += 1
    # Güvenlik: yeterli yanlış şık üretilemezse basit dolgu ekle
    filler = 1
    while len(wrong_answers) < 3:
        candidate = correct_answer + filler
        if candidate != correct_answer:
            wrong_answers.add(candidate)
        filler += 1
    return list(wrong_answers)


def generate_math_question(active_operations: list[str]):
    """Seçili işlem türlerinden 4. sınıf seviyesine uygun karışık bir soru üretir."""
    level = get_difficulty_level()
    operation = random.choice(active_operations)
    question, correct_answer = QUESTION_GENERATORS[operation](level)
    symbol = OPERATIONS[operation]["symbol"]

    # Aynı soru art arda gelmesin diye son soruyla karşılaştırıyoruz
    if st.session_state.get("math_last_question") == question:
        return generate_math_question(active_operations)
    st.session_state.math_last_question = question

    all_options = generate_wrong_options(correct_answer) + [correct_answer]
    random.shuffle(all_options)

    return question, symbol, correct_answer, all_options


MOTIVE_MESAJLARI = [
    "Harika! Doğru Cevap Roza! 🎉 Süpersin!",
    "Muhteşem gidiyorsun canım kızım! 🌟 +10 Puan!",
    "Matematik kraliçesi! 👑 Doğru cevap!",
    "Vay canına! Çok hızlı ve doğru bir hesaplama! 🚀",
    "Adım adım şampiyonluğa! Aferin Roza! ✨",
]

SERI_MESAJLARI = {
    3: "3'te 3! Seri devam ediyor! 🔥",
    5: "5 doğru üst üste! İnanılmazsın! 🔥🔥",
    10: "10'luk seri! Sen bir matematik dahisisin! 🔥🔥🔥",
}

# Doğru cevapta otomatik çalan kısa alkış sesi (CC0 lisanslı, bigsoundbank.com)
ALKIS_SESI_URL = "https://bigsoundbank.com/UPLOAD/mp3/2363.mp3"
ARKA_PLAN_MUZIGI_URL = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3"

SESSION_DEFAULTS = {
    "math_dogru_sayisi": 0,
    "math_yanlis_sayisi": 0,
    "math_seri": 0,
    "math_en_uzun_seri": 0,
    "math_son_seviye": 1,
}


def _reset_game_state():
    """Puan ve istatistikleri sıfırlar, aktif soruyu temizler."""
    st.session_state.total_score = 0
    for key, default in SESSION_DEFAULTS.items():
        st.session_state[key] = default
    for key in ["math_correct", "math_answer", "math_last_question", "math_symbol", "math_question", "math_opts"]:
        st.session_state.pop(key, None)


def render_math_game():
    """Çoktan seçmeli, seviyeli, seri takipli, müzikli ve 100 puan kutlamalı Matematik Sihirbazı"""
    st.subheader("🧮 Matematik Sihirbazı")

    # 📱 IPHONE İÇİN ŞIKLARI PARLATMA VE KOYULAŞTIRMA RENKLERİ
    st.markdown("""
    <style>
        div[data-testid="stMarkdownContainer"] p {
            color: #1A202C !important;
            font-weight: bold !important;
            font-size: 18px !important;
        }
        div[data-testid="stRadio"] label {
            background-color: #FFFFFF !important;
            padding: 12px 15px !important;
            border-radius: 12px !important;
            border: 2px solid #CBD5E0 !important;
            margin-bottom: 8px !important;
            display: flex !important;
            align-items: center;
        }
        div[data-testid="stRadio"] label[data-checked="true"] {
            border-color: #667eea !important;
            background-color: #FAF5FF !important;
        }
    </style>
    """, unsafe_allow_html=True)

    # --- ÜST AYAR ÇUBUĞU: Müzik ve İşlem Seçimi (veli kontrolü için) ---
    ayar_col1, ayar_col2 = st.columns([1, 2])
    with ayar_col1:
        muzik_ac = st.toggle("🎵 Müzik", value=st.session_state.get("math_muzik_ac", True))
        st.session_state.math_muzik_ac = muzik_ac
        if muzik_ac:
            st.audio(ARKA_PLAN_MUZIGI_URL, format="audio/mp3")
    with ayar_col2:
        secili_islemler = st.multiselect(
            "Çalışılacak işlemler:",
            options=list(OPERATIONS.keys()),
            default=st.session_state.get("math_secili_islemler", list(OPERATIONS.keys())),
            format_func=lambda k: f"{OPERATIONS[k]['symbol']} {OPERATIONS[k]['label']}",
        )
    # En az bir işlem seçili olmalı, aksi halde tüm işlemlere geri dön
    if not secili_islemler:
        secili_islemler = list(OPERATIONS.keys())
        st.info("En az bir işlem seçmelisin, şimdilik tüm işlemler dahil edildi. 🙂")
    st.session_state.math_secili_islemler = secili_islemler

    # İstatistik alanları başlatılmamışsa hazırla
    for key, default in SESSION_DEFAULTS.items():
        if key not in st.session_state:
            st.session_state[key] = default

    # --- HEDEF PUAN KUTLAMA EKRANI ---
    if st.session_state.total_score >= HEDEF_PUAN:
        st.balloons()
        st.markdown(f"""
        <div style="background-color: #FFDEE9; background-image: linear-gradient(0deg, #FFDEE9 0%, #B5FFFC 100%); padding: 30px; border-radius: 20px; text-align: center; border: 3px solid #FF8008;">
            <h1 style="color: #FF8008; margin-bottom: 10px;">🎉 TEBRİKLER ROZA! 🎉</h1>
            <h2 style="color: #4A5568;">Aferin Canım Kızım! 👑</h2>
            <p style="font-size: 18px; color: #718096;">Harika bir şekilde {HEDEF_PUAN} puana ulaştın ve şampiyon oldun! 🏆</p>
            <p style="font-size: 15px; color: #718096;">En uzun doğru serin: {st.session_state.math_en_uzun_seri} 🔥</p>
        </div>
        """, unsafe_allow_html=True)

        st.write("")
        if st.button("Puanı Sıfırla ve Yeniden Oyna 🔄", type="primary", use_container_width=True):
            _reset_game_state()
            st.rerun()
        if st.button("Ana Menüye Dön 🏠", use_container_width=True):
            go_to("menu")
        return

    # --- SORU VE OYUN ALANI ---
    if "math_correct" not in st.session_state:
        question, symbol, corr, opts = generate_math_question(secili_islemler)
        st.session_state.math_question = question
        st.session_state.math_symbol = symbol
        st.session_state.math_correct = corr
        st.session_state.math_opts = opts

    question = st.session_state.math_question
    symbol = st.session_state.math_symbol
    correct_answer = st.session_state.math_correct
    options = st.session_state.math_opts
    level = get_difficulty_level()
    level_adi = LEVEL_NAMES[level]

    # Seviye ilk kez atlandığında küçük bir bildirim göster
    if level != st.session_state.math_son_seviye:
        if level > st.session_state.math_son_seviye:
            st.toast(f"Seviye atladın: {level_adi} 🚀")
        st.session_state.math_son_seviye = level

    # --- ÜST BİLGİ ÇUBUĞU: Puan, Seri, Seviye ---
    c1, c2, c3 = st.columns(3)
    c1.metric("Puan", st.session_state.total_score)
    c2.metric("Seri 🔥", st.session_state.math_seri)
    c3.metric("Seviye", level_adi)

    st.progress(min(st.session_state.total_score / HEDEF_PUAN, 1.0))

    # Sorunun ekrandaki büyük, mobil uyumlu tasarımı
    st.markdown(f"""
    <div style="background-color: #f0f2f6; padding: 25px; border-radius: 15px; text-align: center; margin: 15px 0; border: 2px solid #E2E8F0;">
        <span style="font-size: 16px; color: #718096; font-weight: bold;">{symbol} Soru:</span>
        <h2 style="color: #2D3748; margin: 5px 0 0 0; font-size: 36px;">{question} = ?</h2>
    </div>
    """, unsafe_allow_html=True)

    secilen_sik = st.radio(
        "Doğru şıkkı işaretle:",
        options=options,
        index=None,
        key="math_radio",
    )

    st.write("")

    c1, c2 = st.columns(2)
    with c1:
        if st.button("Cevabı Kontrol Et ✨", type="primary", use_container_width=True, disabled=(secilen_sik is None)):
            if secilen_sik == correct_answer:
                st.success(random.choice(MOTIVE_MESAJLARI))
                st.audio(ALKIS_SESI_URL, format="audio/mp3", autoplay=True)

                st.session_state.total_score += PUAN_KAZANC
                st.session_state.math_dogru_sayisi += 1
                st.session_state.math_seri += 1
                st.session_state.math_en_uzun_seri = max(
                    st.session_state.math_en_uzun_seri, st.session_state.math_seri
                )
                if st.session_state.math_seri in SERI_MESAJLARI:
                    st.toast(SERI_MESAJLARI[st.session_state.math_seri])

                del st.session_state.math_correct
                st.rerun()
            else:
                st.error(f"Yaklaştın! Doğru cevap **{correct_answer}** idi ama pes etme! 💪")
                st.session_state.math_yanlis_sayisi += 1
                st.session_state.math_seri = 0

    with c2:
        if st.button("Ana Menüye Dön 🏠", use_container_width=True):
            if "math_correct" in st.session_state:
                del st.session_state.math_correct
            go_to("menu")

    # --- ALT BİLGİ: Toplam doğru/yanlış ve başarı yüzdesi ---
    toplam_soru = st.session_state.math_dogru_sayisi + st.session_state.math_yanlis_sayisi
    basari_yuzdesi = (
        round(100 * st.session_state.math_dogru_sayisi / toplam_soru) if toplam_soru > 0 else 0
    )
    st.caption(
        f"✅ Doğru: {st.session_state.math_dogru_sayisi}  |  "
        f"❌ Yanlış: {st.session_state.math_yanlis_sayisi}  |  "
        f"📊 Başarı: %{basari_yuzdesi}  |  "
        f"🏆 En uzun seri: {st.session_state.math_en_uzun_seri}"
    )
