import streamlit as st
import pandas as pd
import plotlib.express as px
import os

st.set_page_config(
    page_title="Portofolio Critical Thinking",
    page_icon="🧠",
    layout="wide"
)


# ==================================================
# CSS
# ==================================================

st.markdown("""
<style>

.stApp{
    background-color:#F4F7FC;
}

.hero{
    background: linear-gradient(135deg,#0B1F3A,#163D73);
    padding:50px;
    border-radius:20px;
    color:white;
    text-align:center;
    margin-bottom:20px;
    box-shadow:0px 8px 25px rgba(0,0,0,0.2);
}

.material-card{
    background:white;
    padding:20px;
    border-radius:15px;
    margin-bottom:15px;
    box-shadow:0px 4px 12px rgba(0,0,0,0.08);
    border-left:6px solid #163D73;
}

.footer{
    text-align:center;
    padding:20px;
    color:#555;
}

section[data-testid="stSidebar"]{
    background-color:#0B1F3A;
}

section[data-testid="stSidebar"] *{
    color:white;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&family=Merriweather:wght@300;400&display=swap');

h1,h2,h3 {
    font-family: 'Poppins', sans-serif;
}

p, div {
    font-family: 'Merriweather', serif;
    line-height: 1.9;
    text-align: justify;
}
</style>
""", unsafe_allow_html=True)


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.markdown("# **Identitas Mahasiswa**")

    if os.path.exists("assets/foto_diri.jpg"):
        st.image("assets/foto_diri.jpg", width=220)
    else:
        st.warning("Foto profil belum tersedia")

    st.write("Nama : Rambu Marshanda Tamu Ina Paa")
    st.write("NIM : 20254920004")
    st.write("Program Studi : Statistika")
    st.write("Mata Kuliah : Critical Thinking")
    st.write("Dosen Pengampu : Dr. Suhendra")

    st.divider()

    st.markdown("## **Navigasi**")

    st.write("Beranda")
    st.write("Materi")
    st.write("Kelompok")
    st.write("Tugas")
    st.write("Quiz")
    st.write("Refleksi")


# ==================================================
# HERO
# ==================================================
st.markdown("""
<div style="
background: linear-gradient(135deg,#0B1F3A,#163D73);
padding:50px;
border-radius:20px;
color:white;
text-align:center;
">

<h1>🧠 PORTOFOLIO REFLEKTIF</h1>

<h3>Mata Kuliah Critical Thinking</h3>

<hr style="border:1px solid rgba(255,255,255,0.3);">

<h4>Rambu Marshanda Tamu Ina Paa</h4>

<p>
Program Studi Statistika
</p>

<p style="font-style:italic;">
"Pertumbuhan intelektual tidak terjadi ketika saya selalu benar,
    melainkan ketika saya bersedia menguji asumsi, menerima kritik,
    dan memperbaiki cara berpikir saya."
</p>

</div>
""", unsafe_allow_html=True)


# ==================================================
# TIMELINE
# ==================================================

st.header("Timeline Pembelajaran")
        
timeline = [
"Pengantar Critical Thinking",
"Berpikir",
"Term dan Proposisi",
"Berpikir Kritis",
"Proposisi dan Keputusan",
"Dasar-Dasar Logika",
"Deduktif dan Induktif",
"Kebenaran dan Validitas",
"Ragam Kesesatan Logika"
]

for i,item in enumerate(timeline,1):
    st.success(f"Pertemuan {i} • {item}")


# ==================================================
# MATERI
# ==================================================

st.header("Materi yang Dipelajari")

