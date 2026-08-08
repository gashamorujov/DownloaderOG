# GASHAM DownloaderOG

Termux üçün universal media yükləyici. YouTube, TikTok, Instagram, Facebook,
X/Twitter, Reddit, Vimeo, Dailymotion və daha yüzlərlə platformadan link
vasitəsilə video (MP4) və musiqi (MP3) yükləyin — hamısı bir əmrlə, bir dəfəlik
quruluşla.

---

## 1. Layihə haqqında

DownloaderOG yt-dlp yükləmə mühərriki üzərində qurulmuş Python proqramıdır.
Android Termux mühitində işləyir və aşağıdakıları təmin edir:

- Telefondan **Share → Termux** ilə linkin avtomatik qəbulu
- Orijinal başlıqla avtomatik fayl adlandırılması
- Real format/keyfiyyət siyahısı və təxmini fayl ölçüləri
- Progress bar ilə canlı yükləmə göstəricisi
- `GASHAM` animasiyalı terminal başlığı
- Bir dəfəlik avtomatik quraşdırma (dependencies, storage, share)

## 2. Əsas xüsusiyyətlər

- MP4 bölməsi: yalnız mövcud keyfiyyətlər (144p → 4K), ölçü ilə
- MP3 bölməsi: MP4-ün davamı olan avtomatik nömrələmə (64–320 kbps)
- Yalnız seçim nömrəsini yazaraq yükləmə
- Yanlış seçimdə xəta mesajı və yenidən seçim imkanı
- Yükləmə: faiz, yüklənən/ümumi ölçü, sürət, qalan vaxt
- Fayl adı orijinal media başlığından götürülür, eyni ad olduqda `(1)`, `(2)` əlavə olunur
- Yükləmə bitdikdən sonra avtomatik çıxış (əlavə Enter tələb olunmur)
- Təhlükəsiz URL və fayl adı emalı, shell injection-dən qorunma

## 3. Dəstəklənən platformalar

yt-dlp mühərriki sayəsində yüzlərlə platforma avtomatik dəstəklənir:

- YouTube
- TikTok
- Instagram
- Facebook
- X/Twitter
- Reddit
- Vimeo
- Dailymotion
- və yt-dlp extractor sisteminin dəstəklədiyi digər platformalar

Platforma siyahısı əl ilə məhdudlaşdırılmır — yt-dlp yeniləndikcə yeni
platformalar avtomatik əlavə olunur.

> ⚖️ Proqram yalnız qanuni olaraq yükləməyə icazəniz olan və ya müəllif
> hüquqlarını pozmayan məzmun üçün nəzərdə tutulub.

## 4. Termux quraşdırılması

