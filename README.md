# GASHAM DownloaderOG

Termux üçün universal media yükləyici.
YouTube, TikTok, Instagram, Facebook, X/Twitter, Reddit, Vimeo, Dailymotion və
yt-dlp-nin dəstəklədiyi yüzlərlə platformadan video və musiqi yükləyin —
yalnız **Share → Termux** ilə — link avtomatik tanınır, platforma avtomatik
müəyyən olunur və uyğun proses avtomatik başlayır.

---

## 1. Layihə haqqında

GASHAM DownloaderOG yüngül və sürətli bir Termux alətidir. Telefonda videonu
açıb **Paylaş (Share)** düyməsinə basdıqdan sonra **Termux** seçirsiniz —
sistem linki avtomatik tanıyır:

- **Instagram / TikTok / Facebook / X (Twitter)** — menyu göstərilmədən
  avtomatik, ən yüksək keyfiyyətdə yüklənir (video və şəkil); TikTok-da web
  marşrutu uğursuz olarsa sistem avtomatik mobil API marşrutuna keçir
- **YouTube / digər platformalar** — yalnız videoda real mövcud olan
  keyfiyyətlər göstərilir, istədiyinizi seçirsiniz (MP3 seçimi də var)
- **YouTube Shorts** — menyu göstərilmədən avtomatik yüklənir
- **İnteraktiv rejim** — Termux-da `gasham` yazıb Enter etdikdə banner və
  **"Link göndərin:"** görünür, linki yapışdırıb Enter basırsınız
- **Sayt linkləri** — səhifədəki bütün yüklənə bilən videolar avtomatik
  aşkarlanır və nömrəli siyahı kimi təqdim olunur

Yükləmə mühərriki olaraq **yt-dlp** istifadə olunur — ona görə yüzlərlə
platformanın dəstəyi avtomatik yenilənir və yükləmə sürəti maksimumdur.

## 2. Əsas xüsusiyyətlər

- Share → Termux ilə avtomatik link qəbulu
- `gasham` əmri ilə interaktiv işə salma — banner + "Link göndərin:"
- Avtomatik platforma aşkarlama (Instagram/TikTok/Facebook/X → menyusuz,
  ən yüksək keyfiyyət; YouTube/digər → dinamik keyfiyyət siyahısı)
- Dinamik keyfiyyət sistemi — yalnız mənbədə real mövcud keyfiyyətlər
  göstərilir (sabit siyahı yoxdur)
- Sayt səhifələrindəki bütün videoların avtomatik aşkarlanması və nömrəli
  siyahı ilə seçim (məs. `1. Video 1`, `2. Video 2`, ...)
- Hər keyfiyyətin qarşısında təxmini fayl ölçüsü (MB) göstərilir
  (məs. `720p — 450 MB`) — bitrate + müddət əsasında hesablanır
- YouTube Shorts üçün bir kliklə avtomatik yükləmə
- YouTube və digər platformalarda **MP3 yüklə** seçimi
- Canlı yükləmə prosesi (yt-dlp progress bar)
- Orijinal video başlığı ilə fayl adlandırma (`%(title)s.%(ext)s`,
  Unicode/Azərbaycan dili dəstəyi)
- Eyni adlı fayl mövcuddursa üzərinə yazılmır — avtomatik `(1)`, `(2)` əlavə olunur
- Yükləmə temp qovluqda aparılır, bitdikdə **cut (mv)** ilə əvvəlcə
  `/storage/emulated/0/Download`-ə, emal bitdikdən sonra isə
  `/storage/emulated/0/DownloaderOG` klasörünə keçirilir (kök səviyyə) —
  kopya yaradılmır, əlavə yer tutmur
- Fayllar **MediaStore/MediaScanner** (`termux-media-scan`) ilə sistemə
  qeydiyyata alınır — şəkillər Qalereyada, MP3/audio fayllar musiqi
  pleyerlərində avtomatik görünür
- MP3 sürətli yükləmə üçün optimallaşdırılıb (m4a mənbə + sürətli bitrate);
  fayla ID3 metadatası (başlıq/artist) yazılır və `.mp3` / `audio/mpeg`
  kimi qeydiyyata alınır — musiqi pleyerləri avtomatik tanıyır