materi = {
"Pengantar Critical Thinking":
"""
Materi Pengantar Critical Thinking memberikan pemahaman dasar mengenai pentingnya kemampuan berpikir secara logis, rasional, dan reflektif dalam menghadapi berbagai informasi dan permasalahan. Saya belajar bahwa berpikir kritis bukan sekadar mengkritik atau mencari kesalahan, tetapi merupakan proses mengevaluasi informasi berdasarkan bukti, alasan yang logis, dan pertimbangan yang objektif sebelum membentuk suatu kesimpulan atau keputusan.

Melalui materi ini, saya menyadari bahwa banyak keputusan dalam kehidupan sehari-hari sering kali dipengaruhi oleh asumsi, kebiasaan, atau emosi tanpa melalui proses analisis yang memadai. Oleh karena itu, saya mulai memahami pentingnya membiasakan diri untuk mempertanyakan informasi, mencari bukti pendukung, dan mempertimbangkan berbagai sudut pandang agar dapat membuat keputusan yang lebih bijaksana dan bertanggung jawab.
""",

"Berpikir":
"""
Materi tentang berpikir menjelaskan bahwa berpikir merupakan aktivitas mental yang digunakan manusia untuk memahami informasi, membentuk konsep, menyelesaikan masalah, dan mengambil keputusan. Saya memahami bahwa proses berpikir tidak hanya dipengaruhi oleh pengetahuan yang dimiliki, tetapi juga oleh pengalaman, lingkungan, serta kondisi emosional seseorang.

Dari materi ini saya belajar bahwa kualitas hasil yang diperoleh sangat bergantung pada kualitas proses berpikir yang dilakukan. Kesadaran tersebut membuat saya lebih reflektif terhadap cara saya memandang suatu masalah dan lebih berhati-hati dalam mengambil keputusan agar tidak hanya mengandalkan intuisi atau pengalaman pribadi semata.
""",

"Term dan Proposisi":
"""
Materi term dan proposisi memperkenalkan konsep dasar yang digunakan dalam logika dan argumentasi. Term dipahami sebagai konsep atau objek yang menjadi pokok pembahasan, sedangkan proposisi merupakan pernyataan yang dapat dinilai benar atau salah. Materi ini membantu saya memahami bagaimana suatu argumen dibangun dari pernyataan-pernyataan yang memiliki makna dan hubungan tertentu.

Melalui pembelajaran ini, saya menyadari pentingnya menggunakan istilah yang jelas dan tepat dalam berkomunikasi maupun menyusun argumen. Ketidakjelasan dalam penggunaan term dapat menyebabkan kesalahpahaman, sedangkan proposisi yang tidak jelas dapat menghasilkan kesimpulan yang keliru. Oleh karena itu, materi ini menjadi dasar penting dalam memahami logika secara lebih mendalam.
""",

"Berpikir Kritis":
"""
Pada materi ini saya mempelajari bahwa berpikir kritis merupakan kemampuan untuk menganalisis, mengevaluasi, dan menafsirkan informasi secara objektif sebelum menerima atau menolak suatu pendapat. Berpikir kritis menuntut seseorang untuk mempertimbangkan bukti, mengidentifikasi asumsi, serta mengevaluasi kualitas argumen yang digunakan dalam suatu pembahasan.

Materi ini memberikan kesadaran bahwa tidak semua informasi yang diterima dapat langsung dianggap benar. Saya belajar untuk lebih berhati-hati dalam menilai suatu informasi dan berusaha mencari alasan yang logis sebelum membentuk keyakinan atau mengambil keputusan. Kemampuan ini sangat penting baik dalam kehidupan akademik maupun kehidupan sehari-hari.
""",

"Proposisi dan Keputusan":
"""
Materi proposisi dan keputusan membahas bagaimana suatu keputusan dibangun berdasarkan informasi dan proposisi yang digunakan sebagai dasar pertimbangan. Saya memahami bahwa keputusan yang baik tidak hanya bergantung pada hasil akhir yang diperoleh, tetapi juga pada kualitas informasi dan proses berpikir yang digunakan dalam mengevaluasi berbagai alternatif.

Dari materi ini saya belajar bahwa setiap keputusan sebaiknya dibuat melalui pertimbangan yang rasional dan berdasarkan bukti yang relevan. Pemahaman tersebut membantu saya menjadi lebih teliti dalam menilai informasi dan lebih bertanggung jawab terhadap keputusan yang saya ambil dalam berbagai situasi.
""",

"Dasar-Dasar Logika":
"""
Materi dasar-dasar logika memperkenalkan konsep premis, kesimpulan, validitas, dan struktur argumen. Saya belajar bahwa logika membantu seseorang memahami hubungan antara berbagai pernyataan sehingga dapat menentukan apakah suatu kesimpulan diperoleh melalui proses penalaran yang benar atau tidak.

Pembelajaran ini membuat saya lebih kritis dalam mengevaluasi argumen yang saya temui. Saya tidak lagi hanya memperhatikan kesimpulan yang disampaikan, tetapi juga menilai apakah alasan dan proses berpikir yang digunakan sudah logis dan dapat dipertanggungjawabkan. Kemampuan tersebut sangat bermanfaat dalam kegiatan akademik maupun kehidupan sehari-hari.
""",

"Deduktif dan Induktif":
"""
Materi ini membahas dua bentuk penalaran utama, yaitu deduktif dan induktif. Penalaran deduktif digunakan untuk menarik kesimpulan khusus dari prinsip yang bersifat umum, sedangkan penalaran induktif digunakan untuk membentuk kesimpulan umum berdasarkan sejumlah pengamatan atau fakta khusus yang tersedia.

Sebagai mahasiswa Statistika, materi ini memberikan pemahaman yang sangat relevan karena banyak analisis data menggunakan pola berpikir induktif dalam menarik kesimpulan dari sampel menuju populasi. Saya juga memahami bahwa kedua bentuk penalaran tersebut memiliki fungsi yang berbeda tetapi sama-sama penting dalam proses berpikir dan pengambilan keputusan.
""",

"Kebenaran dan Validitas":
"""
Melalui materi ini saya mempelajari bahwa kebenaran dan validitas merupakan dua konsep yang berbeda. Kebenaran berkaitan dengan isi atau fakta dari suatu pernyataan, sedangkan validitas berkaitan dengan struktur logika yang digunakan dalam menghubungkan premis dan kesimpulan suatu argumen.

Materi ini mengubah cara saya menilai suatu argumen. Saya belajar bahwa kesimpulan yang benar belum tentu diperoleh melalui proses berpikir yang valid, dan sebaliknya. Oleh karena itu, saya menjadi lebih teliti dalam mengevaluasi tidak hanya hasil akhir, tetapi juga proses penalaran yang digunakan untuk mencapai kesimpulan tersebut.
""",

"Ragam Kesesatan Logika":
"""
Materi ragam kesesatan logika membahas berbagai bentuk kesalahan berpikir yang dapat menyebabkan seseorang menghasilkan kesimpulan yang tidak logis. Saya mempelajari berbagai contoh logical fallacies seperti generalisasi berlebihan, serangan terhadap pribadi, serta penggunaan alasan yang tidak relevan dalam mendukung suatu argumen.

Materi ini memberikan pemahaman bahwa kesalahan berpikir sering kali terjadi tanpa disadari, baik dalam percakapan sehari-hari maupun dalam media informasi. Setelah mempelajari materi ini, saya menjadi lebih berhati-hati dalam menerima informasi, menyusun argumen, dan mengevaluasi pendapat agar tidak terjebak dalam kesalahan logika yang dapat memengaruhi kualitas keputusan yang diambil.
"""
}