1. Termux-u quraşdırın ([F-Droid](https://f-droid.org/) və ya rəsmi kanaldan).
2. Termux-u açın və ilkin paketlər yenilənsin (ilk açılışda `pkg update` avtomatik təklif olunur).
3. Storage icazəsi verin:

```bash
termux-setup-storage
```

4. Layihəni klonlayın:

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

- Termux paketlərini yoxlayır/yeniləyir
- `python`, `ffmpeg`, `git`, `termux-api` paketlərini quraşdırır
- Python dependency-lərini (yt-dlp) quraşdırır
- Storage icazəsini yoxlayır və `DownloaderOG` qovluğunu yaradır
- `downloaderog` və `gasham` əmrlərini qeydiyyata alır
- `termux-url-opener` vasitəsilə Android Share inteqrasiyasını qurur
- Konfiqurasiya faylını hazırlayır

İkinci dəfə quraşdırma tələb olunmur — proqram hazırdır.

## 6. Storage icazəsinin verilməsi

Termux-da bir dəfə icazə verin:

```bash
termux-setup-storage
```

Android-də açılan pəncərədə **Allow / İcazə ver** düyməsini basın. İcazə
verilməyibsə, proqram bunu aşkar göstərir və eyni əmri təklif edir.

## 7. İstifadə qaydası

```bash
downloaderog
```

Proqram linki soruşacaq. Linki yapışdırın və Enter basın. Siyahıdan MP4 və ya
MP3 seçiminin nömrəsini yazın:

```text
MP4
  1. 144p — 3 MB
  2. 360p — 10 MB
  3. 1080p — 70 MB

MP3
  4. MP3 — 128 kbps — 4 MB
  5. MP3 — 320 kbps — 10 MB

Seçiminizi daxil edin:
```

Link birbaşa da verilə bilər:

```bash
downloaderog --url "https://www.youtube.com/watch?v=..."
```

`gasham` əmri də eyni proqramı işə salır.

## 8. Share sisteminin qurulması

Quraşdırma zamanı `termux-url-opener` faylı avtomatik qurulur. İstifadə:

1. Telefonda YouTube/TikTok/Instagram-da videonu açın
2. **Share (Paylaş)** düyməsini basın
3. Menyudan **Termux** seçin
4. DownloaderOG avtomatik işə düşür və seçim menyusunu göstərir

Qeyd: Termux tamamilə bağlı olduqda Android sistem səviyyəsində avtomatik link
qəbulu bütün cihazlarda mümkün olmur. Bunun üçün Share menyusunda Termux seçin
— Termux yalnız bu zaman açılır və linki qəbul edir. Paylaşılan link həmişə
`termux-url-opener` vasitəsilə proqrama ötürülür.

Share inteqrasiyasını yenidən qurmaq üçün:

```bash
bash scripts/setup-share.sh
```

Əlavə rahatlıq üçün Termux:Widget quraşdırıb ana ekrana `downloaderog`
qısayolu əlavə edə bilərsiniz (`~/.shortcuts/downloaderog.sh` avtomatik yaradılır).

## 9. Faylların harada saxlanıldığı

Bütün yüklənmiş fayllar:

```text
/storage/emulated/0/DownloaderOG
```

qovluğunda saxlanılır (Fallback: `~/storage/shared/DownloaderOG` və ya
`~/DownloaderOG`). Fayl adları video/musiqinin orijinal başlığına uyğun olur və
Android/Linux üçün təhlükəli simvollar avtomatik təmizlənir. Eyni adlı fayl
mövcuddursa, `(1)`, `(2)` şəkilçisi əlavə olunur — heç bir fayl silinmir.

Yükləmə qovluğunu dəyişmək üçün `~/.config/downloaderog/config.json` faylında
`download_dir` dəyərini redaktə edin (məsələn: `"/storage/emulated/0/Music"`).

## 10. Problemlərin həlli

| Problem | Həll |
| --- | --- |
| Storage icazəsi yoxdur | `termux-setup-storage` işlədin və icazəni təsdiqləyin |
| "Link dəstəklənmir" | Linkin tam və düzgün olduğunu yoxlayın, başqa video sınayın |
| "Video əldə edilə bilmədi" | İnternet bağlantısını yoxlayın, bir az sonra yenidən cəhd edin |
| Privat video | Yükləməyə icazəniz olan ictimai video seçin |
| Yükləmə yarımçıq qaldı | Proqram davam etdirməni dəstəkləyir — eyni seçimlə yenidən cəhd edin |
| MP3 çevrilmə xətası | `pkg install -y ffmpeg` ilə FFmpeg-in qurulu olduğunu yoxlayın |
| Paylaş menyusunda Termux görünmür | Termux-u yeniləyin və ya `bash scripts/setup-share.sh` işlədin |

## 11. Yeniləmə

```bash
cd ~/DownloaderOG
git pull
bash install.sh
```

`bash install.sh` yenidən işlədildikdə kod, dependency-lər və inteqrasiya
avtomatik yenilənir.

## 12. License

[MIT License](LICENSE) — 2026 Gasham Orujov.

---

Texniki tapşırıq: [docs/TECHNICAL_SPEC.md](docs/TECHNICAL_SPEC.md)