- Yükləmə **uğurla** tamamlandıqda Termux tamamilə bağlanır — Termux-un rəsmi
  `com.termux.service_stop` mexanizmi ilə bütün sessiyalar dayandırılır və
  proqram avtomatik bağlanır (istifadəçi heç bir düyməyə toxunmur);
  yükləmə uğursuz olarsa Termux açıq qalır və menyuya qayıdılır
- `GASHAM` ASCII başlığı ilə professional terminal interfeysi
- Bir dəfəlik quraşdırma — ikinci dəfə konfiqurasiya tələb olunmur

## 3. Dəstəklənən platformalar

yt-dlp extractor sistemi sayəsində avtomatik:

- YouTube (video + Shorts)
- TikTok
- Instagram
- Facebook
- X/Twitter
- Reddit
- Vimeo
- Dailymotion
- və yt-dlp-nin dəstəklədiyi digər yüzlərlə platforma

> ⚖️ Proqram yalnız qanuni olaraq yükləməyə icazəniz olan və ya müəllif
> hüquqlarını pozmayan məzmun üçün nəzərdə tutulub.

## 4. Termux quraşdırılması

1. Termux-u quraşdırın ([F-Droid](https://f-droid.org/) və ya rəsmi kanaldan).
2. Termux-u açın və klonlayın:

```bash
pkg update -y && pkg install -y git
git clone https://github.com/gashamorujov/DownloaderOG.git
cd DownloaderOG
```

## 5. İlk quraşdırma əmri

```bash
bash install.sh
```

Quraşdırıcı avtomatik olaraq:

- Paketləri yeniləyir (`apt update && apt upgrade`)
- Storage icazəsi istəyir (`termux-setup-storage`)
- `python`, `ffmpeg`, `termux-api` quraşdırır
- `deno` quraşdırır (YouTube üçün tələb olunan JS mühərriki)
- `yt-dlp` quraşdırır/yeniləyir
- `curl_cffi` quraşdırır (TikTok üçün tələb olunan brauzer impersonasiya dəstəyi)
- `~/.config/downloaderog/` qovluğunu yaradır (cookies.txt üçün)
- `/storage/emulated/0/Download` qovluğunu yaradır
- `~/bin/` qovluğunu yaradır
- `~/bin/termux-url-opener` faylını quraşdırır və icra icazəsi verir (Share inteqrasiyası)
- `~/.termux/termux-url-opener` ünvanını da yeniləyir (müasir Termux üçün)

`~/bin/termux-url-opener` artıq mövcuddursa, köhnəsi `termux-url-opener.bak`
kimi backup edilir və yeni versiya ilə avtomatik yenilənir — `install.sh`
hər işlədiləndə bunu özü edir.

## 6. Storage icazəsinin verilməsi

```bash
termux-setup-storage
```

Android-də açılan pəncərədə **Allow / İcazə ver** düyməsini basın. Quraşdırıcı
bunu avtomatik istəyir, lakin istənilən vaxt əl ilə də edə bilərsiniz.

## 7. İstifadə qaydası

Telefonda istənilən videonu/musiqini açın:

1. **Share (Paylaş)** düyməsinə basın
2. Menyudan **Termux** seçin
3. Sistem platformanı avtomatik müəyyən edir:
   - Instagram/TikTok/Facebook/X → yükləmə avtomatik başlayır (seçim yoxdur)
   - YouTube/digər → real keyfiyyətlər göstərilir, nömrə yazıb Enter basın

```text
MP4
  1. 144p — 12 MB
  2. 360p — 120 MB
  3. 720p — 450 MB
  4. 1080p — 850 MB
MP3
  5. MP3 yüklə
╠═▶ A. About
╠═▶ Q. Çıxış
╚═:➤
```

`A` yazdıqda məlumat (About) göstərilir və yenidən seçim menyusuna qayıdılır.
Yuxarıdakı siyahı nümunədir — sistem yalnız həmin videoda həqiqətən mövcud
olan keyfiyyətləri göstərir. Birbaşa fayl linklərində (məs. `.mp4`) keyfiyyət
siyahısı olmadığı üçün **"1. Ən yaxşı keyfiyyət (MP4)"** seçimi göstərilir.
Yükləmə **uğurla** başa çatdıqda yaşıl `[✓]` mesajı göstərilir və dərhal
ardınca Ctrl+C + Enter ekvivalenti avtomatik icra olunur: Termux-un rəsmi
`com.termux.service_stop` aksiyası ilə proqram tamamilə bağlanır —
istifadəçi heç bir düyməyə (Enter, Ctrl+Z, exit) toxunmur, heç bir
əməliyyat tələb olunmur. Yükləmə xəta ilə bitsə, Termux bağlanmır — menyuya
qayıdılır və yenidən cəhd etmək mümkündür.

Əl ilə test üçün link skriptə birbaşa da verilə bilər:

```bash
bash ~/bin/termux-url-opener "https://www.youtube.com/watch?v=..."
bash ~/.termux/termux-url-opener "https://www.youtube.com/watch?v=..."
```

İnteraktiv rejim — Termux açıq olduqda:

```bash
gasham
```

`gasham` komandası quraşdırma zamanı həm `$PREFIX/bin/gasham` (hər açılışda
PATH-dədir), həm də `~/bin/gasham` ünvanına kopyalanır. Əlavə təminat üçün
`~/.bashrc`, `~/.profile` və `~/.bash_profile`-ə `gasham()` funksiyası da
yazılır — executable heç nədən asılı olmayaraq, hər yeni Termux sessiyasında
`gasham` + Enter DownloaderOG-u başladır. Termux bağlanıb yenidən açılsa da
komanda eyni şəkildə işləyir.

Banner göstərilir, altında **"Link göndərin:"** yazılır — linki yapışdırıb
Enter basın. Sayt linki (məs. video siyahısı olan səhifə) göndərsəniz,
səhifədəki bütün videolar avtomatik aşkarlanıb nömrəli siyahı kimi
göstərilir:

```text
Səhifədə 3 video aşkarlandı — birini seçin:
 1. Video 1
 2. Video 2
 3. Video 3
Seçim (1-3):
```

Seçilən video üçün real keyfiyyətlər və təxmini ölçülər (MB) göstərilir.

## 8. Share sisteminin qurulması

Quraşdırma zamanı skript avtomatik olaraq `~/bin/termux-url-opener` ünvanına
kopyalanır və icra icazəsi verilir — Termux paylaşılan linki avtomatik bu
skriptə ötürür, skript isə URL-i birbaşa DownloaderOG proqramına çatdırır.
Müasir Termux versiyaları üçün `~/.termux/termux-url-opener` da sinxron
saxlanılır. Share inteqrasiyası işləmirsə və ya yeniləmək istəyirsinizsə:

```bash
bash install.sh
```

Qeyd: Termux tamamilə bağlı olduqda, Share menyusunda **Termux** seçildiyi
zaman Termux açılır və linki qəbul edir — bu, Android-in standart Share
mexanizminin ən real və stabil həllidir.

## 9. Faylların harada saxlanıldığı

Bütün yüklənmiş faylların **son yeri**:

```text
/storage/emulated/0/DownloaderOG
```

qovluğudur (Fallback: `~/storage/shared/DownloaderOG`). Qeyd: bu qovluq
`Download` qovluğunun **daxilində deyil**, telefon yaddaşının kök səviyyəsində
(`/storage/emulated/0/DownloaderOG/`) yerləşir. Proses:

1. Yükləmə müvəqqəti qovluqda (`~/.cache/downloaderog`) aparılır
2. Bitdikdə fayl **cut (mv)** ilə əvvəlcə `/storage/emulated/0/Download`-ə
   keçirilir
3. Emal tamamlandıqdan sonra yenidən **cut (mv)** ilə
   `/storage/emulated/0/DownloaderOG` klasörünə köçürülür

Kopya yaradılmır — yalnız move/cut edilir, ona görə ilkin `Download`
qovluğunda ikinci nüsxə qalmaz və müvəqqəti qovluq boşalır. Fayl adları
video/musiqinin orijinal başlığına uyğun olur, məsələn:
`GASHAM - Example Video 2026.mp4`. Eyni adlı fayl varsa `(1)`, `(2)` əlavə
olunur və əvvəlki fayl silinmir.

Yükləndikdən sonra fayl avtomatik olaraq MediaScanner vasitəsilə Android
MediaStore-a qeydiyyata alınır — MP4 **Qalereyada**, MP3 (`.mp3` /
`audio/mpeg`, ID3 metadata ilə) **musiqi pleyerlərində** görünür (yalnız fayl
meneceri deyil). Qeydiyyat tamamlandıqdan sonra yaşıl `[✓]` mesajı göstərilir
və Termux avtomatik bağlanır.

Yükləmə klasörünü dəyişmək üçün `~/.termux/termux-url-opener` faylının
əvvəlindəki `final_dir` və `og_dir` dəyərlərini redaktə edin:

```bash
final_dir='/storage/emulated/0/Download'
og_dir='/storage/emulated/0/DownloaderOG'
```

## 10. Instagram/TikTok üçün cookies

Instagram və TikTok hazırda əksər məzmun üçün **giriş (login)** tələb edir —
buna görə yükləmə "empty media response", "login required" və ya
"anti-bot" xətası verə bilər. Bu tam normaldır və asanlıqla həll olunur:

1. Telefon və ya kompüter brauzerində Instagram/TikTok-a **daxil olun**.
2. Brauzerə **"Get cookies.txt LOCALLY"** genişlənməsini əlavə edin
   (Chrome/Edge/Firefox üçün mövcuddur).
3. tiktok.com / instagram.com səhifəsində genişlənmənin düyməsinə basın →
   **Export** → `cookies.txt` faylı endirilir.
4. Faylı telefona köçürün (məs. `~/storage/downloads/cookies.txt`) və sonra:

```bash
cp ~/storage/downloads/cookies.txt ~/.config/downloaderog/cookies.txt
```

5. Videonu yenidən paylaşın — skript cookies faylını avtomatik istifadə edir.

> ⚠️ `cookies.txt` şəxsi sessiya məlumatınızı ehtiva edir — heç kimlə
> paylaşmayın və hesab təhlükəsizliyi üçün yalnız öz cihazınızda saxlayın.
> Cookies olmadan da TikTok/Instagram-ın çoxu **açıq (public)** videoları
> işləyir; lakin giriş tələb edən məzmun üçün cookies məcburidir.

## 11. Problemlərin həlli

| Problem | Həll |
| --- | --- |
| "No such file or directory" (storage) | `termux-setup-storage` işlədin və icazəni təsdiqləyin |
| Share menyusunda Termux görünmür | Termux-u yeniləyin, sonra `bash install.sh` işlədin |
| Instagram/TikTok: login / empty media / anti-bot xətası | Bölmə 10: cookies.txt yaradın → `~/.config/downloaderog/cookies.txt` |
| TikTok: "Unexpected response" / WAF xətası | `bash install.sh` (curl_cffi quraşdırır) + cookies; Wi-Fi-da yoxdursa mobil internetdə sınayın |
| YouTube: "No supported JavaScript runtime" | `pkg install deno -y` (sonra `bash install.sh`) |
| yt-dlp köhnədir / platforma xətası | `python -m pip install -U yt-dlp` |
| TikTok: "no impersonate target is available" | `bash install.sh` — `curl_cffi` quraşdırır |
| Link dəstəklənmir | Linkin tam və düzgün olduğunu yoxlayın |
| İnternet xətası | Bağlantınızı yoxlayın, bir az sonra yenidən cəhd edin |
| Shorts yüklənmir | Shorts linkinin `shorts` hissəsi olduğunu yoxlayın |
| Şəkil Qalereyada / MP3 pleyerdə görünmür | F-Droid-dən **Termux:API tətbiqini** quraşdırın, sonra `bash install.sh` işlədin |
| Yükləmə bitdi, amma Termux bağlanmır / asılır | Termux:API tətbiqinin quraşdığını yoxlayın; `bash install.sh` yenidən çalışdırın (skript media skanını vaxt limiti ilə idarə edir) |

## 12. Yeniləmə

```bash
cd ~/DownloaderOG
git pull
bash install.sh
```

Skript yeniləndikdə `termux-url-opener` avtomatik yenidən quraşdırılır.

## 13. License

[MIT License](LICENSE) — 2026 Gasham Orujov.

---

Texniki tapşırıq: [docs/TECHNICAL_SPEC.md](docs/TECHNICAL_SPEC.md)