for judul, isi in materi.items():
    st.markdown(f"""
    <div class="material-card">
    <h4>{judul}</h4>
    <p>{isi}</p>
    </div>
    """, unsafe_allow_html=True)


# ==================================================
# KELOMPOK
# ==================================================

st.header("Anggota Kelompok")

st.markdown("""
<div class="material-card">

1. Rambu Marshanda Tamu Ina Paa<br>
2. Marcella Ariani<br>
3. Mareka Nazara F.<br>
4. Michael Zidane<br>
5. Muhammad Rafli

</div>
""", unsafe_allow_html=True)


# ==================================================
# TUGAS
# ==================================================

st.header("Tugas dan Proyek")

col1,col2,col3 = st.columns(3)

with col1:
    st.info("📄 Proposal")

with col2:
    st.info("🎥 Reels Instagram")

with col3:
    st.info("📘 Laporan Akhir")

tab1,tab2,tab3 = st.tabs([
    "Proposal",
    "Reels",
    "Laporan Akhir"
])

with tab1:

    st.subheader(
        "Mengapa Rasionalitas Manusia Melemah Saat Jatuh Cinta?"
    )

    if os.path.exists("assets/proposal.pdf"):

        with open("assets/proposal.pdf","rb") as file:

            st.download_button(
                "📄 Download Proposal",
                file,
                file_name="proposal.pdf"
            )

