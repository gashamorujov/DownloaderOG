GASHAM DownloaderOG — GitHub / Termux layihəsi üçün texniki tapşırıq

Mən GitHub üzərində DownloaderOG adlı, Android Termux mühitində işləyən universal media yükləyici layihəsi hazırlamaq istəyirəm.

Layihənin əsas məqsədi istifadəçinin YouTube, TikTok, Instagram və digər dəstəklənən video/audio platformalarından paylaşdığı link vasitəsilə video və ya musiqini yükləyə bilməsidir.

1. Əsas iş prinsipi

Layihə Termux üçün hazırlanmalıdır.

İlk dəfə GitHub-dan layihə Termux-a qurulduqda bütün lazımi komponentlər, paketlər və asılılıqlar avtomatik quraşdırılmalıdır.

İlkin quraşdırmadan sonra istifadəçi hər dəfə ayrıca konfiqurasiya etməməlidir.

Layihə mümkün qədər tək əmrlə başladılan və istifadəsi sadə olmalıdır.

Əsas məqsəd:

1. Termux-da layihəni bir dəfə qurmaq.
2. Lazımi dependency-lərin avtomatik quraşdırılması.
3. Layihənin Termux-da işləməyə hazır vəziyyətə gəlməsi.
4. İstifadəçi video linkini Termux-a paylaşdıqda DownloaderOG avtomatik işə düşməli və linki qəbul etməlidir.

Əgər Android/Termux məhdudiyyətlərinə görə Termux prosesi tam bağlandıqda sistem səviyyəsində avtomatik link qəbul etmək mümkün deyilsə, bunu nəzərə al və Termux:API, Android Share Intent və ya uyğun başqa üsul ilə ən real və stabil həlli qur. İstifadəçidən mümkün qədər az manual əməliyyat tələb olunmalıdır.

---

2. Link qəbul etmə

İstifadəçi YouTube, TikTok, Instagram və digər dəstəklənən platformadan videonun linkini paylaşdıqda proqram həmin URL-ni avtomatik qəbul etməlidir.

URL qəbul edildikdən sonra əvvəlcə link analiz edilməli və videonun:

- başlığı
- müddəti
- mövcud formatları
- mövcud video keyfiyyətləri
- təxmini fayl ölçüləri

müəyyən edilməlidir.

Əgər platforma dəstəklənmirsə, istifadəçiyə səliqəli xəta mesajı göstərilməlidir.

---

3. Terminal interfeysi

Terminal interfeysi kreativ və professional görünməlidir.

Proqram başladıqda böyük və diqqətçəkən şəkildə:

GASHAM

başlığı göstərilsin.

Başlıqda terminal ANSI rənglərindən istifadə edilsin və mümkün olduğu halda mavi, qırmızı və yaşıl rənglər növbəli şəkildə yanıb-sönən/animasiyalı effekt yaratsın.

Məsələn:

GASHAM

başlığının altında layihənin adı və ya qısa məlumat göstərilə bilər.

İnterfeys mümkün qədər səliqəli, minimal və professional olsun.

---

4. MP4 bölməsi

Link analiz edildikdən sonra əvvəlcə MP4 bölməsi göstərilməlidir.

Məsələn:

MP4

1. 144p — 3 MB
2. 240p — 5 MB
3. 360p — 10 MB
4. 480p — 18 MB
5. 720p — 35 MB
6. 1080p — 70 MB

Bu sadəcə nümunədir.

Əsl siyahı həmin videonun platformada real olaraq dəstəklədiyi keyfiyyətlərə əsasən avtomatik yaradılmalıdır.

Yalnız mövcud formatlar göstərilməlidir.

Əgər 144p yoxdursa, 144p göstərilməməlidir.

Əgər 2160p/4K mövcuddursa, o da siyahıya əlavə edilməlidir.

Sistem videonun mövcud olan ən yüksək keyfiyyətinə qədər bütün uyğun seçimləri göstərməlidir.

Fayl ölçüsü mümkün qədər dəqiq hesablanmalı və MB/GB formatında göstərilməlidir.

---

5. MP3 bölməsi

MP4 siyahısı bitdikdən sonra MP3 bölməsi göstərilməlidir.

MP3 seçimləri də nömrələnməlidir.

Çox vacib:

MP3 nömrələnməsi MP4 siyahısının davamı olmalıdır.

Məsələn MP4 1–8 arasındadırsa:

MP3

9. MP3 — 128 kbps — 4 MB
10. MP3 — 192 kbps — 6 MB
11. MP3 — 256 kbps — 8 MB
12. MP3 — 320 kbps — 10 MB

MP4 1–6-dırsa, MP3 7-dən başlamalıdır.

Bu nömrələmə avtomatik hesablanmalıdır.

MP3 üçün mövcud audio keyfiyyətləri/bitrate-lər göstərilməlidir:

