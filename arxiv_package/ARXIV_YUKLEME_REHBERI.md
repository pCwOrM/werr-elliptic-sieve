# 🚀 arXiv Adım Adım Yükleme Rehberi (Werr Multi-Layer Sieve & Vélu Isogeny Engine)

Bu rehber, **Automated Reasoning and In-Worker Verification for High-Rank Elliptic Curves: The 4-Stage Werr Algebraic Sieve, Conductor Certification, and Isogeny Graph Transport on the NSF ICARM Leaderboard** makalesinin **Zerrin Dağlı**'nın arXiv hesabı üzerinden ([arxiv.org/submit](https://arxiv.org/submit)) tek seferde, sıfır hata ile ve en yüksek akademik standartlarda yüklenmesi için ekran ekran hazırlanmıştır.

> [!IMPORTANT]
> **Zerrin Dağlı Hesabı ve Kategori Tercihi:**  
> Makale Zerrin Hanım'ın hesabından yüklenecektir ve kendisinin **`cs.LO` (Logic in Computer Science)** alanında resmi endorsement'ı bulunmaktadır. Bu nedenle ana kategori (Primary Classification) olarak **`cs.LO`** seçilecek, matematiksel ve sembolik hesaplama kategorileri (`math.NT`, `cs.SC`, `math.AG`) ise çapraz kategori (Cross-List) olarak eklenecektir. Makale kurgusu NSF ICARM'ın otomatik ispat/doğrulama motoru (automated reasoning & in-worker certificate verification) üzerine inşa edildiği için `cs.LO` seçimi hem teknik hem de içerik açısından tam uyumludur.
>
> **Yazar Sıralaması ve Unvanlar:**  
> 1. Yazar **Volkan Dağlı**, 2. Yazar **Zerrin Dağlı**, 3. Yazar **Dağhan Dağlı**'dır. arXiv formlarında unvan (Dr., Prof. vb.) kullanılmaz.

---

## 📂 Gönderilecek Dosya ve Konumu