with tab2:

    st.subheader("🎬 Video Refleksi Pembelajaran")

    st.markdown("""
    Video refleksi pembelajaran Critical Thinking dapat diakses melalui tautan berikut:
    """)

    st.link_button(
        "🎥 Tonton Video Refleksi",
        "https://www.instagram.com/reel/DZXDR9JR2IN/"
    )

with tab3:
    st.subheader(
        "Mengapa Rasionalitas Manusia Melemah Saat Jatuh Cinta?"
    )
    if os.path.exists("assets/laporan_akhir.pdf"):

        with open("assets/laporan_akhir.pdf","rb") as file:

            st.download_button(
                "📘 Download Laporan Akhir",
                file,
                file_name="laporan_akhir.pdf"
            )

# ==================================================
# QUIZ
# ==================================================

st.header("Hasil Quiz")

quiz = pd.DataFrame({
    "Quiz":[
        "Quiz 1",
        "Quiz 2",
        "Quiz 3",
        "Quiz 4",
        "Quiz 5",
        "Quiz 6",
        "Quiz 7"
    ],
    "Nilai":[70,65,80,80,87,77,67]
})

fig = px.bar(
    quiz,
    x="Quiz",
    y="Nilai",
    text="Nilai",
    color="Nilai"
)

fig.update_layout(
    paper_bgcolor="white",
    plot_bgcolor="white",
    title="Performa Quiz"
)

st.plotly_chart(fig, width='stretch')

# ==================================================
# DASHBOARD NILAI
# ==================================================

avg = round(quiz["Nilai"].mean(),2)

c1,c2,c3 = st.columns(3)

with c1:
    st.metric("Rata-rata", avg)

with c2:
    st.metric("Nilai Tertinggi", 87)

with c3:
    st.metric("Jumlah Quiz", 7)

# ==================================================
# BUKTI QUIZ
# ==================================================

st.header("Bukti Hasil Quiz")

col1,col2,col3 = st.columns(3)

with col1:
    if os.path.exists("assets/quiz1.jpg"):
        st.image("assets/quiz1.jpg")

    if os.path.exists("assets/quiz4.jpg"):
        st.image("assets/quiz4.jpg")

    if os.path.exists("assets/quiz7.jpg"):
        st.image("assets/quiz7.jpg")

with col2:
    if os.path.exists("assets/quiz2.jpg"):
        st.image("assets/quiz2.jpg")

    if os.path.exists("assets/quiz5.jpg"):
        st.image("assets/quiz5.jpg")

with col3:
    if os.path.exists("assets/quiz3.jpg"):
        st.image("assets/quiz3.jpg")

    if os.path.exists("assets/quiz6.jpg"):
        st.image("assets/quiz6.jpg")

# ==================================================
# REFLEKSI
# ==================================================

st.header("Refleksi Pribadi")

tab1,tab2,tab3,tab4,tab5,tab6 = st.tabs([
    "Pertumbuhan",
    "Kompetensi",
    "Manfaat",
    "Pentingnya",
    "Hambatan",
    "Siapa Aku"
])