- 64 kbps
- 96 kbps
- 128 kbps
- 160 kbps
- 192 kbps
- 256 kbps
- 320 kbps

Lakin yalnız həmin media üçün real olaraq mövcud və ya texniki olaraq yaradıla bilən uyğun seçimlər göstərilməlidir.

---

6. Seçim sistemi

İstifadəçi yalnız seçim nömrəsini yazaraq formatı seçməlidir.

Məsələn:

"Seçiminizi daxil edin: 5"

İstifadəçi 5 yazdıqda sistem dərhal həmin formatın yüklənməsinə başlamalıdır.

Əlavə menyular və lazımsız suallar mümkün qədər azaldılmalıdır.

İstifadəçi yanlış nömrə daxil edərsə:

- xəta göstərilsin;
- düzgün seçim diapazonu bildirilsin;
- proqram bağlanmasın;
- istifadəçiyə yenidən seçim etmək imkanı verilsin.

---

7. Yükləmə prosesi

Seçim edildikdən sonra yükləmə mümkün qədər sürətli və stabil şəkildə başlamalıdır.

Terminalda yükləmə progress bar göstərilsin.

Məsələn:

"Downloading ███████████████░░░ 78%"

və mümkün olduqda:

- faiz
- yüklənən ölçü
- ümumi ölçü
- sürət
- qalan vaxt

göstərilsin.

Yükləmə zamanı terminal interfeysi mümkün qədər səliqəli qalmalıdır.

---

8. Faylların saxlanılması

Bütün yüklənmiş fayllar Android cihazında:

DownloaderOG

adlı qovluqda saxlanılmalıdır.

Mümkün olduqda bu qovluq:

"/storage/emulated/0/DownloaderOG"

yolunda yaradılmalıdır.

Əgər Termux storage icazəsi verilməyibsə, proqram istifadəçiyə bunu aşkar şəkildə bildirməli və storage permission üçün lazım olan əmri göstərməlidir.

MP4 və MP3 faylları həmin qovluqda saxlanılmalıdır.

Fayl adları mümkün qədər orijinal video/musiqi adına uyğun olmalıdır.

Fayl adlarında Android/Linux üçün problem yarada biləcək simvollar avtomatik təmizlənməlidir.

---

9. Yükləmə tamamlandıqdan sonra

Yükləmə uğurla tamamlandıqda terminalda məsələn:

"Download completed successfully!"

və faylın saxlanıldığı yol göstərilsin.

Məsələn:

"Saved to: /storage/emulated/0/DownloaderOG/Video Name.mp4"

Bundan sonra proqram avtomatik şəkildə Termux prosesindən çıxmalıdır.

Yəni yükləmə tamamlandıqdan sonra istifadəçidən əlavə "Enter" və ya başqa komanda tələb edilməməlidir.

Əgər Android/Termux mühiti tam proqram pəncərəsinin bağlanmasına icazə vermirsə, mümkün olan ən yaxın avtomatik çıxış mexanizmi tətbiq edilməlidir.

---

10. Platforma dəstəyi

Layihə mümkün qədər geniş platforma dəstəyi ilə hazırlanmalıdır.

Əsas platformalar:

- YouTube
- TikTok
- Instagram
- Facebook
- X/Twitter
- Reddit
- Vimeo
- Dailymotion
- və media yükləmə kitabxanası tərəfindən dəstəklənən digər platformalar.

Platforma siyahısını kodda əl ilə məhdudlaşdırmaq əvəzinə, mümkün olduğu halda yt-dlp və onun extractor sistemindən istifadə et ki, gələcəkdə platformaların dəstəyi avtomatik yenilənə bilsin.

Layihə yalnız qanuni olaraq istifadəçinin yükləməyə icazəsi olan və ya müəllif hüquqları pozulmayan məzmun üçün nəzərdə tutulmalıdır.

---

11. Texniki struktur

Layihəni GitHub üçün professional repository formasında hazırla.

Mümkün struktur:

DownloaderOG/
├── downloaderog/
├── scripts/
├── config/
├── assets/
├── requirements.txt
├── install.sh
├── downloaderog.sh
├── README.md
└── LICENSE

Lazım olarsa strukturu daha yaxşı şəkildə dəyişə bilərsən.

Əsas proqramın Python ilə hazırlanması məqsədəuyğundur.

Media məlumatlarının əldə edilməsi və yükləmə üçün stabil və aktual kitabxanalardan istifadə et.

FFmpeg lazım olduğu halda avtomatik quraşdırılmalıdır.

---

12. Avtomatik quraşdırma

Ən vacib tələblərdən biri budur:

İstifadəçi GitHub repository-ni Termux-a gətirdikdən sonra bir dəfə quraşdırma əmri işlətməlidir.

Quraşdırıcı avtomatik olaraq:

