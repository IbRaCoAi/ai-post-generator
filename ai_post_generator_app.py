
import streamlit as st
import random

# Örnek metin türlerine göre içerik havuzu
turler = {
    "Duygusal": [
        "Kelimeler susar bazen, gözler anlatır her şeyi...",
        "Kalbinin sesini duymak için biraz sessizlik yeter...",
        "Bazı duygular kelimelere sığmaz, sadece hissedilir.",
        "Kalbini susturamazsın, doğru zaman geldiğinde konuşur."
    ],
    "Gizemli": [
        "Karanlıkta saklanan gerçekler, ışığa çıkmak için sabırsızdır.",
        "Her iz bir sırrı fısıldar; görmeyi bilen gözlere...",
        "Gölgenin ardında saklı olan, gerçeğin ta kendisidir.",
        "Sustuğum yerlerde en derin hikâyeler saklı."
    ],
    "Sert & Tok": [
        "Kimseyi bekleme. Yolu kendin aç, adımı sen koy.",
        "İz bırakmak istiyorsan, yandığın yerden geçmeye razı ol.",
        "Yıkmadığın duvar, önünde kalmaya devam eder.",
        "Gerçek güç, yalnızken de yürüyebilmektir."
    ]
}

st.set_page_config(page_title="AI İçerik Üretici", layout="centered")
st.title("🧠 AI Destekli Instagram / X İçerik Üretici")
st.markdown("Anonim sayfan için özgün, etkileyici metinler oluştur!")

# Kullanıcıdan seçim alınır
tur = st.selectbox("Yazı tarzını seç:", list(turler.keys()))

# Butona basınca içerik oluşur
if st.button("📝 İçerik Üret"):
    secim = random.choice(turler[tur])
    st.markdown(f"### "{secim}"")
    st.image("https://source.unsplash.com/800x400/?dark,aesthetic", caption="AI stili görsel (rastgele)")
    st.success("İçeriğini kopyala ve paylaş!")