with tab1:
    st.write("""
        Mata kuliah Critical Thinking menjadi salah satu pengalaman belajar yang memberikan dampak signifikan terhadap cara saya memahami dunia di sekitar saya. Sebelum mengikuti perkuliahan ini, saya cenderung memandang proses berpikir sebagai aktivitas yang berlangsung secara alami tanpa perlu dievaluasi secara mendalam. Saya sering menganggap bahwa selama suatu pendapat terdengar masuk akal atau didukung oleh pengalaman pribadi, maka pendapat tersebut sudah cukup kuat untuk dijadikan dasar pengambilan keputusan. Namun, seiring berjalannya perkuliahan, saya mulai menyadari bahwa banyak kesalahan berpikir justru muncul dari asumsi-asumsi yang tidak pernah dipertanyakan. Mata kuliah ini mengajarkan bahwa berpikir bukan hanya tentang menghasilkan jawaban, tetapi juga tentang mengevaluasi bagaimana jawaban tersebut diperoleh.

        Berbagai aktivitas pembelajaran seperti diskusi kelas, analisis kasus, refleksi diri, serta evaluasi terhadap argumen membuat saya menyadari bahwa setiap informasi perlu ditinjau dari berbagai sudut pandang. Saya belajar bahwa sebuah kesimpulan yang tampak benar belum tentu didukung oleh alasan yang kuat. Sebaliknya, suatu pendapat yang berbeda dari keyakinan saya mungkin memiliki dasar argumentasi yang lebih logis dan lebih didukung oleh bukti. Kesadaran ini mendorong saya untuk lebih berhati-hati dalam menerima informasi dan lebih terbuka terhadap kemungkinan bahwa pemahaman saya sebelumnya tidak selalu tepat.

        Salah satu pembelajaran paling berharga yang saya peroleh adalah pentingnya kemampuan untuk mempertanyakan asumsi. Dalam banyak situasi, manusia cenderung menerima sesuatu sebagai kebenaran hanya karena telah dipercaya dalam waktu yang lama atau karena berasal dari sumber yang dianggap berwenang. Melalui mata kuliah ini, saya belajar bahwa sikap kritis tidak berarti menolak semua informasi, tetapi menempatkan informasi tersebut pada proses evaluasi yang rasional dan objektif. Saya mulai memahami bahwa berpikir kritis merupakan bentuk tanggung jawab intelektual yang membantu seseorang menghindari kesalahan penalaran dan membuat keputusan yang lebih baik.

        Pada akhirnya, mata kuliah ini tidak hanya mengajarkan keterampilan akademik, tetapi juga memberikan perubahan dalam cara saya memandang proses belajar itu sendiri. Saya menjadi lebih sadar bahwa pembelajaran bukan sekadar mengumpulkan pengetahuan, melainkan proses berkelanjutan untuk mempertanyakan, mengevaluasi, dan memperbaiki cara berpikir. Pengalaman tersebut menjadi fondasi penting bagi perkembangan pribadi maupun profesional saya di masa depan.
    """)
        

with tab2:
    st.write("""
        Setelah melakukan refleksi terhadap proses pembelajaran selama satu semester, saya menyadari bahwa salah satu kekuatan utama yang saya miliki adalah rasa ingin tahu yang tinggi terhadap berbagai fenomena dan permasalahan. Saya cenderung tertarik untuk mencari alasan mengapa suatu hal terjadi dan bagaimana suatu kesimpulan dapat dibentuk. Rasa ingin tahu tersebut mendorong saya untuk tidak mudah puas dengan jawaban yang bersifat sederhana, melainkan berusaha menggali informasi lebih dalam agar memperoleh pemahaman yang lebih komprehensif. Dalam konteks berpikir kritis, karakteristik ini menjadi modal penting karena proses berpikir yang baik selalu diawali oleh keinginan untuk memahami sesuatu secara lebih mendalam.

        Selain rasa ingin tahu, saya juga melihat adanya perkembangan dalam kemampuan analitis yang saya miliki. Selama mengikuti perkuliahan, saya semakin terbiasa mengidentifikasi hubungan antara fakta, asumsi, dan kesimpulan dalam suatu argumen. Saya mulai mampu membedakan mana informasi yang didukung oleh bukti dan mana yang hanya berdasarkan opini atau dugaan. Kemampuan ini membantu saya melihat suatu permasalahan secara lebih sistematis sehingga tidak hanya berfokus pada hasil akhir, tetapi juga memperhatikan proses yang mengarah pada hasil tersebut.

        Kekuatan lain yang saya nilai penting adalah kesediaan untuk belajar dari kesalahan. Dalam beberapa kesempatan, saya menemukan bahwa pendapat yang saya yakini ternyata memiliki kelemahan ketika diuji melalui diskusi atau analisis yang lebih mendalam. Alih-alih mempertahankan pendapat tersebut secara emosional, saya berusaha menerima kritik dan menggunakan masukan tersebut sebagai sarana pembelajaran. Saya menyadari bahwa kemampuan untuk mengubah pandangan berdasarkan bukti yang lebih kuat merupakan bagian penting dari kejujuran intelektual.

        Meskipun demikian, saya memahami bahwa kekuatan yang saya miliki masih perlu terus dikembangkan. Rasa ingin tahu harus diimbangi dengan kemampuan mengevaluasi sumber informasi secara kritis. Kemampuan analitis perlu dilatih agar semakin sistematis dan mendalam. Oleh karena itu, saya memandang kekuatan-kekuatan tersebut bukan sebagai pencapaian akhir, melainkan sebagai fondasi yang perlu terus diperkuat melalui pengalaman belajar yang berkelanjutan.
    """)


