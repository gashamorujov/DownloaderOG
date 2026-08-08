# GASHAM-MASDİ DownloaderOG

Termux üçün universal media yükləyici — Termux-YTD2.0 işləmə məntiqi ilə.
YouTube, TikTok, Instagram, Facebook, X/Twitter, Reddit, Vimeo, Dailymotion və
yt-dlp-nin dəstəklədiyi yüzlərlə platformadan video və musiqi yükləyin —
yalnız **2 kliklə**: *Share → Termux → keyfiyyət seçimi*.

---

## 1. Layihə haqqında

GASHAM-MASDİ DownloaderOG yüngül və sürətli bir Termux alətidir. Telefonda videonu
açıb **Paylaş (Share)** düyməsinə basdıqdan sonra **Termux** seçirsiniz və
ekranda açılan menyudan keyfiyyəti qeyd edirsiniz — video/musiqi avtomatik
yüklənir. YouTube **Shorts** paylaşdıqda isə menyu göstərilmədən birbaşa
avtomatik yüklənir.

Yükləmə mühərriki olaraq **yt-dlp** istifadə olunur — ona görə yüzlərlə
platformanın dəstəyi avtomatik yenilənir və yükləmə sürəti maksimumdur.

## 2. Əsas xüsusiyyətlər

- Share → Termux ilə avtomatik link qəbulu
- YouTube Shorts üçün bir kliklə avtomatik yükləmə
- Keyfiyyət seçimi: **Music MP3**, **360p**, **480p**, **720p**, **1080p**, **2160p**
- Canlı yükləmə prosesi (yt-dlp progress bar)
- Orijinal video başlığı ilə fayl adlandırma (`%(title)s.%(ext)s`)
- Yükləmə temp qovluqda aparılır, bitdikdə **cut (mv)** ilə birbaşa
  `/storage/emulated/0/DownloaderOG` klasörünə keçirilir — əlavə yer tutmur
- `GASHAM-MASDİ` başlığı ilə professional terminal interfeysi
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
- `python` quraşdırır
- `yt-dlp` quraşdırır/yeniləyir
- `/storage/emulated/0/DownloaderOG` qovluğunu yaradır
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
3. Ekranda `GASHAM-MASDİ DownloaderOG` menyusu açılır
4. İstədiyiniz seçimin nömrəsini yazın və Enter basın

```text
╠═▶ 1. Music MP3♫
╠═▶ 2. Video 360p
╠═▶ 3. Video 480p
╠═▶ 4. Video 720p
╠═▶ 5. Video 1080p
╠═▶ 6. Video 2160p
╠═▶ 7. Exit DownloaderOG
╠═▶ A. About
╚═:➤
```

`A` yazdıqda məlumat (About) göstərilir və yenidən seçim menyusuna qayıdılır.

Əl ilə test üçün link skriptə birbaşa da verilə bilər:

```bash
bash ~/bin/termux-url-opener "https://www.youtube.com/watch?v=..."
bash ~/.termux/termux-url-opener "https://www.youtube.com/watch?v=..."
```

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

Bütün yüklənmiş fayllar:

```text
/storage/emulated/0/DownloaderOG
```

qovluğunda saxlanılır (Fallback: `~/storage/shared/DownloaderOG`). Fayl adları
video/musiqinin orijinal başlığına uyğun olur, məsələn:
`GASHAM-MASDİ - Example Video 2026.mp4`.

Yükləmə əvvəlcə müvəqqəti qovluqda (`~/.cache/downloaderog`) aparılır;
yükləmə tamamlandıqda fayl **cut (mv)** əmri ilə hədəf klasörə keçirilir və
müvəqqəti qovluq boşalır — cihaz yaddaşında əlavə yer tutmur.

Yükləmə klasörünü dəyişmək üçün `~/.termux/termux-url-opener` faylının
əvvəlindəki `final_dir` dəyərini redaktə edin:

```bash
final_dir='/storage/emulated/0/Music'
```

## 10. Problemlərin həlli

| Problem | Həll |
| --- | --- |
| "No such file or directory" (storage) | `termux-setup-storage` işlədin və icazəni təsdiqləyin |
| Share menyusunda Termux görünmür | Termux-u yeniləyin, sonra `bash install.sh` işlədin |
| yt-dlp köhnədir / platforma xətası | `python -m pip install -U yt-dlp` |
| Link dəstəklənmir | Linkin tam və düzgün olduğunu yoxlayın |
| İnternet xətası | Bağlantınızı yoxlayın, bir az sonra yenidən cəhd edin |
| Shorts yüklənmir | Shorts linkinin `shorts` hissəsi olduğunu yoxlayın |

## 11. Yeniləmə

```bash
cd ~/DownloaderOG
git pull
bash install.sh
```

Skript yeniləndikdə `termux-url-opener` avtomatik yenidən quraşdırılır.

## 12. License

[MIT License](LICENSE) — 2026 Gasham Orujov.

---

Texniki tapşırıq: [docs/TECHNICAL_SPEC.md](docs/TECHNICAL_SPEC.md)
