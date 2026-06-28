import streamlit as st

# DATABASE OBAT UTAMA
DATABASE_OBAT = [
    {"nama": "Parasetamol", "indikasi": ["demam", "sakit kepala", "nyeri"], "kontraindikasi": ["gangguan hati", "alergi parasetamol"], "dosis": "500mg, 3-4 kali sehari setelah makan."},
    {"nama": "Ibuprofen", "indikasi": ["demam", "nyeri otot", "sakit gigi", "radang"], "kontraindikasi": ["sakit maag", "gangguan ginjal", "kehamilan"], "dosis": "400mg, 3 kali sehari setelah makan."},
    {"nama": "Cetirizine", "indikasi": ["gatal", "alergi", "bersin-bersin"], "kontraindikasi": ["gangguan ginjal berat", "menyusui"], "dosis": "10mg, 1 kali sehari sebelum tidur."},
    {"nama": "Antasida Doen", "indikasi": ["sakit maag", "nyeri lambung", "asam lambung", "kembung"], "kontraindikasi": ["gangguan ginjal berat", "alergi antasida"], "dosis": "1-2 tablet, dikunyah 1-2 jam sebelum makan."},
    {"nama": "Guaifenesin (Gilasen)", "indikasi": ["batuk berdahak", "pengencer dahak"], "kontraindikasi": ["alergi guaifenesin", "anak di bawah 2 tahun"], "dosis": "200mg - 400mg, setiap 4 jam sekali sesudah makan."}
]

# DESAIN HALAMAN WEB
st.set_page_config(page_title="Asisten Obat", page_icon="💊", layout="centered")

st.title("💊 Asisten Referensi Obat")
st.write("Aplikasi pintar penyaringan obat berdasarkan keluhan dan kondisi keamanan pasien.")
st.markdown("---")

# INPUT PENGGUNA
keluhan_input = st.text_input("Masukkan Keluhan Pasien:", placeholder="Contoh: demam, batuk berdahak")
kondisi_input = st.text_input("Masukkan Kondisi/Kontraindikasi (Jika tidak ada, kosongkan):", placeholder="Contoh: sakit maag")

# TOMBOL PROSES
if st.button("Cek Rekomendasi Obat", type="primary"):
    if keluhan_input:
        keluhan = keluhan_input.lower()
        kondisi = kondisi_input.lower()
        
        obat_rekomendasi = []
        for obat in DATABASE_OBAT:
            cocok_indikasi = any(indika in keluhan for indika in obat["indikasi"])
            ada_kontraindikasi = any(kontra in kondisi for kontra in obat["kontraindikasi"]) if kondisi else False
            
            if cocok_indikasi and not ada_kontraindikasi:
                obat_rekomendasi.append(obat)
        
        st.subheader("📋 Hasil Analisis")
        if obat_rekomendasi:
            for ob in obat_rekomendasi:
                with st.expander(f"➔ {ob['nama']}", expanded=True):
                    st.write(f"**Dosis:** {ob['dosis']}")
        else:
            st.warning("Tidak ada obat yang cocok atau aman berdasarkan database saat ini.")
    else:
        st.info("Silakan ketik keluhan pasien terlebih dahulu.")
