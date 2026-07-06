import streamlit as st
import random
from core.state import go_to

# =========================================================================
# 4. SINIF TÜRKÇE MÜFREDATINA UYGUN SORU KATEGORİLERİ
# =========================================================================
# Kaynak: MEB 4. sınıf Türkçe dersi kazanımları
#   - Eş anlamlı (anlamdaş) kelimeler
#   - Zıt anlamlı (karşıt) kelimeler
#   - Atasözü ve deyimlerin anlamını / tamamlanmasını kavrama
#   - Genel kültür bilmeceleri (kelime dağarcığını zenginleştirme)

PUAN_KAZANC = 10
HEDEF_PUAN = 100

QUESTION_BANK = {
    "bilmece": {
        "label": "Bilmece",
        "icon": "🧩",
        "items": [
            ("Geceleri gökyüzünde parıldayan sihirli nesne nedir? ✨", "Yıldız"),
            ("Yazın bizi ısıtan, gökyüzündeki dev ateş topu hangisidir? ☀️", "Güneş"),
            ("Bize taze süt veren, çimenleri çok seven sevimli hayvan? 🐄", "İnek"),
            ("Kırmızı, tatlı ve sulu bir yaz meyvesi? 🍉", "Karpuz"),
            ("Kanatları rengarenk olan, çiçekten çiçeğe uçan sevimli böcek? 🦋", "Kelebek"),
            ("Gökkuşağı çıktıktan sonra havada süzülen beyaz, yumuşak pamuklar? ☁️", "Bulut"),
            ("Kışın gökten yağan, beyaz ve soğuk taneler nedir? ❄️", "Kar"),
            ("Ormanların kralı olarak bilinen, yelesiyle ünlü hayvan? 🦁", "Aslan"),
            ("Sabah erkenden öten, kırmızı ibikli çiftlik hayvanı? 🐓", "Horoz"),
            ("Suyun içinde yaşayan, solungaçlarıyla nefes alan hayvan? 🐟", "Balık"),
            ("Kitapların saklandığı, sessizce okuma yapılan yer? 📚", "Kütüphane"),
            ("Yılın en soğuk mevsimi hangisidir? 🥶", "Kış"),
        ],
    },
    "es_anlamli": {
        "label": "Eş Anlamlı Kelime",
        "icon": "🔁",
        "items": [
            ("\"Büyük\" kelimesinin eş anlamlısı hangisidir?", "İri"),
            ("\"Akıllı\" kelimesinin eş anlamlısı hangisidir?", "Zeki"),
            ("\"Konuşmak\" kelimesinin eş anlamlısı hangisidir?", "Söylemek"),
            ("\"Mutlu\" kelimesinin eş anlamlısı hangisidir?", "Sevinçli"),
            ("\"Güzel\" kelimesinin eş anlamlısı hangisidir?", "Hoş"),
            ("\"Hızlı\" kelimesinin eş anlamlısı hangisidir?", "Süratli"),
            ("\"Yol\" kelimesinin eş anlamlısı hangisidir?", "Güzergah"),
            ("\"Kederli\" kelimesinin eş anlamlısı hangisidir?", "Üzgün"),
            ("\"Çabuk\" kelimesinin eş anlamlısı hangisidir?", "Hızlı"),
            ("\"Öğretmen\" kelimesinin eş anlamlısı hangisidir?", "Muallim"),
        ],
    },
    "zit_anlamli": {
        "label": "Zıt Anlamlı Kelime",
        "icon": "↔️",
        "items": [
            ("\"Uzun\" kelimesinin zıt anlamlısı hangisidir?", "Kısa"),
            ("\"Sıcak\" kelimesinin zıt anlamlısı hangisidir?", "Soğuk"),
            ("\"Aydınlık\" kelimesinin zıt anlamlısı hangisidir?", "Karanlık"),
            ("\"Mutlu\" kelimesinin zıt anlamlısı hangisidir?", "Üzgün"),
            ("\"Hızlı\" kelimesinin zıt anlamlısı hangisidir?", "Yavaş"),
            ("\"Kalın\" kelimesinin zıt anlamlısı hangisidir?", "İnce"),
            ("\"Temiz\" kelimesinin zıt anlamlısı hangisidir?", "Kirli"),
            ("\"Doğru\" kelimesinin zıt anlamlısı hangisidir?", "Yanlış"),
            ("\"Kolay\" kelimesinin zıt anlamlısı hangisidir?", "Zor"),
            ("\"Sevinçli\" kelimesinin zıt anlamlısı hangisidir?", "Kederli"),
        ],
    },
    "atasozu_deyim": {
        "label": "Atasözü / Deyim",
        "icon": "📖",
        "items": [
            ("\"Damlaya damlaya ___ olur.\" cümlesini tamamlayan kelime nedir?", "Göl"),
            ("\"Ağaç yaşken ___.\" cümlesini tamamlayan kelime nedir?", "Eğilir"),
            ("\"Gülü seven dikenine ___.\" cümlesini tamamlayan kelime nedir?", "Katlanır"),
            ("\"Aç tavuk kendini ___ ambarında sanır.\" cümlesini tamamlayan kelime nedir?", "Buğday"),
            ("\"Bir elin nesi var, iki elin ___.\" cümlesini tamamlayan kelime nedir?", "Sesi var"),
            ("\"Göze girmek\" deyiminin anlamı nedir? Kısaca ne olmaktır?", "Beğenilmek"),
            ("\"Ağzı kulaklarına varmak\" deyimi neyi anlatır?", "Sevinmek"),
            ("\"Dokuz doğurmak\" deyimi ne anlama gelir?", "Sabırsızlanmak"),
        ],
    },
}