with tab3:
    st.write("""
        Sebelum mengikuti mata kuliah ini, saya memandang berpikir kritis sebagai kemampuan untuk memberikan pendapat atau mengkritik suatu gagasan. Namun, seiring dengan proses pembelajaran yang saya jalani, pemahaman tersebut mengalami perubahan yang cukup mendasar. Saya mulai memahami bahwa berpikir kritis merupakan kemampuan untuk mengevaluasi informasi secara rasional, objektif, dan sistematis sebelum membentuk keyakinan atau mengambil keputusan. Proses ini melibatkan kemampuan untuk mengidentifikasi asumsi, menilai kualitas bukti, mempertimbangkan alternatif penjelasan, serta menghindari berbagai bentuk bias yang dapat memengaruhi penilaian.

        Bagi saya, berpikir kritis bukan berarti selalu meragukan segala sesuatu atau mencari kesalahan dalam setiap argumen. Sebaliknya, berpikir kritis adalah upaya untuk memastikan bahwa suatu kesimpulan dibangun di atas dasar yang kuat dan dapat dipertanggungjawabkan. Dalam proses tersebut, seseorang perlu memiliki keseimbangan antara keterbukaan terhadap ide baru dan kemampuan untuk mengevaluasi ide tersebut secara objektif. Tanpa keterbukaan, seseorang akan sulit menerima perspektif yang berbeda. Namun tanpa evaluasi yang kritis, seseorang akan mudah menerima informasi yang belum tentu benar.

        Saya juga menyadari bahwa berpikir kritis memiliki peran yang sangat penting dalam kehidupan sehari-hari. Di era digital saat ini, informasi dapat diperoleh dengan sangat mudah, tetapi tidak semua informasi memiliki kualitas yang baik. Kemampuan berpikir kritis membantu saya memilah informasi yang dapat dipercaya dan menghindari kesimpulan yang didasarkan pada informasi yang menyesatkan. Selain itu, kemampuan ini juga membantu saya dalam menyelesaikan masalah, membuat keputusan, dan berkomunikasi dengan lebih efektif karena setiap pendapat yang saya sampaikan perlu didukung oleh alasan yang jelas.

        Oleh karena itu, saya memandang berpikir kritis sebagai keterampilan hidup yang tidak hanya relevan dalam lingkungan akademik, tetapi juga dalam berbagai aspek kehidupan. Kemampuan ini membantu saya menjadi individu yang lebih reflektif, lebih objektif, dan lebih bertanggung jawab terhadap setiap keputusan yang saya ambil.
    """)

