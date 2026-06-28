import streamlit as st

# DATABASE OBAT UTAMA (SUDAH DITAMBAH BANYAK OBAT)
DATABASE_OBAT = [
    {"nama": "Parasetamol", "indikasi": ["demam", "sakit kepala", "nyeri"], "kontraindikasi": ["gangguan hati", "alergi parasetamol"], "dosis": "500mg, 3-4 kali sehari setelah makan."},
    {"nama": "Ibuprofen", "indikasi": ["demam", "nyeri otot", "sakit gigi", "radang"], "kontraindikasi": ["sakit maag", "gangguan ginjal", "kehamilan"], "dosis": "400mg, 3 kali sehari setelah makan."},
    {"nama": "Cetirizine", "indikasi": ["gatal", "alergi", "bersin-bersin", "pilek"], "kontraindikasi": ["gangguan ginjal berat", "menyusui"], "dosis": "10mg, 1 kali sehari sebelum tidur."},
    {"nama": "Antasid Doen", "indikasi": ["sakit maag", "nyeri lambung", "asam lambung", "kembung"], "kontraindikasi": ["gangguan ginjal berat", "alergi antasida"], "dosis": "1-2 tablet, dikunyah 1-2 jam sebelum makan."},
    {"nama": "Guaifenesin (Gilasen)", "indikasi": ["batuk berdahak", "pengencer dahak"], "kontraindikasi": ["alergi guaifenesin", "anak di bawah 2 tahun"], "dosis": "200mg - 400mg, setiap 4 jam sekali sesudah makan."},
    {"nama": "Amoksisilin (Amoxicillin)", "indikasi": ["infeksi bakteri", "sakit gigi karena infeksi", "radang tenggorokan bakteri"], "kontraindikasi": ["alergi penisilin", "gangguan ginjal berat"], "dosis": "500mg, 3 kali sehari sesudah makan (Wajib dihabiskan)."},
    {"nama": "Captopril", "indikasi": ["hipertensi", "tekanan darah tinggi"], "kontraindikasi": ["kehamilan", "riwayat angioedema", "gangguan ginjal berat"], "dosis": "12.5mg - 25mg, 2-3 kali sehari (1 jam sebelum makan)."},
    {"nama": "Metformin", "indikasi": ["diabetes", "gula darah tinggi", "kencing manis"], "kontraindikasi": ["gangguan fungsi ginjal", "gangguan hati berat", "dehidrasi"], "dosis": "500mg, 2-3 kali sehari bersama atau sesudah makan."},
    {"nama": "Amlodipine", "indikasi": ["hipertensi", "tekanan darah tinggi", "nyeri dada"], "kontraindikasi": ["syok kardiogenik", "hipotensi berat"], "dosis": "5mg - 10mg, 1 kali sehari sebelum atau sesudah makan."},
    {"nama": "Asam Mefenamat", "indikasi": ["nyeri gigi", "nyeri haid", "nyeri pasca operasi"], "kontraindikasi": ["sakit maag berat", "tukak lambung", "gangguan ginjal"], "dosis": "500mg, 3 kali sehari sesudah makan."}
]

# DESAIN HALAMAN WEB
st.set_page_config(page_title="Asisten Obat", page_icon="💊", layout="centered")

st.title("💊 Asisten Referensi Obat")
st.write("Aplikasi pintar penyaringan obat berdasarkan keluhan dan kondisi keamanan pasien.")
st.markdown("---")

# INPUT PENGGUNA
keluhan_input = st.text_input("Masukkan Keluhan Pasien:", placeholder="Contoh: demam, tekanan darah tinggi")
kondisi_input = st.text_input("Masukkan Kondisi/Kontraindikasi (Jika tidak ada, kosongkan):", placeholder="Contoh: sakit maag, kehamilan")

# TOMBOL PROSES
if st.button("Cek Rekomendasi Obat", type="primary"):
    if keluhan_input:
        keluhan = keluhan_input.lower()
        kondisi = kondisi_input.lower()
        
        obat_rekomendasi = []
        for obat in DATABASE_OBAT:
            # Memeriksa apakah keluhan cocok dengan indikasi obat
            cocok_indikasi = any(indika in keluhan for indika in obat["indikasi"])
            # Memeriksa apakah kondisi pasien ada di dalam kontraindikasi obat
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