CATEGORY_KEYS = list(QUESTION_BANK.keys())

# Türkçe odasına özel arka plan müziği
ARKA_PLAN_MUZIGI_URL = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"

DOGRU_MESAJLARI = [
    "Harika bir tahmin Roza! Doğru! 👏",
    "Kelime sihirbazı canım kızım benim! 🎉 +10 Puan!",
    "Müthişsin! Doğru kelimeyi hemen buldun! 👑",
    "İşte bu kadar! Kitap kurdu Roza iş başında! 📚",
    "Süpersin! Türkçe'de ustalaşıyorsun! ✨",
]

SERI_MESAJLARI = {
    3: "3'te 3! Seri devam ediyor! 🔥",
    5: "5 doğru üst üste! İnanılmazsın! 🔥🔥",
    10: "10'luk seri! Sen bir kelime dahisisin! 🔥🔥🔥",
}

SESSION_DEFAULTS = {
    "word_dogru_sayisi": 0,
    "word_yanlis_sayisi": 0,
    "word_seri": 0,
    "word_en_uzun_seri": 0,
}


def generate_wrong_options(category: str, correct_answer: str) -> list[str]:
    """Doğru cevapla aynı kategoriden, anlamlı yanlış şıklar üretir.

    Aynı kategoride yeterli sayıda alternatif yoksa diğer kategorilerden
    tamamlama yapılır, böylece her zaman 3 farklı yanlış şık garanti edilir.
    """
    aday_havuz = [cevap for (_, cevap) in QUESTION_BANK[category]["items"] if cevap != correct_answer]

    if len(aday_havuz) < 3:
        for diger_kategori, veri in QUESTION_BANK.items():
            if diger_kategori == category:
                continue
            aday_havuz += [cevap for (_, cevap) in veri["items"] if cevap != correct_answer]

    aday_havuz = list(dict.fromkeys(aday_havuz))  # sırayı koruyarak tekrarları temizle
    return random.sample(aday_havuz, 3)


def generate_word_question(active_categories: list[str]):
    """Seçili kategorilerden 4. sınıf seviyesine uygun bir Türkçe sorusu üretir."""
    category = random.choice(active_categories)
    soru_metni, dogru_cevap = random.choice(QUESTION_BANK[category]["items"])

    # Aynı soru art arda gelmesin diye son soruyla karşılaştırıyoruz
    if st.session_state.get("word_last_question") == soru_metni and len(
        QUESTION_BANK[category]["items"]
    ) > 1:
        return generate_word_question(active_categories)
    st.session_state.word_last_question = soru_metni

    yanlis_siklar = generate_wrong_options(category, dogru_cevap)
    all_options = yanlis_siklar + [dogru_cevap]
    random.shuffle(all_options)

    kategori_etiketi = f"{QUESTION_BANK[category]['icon']} {QUESTION_BANK[category]['label']}"
    return soru_metni, dogru_cevap, all_options, kategori_etiketi


def _reset_game_state():
    """Puan ve istatistikleri sıfırlar, aktif soruyu temizler."""
    st.session_state.total_score = 0
    for key, default in SESSION_DEFAULTS.items():
        st.session_state[key] = default
    for key in ["word_correct", "word_answer", "word_last_question", "word_soru", "word_opts", "word_kategori"]:
        st.session_state.pop(key, None)