- Termux paketlərini yoxlamalı;
- Python-u yoxlamalı/quraşdırmalı;
- FFmpeg-i yoxlamalı/quraşdırmalı;
- lazımi Python dependency-lərini quraşdırmalı;
- storage icazəsini yoxlamalı;
- DownloaderOG qovluğunu yaratmalı;
- bütün lazımi faylları konfiqurasiya etməli;
- proqramı istifadəyə hazır vəziyyətə gətirməlidir.

İkinci dəfə istifadəçi bütün bunları yenidən etməməlidir.

---

13. Share/Link inteqrasiyası

Ən vacib istifadə ssenarisi:

İstifadəçi telefonda YouTube/TikTok/Instagram-da videonu açır.

Share → DownloaderOG / Termux

seçir.

Link avtomatik olaraq DownloaderOG proqramına ötürülür.

Proqram linki qəbul edir və seçim menyusunu avtomatik göstərir.

Əgər Android-in standart Share menyusunda ayrıca "DownloaderOG" tətbiqi kimi görünmək texniki olaraq mümkün deyilsə, Termux üçün real işləyən alternativ qur:

- Termux:API
- Android Intent
- uyğun ".desktop"/launcher mexanizmi
- və ya başqa etibarlı üsul.

Əsas məqsəd istifadəçinin linki əl ilə kopyalayıb yapışdırmaq məcburiyyətini minimuma endirməkdir.

---

14. Təhlükəsizlik və stabillik

Proqram:

- istifadəçi tərəfindən verilən URL-ni yoxlamalı;
- zərərli shell injection hallarının qarşısını almalı;
- fayl adlarını təhlükəsiz şəkildə emal etməli;
- şəbəkə xətalarını idarə etməli;
- yükləmə yarımçıq qaldıqda düzgün xəta göstərməli;
- platforma tərəfindən format tapılmadıqda düzgün mesaj verməli;
- dependency problemi olduqda izah etməlidir.

Proqram qəfil bağlanmamalıdır.

---

15. README

GitHub repository-də Azərbaycan dilində aydın README.md hazırla.

README-də:

1. Layihə haqqında
2. Əsas xüsusiyyətlər
3. Dəstəklənən platformalar
4. Termux quraşdırılması
5. İlk quraşdırma əmri
6. Storage icazəsinin verilməsi
7. İstifadə qaydası
8. Share sisteminin qurulması
9. Faylların harada saxlanıldığı
10. Problemlərin həlli
11. Yeniləmə
12. License

bölmələri olsun.

---

16. Vacib tələb

Mənə yalnız konsept və ya pseudocode vermə.

Tam işlək GitHub layihəsi hazırla.

Bütün lazımi faylların kodunu tam şəkildə təqdim et.

Kodda "TODO", "your_code_here", "example_function()" kimi yarımçıq hissələr saxlamamağa çalış.

Əgər hansısa funksiya Termux və ya Android məhdudiyyətinə görə tam avtomatik həyata keçirilə bilmirsə, bunu README-də izah et və mümkün olan ən yaxşı alternativi kodla tətbiq et.

Layihə real Android Termux mühitində sınaqdan keçirilə biləcək şəkildə hazırlanmalıdır.

Əsas prioritetlər:

Sadə istifadə → sürətli yükləmə → stabil işləmə → professional terminal görünüşü → avtomatik quraşdırma → Android Share inteqrasiyası.

Layihənin adı:

DownloaderOG

Terminal başlığı:

GASHAM



17. Fayl adının qorunması

Yüklənən MP4 və MP3 faylları videonun/musiqinin orijinal adına uyğun adlandırılmalıdır.

Məsələn, YouTube-da videonun adı:

"GASHAM - Example Video 2026"

olarsa:

- MP4 → "GASHAM - Example Video 2026.mp4"
- MP3 → "GASHAM - Example Video 2026.mp3"

Fayl adı avtomatik olaraq media mənbəyindən götürülməlidir.

Vacib: Faylın adı dəyişdirilməməli, "video.mp4", "download.mp4", "audio.mp3" və ya başqa ümumi adlardan istifadə edilməməlidir.

Lakin Android/Linux fayl sistemində problem yarada biləcək simvollar varsa, yalnız həmin simvollar təhlükəsiz şəkildə dəyişdirilə və ya silinə bilər. Fayl adının əsas hissəsi və orijinal adı maksimum dərəcədə qorunmalıdır.

Əgər eyni adlı fayl artıq "DownloaderOG" qovluğunda mövcuddursa, əvvəlki faylın üzərinə təsadüfən yazılmamalıdır. Lazım gəldikdə avtomatik olaraq:

"GASHAM - Example Video 2026 (1).mp4"

"GASHAM - Example Video 2026 (2).mp4"

formatında yeni ad yaradılmalıdır.