with tab4:
    st.write("""
        Sebagai mahasiswa Statistika, saya melihat hubungan yang sangat erat antara berpikir kritis dan bidang ilmu yang saya pelajari. Statistika sering kali dipandang sebagai disiplin ilmu yang berfokus pada angka, rumus, dan perhitungan. Namun, melalui proses pembelajaran, saya menyadari bahwa angka tidak selalu berbicara dengan sendirinya. Di balik setiap data terdapat proses pengumpulan, pengolahan, interpretasi, dan pengambilan keputusan yang memerlukan kemampuan berpikir kritis agar hasil yang diperoleh dapat dipahami secara tepat.

        Dalam analisis statistik, kesalahan tidak selalu terjadi pada tahap perhitungan. Kesalahan sering kali muncul ketika seseorang gagal mempertanyakan kualitas data yang digunakan, asumsi yang mendasari metode analisis, atau konteks yang memengaruhi interpretasi hasil. Oleh karena itu, berpikir kritis membantu saya untuk tidak hanya menerima hasil analisis secara langsung, tetapi juga mengevaluasi bagaimana hasil tersebut diperoleh dan sejauh mana hasil tersebut dapat dipercaya.

        Mata kuliah Critical Thinking memberikan pemahaman bahwa seorang analis data tidak boleh hanya fokus pada aspek teknis. Kemampuan untuk mempertanyakan validitas data, mengidentifikasi potensi bias, dan mempertimbangkan berbagai kemungkinan interpretasi merupakan bagian penting dari proses analisis yang bertanggung jawab. Saya belajar bahwa keputusan yang diambil berdasarkan data harus mempertimbangkan kualitas bukti dan keterbatasan yang ada, bukan hanya berdasarkan hasil perhitungan semata.

        Ke depan, saya berharap dapat menerapkan prinsip-prinsip berpikir kritis dalam setiap proses analisis yang saya lakukan. Dengan demikian, saya tidak hanya menjadi individu yang mampu mengolah data secara teknis, tetapi juga mampu menghasilkan kesimpulan yang relevan, akurat, dan memiliki nilai bagi pengambilan keputusan.with tab5:
    """)

with tab5:
    st.write("""
        Salah satu tantangan terbesar yang saya hadapi dalam mengembangkan kemampuan berpikir kritis adalah kecenderungan untuk mengambil kesimpulan terlalu cepat. Dalam beberapa situasi, saya menyadari bahwa pengalaman pribadi sering kali menjadi dasar utama dalam menilai suatu permasalahan. Meskipun pengalaman memiliki nilai yang penting, saya belajar bahwa pengalaman individu tidak selalu cukup untuk menjelaskan realitas yang lebih luas. Ketika suatu informasi sesuai dengan pengalaman atau keyakinan yang saya miliki, saya cenderung menerimanya tanpa melakukan evaluasi yang memadai.

        Selain itu, saya juga menyadari adanya kecenderungan untuk mencari informasi yang mendukung pandangan saya dibandingkan informasi yang menentangnya. Setelah mempelajari konsep bias kognitif dalam mata kuliah ini, saya memahami bahwa kecenderungan tersebut dapat menghambat objektivitas dan menyebabkan kesalahan dalam pengambilan keputusan. Kesadaran terhadap kelemahan ini menjadi langkah awal yang penting dalam proses perbaikan diri.

        Hambatan lainnya adalah keterbatasan waktu dan kesabaran dalam menganalisis suatu permasalahan secara mendalam. Dalam situasi tertentu, saya lebih memilih solusi yang cepat dibandingkan proses evaluasi yang lebih komprehensif. Namun, saya mulai menyadari bahwa keputusan yang dibuat secara terburu-buru sering kali menghasilkan konsekuensi yang kurang optimal. Oleh karena itu, saya berusaha melatih diri untuk memberikan ruang bagi proses refleksi sebelum mengambil keputusan.

        Saya memahami bahwa kemampuan berpikir kritis tidak berkembang secara instan. Diperlukan latihan yang konsisten, kesediaan untuk menerima kritik, dan keberanian untuk mengakui kesalahan ketika ditemukan bukti yang lebih kuat. Dengan terus mengevaluasi kelemahan yang saya miliki, saya berharap dapat menjadi individu yang lebih objektif dan lebih matang dalam menghadapi berbagai permasalahan.
    """)

