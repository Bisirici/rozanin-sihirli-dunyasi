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
    ("Gece gökyüzünde bazen tam, bazen yarım görünen gök cismi hangisidir? 🌙", "Ay"),
    ("Yağmurdan sonra gökyüzünde oluşan rengârenk yay nedir? 🌈", "Gökkuşağı"),
    ("Ağaçların yapraklarını döktüğü mevsim hangisidir? 🍂", "Sonbahar"),
    ("Çiçeklerin açtığı ve doğanın canlandığı mevsim hangisidir? 🌸", "İlkbahar"),
    ("Dünyamızın etrafında dönen gök cismi hangisidir? 🌍", "Ay"),
    ("En büyük kara hayvanı hangisidir? 🐘", "Fil"),
    ("Boynu çok uzun olan Afrika hayvanı hangisidir? 🦒", "Zürafa"),
    ("Sırtında kabuğunu taşıyan yavaş hayvan hangisidir? 🐢", "Kaplumbağa"),
    ("Kış uykusuna yatan iri orman hayvanı hangisidir? 🐻", "Ayı"),
    ("Bal yapan çalışkan böcek hangisidir? 🍯", "Arı"),
    ("Sekiz kola sahip deniz canlısı hangisidir? 🐙", "Ahtapot"),
    ("Çölde yaşayan ve hörgücü bulunan hayvan hangisidir? 🐫", "Deve"),
    ("En hızlı koşan kara hayvanı hangisidir? 🐆", "Çita"),
    ("Penguenler en çok hangi kıtada yaşar? 🧊", "Antarktika"),
    ("Kendi ağını ören küçük canlı hangisidir? 🕸️", "Örümcek"),
    ("Bitkilerin topraktan su çekmesini sağlayan kısmı nedir? 🌱", "Kök"),
    ("Ağaçların oksijen üretmesini sağlayan yeşil bölümü hangisidir? 🍃", "Yaprak"),
    ("Meyvenin içinde bulunan ve yeni bitkiyi oluşturan yapı nedir? 🌰", "Tohum"),
    ("İnsan vücudunda kanı pompalayan organ hangisidir? ❤️", "Kalp"),
    ("Nefes almamızı sağlayan organımız hangisidir? 🫁", "Akciğer"),
    ("Düşündüğümüz ve öğrendiğimiz organımız hangisidir? 🧠", "Beyin"),
    ("Haftanın yedinci günü hangisidir? 📅", "Pazar"),
    ("Bir yılda kaç mevsim vardır? 🍀", "Dört"),
    ("Bir haftada kaç gün bulunur? 🗓️", "Yedi"),
    ("Saati icat edilmeden önce insanlar zamanı görmek için gökyüzünde en çok neye bakardı? ☀️", "Güneş"),
    ("Mektupların gönderildiği kurumun adı nedir? 📮", "Postane"),
    ("Hasta olduğumuzda gittiğimiz sağlık kurumu hangisidir? 🏥", "Hastane"),
    ("Yangın çıktığında yardım istediğimiz ekip hangisidir? 🚒", "İtfaiye"),
    ("Suçları önleyen ve güvenliği sağlayan meslek hangisidir? 👮", "Polis"),
    ("Öğrencilere ders anlatan kişinin mesleği nedir? 👩‍🏫", "Öğretmen"),
    ("Türkiye'nin başkenti neresidir? 🇹🇷", "Ankara"),
    ("Üç tarafı denizlerle çevrili ülkemizin adı nedir? 🇹🇷", "Türkiye"),
    ("Türk bayrağındaki yıldızın yanında bulunan şekil nedir? 🇹🇷", "Hilal"),
    ("En yakın yıldızımızın adı nedir? ☀️", "Güneş"),
    ("Dünya'nın üzerinde yaşadığımız kısmına ne denir? 🌍", "Yeryüzü"),
    ("Yağmur, kar ve dolu gibi olayların genel adına ne denir? 🌦️", "Yağış"),
    ("Elektrik kesildiğinde etrafı aydınlatmak için kullanılan taşınabilir ışık nedir? 🔦", "El feneri"),
    ("Harfleri bir araya getirerek oluşturduğumuz anlamlı yapıya ne denir? 🔤", "Kelime"),
    ("Kelimelerin bir araya gelmesiyle oluşan yapıya ne denir? 📝", "Cümle"),
    ("12 ayın tamamına verilen ortak ad nedir? 📆", "Yıl"),
    ("Güneş'in doğduğu yön hangisidir? 🌅", "Doğu"),
    ("Güneş'in battığı yön hangisidir? 🌇", "Batı"),
    ("Pusulada kuzeyi gösteren harf hangisidir? 🧭", "K"),
    ("Yeryüzünün büyük bölümünü kaplayan tuzlu su kütlesine ne denir? 🌊", "Okyanus"),
    ("İki kıtayı birbirinden ayıran dar su geçidine ne ad verilir? 🚢", "Boğaz")
    ("İki kere iki kaç eder? ➕", "Dört"),
    ("Bir elinde 5, diğer elinde 5 parmak vardır. Toplam kaç parmak vardır? ✋", "On"),
    ("Haftada kaç gün vardır? 📅", "Yedi"),
    ("Bir üçgenin kaç köşesi vardır? 🔺", "Üç"),
    ("Bir örümceğin kaç bacağı vardır? 🕷️", "Sekiz"),
    ("Bir bisikletin kaç tekerleği vardır? 🚲", "İki"),
    ("Bir ördeğin iki ayağı varsa, iki ördeğin toplam kaç ayağı vardır? 🦆", "Dört"),
    ("3'ten sonra hangi sayı gelir? 🔢", "Dört"),
    ("10'dan önce hangi sayı gelir? 🔢", "Dokuz"),
    ("Yarım elmanın diğer yarısına ne denir? 🍎", "Yarım"),
    ("Ben konuşamam ama bana ne söylersen onu tekrar ederim. Ben neyim? 🗣️", "Yankı"),
    ("Kanatlarım var ama uçamam. Ben neyim? 🐧", "Penguen"),
    ("Ayağı var ama yürüyemez. Ben neyim? 🪑", "Masa"),
    ("Dişleri vardır ama yemek yemez. Ben neyim? 🪮", "Tarak"),
    ("Yüzü vardır ama gözü yoktur. Ben neyim? 🕒", "Saat"),
    ("Ağzı vardır ama konuşamaz. Ben neyim? 🏞️", "Mağara"),
    ("Kolları vardır ama sarılamaz. Ben neyim? 👕", "Gömlek"),
    ("Her gün büyür ama hiç canlı değildir. Ben neyim? 📅", "Takvim"),
    ("Bir tavuk günde bir yumurta yaparsa, iki tavuk bir günde kaç yumurta yapar? 🥚", "İki"),
    ("Bir arabada 4 tekerlek vardır. İki arabada kaç tekerlek olur? 🚗", "Sekiz"),
    ("Bir kedinin 4 ayağı vardır. Üç kedinin toplam kaç ayağı vardır? 🐈", "Oniki"),
    ("5 elmanın 2'sini yersen geriye kaç elma kalır? 🍏", "Üç"),
    ("En hafif sayı hangisidir? Çünkü içinde tüy vardır. 😄", "Üç"),
    ("Gece ortaya çıkar, sabah kaybolurum. Ben neyim? 🌙", "Ay"),
    ("Beni kullandıkça küçülürüm. Ben neyim? 🕯️", "Mum"),
    ("Kırılınca sesi çıkar ama kendisi konuşmaz. Ben neyim? 🥚", "Yumurta"),
    ("Anahtarı vardır ama kapı açmaz. Ben neyim? 🎹", "Piyano"),
    ("Sayfaları vardır ama ağaç değildir. Ben neyim? 📖", "Kitap"),
    ("Kolları döner ama yorulmaz. Ben neyim? 🌬️", "Vantilatör"),
    ("İçinde su vardır ama deniz değildir. Ben neyim? 🚰", "Şişe"),
    ("Bir odada 4 kedi var. Her kedinin karşısında 3 kedi var. Odada toplam kaç kedi vardır? 🐱", "Dört"),
    ("Bir çiçeğin 5 yaprağı varsa, iki çiçeğin toplam kaç yaprağı olur? 🌸", "On"),
    ("Bir düzinede kaç tane bulunur? 📦", "Oniki"),
    ("Hangisi daha ağırdır: 1 kilogram pamuk mu, 1 kilogram demir mi? ⚖️", "Eşit"),
    ("Saat tam 12'yi gösteriyorsa, akrep ile yelkovan nerededir? 🕛", "Üstte"),
    ("En son hangi ay gelir? 📆", "Aralık"),
    ("Benim iki elim var ama alkış yapamam. Ben neyim? ⏰", "Saat"),
    ("Ne kadar çok yıkarsan o kadar kirlenir. Ben neyim? 💧", "Su"),
    ("Ağzı vardır ama yemek yiyemez. Boynu vardır ama başı yoktur. Ben neyim? 🍾", "Şişe"),
    ("Dünyanın etrafında döner ama hiç yorulmaz. Ben neyim? 🌕", "Ay")        
        ],
    },
    "es_anlamli": {
        "label": "Eş Anlamlı Kelime",
        "icon": "🔁",
        "items": [
    ("\"Ad\" kelimesinin eş anlamlısı hangisidir?", "İsim"),
    ("\"İsim\" kelimesinin eş anlamlısı hangisidir?", "Ad"),
    ("\"Anı\" kelimesinin eş anlamlısı hangisidir?", "Hatıra"),
    ("\"Hatıra\" kelimesinin eş anlamlısı hangisidir?", "Anı"),
    ("\"Araç\" kelimesinin eş anlamlısı hangisidir?", "Vasıta"),
    ("\"Asır\" kelimesinin eş anlamlısı hangisidir?", "Yüzyıl"),
    ("\"Acele\" kelimesinin eş anlamlısı hangisidir?", "Çabuk"),
    ("\"Ak\" kelimesinin eş anlamlısı hangisidir?", "Beyaz"),
    ("\"Beyaz\" kelimesinin eş anlamlısı hangisidir?", "Ak"),
    ("\"Kara\" kelimesinin eş anlamlısı hangisidir?", "Siyah"),
    ("\"Siyah\" kelimesinin eş anlamlısı hangisidir?", "Kara"),
    ("\"Büyük\" kelimesinin eş anlamlısı hangisidir?", "İri"),
    ("\"İri\" kelimesinin eş anlamlısı hangisidir?", "Büyük"),
    ("\"Küçük\" kelimesinin eş anlamlısı hangisidir?", "Ufak"),
    ("\"Ufak\" kelimesinin eş anlamlısı hangisidir?", "Küçük"),
    ("\"Akıllı\" kelimesinin eş anlamlısı hangisidir?", "Zeki"),
    ("\"Zeki\" kelimesinin eş anlamlısı hangisidir?", "Akıllı"),
    ("\"Mutlu\" kelimesinin eş anlamlısı hangisidir?", "Sevinçli"),
    ("\"Sevinçli\" kelimesinin eş anlamlısı hangisidir?", "Mutlu"),
    ("\"Üzgün\" kelimesinin eş anlamlısı hangisidir?", "Kederli"),
    ("\"Kederli\" kelimesinin eş anlamlısı hangisidir?", "Üzgün"),
    ("\"Çabuk\" kelimesinin eş anlamlısı hangisidir?", "Hızlı"),
    ("\"Hızlı\" kelimesinin eş anlamlısı hangisidir?", "Süratli"),
    ("\"Süratli\" kelimesinin eş anlamlısı hangisidir?", "Hızlı"),
    ("\"Doktor\" kelimesinin eş anlamlısı hangisidir?", "Hekim"),
    ("\"Hekim\" kelimesinin eş anlamlısı hangisidir?", "Doktor"),
    ("\"Cevap\" kelimesinin eş anlamlısı hangisidir?", "Yanıt"),
    ("\"Yanıt\" kelimesinin eş anlamlısı hangisidir?", "Cevap"),
    ("\"Misafir\" kelimesinin eş anlamlısı hangisidir?", "Konuk"),
    ("\"Konuk\" kelimesinin eş anlamlısı hangisidir?", "Misafir"),
    ("\"Fayda\" kelimesinin eş anlamlısı hangisidir?", "Yarar"),
    ("\"Yarar\" kelimesinin eş anlamlısı hangisidir?", "Fayda"),
    ("\"Görev\" kelimesinin eş anlamlısı hangisidir?", "Vazife"),
    ("\"Vazife\" kelimesinin eş anlamlısı hangisidir?", "Görev"),
    ("\"Yoksul\" kelimesinin eş anlamlısı hangisidir?", "Fakir"),
    ("\"Fakir\" kelimesinin eş anlamlısı hangisidir?", "Yoksul"),
    ("\"Zengin\" kelimesinin eş anlamlısı hangisidir?", "Varlıklı"),
    ("\"Varlıklı\" kelimesinin eş anlamlısı hangisidir?", "Zengin"),
    ("\"Şehir\" kelimesinin eş anlamlısı hangisidir?", "Kent"),
    ("\"Kent\" kelimesinin eş anlamlısı hangisidir?", "Şehir"),
    ("\"Doğa\" kelimesinin eş anlamlısı hangisidir?", "Tabiat"),
    ("\"Tabiat\" kelimesinin eş anlamlısı hangisidir?", "Doğa"),
    ("\"Yurt\" kelimesinin eş anlamlısı hangisidir?", "Vatan"),
    ("\"Vatan\" kelimesinin eş anlamlısı hangisidir?", "Yurt"),
    ("\"Öykü\" kelimesinin eş anlamlısı hangisidir?", "Hikâye"),
    ("\"Hikâye\" kelimesinin eş anlamlısı hangisidir?", "Öykü"),
    ("\"İmkân\" kelimesinin eş anlamlısı hangisidir?", "Olanak"),
    ("\"Olanak\" kelimesinin eş anlamlısı hangisidir?", "İmkân"),
    ("\"Kalp\" kelimesinin eş anlamlısı hangisidir?", "Yürek"),
    ("\"Yürek\" kelimesinin eş anlamlısı hangisidir?", "Kalp"),
    ("\"Düş\" kelimesinin eş anlamlısı hangisidir?", "Rüya"),
    ("\"Rüya\" kelimesinin eş anlamlısı hangisidir?", "Düş"),
    ("\"Yıl\" kelimesinin eş anlamlısı hangisidir?", "Sene"),
    ("\"Sene\" kelimesinin eş anlamlısı hangisidir?", "Yıl"),
    ("\"Yüzyıl\" kelimesinin eş anlamlısı hangisidir?", "Asır"),
    ("\"Cesur\" kelimesinin eş anlamlısı hangisidir?", "Yiğit"),
    ("\"Yiğit\" kelimesinin eş anlamlısı hangisidir?", "Cesur"),
    ("\"Öğrenci\" kelimesinin eş anlamlısı hangisidir?", "Talebe"),
    ("\"Talebe\" kelimesinin eş anlamlısı hangisidir?", "Öğrenci"),
    ("\"Okul\" kelimesinin eş anlamlısı hangisidir?", "Mektep"),
    ("\"Mektep\" kelimesinin eş anlamlısı hangisidir?", "Okul"),
    ("\"Ev\" kelimesinin eş anlamlısı hangisidir?", "Konut"),
    ("\"Konut\" kelimesinin eş anlamlısı hangisidir?", "Ev"),
    ("\"Ulus\" kelimesinin eş anlamlısı hangisidir?", "Millet"),
    ("\"Millet\" kelimesinin eş anlamlısı hangisidir?", "Ulus"),
    ("\"Söylemek\" kelimesinin eş anlamlısı hangisidir?", "Konuşmak"),
    ("\"Konuşmak\" kelimesinin eş anlamlısı hangisidir?", "Söylemek"),
    ("\"Yetenek\" kelimesinin eş anlamlısı hangisidir?", "Kabiliyet"),
    ("\"Kabiliyet\" kelimesinin eş anlamlısı hangisidir?", "Yetenek"),
    ("\"Sınav\" kelimesinin eş anlamlısı hangisidir?", "İmtihan"),
    ("\"İmtihan\" kelimesinin eş anlamlısı hangisidir?", "Sınav"),
    ("\"Lüzum\" kelimesinin eş anlamlısı hangisidir?", "Gerek"),
    ("\"Gerek\" kelimesinin eş anlamlısı hangisidir?", "Lüzum"),
    ("\"Ödül\" kelimesinin eş anlamlısı hangisidir?", "Mükâfat"),
    ("\"Mükâfat\" kelimesinin eş anlamlısı hangisidir?", "Ödül"),
    ("\"Barış\" kelimesinin eş anlamlısı hangisidir?", "Sulh"),
    ("\"Sulh\" kelimesinin eş anlamlısı hangisidir?", "Barış"),
    ("\"Yurtsever\" kelimesinin eş anlamlısı hangisidir?", "Vatansever"),
    ("\"Vatansever\" kelimesinin eş anlamlısı hangisidir?", "Yurtsever"),
    ("\"Misal\" kelimesinin eş anlamlısı hangisidir?", "Örnek"),
    ("\"Örnek\" kelimesinin eş anlamlısı hangisidir?", "Misal"),
    ("\"Sebep\" kelimesinin eş anlamlısı hangisidir?", "Neden"),
    ("\"Neden\" kelimesinin eş anlamlısı hangisidir?", "Sebep"),
    ("\"Cümle\" kelimesinin eş anlamlısı hangisidir?", "Tümce"),
    ("\"Tümce\" kelimesinin eş anlamlısı hangisidir?", "Cümle"),
    ("\"Doğal\" kelimesinin eş anlamlısı hangisidir?", "Tabii"),
    ("\"Tabii\" kelimesinin eş anlamlısı hangisidir?", "Doğal"),
    ("\"İlave\" kelimesinin eş anlamlısı hangisidir?", "Ek"),
    ("\"Ek\" kelimesinin eş anlamlısı hangisidir?", "İlave"),
    ("\"Medeniyet\" kelimesinin eş anlamlısı hangisidir?", "Uygarlık"),
    ("\"Uygarlık\" kelimesinin eş anlamlısı hangisidir?", "Medeniyet"),
    ("\"Yöntem\" kelimesinin eş anlamlısı hangisidir?", "Metot"),
    ("\"Metot\" kelimesinin eş anlamlısı hangisidir?", "Yöntem"),
    ("\"Sual\" kelimesinin eş anlamlısı hangisidir?", "Soru"),
    ("\"Soru\" kelimesinin eş anlamlısı hangisidir?", "Sual"),
    ("\"Civar\" kelimesinin eş anlamlısı hangisidir?", "Çevre"),
    ("\"Çevre\" kelimesinin eş anlamlısı hangisidir?", "Civar")
        ],
    },
    "zit_anlamli": {
        "label": "Zıt Anlamlı Kelime",
        "icon": "↔️",
        "items": [
            ("\"Uzun\" kelimesinin zıt anlamlısı hangisidir?", "Kısa"),
    ("\"Kısa\" kelimesinin zıt anlamlısı hangisidir?", "Uzun"),
    ("\"Sıcak\" kelimesinin zıt anlamlısı hangisidir?", "Soğuk"),
    ("\"Soğuk\" kelimesinin zıt anlamlısı hangisidir?", "Sıcak"),
    ("\"Aydınlık\" kelimesinin zıt anlamlısı hangisidir?", "Karanlık"),
    ("\"Karanlık\" kelimesinin zıt anlamlısı hangisidir?", "Aydınlık"),
    ("\"Mutlu\" kelimesinin zıt anlamlısı hangisidir?", "Üzgün"),
    ("\"Üzgün\" kelimesinin zıt anlamlısı hangisidir?", "Mutlu"),
    ("\"Hızlı\" kelimesinin zıt anlamlısı hangisidir?", "Yavaş"),
    ("\"Yavaş\" kelimesinin zıt anlamlısı hangisidir?", "Hızlı"),
    ("\"Kalın\" kelimesinin zıt anlamlısı hangisidir?", "İnce"),
    ("\"İnce\" kelimesinin zıt anlamlısı hangisidir?", "Kalın"),
    ("\"Temiz\" kelimesinin zıt anlamlısı hangisidir?", "Kirli"),
    ("\"Kirli\" kelimesinin zıt anlamlısı hangisidir?", "Temiz"),
    ("\"Doğru\" kelimesinin zıt anlamlısı hangisidir?", "Yanlış"),
    ("\"Yanlış\" kelimesinin zıt anlamlısı hangisidir?", "Doğru"),
    ("\"Kolay\" kelimesinin zıt anlamlısı hangisidir?", "Zor"),
    ("\"Zor\" kelimesinin zıt anlamlısı hangisidir?", "Kolay"),
    ("\"Sevinçli\" kelimesinin zıt anlamlısı hangisidir?", "Kederli"),
    ("\"Kederli\" kelimesinin zıt anlamlısı hangisidir?", "Sevinçli"),
    ("\"Genç\" kelimesinin zıt anlamlısı hangisidir?", "Yaşlı"),
    ("\"Yaşlı\" kelimesinin zıt anlamlısı hangisidir?", "Genç"),
    ("\"Erken\" kelimesinin zıt anlamlısı hangisidir?", "Geç"),
    ("\"Geç\" kelimesinin zıt anlamlısı hangisidir?", "Erken"),
    ("\"Aç\" kelimesinin zıt anlamlısı hangisidir?", "Tok"),
    ("\"Tok\" kelimesinin zıt anlamlısı hangisidir?", "Aç"),
    ("\"Yeni\" kelimesinin zıt anlamlısı hangisidir?", "Eski"),
    ("\"Eski\" kelimesinin zıt anlamlısı hangisidir?", "Yeni"),
    ("\"Büyük\" kelimesinin zıt anlamlısı hangisidir?", "Küçük"),
    ("\"Küçük\" kelimesinin zıt anlamlısı hangisidir?", "Büyük"),
    ("\"Yüksek\" kelimesinin zıt anlamlısı hangisidir?", "Alçak"),
    ("\"Alçak\" kelimesinin zıt anlamlısı hangisidir?", "Yüksek"),
    ("\"İleri\" kelimesinin zıt anlamlısı hangisidir?", "Geri"),
    ("\"Geri\" kelimesinin zıt anlamlısı hangisidir?", "İleri"),
    ("\"Alt\" kelimesinin zıt anlamlısı hangisidir?", "Üst"),
    ("\"Üst\" kelimesinin zıt anlamlısı hangisidir?", "Alt"),
    ("\"İç\" kelimesinin zıt anlamlısı hangisidir?", "Dış"),
    ("\"Dış\" kelimesinin zıt anlamlısı hangisidir?", "İç"),
    ("\"Sağ\" kelimesinin zıt anlamlısı hangisidir?", "Sol"),
    ("\"Sol\" kelimesinin zıt anlamlısı hangisidir?", "Sağ"),
    ("\"Sabah\" kelimesinin zıt anlamlısı hangisidir?", "Akşam"),
    ("\"Akşam\" kelimesinin zıt anlamlısı hangisidir?", "Sabah"),
    ("\"Gündüz\" kelimesinin zıt anlamlısı hangisidir?", "Gece"),
    ("\"Gece\" kelimesinin zıt anlamlısı hangisidir?", "Gündüz"),
    ("\"Yakın\" kelimesinin zıt anlamlısı hangisidir?", "Uzak"),
    ("\"Uzak\" kelimesinin zıt anlamlısı hangisidir?", "Yakın"),
    ("\"Ön\" kelimesinin zıt anlamlısı hangisidir?", "Arka"),
    ("\"Arka\" kelimesinin zıt anlamlısı hangisidir?", "Ön"),
    ("\"Dolu\" kelimesinin zıt anlamlısı hangisidir?", "Boş"),
    ("\"Boş\" kelimesinin zıt anlamlısı hangisidir?", "Dolu"),
    ("\"Canlı\" kelimesinin zıt anlamlısı hangisidir?", "Cansız"),
    ("\"Cansız\" kelimesinin zıt anlamlısı hangisidir?", "Canlı"),
    ("\"Güçlü\" kelimesinin zıt anlamlısı hangisidir?", "Güçsüz"),
    ("\"Güçsüz\" kelimesinin zıt anlamlısı hangisidir?", "Güçlü"),
    ("\"Çalışkan\" kelimesinin zıt anlamlısı hangisidir?", "Tembel"),
    ("\"Tembel\" kelimesinin zıt anlamlısı hangisidir?", "Çalışkan"),
    ("\"Cesur\" kelimesinin zıt anlamlısı hangisidir?", "Korkak"),
    ("\"Korkak\" kelimesinin zıt anlamlısı hangisidir?", "Cesur"),
    ("\"Zengin\" kelimesinin zıt anlamlısı hangisidir?", "Fakir"),
    ("\"Fakir\" kelimesinin zıt anlamlısı hangisidir?", "Zengin"),
    ("\"Açık\" kelimesinin zıt anlamlısı hangisidir?", "Kapalı"),
    ("\"Kapalı\" kelimesinin zıt anlamlısı hangisidir?", "Açık"),
    ("\"Sert\" kelimesinin zıt anlamlısı hangisidir?", "Yumuşak"),
    ("\"Yumuşak\" kelimesinin zıt anlamlısı hangisidir?", "Sert"),
    ("\"Tatlı\" kelimesinin zıt anlamlısı hangisidir?", "Acı"),
    ("\"Acı\" kelimesinin zıt anlamlısı hangisidir?", "Tatlı"),
    ("\"Islak\" kelimesinin zıt anlamlısı hangisidir?", "Kuru"),
    ("\"Kuru\" kelimesinin zıt anlamlısı hangisidir?", "Islak"),
    ("\"Şişman\" kelimesinin zıt anlamlısı hangisidir?", "Zayıf"),
    ("\"Zayıf\" kelimesinin zıt anlamlısı hangisidir?", "Şişman"),
    ("\"Geniş\" kelimesinin zıt anlamlısı hangisidir?", "Dar"),
    ("\"Dar\" kelimesinin zıt anlamlısı hangisidir?", "Geniş"),
    ("\"Sessiz\" kelimesinin zıt anlamlısı hangisidir?", "Gürültülü"),
    ("\"Gürültülü\" kelimesinin zıt anlamlısı hangisidir?", "Sessiz"),
    ("\"Güzel\" kelimesinin zıt anlamlısı hangisidir?", "Çirkin"),
    ("\"Çirkin\" kelimesinin zıt anlamlısı hangisidir?", "Güzel"),
    ("\"İyi\" kelimesinin zıt anlamlısı hangisidir?", "Kötü"),
    ("\"Kötü\" kelimesinin zıt anlamlısı hangisidir?", "İyi"),
    ("\"Doğru\" kelimesinin zıt anlamlısı hangisidir?", "Eğri"),
    ("\"Eğri\" kelimesinin zıt anlamlısı hangisidir?", "Doğru"),
    ("\"Var\" kelimesinin zıt anlamlısı hangisidir?", "Yok"),
    ("\"Yok\" kelimesinin zıt anlamlısı hangisidir?", "Var"),
    ("\"Kazanç\" kelimesinin zıt anlamlısı hangisidir?", "Zarar"),
    ("\"Zarar\" kelimesinin zıt anlamlısı hangisidir?", "Kazanç"),
    ("\"Başlangıç\" kelimesinin zıt anlamlısı hangisidir?", "Bitiş"),
    ("\"Bitiş\" kelimesinin zıt anlamlısı hangisidir?", "Başlangıç"),
    ("\"Giriş\" kelimesinin zıt anlamlısı hangisidir?", "Çıkış"),
    ("\"Çıkış\" kelimesinin zıt anlamlısı hangisidir?", "Giriş"),
    ("\"Artı\" kelimesinin zıt anlamlısı hangisidir?", "Eksi"),
    ("\"Eksi\" kelimesinin zıt anlamlısı hangisidir?", "Artı")
        ],
    },
    "atasozu_deyim": {
        "label": "Atasözü / Deyim",
        "icon": "📖",
        "items": [
           ("\"Damlaya damlaya ___ olur.\" atasözünü tamamlayan kelime nedir?", "Göl"),
    ("\"Ağaç yaşken ___.\" atasözünü tamamlayan kelime nedir?", "Eğilir"),
    ("\"Gülü seven dikenine ___.\" atasözünü tamamlayan kelime nedir?", "Katlanır"),
    ("\"Aç tavuk kendini ___ ambarında sanır.\" atasözünü tamamlayan kelime nedir?", "Buğday"),
    ("\"Bir elin nesi var, iki elin ___ var.\" atasözünü tamamlayan kelime nedir?", "Sesi"),
    ("\"Sakla samanı, gelir ___.\" atasözünü tamamlayan kelime nedir?", "Zamanı"),
    ("\"İşleyen demir ___.\" atasözünü tamamlayan kelime nedir?", "Işıldar"),
    ("\"Bugünün işini yarına ___.\" atasözünü tamamlayan kelime nedir?", "Bırakma"),
    ("\"Ne ekersen onu ___.\" atasözünü tamamlayan kelime nedir?", "Biçersin"),
    ("\"Ayağını yorganına göre ___.\" atasözünü tamamlayan kelime nedir?", "Uzat"),
    ("\"Komşu komşunun külüne ___.\" atasözünü tamamlayan kelime nedir?", "Muhtaçtır"),
    ("\"Birlikten ___ doğar.\" atasözünü tamamlayan kelime nedir?", "Kuvvet"),
    ("\"Erken kalkan yol ___.\" atasözünü tamamlayan kelime nedir?", "Alır"),
    ("\"Tatlı dil yılanı ___.\" atasözünü tamamlayan kelime nedir?", "Deliğinden"),
    ("\"Yalancının mumu yatsıya kadar ___.\" atasözünü tamamlayan kelime nedir?", "Yanar"),
    ("\"Ak akçe kara gün ___.\" atasözünü tamamlayan kelime nedir?", "İçindir"),
    ("\"Dost kara günde ___.\" atasözünü tamamlayan kelime nedir?", "Belli olur"),
    ("\"Su testisi su yolunda ___.\" atasözünü tamamlayan kelime nedir?", "Kırılır"),
    ("\"Emek olmadan yemek ___.\" atasözünü tamamlayan kelime nedir?", "Olmaz"),
    ("\"Keskin sirke küpüne ___.\" atasözünü tamamlayan kelime nedir?", "Zarar"),
    ("\"Acele işe şeytan ___.\" atasözünü tamamlayan kelime nedir?", "Karışır"),
    ("\"Can boğazdan ___.\" atasözünü tamamlayan kelime nedir?", "Gelir"),
    ("\"Az veren candan, çok veren ___.\" atasözünü tamamlayan kelime nedir?", "Maldan"),
    ("\"Üzüm üzüme baka baka ___.\" atasözünü tamamlayan kelime nedir?", "Kararır"),
    ("\"Bugünkü tavuk yarınki kazdan ___.\" atasözünü tamamlayan kelime nedir?", "İyidir"),
    ("\"Göze girmek\" deyiminin anlamı nedir?", "Beğenilmek"),
    ("\"Ağzı kulaklarına varmak\" deyiminin anlamı nedir?", "Sevinmek"),
    ("\"Dokuz doğurmak\" deyiminin anlamı nedir?", "Sabırsızlanmak"),
    ("\"Kulak vermek\" deyiminin anlamı nedir?", "Dinlemek"),
    ("\"Göz atmak\" deyiminin anlamı nedir?", "İncelemek"),
    ("\"Dilinde tüy bitmek\" deyiminin anlamı nedir?", "Uyarmak"),
    ("\"Etekleri zil çalmak\" deyiminin anlamı nedir?", "Sevinmek"),
    ("\"Burnu havada olmak\" deyiminin anlamı nedir?", "Kibirlenmek"),
    ("\"Burnundan solumak\" deyiminin anlamı nedir?", "Öfkelenmek"),
    ("\"Kulağına küpe olmak\" deyiminin anlamı nedir?", "Unutmamak"),
    ("\"Gözden düşmek\" deyiminin anlamı nedir?", "Değerkaybetmek"),
    ("\"İçi içine sığmamak\" deyiminin anlamı nedir?", "Heyecanlanmak"),
    ("\"Parmakla göstermek\" deyiminin anlamı nedir?", "Övmek"),
    ("\"El ele vermek\" deyiminin anlamı nedir?", "Yardımlaşmak"),
    ("\"Kulak kabartmak\" deyiminin anlamı nedir?", "Dinlemek"),
    ("\"Sözünü tutmak\" deyiminin anlamı nedir?", "Güvenilirolmak"),
    ("\"İpe un sermek\" deyiminin anlamı nedir?", "Bahane"),
    ("\"Dört gözle beklemek\" deyiminin anlamı nedir?", "Özlemek"),
    ("\"Eli açık olmak\" deyiminin anlamı nedir?", "Cömert"),
    ("\"Gözü tok olmak\" deyiminin anlamı nedir?", "Kanaatkâr"),
    ("\"İçi rahat etmek\" deyiminin anlamı nedir?", "Huzurlu"),
    ("\"Yüzü gülmek\" deyiminin anlamı nedir?", "Mutlu"),
    ("\"Elinden geleni yapmak\" deyiminin anlamı nedir?", "Çabalamak"),
    ("\"Başına buyruk\" deyiminin anlamı nedir?", "Bağımsız"),
    ("\"Can kulağıyla dinlemek\" deyiminin anlamı nedir?", "Dikkat")
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
