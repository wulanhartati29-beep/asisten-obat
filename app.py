import streamlit as st

# DATABASE OBAT LENGKAP: ANAK (BB), DEWASA, & SALEP/TETES MATA
DATABASE_OBAT = [
    # --- OBAT SIRUP ANAK DENGAN RUMUS DOSIS BB ---
    {
        "nama": "Yusimox Sirup (Amoxicillin 125mg/5ml)", 
        "kategori": "Anak",
        "indikasi": ["infeksi bakteri", "sakit gigi anak", "radang tenggorokan bakteri anak", "batuk", "demam"], 
        "kontraindikasi": ["alergi penisilin"], 
        "rumus_bb": lambda bb: f"{(bb * 30) / 3 / 125 * 5:.1f} ml setiap 8 jam (3 kali sehari). \n*(Rumus standar: 30mg/kgBB/hari dibagi 3 dosis, sediaan 125mg/5ml)*"
    },
    {
        "nama": "Fasgo Forte Sirup (Paracetamol 250mg/5ml)", 
        "kategori": "Anak",
        "indikasi": ["demam anak", "nyeri anak", "sakit kepala anak", "pusing", "demam"], 
        "kontraindikasi": ["gangguan fungsi hati berat"], 
        "rumus_bb": lambda bb: f"{(bb * 10) / 250 * 5:.1f} ml setiap 6-8 jam (3-4 kali sehari) jika demam. \n*(Rumus standar: 10mg/kgBB/dosis, sediaan Forte 250mg/5ml)*"
    },
    {
        "nama": "Insic Forte Sirup (Ibuprofen 200mg/5ml)", 
        "kategori": "Anak",
        "indikasi": ["demam tinggi anak", "nyeri anak", "sakit gigi anak", "pusing", "demam"], 
        "kontraindikasi": ["sakit maag berat", "gangguan fungsi ginjal"], 
        "rumus_bb": lambda bb: f"{(bb * 5) / 200 * 5:.1f} ml hingga {(bb * 10) / 200 * 5:.1f} ml, 3-4 kali sehari setelah makan. \n*(Rumus standar: 5-10mg/kgBB/dosis, sediaan Forte 200mg/5ml)*"
    },
    {
        "nama": "Hufaxol Sirup (Ambroxol 15mg/5ml)", 
        "kategori": "Anak",
        "indikasi": ["batuk berdahak anak", "pengencer dahak anak", "batuk"], 
        "kontraindikasi": ["alergi ambroxol"], 
        "rumus_bb": lambda bb: f"{(bb * 0.5) / 15 * 5:.1f} ml hingga {(bb * 0.6) / 15 * 5:.1f} ml, 3 kali sehari sesudah makan. \n*(Rumus standar: 0.5mg/kgBB/dosis, sediaan 15mg/5ml)*"
    },
    {
        "nama": "Zinc Sirup (20mg/5ml)", 
        "kategori": "Anak",
        "indikasi": ["diare anak pelengkap", "mencret anak pendamping oralit", "diare"], 
        "kontraindikasi": ["alergi zinc"], 
        "rumus_bb": lambda bb: "2.5 ml (10mg) 1 kali sehari selama 10 hari berturut-turut." if bb < 10 else "5.0 ml (20mg) 1 kali sehari selama 10 hari berturut-turut. \n*(Wajib dihabiskan meskipun diare sudah sembuh)*"
    },
    
    # --- OBAT SIRUP ANAK DOSIS FIX (BERDASARKAN RANGE USIA) ---
    {"nama": "Ternix Sirup", "kategori": "Anak", "indikasi": ["flu anak", "batuk", "demam anak", "pilek", "demam", "flu"], "kontraindikasi": ["gangguan fungsi hati berat"], "dosis_fix": "Anak 2-6 th: 5ml (1 sdt), 3x sehari sesudah makan."},
    {"nama": "Ternix Plus Sirup", "kategori": "Anak", "indikasi": ["flu anak disertai batuk", "batuk berdahak anak", "batuk", "demam", "flu"], "kontraindikasi": ["hipertensi berat"], "dosis_fix": "Anak 6-12 th: 10ml (2 sdt), 3x sehari sesudah makan."},
    {"nama": "Coldrexin Sirup", "kategori": "Anak", "indikasi": ["flu anak", "demam pilek anak", "batuk", "demam", "flu"], "kontraindikasi": ["gangguan fungsi hati berat"], "dosis_fix": "Anak 2-6 th: 5ml (1 sdt), 3x sehari sesudah makan."},
    {"nama": "Zenirex Sirup", "kategori": "Anak", "indikasi": ["batuk anak", "batuk berdahak", "batuk"], "kontraindikasi": ["anak di bawah 2 tahun"], "dosis_fix": "Anak 2-6 th: 2.5ml - 5ml, 3x sehari."},
    {"nama": "Biolysin Sirup", "kategori": "Anak", "indikasi": ["suplemen anak", "nafsu makan anak", "vitamin"], "kontraindikasi": ["hipervitaminosis"], "dosis_fix": "Anak 1-12 th: 5ml (1 sdt), 1x sehari."},
    {"nama": "Guanistrep Sirup", "kategori": "Anak", "indikasi": ["diare anak", "mencret", "diare"], "kontraindikasi": ["konstipasi"], "dosis_fix": "Anak 3-6 th: 5ml-10ml tiap setelah BAB."},
    {"nama": "Oratifed Sirup", "kategori": "Anak", "indikasi": ["flu pilek anak", "hidung tersumbat", "batuk", "flu", "pilek"], "kontraindikasi": ["hipertensi berat"], "dosis_fix": "Anak 2-6 th: 2.5ml (1/2 sdt), 3x sehari."},
    {"nama": "Lambucid Sirup", "kategori": "Anak", "indikasi": ["sakit maag", "kembung", "mual", "maag", "lambung"], "kontraindikasi": ["gangguan ginjal berat"], "dosis_fix": "Anak 6-12 th: 2.5ml - 5ml (1/2 - 1 sdt), 3-4x sehari."},

    # --- OBAT DEWASA (TABLET / KAPLET) ---
    {"nama": "Aciclovir Tablet", "kategori": "Dewasa", "indikasi": ["herpes", "cacar air", "virus"], "kontraindikasi": ["gangguan ginjal berat"], "dosis": "Dewasa: 200mg - 400mg, 5x sehari sesudah makan."},
    {"nama": "Ketoconazole Tablet", "kategori": "Dewasa", "indikasi": ["panu", "kadas", "jamur"], "kontraindikasi": ["gangguan hati berat"], "dosis": "Dewasa: 200mg, 1x sehari bersama makan."},
    {"nama": "Asam Mefenamat", "kategori": "Dewasa", "indikasi": ["nyeri gigi", "nyeri haid", "nyeri otot", "pusing", "sakit kepala", "nyeri"], "kontraindikasi": ["sakit maag berat"], "dosis": "Dewasa: 500mg, 3x sehari sesudah makan."},
    {"nama": "Parasetamol / Fasidol", "kategori": "Dewasa", "indikasi": ["demam", "pusing", "sakit kepala", "nyeri"], "kontraindikasi": ["gangguan hati berat"], "dosis": "Dewasa: 500mg, 3-4x sehari sesudah makan."},
    {"nama": "Amlodipin", "kategori": "Dewasa", "indikasi": ["hipertensi", "tekanan darah tinggi", "tensi"], "kontraindikasi": ["hipotensi berat"], "dosis": "Dewasa: 5mg - 10mg, 1x sehari pagi atau malam."},
    {"nama": "Omeprazole", "kategori": "Dewasa", "indikasi": ["sakit maag", "asam lambung", "gerd", "mual", "maag"], "kontraindikasi": ["alergi omeprazole"], "dosis": "Dewasa: 20mg, 1-2x sehari 30 menit sebelum makan."},
    {"nama": "Ondansetron", "kategori": "Dewasa", "indikasi": ["mual", "muntah"], "kontraindikasi": ["alergi ondansetron"], "dosis": "Dewasa: 4mg - 8mg, 2-3x sehari sebelum makan."},
    {"nama": "Vesperum (Domperidone)", "kategori": "Dewasa", "indikasi": ["mual", "muntah", "kembung"], "kontraindikasi": ["gangguan jantung"], "dosis": "Dewasa: 10mg, 3x sehari sebelum makan."},
    {"nama": "Metformin", "kategori": "Dewasa", "indikasi": ["diabetes", "gula darah tinggi", "kencing manis", "gula"], "kontraindikasi": ["gangguan ginjal berat"], "dosis": "Dewasa: 500mg, 2-3x sehari sesudah makan."},

    # --- OBAT LUAR (SALEP & TETES MATA) ---
    {"nama": "Betason N Salep", "kategori": "Dewasa", "indikasi": ["gatal eksim", "radang kulit", "alergi kulit", "eksim", "gatal"], "kontraindikasi": ["infeksi virus aktif"], "dosis": "Oleskan tipis, 2-3 kali sehari."},
    {"nama": "Zensoderm Salep", "kategori": "Dewasa", "indikasi": ["infeksi bakteri kulit", "radang kulit gatal", "eksim berair", "gatal"], "kontraindikasi": ["alergi betamethasone"], "dosis": "Oleskan tipis, 2-3 kali sehari."},
    {"nama": "Synalten Salep", "kategori": "Dewasa", "indikasi": ["eksim berat", "radang kulit kronis", "gatal alergi tebal", "gatal"], "kontraindikasi": ["TBC kulit"], "dosis": "Oleskan tipis, 2-4 kali sehari."},
    {"nama": "Betadine Salep", "kategori": "Dewasa", "indikasi": ["luka bakar ringan", "luka robek", "infeksi luka", "luka"], "kontraindikasi": ["alergi iodium"], "dosis": "Oleskan pada luka 1-2 kali sehari."},
    {"nama": "Gentamicin Salep", "kategori": "Dewasa", "indikasi": ["infeksi bakteri kulit", "bisul", "impetigo", "luka bernanah"], "kontraindikasi": ["alergi gentamicin"], "dosis": "Oleskan tipis pada luka, 3-4 kali sehari."},
    {"nama": "Klorfeson Salep", "kategori": "Dewasa", "indikasi": ["alergi kulit", "eksim infeksi bakteri", "gatal radang"], "kontraindikasi": ["infeksi jamur kulit"], "dosis": "Oleskan tipis pada kulit, 2-3 kali sehari."},
    {"nama": "Ketoconazole Salep", "kategori": "Dewasa", "indikasi": ["jamur kulit", "panu", "kadas", "kurap", "kutu air"], "kontraindikasi": ["alergi ketoconazole"], "dosis": "Oleskan pada area jamur, 1-2 kali sehari."},
    {"nama": "Aciclovir Salep", "kategori": "Dewasa", "indikasi": ["herpes kulit", "dompo", "cacar ular"], "kontraindikasi": ["alergi aciclovir"], "dosis": "Oleskan tiap 4 jam (5x sehari) selama 5 hari."},
    {"nama": "Bioplasenton Salep", "kategori": "Dewasa", "indikasi": ["luka bakar", "luka tekan", "pemulihan luka", "luka"], "kontraindikasi": ["alergi komponen obat"], "dosis": "Oleskan langsung pada luka, 4-6 kali sehari."},
    {"nama": "Genoint Tetes Mata", "kategori": "Dewasa", "indikasi": ["infeksi mata bakteri", "mata merah bernanah", "mata bernanah"], "kontraindikasi": ["infeksi virus/jamur mata"], "dosis": "Teteskan 1-2 tetes setiap 4 jam sekali."},
    {"nama": "Kloramfenikol Tetes Mata", "kategori": "Dewasa", "indikasi": ["mata merah", "infeksi mata luar", "bintitan bernanah"], "kontraindikasi": ["alergi kloramfenikol"], "dosis": "Teteskan 1-2 tetes, 3-4 kali sehari."}
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
keluhan_input = st.text_input("Masukkan Keluhan / Gejala Utama:", placeholder="Contoh: demam, batuk, gatal, mata merah")
kondisi_input = st.text_input("Masukkan Kondisi Penyerta / Kontraindikasi (Jika tidak ada, kosongkan):", placeholder="Contoh: alergi penisilin, sakit maag")

# PROSES SKRINING
if st.button("Hitung & Cek Rekomendasi Obat", type="primary"):
    if keluhan_input:
        stop_words = ["dan", "yang", "dengan", "atau", "pada", "ada", "bisa"]
        keluhan_words = [word.strip(",. ") for word in keluhan_input.lower().split() if word.strip(",. ") not in stop_words and len(word) > 1]
        
        kondisi = kondisi_input.lower()
        kat_filter = "Anak" if kategori_pasien == "Pasien Anak-Anak" else "Dewasa"
        
        obat_rekomendasi = []
        for obat in DATABASE_OBAT:
            if obat["kategori"] == kat_filter:
                cocok_indikasi = False
                for word in keluhan_words:
                    for indika in obat["indikasi"]:
                        # Pencarian kata utuh yang presisi
                        if word in indika.split():
                            cocok_indikasi = True
                            break
                    if cocok_indikasi: break
                
                ada_kontraindikasi = any(kontra in kondisi for kontra in obat["kontraindikasi"]) if kondisi else False
                
                if cocok_indikasi and not ada_kontraindikasi:
                    obat_rekomendasi.append(obat)
                    
        st.subheader("📋 Hasil Analisis & Rekomendasi Dosis")
        if obat_rekomendasi:
            st.success(f"Ditemukan {len(obat_rekomendasi)} obat yang cocok dan aman untuk {kategori_pasien}:")
            for ob in obat_rekomendasi:
                with st.expander(f"➔ {ob['nama']}", expanded=True):
                    if "rumus_bb" in ob and berat_badan > 0:
                        hasil_dosis = ob["rumus_bb"](berat_badan)
                        st.info(f"**Dosis Hasil Hitung Otomatis (BB {berat_badan} kg):**\n\n{hasil_dosis}")
                    elif "dosis_fix" in ob:
                        st.write(f"**Dosis Berdasarkan Panduan Usia:**\n{ob['dosis_fix']}")
                    else:
                        st.write(f"**Dosis Standar:**\n{ob['dosis']}")
        else:
            st.warning("Tidak ada obat yang cocok atau aman berdasarkan database untuk kriteria tersebut.")
    else:
        st.info("Silakan masukkan keluhan pasien terlebih dahulu.")
