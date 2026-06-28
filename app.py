import streamlit as st

# DATABASE OBAT DENGAN FORMAT KALKULATOR DOSIS
DATABASE_OBAT = [
    # --- OBAT SIRUP ANAK DENGAN RUMUS DOSIS BB ---
    {
        "nama": "Yusimox Sirup (Amoxicillin 125mg/5ml)", 
        "kategori": "Anak",
        "indikasi": ["infeksi bakteri", "sakit gigi anak", "radang tenggorokan bakteri anak"], 
        "kontraindikasi": ["alergi penisilin"], 
        "rumus_bb": lambda bb: f"{(bb * 30) / 3 / 125 * 5:.1f} ml setiap 8 jam (3 kali sehari). \n*(Rumus standar: 30mg/kgBB/hari dibagi 3 dosis, sediaan 125mg/5ml)*"
    },
    {
        "nama": "Fasgo Forte Sirup (Paracetamol 250mg/5ml)", 
        "kategori": "Anak",
        "indikasi": ["demam anak", "nyeri anak", "sakit kepala anak"], 
        "kontraindikasi": ["gangguan fungsi hati berat"], 
        "rumus_bb": lambda bb: f"{(bb * 10) / 250 * 5:.1f} ml setiap 6-8 jam (3-4 kali sehari) jika demam. \n*(Rumus standar: 10mg/kgBB/dosis, sediaan Forte 250mg/5ml)*"
    },
    {
        "nama": "Insic Forte Sirup (Ibuprofen 200mg/5ml)", 
        "kategori": "Anak",
        "indikasi": ["demam tinggi anak", "nyeri anak", "sakit gigi anak"], 
        "kontraindikasi": ["sakit maag berat", "gangguan fungsi ginjal"], 
        "rumus_bb": lambda bb: f"{(bb * 5) / 200 * 5:.1f} ml hingga {(bb * 10) / 200 * 5:.1f} ml, 3-4 kali sehari setelah makan. \n*(Rumus standar: 5-10mg/kgBB/dosis, sediaan Forte 200mg/5ml)*"
    },
    {
        "nama": "Hufaxol Sirup (Ambroxol 15mg/5ml)", 
        "kategori": "Anak",
        "indikasi": ["batuk berdahak anak", "pengencer dahak anak"], 
        "kontraindikasi": ["alergi ambroxol"], 
        "rumus_bb": lambda bb: f"{(bb * 0.5) / 15 * 5:.1f} ml hingga {(bb * 0.6) / 15 * 5:.1f} ml, 3 kali sehari sesudah makan. \n*(Rumus standar: 0.5mg/kgBB/dosis, sediaan 15mg/5ml)*"
    },
    {
        "nama": "Zinc Sirup (20mg/5ml)", 
        "kategori": "Anak",
        "indikasi": ["diare anak pelengkap", "mencret anak pendamping oralit"], 
        "kontraindikasi": ["alergi zinc"], 
        "rumus_bb": lambda bb: "2.5 ml (10mg) 1 kali sehari selama 10 hari berturut-turut." if bb < 10 else "5.0 ml (20mg) 1 kali sehari selama 10 hari berturut-turut. \n*(Wajib dihabiskan meskipun diare sudah sembuh)*"
    },
    
    # --- OBAT SIRUP ANAK DOSIS FIX (BERDASARKAN RANGE USIA UMUM) ---
    {"nama": "Ternix Sirup (Flu & Batuk Anak)", "kategori": "Anak", "indikasi": ["flu anak", "batuk", "demam anak", "pilek bersin"], "kontraindikasi": ["gangguan fungsi hati berat"], "dosis_fix": "Anak 2-6 tahun: 5ml (1 sendok takar), 3 kali sehari sesudah makan."},
    {"nama": "Ternix Plus Sirup", "kategori": "Anak", "indikasi": ["flu anak disertai batuk berdahak", "batuk berdahak anak", "demam pilek anak"], "kontraindikasi": ["hipertensi berat"], "dosis_fix": "Anak 6-12 tahun: 10ml (2 sendok takar), 3 kali sehari sesudah makan."},
    {"nama": "Coldrexin Sirup", "kategori": "Anak", "indikasi": ["flu anak", "demam pilek anak", "batuk flu anak"], "kontraindikasi": ["gangguan fungsi hati berat"], "dosis_fix": "Anak 2-6 tahun: 5ml (1 sendok takar), 3 kali sehari sesudah makan."},
    {"nama": "Zenirex Sirup", "kategori": "Anak", "indikasi": ["batuk anak", "batuk berdahak disertai alergi", "flu batuk anak"], "kontraindikasi": ["anak di bawah 2 tahun tanpa pengawasan"], "dosis_fix": "Anak 2-6 tahun: 2.5ml - 5ml, 3 kali sehari sesudah makan."},
    {"nama": "Biolysin Sirup", "kategori": "Anak", "indikasi": ["suplemen anak", "nafsu makan anak", "vitamin pertumbuhan anak"], "kontraindikasi": ["hipervitaminosis"], "dosis_fix": "Anak 1-12 tahun: 5ml (1 sendok takar), 1 kali sehari sesudah makan."},
    {"nama": "Guanistrep Sirup", "kategori": "Anak", "indikasi": ["diare anak", "mencret anak"], "kontraindikasi": ["konstipasi"], "dosis_fix": "Anak 3-6 tahun: 5ml-10ml (1-2 sendok takar) setiap setelah buang air besar."},
    {"nama": "Oratifed Sirup", "kategori": "Anak", "indikasi": ["flu pilek anak", "hidung tersumbat", "batuk alergi anak"], "kontraindikasi": ["hipertensi berat"], "dosis_fix": "Anak 2-6 tahun: 2.5ml (1/2 sendok takar), 3 kali sehari sesudah makan."},
    {"nama": "Lambucid Sirup", "kategori": "Anak", "indikasi": ["sakit maag", "kembung cair", "asam lambung anak dewasa", "perih lambung"], "kontraindikasi": ["gangguan ginjal berat"], "dosis_fix": "Anak 6-12 tahun: 2.5ml - 5ml (1/2 - 1 sendok takar), 3-4 kali sehari sebelum makan."},

    # --- OBAT DEWASA (TABLET / KAPLET) ---
    {"nama": "Aciclovir Tablet", "kategori": "Dewasa", "indikasi": ["herpes", "cacar air", "infeksi virus"], "kontraindikasi": ["gangguan ginjal berat"], "dosis": "Dewasa: 200mg - 400mg, 5 kali sehari (tiap 4 jam) sesudah makan."},
    {"nama": "Ketoconazole Tablet", "kategori": "Dewasa", "indikasi": ["panu", "kadas", "infeksi jamur"], "kontraindikasi": ["gangguan hati berat"], "dosis": "Dewasa: 200mg, 1 kali sehari bersama makan."},
    {"nama": "Cotrimoxazole Tablet", "kategori": "Dewasa", "indikasi": ["infeksi bakteri", "infeksi saluran kemih", "isk"], "kontraindikasi": ["gangguan fungsi hati berat", "kehamilan"], "dosis": "Dewasa: 2 tablet, 2 kali sehari sesudah makan."},
    {"nama": "Asam Mefenamat", "kategori": "Dewasa", "indikasi": ["nyeri gigi", "nyeri haid", "nyeri otot"], "kontraindikasi": ["sakit maag berat", "tukak lambung"], "dosis": "Dewasa: 500mg, 3 kali sehari sesudah makan."},
    {"nama": "Cefixime 100mg", "kategori": "Dewasa", "indikasi": ["infeksi bakteri", "infeksi saluran kemih", "isk", "gonore"], "kontraindikasi": ["alergi antibiotik sefalosforin"], "dosis": "Dewasa: 1-2 kapsul, 2 kali sehari sesudah makan."},
    {"nama": "Amlodipin", "kategori": "Dewasa", "indikasi": ["hipertensi", "tekanan darah tinggi"], "kontraindikasi": ["hipotensi berat"], "dosis": "Dewasa: 5mg - 10mg, 1 kali sehari pagi atau malam."},
    {"nama": "Omeprazole", "kategori": "Dewasa", "indikasi": ["sakit maag", "asam lambung", "gerd"], "kontraindikasi": ["alergi omeprazole"], "dosis": "Dewasa: 20mg, 1-2 kali sehari 30 menit sebelum makan."},
    {"nama": "Metformin", "kategori": "Dewasa", "indikasi": ["diabetes", "gula darah tinggi", "kencing manis"], "kontraindikasi": ["gangguan fungsi ginjal berat"], "dosis": "Dewasa: 500mg, 2-3 kali sehari bersama atau sesudah makan."}
]