def render_turkce_game():
    """Çoktan seçmeli, kategorili, seri takipli ve müzikli Türkçe Kelime Oyunu"""
    st.subheader("📘 Türkçe Kelime Dünyası")

    # --- ÜST AYAR ÇUBUĞU: Müzik ve Kategori Seçimi (veli kontrolü için) ---
    ayar_col1, ayar_col2 = st.columns([1, 2])
    with ayar_col1:
        muzik_ac = st.toggle("🎵 Müzik", value=st.session_state.get("word_muzik_ac", True))
        st.session_state.word_muzik_ac = muzik_ac
        if muzik_ac:
            st.audio(ARKA_PLAN_MUZIGI_URL, format="audio/mp3")
    with ayar_col2:
        secili_kategoriler = st.multiselect(
            "Çalışılacak kelime türleri:",
            options=CATEGORY_KEYS,
            default=st.session_state.get("word_secili_kategoriler", CATEGORY_KEYS),
            format_func=lambda k: f"{QUESTION_BANK[k]['icon']} {QUESTION_BANK[k]['label']}",
        )
    if not secili_kategoriler:
        secili_kategoriler = CATEGORY_KEYS
        st.info("En az bir kategori seçmelisin, şimdilik tüm kategoriler dahil edildi. 🙂")
    st.session_state.word_secili_kategoriler = secili_kategoriler

    # İstatistik alanları başlatılmamışsa hazırla
    for key, default in SESSION_DEFAULTS.items():
        if key not in st.session_state:
            st.session_state[key] = default

    # --- HEDEF PUAN KUTLAMA EKRANI ---
    if st.session_state.total_score >= HEDEF_PUAN:
        st.balloons()
        st.markdown(f"""
        <div style="background-color: #EBF8FF; padding: 30px; border-radius: 20px; text-align: center; border: 3px solid #3182CE;">
            <h1 style="color: #3182CE; margin-bottom: 10px;">🎉 KELİME ŞAMPİYONU ROZA! 🎉</h1>
            <h2 style="color: #4A5568;">Harikasın Canım Kızım! 👑</h2>
            <p style="font-size: 18px; color: #718096;">Bütün kelimeleri bildin ve {HEDEF_PUAN} puana ulaştın! 🏆</p>
            <p style="font-size: 15px; color: #718096;">En uzun doğru serin: {st.session_state.word_en_uzun_seri} 🔥</p>
        </div>
        """, unsafe_allow_html=True)

        st.write("")
        if st.button("Puanı Sıfırla ve Yeniden Oyna 🔄", type="primary", use_container_width=True):
            _reset_game_state()
            st.rerun()
        if st.button("Ana Menüye Dön 🏠", use_container_width=True):
            go_to("menu")
        return

    # --- SORU ALANI ---
    if "word_correct" not in st.session_state:
        soru, corr, opts, kategori_etiketi = generate_word_question(secili_kategoriler)
        st.session_state.word_soru = soru
        st.session_state.word_correct = corr
        st.session_state.word_opts = opts
        st.session_state.word_kategori = kategori_etiketi

    soru = st.session_state.word_soru
    correct_answer = st.session_state.word_correct
    options = st.session_state.word_opts
    kategori_etiketi = st.session_state.word_kategori

    # --- ÜST BİLGİ ÇUBUĞU: Puan, Seri ---
    c1, c2 = st.columns(2)
    c1.metric("Puan", st.session_state.total_score)
    c2.metric("Seri 🔥", st.session_state.word_seri)
    st.progress(min(st.session_state.total_score / HEDEF_PUAN, 1.0))

    # Sorunun tasarımı
    st.markdown(f"""
    <div style="background-color: #EBF8FF; padding: 25px; border-radius: 15px; text-align: center; margin-bottom: 15px; border: 2px solid #BEE3F8;">
        <span style="font-size: 14px; color: #2B6CB0; font-weight: bold;">{kategori_etiketi}</span>
        <h3 style="color: #2D3748; margin: 10px 0 0 0; font-size: 22px;">{soru}</h3>
    </div>
    """, unsafe_allow_html=True)

    secilen_sik = st.radio(
        "Doğru cevabı seç:",
        options=options,
        index=None,
        key="word_radio",
    )

    st.write("")

    c1, c2 = st.columns(2)
    with c1:
        if st.button("Cevabı Kontrol Et ✨", type="primary", use_container_width=True, disabled=(secilen_sik is None)):
            if secilen_sik == correct_answer:
                st.success(random.choice(DOGRU_MESAJLARI))
                st.session_state.total_score += PUAN_KAZANC
                st.session_state.word_dogru_sayisi += 1
                st.session_state.word_seri += 1
                st.session_state.word_en_uzun_seri = max(
                    st.session_state.word_en_uzun_seri, st.session_state.word_seri
                )
                if st.session_state.word_seri in SERI_MESAJLARI:
                    st.toast(SERI_MESAJLARI[st.session_state.word_seri])

                del st.session_state.word_correct
                st.rerun()
            else:
                st.error(f"Küçük bir karışıklık oldu, doğru cevap **{correct_answer}** idi. Tekrar dene Roza! 💪")
                st.session_state.word_yanlis_sayisi += 1
                st.session_state.word_seri = 0

    with c2:
        if st.button("Ana Menüye Dön 🏠", use_container_width=True):
            if "word_correct" in st.session_state:
                del st.session_state.word_correct
            go_to("menu")

    # --- ALT BİLGİ: Toplam doğru/yanlış ve başarı yüzdesi ---
    toplam_soru = st.session_state.word_dogru_sayisi + st.session_state.word_yanlis_sayisi
    basari_yuzdesi = (
        round(100 * st.session_state.word_dogru_sayisi / toplam_soru) if toplam_soru > 0 else 0
    )
    st.caption(
        f"✅ Doğru: {st.session_state.word_dogru_sayisi}  |  "
        f"❌ Yanlış: {st.session_state.word_yanlis_sayisi}  |  "
        f"📊 Başarı: %{basari_yuzdesi}  |  "
        f"🏆 En uzun seri: {st.session_state.word_en_uzun_seri}"
    )