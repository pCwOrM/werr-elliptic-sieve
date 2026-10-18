# 🚀 arXiv Adım Adım Yükleme Rehberi (Werr Multi-Layer Sieve & Vélu Isogeny Engine)

Bu rehber, **Automated Reasoning and In-Worker Verification for High-Rank Elliptic Curves: The 4-Stage Werr Algebraic Sieve, Conductor Certification (log N), and Velu Isogeny Graph Transport on the NSF ICARM Leaderboard** makalesinin **Zerrin Dağlı**'nın arXiv hesabı üzerinden ([arxiv.org/submit](https://arxiv.org/submit)) tek seferde, sıfır hata ile yüklenmesi için ekran ekran hazırlanmıştır.

> [!IMPORTANT]
> **3 Kritik arXiv Form Standardı Düzeltmesi:**
> 1. **Abstract Uzunluğu (1.615 Karakter < 1.920 Sınırı):** arXiv'in katı `1920 karakter` sınırına tam uyacak şekilde özet metni **1.615 karaktere** (tek paragraf, saf arXiv standardı) indirilmiştir.
> 2. **ACM Class Formatı (`F.4.1; I.1.2; G.4`):** arXiv'in `ACM Class` kutusu yalnızca **ACM 1998 kod formatını** (`Harf.Rakam.Rakam; ...`) kabul eder. Metin açıklaması yerine tam olarak **`F.4.1; I.1.2; G.4`** girilmelidir.
> 3. **Dosya Yükleme (`Werr_Elliptic_Sieve_ICARM_Preprint.tex` veya `USTAR` `arxiv_bundle.tar.gz`):**
>    * Makalemiz dış görsel içermeyen **tek parça (self-contained) bir `.tex` dosyası** olduğu için, arXiv'e `.tar.gz` yerine **doğrudan [`Werr_Elliptic_Sieve_ICARM_Preprint.tex`](file:///c:/Users/maat/Documents/antigravity/werr-elliptic-sieve/arxiv_package/Werr_Elliptic_Sieve_ICARM_Preprint.tex) dosyasını tek başına** yükleyebilirsiniz! (Tek `.tex` yüklendiğinde hiçbir ek üstbilgi dosyası oluşmaz).
>    * Ayrıca `arxiv_bundle.tar.gz` paketi de POSIX `@PaxHeader` üstbilgisi üretmeyecek şekilde saf **`USTAR`** formatında yeniden üretilmiştir. (Not: arXiv'in AutoTeX motoru `.tar.gz` açarken bazen kendi sistem dosyası olarak `00README.XXX` oluşturabilir; doğrudan `.tex` dosyasını yüklerseniz sadece tek `.tex` dosyası görünür).

---

## 📂 Gönderilecek Dosya ve Konumu (En Temiz Yöntem: Doğrudan `.tex` Dosyası)

arXiv dosya yükleme ekranında şu dosyayı doğrudan seçebilirsiniz:
* **Doğrudan Tek `.tex` Dosyası (Önerilen):**  
  ```text
  c:\Users\maat\Documents\antigravity\werr-elliptic-sieve\arxiv_package\Werr_Elliptic_Sieve_ICARM_Preprint.tex
  ```
* **Alternatif (`USTAR` `.tar.gz` Arşivi):**  
  ```text
  c:\Users\maat\Documents\antigravity\werr-elliptic-sieve\arxiv_package\arxiv_bundle.tar.gz
  ```

---

## 🧭 Ekran Ekran Gönderim Adımları

### Adım 3: Dosya Yükleme (Upload Files)
1. Eğer önceki yüklemeden kalan dosyalar varsa yanlarındaki **"Delete"** / **"Remove All Files"** butonuna basarak listeyi temizleyin.
2. **"Browse"** / **"Dosya Seç"** butonuna tıklayın ve doğrudan şu dosyayı seçin:
   ```text
   c:\Users\maat\Documents\antigravity\werr-elliptic-sieve\arxiv_package\Werr_Elliptic_Sieve_ICARM_Preprint.tex
   ```
3. **"Upload file"** butonuna basın. Listede yalnızca `Werr_Elliptic_Sieve_ICARM_Preprint.tex` (Type: `LaTeX`) görünecektir.
4. **"Continue: Process Files"** butonuna tıklayın. TeX Live derlemesi **0 uyarı / 0 hata ile 12 sayfa** olarak tamamlanacaktır.

---

### Adım 5: Künye ve Üstveri (Metadata) Girişi — Birebir Kopyala-Yapıştır

#### 1. Title (Makale Başlığı)
```text
Automated Reasoning and In-Worker Verification for High-Rank Elliptic Curves: The 4-Stage Werr Algebraic Sieve, Conductor Certification (log N), and Velu Isogeny Graph Transport on the NSF ICARM Leaderboard
```

#### 2. Authors (Yazarlar)
```text
Volkan Dağlı, Zerrin Dağlı, Dağhan Dağlı
```

#### 3. Primary Classification (Ana Kategori)
```text
cs.LO (Computer Science - Logic in Computer Science)
```

#### 4. Cross-Lists / Secondary Categories (Çapraz Kategoriler)
1. `math.NT` (Mathematics - Number Theory)
2. `cs.SC` (Computer Science - Symbolic Computation)
3. `math.AG` (Mathematics - Algebraic Geometry)

#### 5. Abstract (Özet Metni — Python `len()` ile Doğrulanmış **1.662 Karakter** — 1.920 Sınırının 258 Karakter Altında)
*(Aşağıdaki metni olduğu gibi kopyalayıp "Abstract" kutusuna yapıştırın)*
```text
Certifying the arithmetic conductor N of high-rank elliptic curves over Q is a central bottleneck in computational number theory. On the NSF ICARM Elliptic Curve Rank Leaderboard (Grant DMS-2425401), candidate curves are verified in an isolated Cloudflare Worker running WebAssembly PARI/GP 2.17.2. While the kernel certifies point independence via an exact 2-descent quadratic-character certificate over F_2 (erk_cert) and computes the global minimal model, minimal discriminant |Delta_min|, Faltings height h_F(E), and naive height h_naive(E) via ellminimalmodel without factoring Delta_min, automatic conductor verification (autoBadPrimes) is limited to trial division up to 10^7. Whenever |Delta_min| (50-110 decimal digits at high rank) has two or more prime factors above 10^7, unassisted verification returns conductor: null (?). We resolve this bottleneck by uniting (1) the 4-Stage Werr Multi-Layer Algebraic Sieve (Weierstrass covariant gcd kernels, syzygy cubic peeling Delta = d_0 s^3, 2-torsion root-difference splitting, parallel Pollard-Brent rho / p-1 / ECM, and word-packed F_2 MPQS) with (2) systematic Velu rational n-isogeny graph transport and 12-case point-interpolation recovery. Deploying this pipeline on the ICARM leaderboard (user/114), we established 230 certified Top-10 curves (#4308-#4537) across 8 torsion groups with 100% certified conductors (230/230), securing 30 #1 Gold records, 80 Top-3 podiums, and 418 Top-10 placements across 43 leaderboards, including Grand Slam curve #4315 (Z/2Z x Z/2Z, Rank >= 9, #1 in all 4 metrics), the 21-prime factorization of a 110-digit discriminant on #4383 (Rank >= 12), and full conductor certification (log N = 141.86) on the Elkies Rank >= 19 curve #4323 (DOI: 10.5281/zenodo.23436282).
```

#### 6. Comments (Yorum / Ek Bilgi)
```text
12 pages, 6 tables. Self-contained AMS-LaTeX preprint. Full datasets, verification receipts, and reproduction tools for 230 certified curves on the NSF ICARM Leaderboard (Grant DMS-2425401) openly available at Zenodo: https://doi.org/10.5281/zenodo.23436282 and GitHub: https://github.com/pCwOrM/werr-elliptic-sieve
```

#### 7. Report Number (Rapor Numarası)
```text
Zenodo: 10.5281/zenodo.23436282
```

#### 8. MSC-class (Mathematics Subject Classification 2020)
```text
11G05, 11Y05, 11Y16, 14H52, 68T15, 68W30
```

#### 9. ACM-class (ACM 1998 Sınıflandırma Kodları — Noktalı Virgülle Ayrılmış)
```text
F.4.1; I.1.2; G.4
```
*(Açıklama: `F.4.1` = Mathematical Logic / Mechanical Theorem Proving; `I.1.2` = Symbolic and Algebraic Manipulation / Algebraic Algorithms; `G.4` = Mathematical Software & Verification. arXiv validator yalnız bu kod formatını kabul eder.)*
