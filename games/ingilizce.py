import streamlit as st
import random
from core.state import go_to

# =========================================================================
# 4. SINIF İNGİLİZCE MÜFREDATINA UYGUN SÖZCÜK KATEGORİLERİ
# =========================================================================
# Kaynak: MEB 4. sınıf İngilizce dersi temel kelime dağarcığı üniteleri
#   - Hayvanlar (Animals)
#   - Renkler (Colours)
#   - Yiyecekler (Food)
#   - Aile (Family)
#   - Okul Eşyaları (Classroom Objects)
#   - Sayılar (Numbers)

PUAN_KAZANC = 10
HEDEF_PUAN = 100

QUESTION_BANK = {
    "hayvanlar": {
        "label": "Animals",
        "icon": "🐾",
        "items": [
            ("Gökyüzünde süzülen neşeli dostumuz: 'Bird' ne demektir? 🐦", "Kuş"),
            ("Denizlerde yüzen sevimli dostumuz: 'Fish' ne anlama gelir? 🐟", "Balık"),
            ("En sevdiğimiz hayvanlardan biri: 'Cat' hangi hayvandır? 🐱", "Kedi"),
            ("İnsanın en sadık dostu: 'Dog' hangi hayvandır? 🐶", "Köpek"),
            ("Havuçları çok seven, uzun kulaklı hayvan: 'Rabbit' nedir? 🐰", "Tavşan"),
            ("Çiftlikte yaşayan, süt veren hayvan: 'Cow' nedir? 🐄", "İnek"),
            ("Ormanların kralı: 'Lion' hangi hayvandır? 🦁", "Aslan"),
            ("Sabah erkenden öten çiftlik hayvanı: 'Rooster' nedir? 🐓", "Horoz"),
        ],
    },
    "renkler": {
        "label": "Colours",
        "icon": "🎨",
        "items": [
            ("Gökkuşağındaki en tatlı renklerden biri: 'Pink' hangi renktir? 🌸", "Pembe"),
            ("Güneşin o sıcak rengi: 'Yellow' hangi renktir? ☀️", "Sarı"),
            ("Çimenlerin ve yaprakların rengi: 'Green' hangi renktir? 🌿", "Yeşil"),
            ("Gökyüzünün açık havadaki rengi: 'Blue' hangi renktir? 💙", "Mavi"),
            ("Elmaların çoğu zaman rengi: 'Red' hangi renktir? ❤️", "Kırmızı"),
            ("Karın ve bulutların rengi: 'White' hangi renktir? ☁️", "Beyaz"),
            ("Gecenin ve karanlığın rengi: 'Black' hangi renktir? 🌑", "Siyah"),
            ("Portakalın kabuğunun rengi: 'Orange' hangi renktir? 🍊", "Turuncu"),
        ],
    },
    "yiyecekler": {
        "label": "Food",
        "icon": "🍎",
        "items": [
            ("Yazın yemeyi çok sevdiğimiz meyve: 'Apple' hangisidir? 🍎", "Elma"),
            ("Maymunların en sevdiği meyve: 'Banana' hangisidir? 🍌", "Muz"),
            ("Kahvaltıda içtiğimiz beyaz içecek: 'Milk' nedir? 🥛", "Süt"),
            ("Fırından çıkan, ekmeğin kardeşi: 'Bread' nedir? 🍞", "Ekmek"),
            ("Tavuklardan elde ettiğimiz besin: 'Egg' nedir? 🥚", "Yumurta"),
            ("Kırmızı, tatlı ve sulu bir yaz meyvesi: 'Watermelon' nedir? 🍉", "Karpuz"),
            ("İtalyanların meşhur yemeği: 'Pasta' nedir? 🍝", "Makarna"),
            ("Soğuk günlerde içtiğimiz sıcak içecek: 'Tea' nedir? 🍵", "Çay"),
        ],
    },
    "aile": {
        "label": "Family",
        "icon": "👪",
        "items": [
            ("Bizi büyüten ve çok seven kadın: 'Mother' kimdir? 👩", "Anne"),
            ("Bizi büyüten ve çok seven erkek: 'Father' kimdir? 👨", "Baba"),
            ("Bizden büyük olan kız kardeş: 'Sister' kimdir? 👧", "Kız kardeş"),
            ("Bizden büyük olan erkek kardeş: 'Brother' kimdir? 👦", "Erkek kardeş"),
            ("Annemizin ya da babamızın annesi: 'Grandmother' kimdir? 👵", "Büyükanne"),
            ("Annemizin ya da babamızın babası: 'Grandfather' kimdir? 👴", "Büyükbaba"),
            ("Ailenin en küçük üyesi olabilir: 'Baby' kimdir? 👶", "Bebek"),
        ],
    },
    "okul_esyalari": {
        "label": "Classroom Objects",
        "icon": "🎒",
        "items": [
            ("Sırtımıza takıp okula taşıdığımız eşya: 'Bag' nedir? 🎒", "Çanta"),
            ("Yazı yazmak için kullandığımız araç: 'Pencil' nedir? ✏️", "Kalem"),
            ("Yazdıklarımızı sildiğimiz araç: 'Eraser' nedir? 🧹", "Silgi"),
            ("Ders çalıştığımız, üzerine yazı yazdığımız yaprak: 'Book' nedir? 📕", "Kitap"),
            ("Resim yaptığımız veya yazı yazdığımız kağıt yaprak: 'Paper' nedir? 📄", "Kağıt"),
            ("Öğretmenimizin tahtaya yazı yazdığı şey: 'Board' nedir? 🖊️", "Tahta"),
            ("Kalemleri koyduğumuz kutu: 'Pencil case' nedir? 🖍️", "Kalem kutusu"),
        ],
    },
    "sayilar": {
        "label": "Numbers",
        "icon": "🔢",
        "items": [
            ("İngilizce 'one' sayısı hangi sayıya karşılık gelir?", "1"),
            ("İngilizce 'three' sayısı hangi sayıya karşılık gelir?", "3"),
            ("İngilizce 'five' sayısı hangi sayıya karşılık gelir?", "5"),
            ("İngilizce 'seven' sayısı hangi sayıya karşılık gelir?", "7"),
            ("İngilizce 'ten' sayısı hangi sayıya karşılık gelir?", "10"),
            ("İngilizce 'four' sayısı hangi sayıya karşılık gelir?", "4"),
            ("İngilizce 'eight' sayısı hangi sayıya karşılık gelir?", "8"),
            ("İngilizce 'two' sayısı hangi sayıya karşılık gelir?", "2"),
        ],
    },
}