# TAMPILAN UTAMA WEBSITE
st.set_page_config(page_title="Asisten Obat Plus", page_icon="💊", layout="centered")

st.title("💊 Asisten Obat & Kalkulator Dosis")
st.write("Aplikasi penyaringan obat Puskesmas dilengkapi dengan perhitungan dosis BB otomatis untuk anak.")
st.markdown("---")

# KATEGORI PASIEN
kategori_pasien = st.radio("Pilih Kategori Pasien:", ["Pasien Dewasa", "Pasien Anak-Anak"], horizontal=True)

# INPUT UNTUK ANAK-ANAK
berat_badan = 0.0
if kategori_pasien == "Pasien Anak-Anak":
    berat_badan = st.number_input("Masukkan Berat Badan Anak (kg):", min_value=0.0, max_value=100.0, value=10.0, step=0.5)

# INPUT KELUHAN & KONTRAINDIKASI
keluhan_input = st.text_input("Masukkan Keluhan / Gejala Utama:", placeholder="Contoh: demam, batuk berdahak, sakit maag")
kondisi_input = st.text_input("Masukkan Kondisi Penyerta / Kontraindikasi (Jika tidak ada, kosongkan):", placeholder="Contoh: alergi penisilin, sakit maag")

# PROSES SKRINING
if st.button("Hitung & Cek Rekomendasi Obat", type="primary"):
    if keluhan_input:
        keluhan = keluhan_input.lower()
        kondisi = kondisi_input.lower()
        kat_filter = "Anak" if kategori_pasien == "Pasien Anak-Anak" else "Dewasa"
        
        obat_rekomendasi = []
        for obat in DATABASE_OBAT:
            # Filter Kategori Pasien
            if obat["kategori"] == kat_filter:
                # Cek Indikasi
                cocok_indikasi = any(indika in keluhan for indika in obat["indikasi"])
                # Cek Kontraindikasi
                ada_kontraindikasi = any(kontra in kondisi for kontra in obat["kontraindikasi"]) if kondisi else False
                
                if cocok_indikasi and not ada_kontraindikasi:
                    obat_rekomendasi.append(obat)
                    
        st.subheader("📋 Hasil Analisis & Rekomendasi Dosis")
        if obat_rekomendasi:
            st.success(f"Ditemukan {len(obat_rekomendasi)} obat yang cocok dan aman untuk {kategori_pasien}:")
            for ob in obat_rekomendasi:
                with st.expander(f"➔ {ob['nama']}", expanded=True):
                    # Jika obat punya rumus hitung BB otomatis
                    if "rumus_bb" in ob and berat_badan > 0:
                        hasil_dosis = ob["rumus_bb"](berat_badan)
                        st.info(f"**Dosis Hasil Hitung Otomatis (BB {berat_badan} kg):**\n\n{hasil_dosis}")
                    # Jika obat anak dengan dosis usia fix
                    elif "dosis_fix" in ob:
                        st.write(f"**Dosis Berdasarkan Panduan Usia:**\n{ob['dosis_fix']}")
                    # Jika obat dewasa
                    else:
                        st.write(f"**Dosis Standar:**\n{ob['dosis']}")
        else:
            st.warning("Tidak ada obat yang cocok atau aman berdasarkan database untuk kriteria tersebut.")
    else:
        st.info("Silakan masukkan keluhan pasien terlebih dahulu.")