arXiv'e yüklenecek tek dosya şudur:
* **Dosya Yolu:**  
  [`c:\Users\maat\Documents\antigravity\werr-elliptic-sieve\arxiv_package\arxiv_bundle.tar.gz`](file:///c:/Users/maat/Documents/antigravity/werr-elliptic-sieve/arxiv_package/arxiv_bundle.tar.gz)  
  *(Aynası: [`c:\Users\maat\Documents\antigravity\wonderful-raman\arxiv_werr_elliptic_sieve_package\arxiv_bundle.tar.gz`](file:///c:/Users/maat/Documents/antigravity/wonderful-raman/arxiv_werr_elliptic_sieve_package/arxiv_bundle.tar.gz))*

> [!WARNING]
> Arşiv paketinin (`arxiv_bundle.tar.gz`) içinde **sadece saf `.tex` kaynak dosyası** (`Werr_Elliptic_Sieve_ICARM_Preprint.tex`) yer alır. Sakın arşive PDF veya rehber dosyası eklemeyiniz; arXiv sistemi kendi sunucusunda bu `.tex` dosyasını derleyerek resmi PDF'i kendisi üretir. Önizleme için paket klasöründeki `Werr_Elliptic_Sieve_ICARM_Preprint.pdf` dosyasını bilgisayarınızda inceleyebilirsiniz.

---

## 🧭 Ekran Ekran Gönderim Adımları

### Adım 1: arXiv Girişi ve Gönderim Başlatma
1. Tarayıcınızda [https://arxiv.org/submit](https://arxiv.org/submit) adresine gidin.
2. **Zerrin Dağlı**'nın kullanıcı hesabı ile giriş yapın.
3. **"Start New Submission"** butonuna tıklayın.

---

### Adım 2: Lisans ve Şartlar (Verify & License)
1. **Terms of Service:** Şartları onaylayın (Checkboxes).
2. **Authorship Status:**  
   * *"I am an author of this paper and have permission from all co-authors to submit it."* seçeneğini işaretleyin.
3. **Select a License:**  
   * **`arXiv.org perpetual non-exclusive license to distribute this article`** seçeneğini ve yanındaki:
   * **`Creative Commons Attribution (CC BY 4.0)`** lisansını seçin.

---

### Adım 3: Dosya Yükleme (Upload Files)
1. **"Browse"** veya **"Dosya Seç"** butonuna tıklayın.
2. Bilgisayarınızdan şu dosyayı seçin:
   ```text
   c:\Users\maat\Documents\antigravity\werr-elliptic-sieve\arxiv_package\arxiv_bundle.tar.gz
   ```
3. **"Upload file"** butonuna basın.
4. Dosya yüklendikten sonra sistem arşivi açacak ve listede `Werr_Elliptic_Sieve_ICARM_Preprint.tex` dosyasını gösterecektir.
5. **"Continue: Process Files"** butonuna tıklayın. Sistem LaTeX derlemesini başlatır. 5-10 saniye içinde **"Processing Successful"** onayı gelecektir (Bağımsız AMS-LaTeX yapısıyla test edilip onaylanmıştır).

---

### Adım 4: Üretilen PDF'i İnceleme (View Paper)
1. Ekranda beliren **"View PDF"** butonuna tıklayın.
2. Üretilen resmi PDF'in sayfa düzenini, tabloları ve kaynakçayı kontrol edin.
3. Kontrol tamamlanınca **"Next: Metadata"** butonuna tıklayın.

---

### Adım 5: Künye ve Üstveri (Metadata) Girişi

Aşağıdaki kutularda yer alan metinleri birebir kopyalayıp ilgili alanlara yapıştırın:

#### 1. Title (Makale Başlığı)
```text
Automated Reasoning and In-Worker Verification for High-Rank Elliptic Curves: The 4-Stage Werr Algebraic Sieve, Conductor Certification (log N), and Velu Isogeny Graph Transport on the NSF ICARM Leaderboard
```

#### 2. Authors (Yazarlar)
```text
Volkan Dağlı, Zerrin Dağlı, Dağhan Dağlı
```

#### 3. Primary Classification (Ana Kategori)
* Açılır menüden Zerrin Hanım'ın endorse yetkisinin bulunduğu kategoriyi seçin:
  ```text
  cs.LO (Computer Science - Logic in Computer Science)
  ```

#### 4. Cross-Lists / Secondary Categories (Ek / Çapraz Kategoriler)
* Sırasıyla şu 3 kategoriyi ekleyin (**"Add cross-list"**):
  1. `math.NT` (Mathematics - Number Theory)
  2. `cs.SC` (Computer Science - Symbolic Computation)
  3. `math.AG` (Mathematics - Algebraic Geometry)

#### 5. Abstract (Özet Metni)
*(Aşağıdaki düz metni kopyalayıp "Abstract" kutusuna yapıştırın)*
```text
The computational verification of high-rank elliptic curves over Q has long been bottlenecked by the difficulty of certifying global arithmetic invariants, most notably the arithmetic conductor N. In modern automated reasoning platforms such as the NSF Institute for Computer-Aided Reasoning in Mathematics (ICARM) Elliptic Curve Rank Leaderboard (maintained under U.S. National Science Foundation Grant DMS-2425401), candidate curves are verified inside an isolated Cloudflare Worker running a WebAssembly build of PARI/GP 2.17.2. While the ICARM kernel certifies rational point independence via an exact, floating-point-free 2-descent quadratic-character proof certificate over F_2 and computes the global minimal model, minimal discriminant |Delta_min|, Faltings height h_F(E), and naive height h_naive(E) via ellminimalmodel without factoring Delta_min, automatic conductor determination (autoBadPrimes) is restricted to trial division up to 10^7. Whenever |Delta_min| contains two or more prime factors exceeding 10^7---as routinely occurs for high-rank curves where |Delta_min| spans 50 to 110 decimal digits---unassisted verification returns conductor: null (?), excluding the curve from the Conductor N leaderboard.

In this paper, we present an automated proof-certificate generation and isogeny graph exploration framework that resolves this bottleneck. Our methodology unites two engines tailored to the arithmetic of elliptic curves: (1) the 4-Stage Werr Multi-Layer Algebraic Sieve, which couples Stage 1 Weierstrass covariant gcd kernels (gcd(a_4, a_6, Delta, c_4, c_6)) and division-polynomial root bracketing, Stage 2 elliptic syzygy cubic divisor peeling (Delta = d_0 * s^3) and 2-torsion pairwise root-difference decomposition, Stage 3 parallel Pollard-Brent rho, Pollard p-1, and multi-curve Montgomery/Weierstrass ECM, and Stage 4 word-packed F_2 Multipolynomial Quadratic Sieve (MPQS) with deterministic primality closure; and (2) systematic Velu Isogeny Graph Transport, traversing rational n-isogeny neighborhoods (n in {2, 3, 4, 5, 6, 8, 10, 12}) and exact 12-case Weierstrass point-interpolation recovery to discover minimal models with strictly reduced discriminants and heights while preserving Mordell-Weil rank and conductor.

Deploying this pipeline on the NSF ICARM leaderboard, we established 230 newly certified curves (#4308-#4537) across 8 rational torsion subgroups with 100% certified conductor factorizations (230/230, zero unknown conductors), securing 30 #1 Gold records, 80 Top-3 podiums, and 418 Top-10 placements across 43 active leaderboards. Landmark achievements include the "Grand Slam" curve #4315 (T = Z/2Z x Z/2Z, Rank >= 9), which simultaneously ranks #1 in all four metrics (N, |Delta|, h_F, h_naive); the complete 21-prime factorization of a 110-digit discriminant for the Klagsbrun-Dujella Rank >= 12 curve #4383; and full conductor certification (log N = 141.86) of a 54-digit composite cofactor for the Elkies Rank >= 19 curve #4323. All datasets, reproduction scripts, and verification receipts are permanently archived at CERN Zenodo (DOI: 10.5281/zenodo.23436282).
```

#### 6. Comments (Yorum / Ek Bilgi)
```text
12 pages, 6 tables. Self-contained AMS-LaTeX preprint. Full datasets, verification receipts, and reproduction tools for 230 certified curves on the NSF ICARM Leaderboard (Grant DMS-2425401) openly available at Zenodo: https://doi.org/10.5281/zenodo.23436282 and GitHub: https://github.com/pCwOrM/werr-elliptic-sieve
```

#### 7. MSC Class (Mathematics Subject Classification 2020)
```text
11G05, 11Y05, 11Y16, 14H52, 68T15, 68W30
```

#### 8. ACM Class (ACM Computing Classification System 2012)
```text
Theory of computation -> Logic and verification; Automated reasoning; Symbolic and algebraic manipulation; Computational number theory
```

#### 9. Report Number (Rapor Numarası)
```text
ICARM-WERR-2026-01
```

---

### Adım 6: Önizleme ve Son Onay (Preview & Submit)
1. Bütün alanları girdikten sonra **"Save and Continue"** butonuna tıklayın.
2. Önizleme özet sayfasında:
   * **Title**, **Authors** (Volkan Dağlı, Zerrin Dağlı, Dağhan Dağlı), **Primary Category** (`cs.LO`) ve **Cross-Lists** (`math.NT`, `cs.SC`, `math.AG`) bilgilerini son kez teyit edin.
3. Sayfanın en altındaki **"Submit Article"** butonuna basarak gönderimi tamamlayın.
4. Ekrana `submit/XXXXXXX` şeklinde geçici gönderim numarası gelecektir.

---

## 📌 Gönderim Sonrası Yapılacaklar
Gönderim onay e-postası Zerrin Hanım'ın adresine ulaştığında geçici numara (`submit/XXXXXXX`) not edilecek ve arXiv duyuru gününde makale resmi arXiv ID'sine (örneğin `arXiv:2610.XXXXX`) kavuşacaktır.