CATEGORY_KEYS = list(QUESTION_BANK.keys())

# İngilizce odasına özel arka plan müziği
ARKA_PLAN_MUZIGI_URL = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3"

TEBRIK_MESAJLARI = [
    "Excellent! Harika bir tahmin Roza! 🌟",
    "Very good! İngilizce kraliçesi canım kızım benim! 🎉 +10 Puan!",
    "Amazing! Kelimeyi saniyeler içinde bildin! 👑",
    "İşte bu kadar! Roza yeni diller öğreniyor! 🌍✨",
    "Great job! Süpersin Roza! 🏆",
]

SERI_MESAJLARI = {
    3: "3'te 3! Seri devam ediyor! 🔥",
    5: "5 doğru üst üste! İnanılmazsın! 🔥🔥",
    10: "10'luk seri! Sen bir dil dahisisin! 🔥🔥🔥",
}

SESSION_DEFAULTS = {
    "eng_dogru_sayisi": 0,
    "eng_yanlis_sayisi": 0,
    "eng_seri": 0,
    "eng_en_uzun_seri": 0,
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


def generate_english_question(active_categories: list[str]):
    """Seçili kategorilerden 4. sınıf seviyesine uygun bir İngilizce sorusu üretir."""
    category = random.choice(active_categories)
    ipucu, dogru_cevap = random.choice(QUESTION_BANK[category]["items"])

    # Aynı soru art arda gelmesin diye son soruyla karşılaştırıyoruz
    if st.session_state.get("eng_last_question") == ipucu and len(
        QUESTION_BANK[category]["items"]
    ) > 1:
        return generate_english_question(active_categories)
    st.session_state.eng_last_question = ipucu

    yanlis_siklar = generate_wrong_options(category, dogru_cevap)
    all_options = yanlis_siklar + [dogru_cevap]
    random.shuffle(all_options)

    kategori_etiketi = f"{QUESTION_BANK[category]['icon']} {QUESTION_BANK[category]['label']}"
    return ipucu, dogru_cevap, all_options, kategori_etiketi


def _reset_game_state():
    """Puan ve istatistikleri sıfırlar, aktif soruyu temizler."""
    st.session_state.total_score = 0
    for key, default in SESSION_DEFAULTS.items():
        st.session_state[key] = default
    for key in ["eng_correct", "eng_answer", "eng_last_question", "eng_ipucu", "eng_opts", "eng_kategori"]:
        st.session_state.pop(key, None)


def render_ingilizce_game():
    """Çoktan seçmeli, kategorili, seri takipli ve müzikli İngilizce Kelime Oyunu"""
    st.subheader("🌍 İngilizce Dünyası")

    # --- ÜST AYAR ÇUBUĞU: Müzik ve Kategori Seçimi (veli kontrolü için) ---
    ayar_col1, ayar_col2 = st.columns([1, 2])
    with ayar_col1:
        muzik_ac = st.toggle("🎵 Müzik", value=st.session_state.get("eng_muzik_ac", True))
        st.session_state.eng_muzik_ac = muzik_ac
        if muzik_ac:
            st.audio(ARKA_PLAN_MUZIGI_URL, format="audio/mp3")
    with ayar_col2:
        secili_kategoriler = st.multiselect(
            "Çalışılacak kelime türleri:",
            options=CATEGORY_KEYS,
            default=st.session_state.get("eng_secili_kategoriler", CATEGORY_KEYS),
            format_func=lambda k: f"{QUESTION_BANK[k]['icon']} {QUESTION_BANK[k]['label']}",
        )
    if not secili_kategoriler:
        secili_kategoriler = CATEGORY_KEYS
        st.info("En az bir kategori seçmelisin, şimdilik tüm kategoriler dahil edildi. 🙂")
    st.session_state.eng_secili_kategoriler = secili_kategoriler

    # İstatistik alanları başlatılmamışsa hazırla
    for key, default in SESSION_DEFAULTS.items():
        if key not in st.session_state:
            st.session_state[key] = default

    # --- HEDEF PUAN KUTLAMA EKRANI ---
    if st.session_state.total_score >= HEDEF_PUAN:
        st.balloons()
        st.markdown(f"""
        <div style="background-color: #FEEBC8; padding: 30px; border-radius: 20px; text-align: center; border: 3px solid #DD6B20;">
            <h1 style="color: #DD6B20; margin-bottom: 10px;">🎉 ENGLISH CHAMPION ROZA! 🎉</h1>
            <h2 style="color: #4A5568;">Wonderful! Canım Kızım Benim! 👑</h2>
            <p style="font-size: 18px; color: #718096;">İngilizce kelimelerin hepsini bilerek {HEDEF_PUAN} puana ulaştın! 🏆</p>
            <p style="font-size: 15px; color: #718096;">En uzun doğru serin: {st.session_state.eng_en_uzun_seri} 🔥</p>
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
    if "eng_correct" not in st.session_state:
        ipucu, corr, opts, kategori_etiketi = generate_english_question(secili_kategoriler)
        st.session_state.eng_ipucu = ipucu
        st.session_state.eng_correct = corr
        st.session_state.eng_opts = opts
        st.session_state.eng_kategori = kategori_etiketi

    ipucu = st.session_state.eng_ipucu
    correct_answer = st.session_state.eng_correct
    options = st.session_state.eng_opts
    kategori_etiketi = st.session_state.eng_kategori

    # --- ÜST BİLGİ ÇUBUĞU: Puan, Seri ---
    c1, c2 = st.columns(2)
    c1.metric("Puan", st.session_state.total_score)
    c2.metric("Seri 🔥", st.session_state.eng_seri)
    st.progress(min(st.session_state.total_score / HEDEF_PUAN, 1.0))

    # Sorunun yeşil/doğa tonlarında şık tasarımı
    st.markdown(f"""
    <div style="background-color: #E6FFFA; padding: 25px; border-radius: 15px; text-align: center; margin-bottom: 15px; border: 2px solid #319795;">
        <span style="font-size: 14px; color: #234E52; font-weight: bold;">{kategori_etiketi}</span>
        <h3 style="color: #2D3748; margin: 10px 0 0 0; font-size: 22px;">{ipucu}</h3>
    </div>
    """, unsafe_allow_html=True)

    secilen_sik = st.radio(
        "Doğru Türkçe karşılığını seç:",
        options=options,
        index=None,
        key="eng_radio",
    )

    st.write("")

    c1, c2 = st.columns(2)
    with c1:
        if st.button("Cevabı Kontrol Et ✨", type="primary", use_container_width=True, disabled=(secilen_sik is None)):
            if secilen_sik == correct_answer:
                st.success(random.choice(TEBRIK_MESAJLARI))
                st.session_state.total_score += PUAN_KAZANC
                st.session_state.eng_dogru_sayisi += 1
                st.session_state.eng_seri += 1
                st.session_state.eng_en_uzun_seri = max(
                    st.session_state.eng_en_uzun_seri, st.session_state.eng_seri
                )
                if st.session_state.eng_seri in SERI_MESAJLARI:
                    st.toast(SERI_MESAJLARI[st.session_state.eng_seri])

                del st.session_state.eng_correct
                st.rerun()
            else:
                st.error(f"Küçük bir dil karışıklığı oldu, doğru cevap **{correct_answer}** idi. Tekrar dene Roza! 💪")
                st.session_state.eng_yanlis_sayisi += 1
                st.session_state.eng_seri = 0

    with c2:
        if st.button("Ana Menüye Dön 🏠", use_container_width=True):
            if "eng_correct" in st.session_state:
                del st.session_state.eng_correct
            go_to("menu")

    # --- ALT BİLGİ: Toplam doğru/yanlış ve başarı yüzdesi ---
    toplam_soru = st.session_state.eng_dogru_sayisi + st.session_state.eng_yanlis_sayisi
    basari_yuzdesi = (
        round(100 * st.session_state.eng_dogru_sayisi / toplam_soru) if toplam_soru > 0 else 0
    )
    st.caption(
        f"✅ Doğru: {st.session_state.eng_dogru_sayisi}  |  "
        f"❌ Yanlış: {st.session_state.eng_yanlis_sayisi}  |  "
        f"📊 Başarı: %{basari_yuzdesi}  |  "
        f"🏆 En uzun seri: {st.session_state.eng_en_uzun_seri}"
    )