with tab6:
    st.write("""
        Setelah menjalani proses pembelajaran selama satu semester, saya melihat diri saya sebagai individu yang sedang berada dalam proses perkembangan yang berkelanjutan. Saya menyadari bahwa identitas intelektual seseorang tidak ditentukan oleh seberapa banyak pengetahuan yang dimiliki, tetapi oleh kesediaannya untuk terus belajar, mempertanyakan pemikirannya sendiri, dan memperbaiki kesalahan yang ditemukan. Kesadaran ini menjadi salah satu hasil refleksi paling penting yang saya peroleh dari mata kuliah Critical Thinking.

        Saya memahami bahwa setiap individu memiliki keterbatasan dalam cara berpikirnya. Tidak ada seseorang yang sepenuhnya bebas dari bias, asumsi, atau kesalahan penalaran. Namun, yang membedakan adalah sejauh mana seseorang bersedia menyadari keterbatasan tersebut dan berupaya mengatasinya. Melalui berbagai pengalaman belajar, saya menjadi lebih sadar terhadap proses berpikir yang saya lakukan dan lebih berhati-hati dalam membentuk kesimpulan.

        Saya juga mulai melihat bahwa pembelajaran bukanlah tujuan yang memiliki titik akhir. Setiap pengalaman, diskusi, kegagalan, maupun keberhasilan dapat menjadi sumber pembelajaran apabila direfleksikan secara kritis. Oleh karena itu, saya ingin terus mengembangkan kebiasaan refleksi sebagai bagian dari proses pertumbuhan pribadi dan profesional. Saya percaya bahwa kemampuan untuk mengevaluasi diri sendiri merupakan salah satu bentuk kecerdasan yang sangat penting dalam menghadapi perubahan dan tantangan di masa depan.

        Pada akhirnya, saya melihat diri saya sebagai seorang pembelajar sepanjang hayat yang terus berusaha menjadi lebih baik dari waktu ke waktu. Mata kuliah Critical Thinking memberikan bekal yang berharga untuk perjalanan tersebut, karena mengajarkan bahwa pertumbuhan tidak hanya terjadi melalui penambahan pengetahuan, tetapi juga melalui keberanian untuk mempertanyakan, merefleksikan, dan memperbaiki cara berpikir yang dimiliki.
    """)

# ==================================================
# PENUTUP
# ==================================================

st.header("Penutup")

st.markdown("""
<div class="material-card">
            
Perjalanan saya dalam mata kuliah Critical Thinking tidak hanya memberikan pemahaman mengenai konsep dan teori berpikir kritis, tetapi juga membantu saya mengenali cara saya berpikir, mengambil keputusan, dan memandang berbagai permasalahan dalam kehidupan sehari-hari. Melalui berbagai diskusi, tugas, refleksi, dan analisis kasus, saya belajar bahwa tidak semua informasi dapat diterima begitu saja. Setiap informasi perlu dievaluasi secara rasional, didukung oleh bukti yang memadai, serta dipertimbangkan dari berbagai sudut pandang sebelum dijadikan dasar dalam membentuk keyakinan atau mengambil keputusan.

Sebagai mahasiswa Statistika, pengalaman belajar ini memberikan kesadaran bahwa kemampuan teknis saja tidak cukup untuk menghasilkan analisis yang berkualitas. Dibutuhkan kemampuan berpikir kritis untuk mempertanyakan asumsi, mengevaluasi kualitas data, mengidentifikasi potensi bias, serta menafsirkan hasil secara objektif dan bertanggung jawab. Saya menyadari bahwa proses berpikir yang baik merupakan fondasi penting dalam menghasilkan keputusan yang valid, baik dalam konteks akademik, profesional, maupun kehidupan bermasyarakat.

Melalui portofolio reflektif ini, saya dapat melihat perkembangan diri yang telah terjadi selama satu semester. Saya menyadari berbagai kekuatan yang dapat terus dikembangkan sekaligus mengenali kelemahan yang perlu diperbaiki. Mata kuliah ini mengajarkan bahwa belajar bukan hanya tentang memperoleh pengetahuan baru, tetapi juga tentang keberanian untuk mempertanyakan asumsi, merefleksikan pengalaman, dan memperbaiki cara berpikir secara berkelanjutan. Oleh karena itu, saya berkomitmen untuk terus menerapkan prinsip-prinsip berpikir kritis dalam setiap proses pembelajaran, pengambilan keputusan, dan tantangan yang akan saya hadapi di masa depan sebagai seorang pembelajar sepanjang hayat.

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="footer">

<hr>

<b>Portofolio Reflektif Critical Thinking</b><br>
Program Studi Statistika<br>
Matana University<br><br>

© 2026

</div>
""", unsafe_allow_html=True)