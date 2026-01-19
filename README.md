# HeadFlow - AI Tabanlı Temassız Mouse Kontrolü

Baş hareketleri ve yüz mimikleri ile bilgisayar kontrolü sağlayan erişilebilirlik yazılımı.

## Proje Amacı

ALS, felç veya ampütasyon gibi nedenlerle ellerini kullanamayan bireylerin sadece kamera ile bilgisayarı kontrol etmesini sağlamak.

## Teknolojiler

- Python 3.9+
- OpenCV - Görüntü işleme ve kamera kontrolü
- MediaPipe - Google'ın yüz tanıma teknolojisi (468 landmark)
- PyAutoGUI - Mouse ve klavye kontrolü
- NumPy - Matematiksel hesaplamalar

## Özellikler (Planlanan)

- [x] Kamera ile görüntü alma
- [ ] Yüz tanıma (468 nokta tespit)
- [ ] Baş hareketi ile mouse kontrolü
- [ ] Titreme önleme algoritması (Exponential Moving Average)
- [ ] Göz kırpma ile sol tıklama
- [ ] Ağız açma ile sağ tıklama
- [ ] Ayarlanabilir hassasiyet
- [ ] Kullanıcı arayüzü

## Kurulum

### Gereksinimler
- Python 3.9 veya üstü
- Webcam
- macOS / Windows / Linux

### Adımlar

1. Repoyu klonla:
```bash
git clone https://github.com/b1rcan/HeadFlow.git
cd HeadFlow
```

2. Virtual environment oluştur:
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
```

3. Gereksinimleri yükle:
```bash
pip install -r requirements.txt
```

4. Çalıştır:
```bash
python main.py
```

## Proje Durumu

Geliştirme Aşaması: Gün 1/7 tamamlandı

- Gün 1: Kurulum ve Altyapı (Tamamlandı)
- Gün 2: MediaPipe Yüz Tanıma (Devam ediyor)
- Gün 3: Mouse Hareketi
- Gün 4: Smoothing Algoritması
- Gün 5: Tıklama Mekanizmaları
- Gün 6: GUI Geliştirme
- Gün 7: Test ve Dokümantasyon

## Demo

Demo videosu yakında eklenecek.

## Katkıda Bulunma

Bu proje öğrenme amaçlı geliştirilmektedir. Önerileriniz için issue açabilirsiniz.

## Lisans

MIT License

## Geliştirici

[1hp]
- GitHub: @b1rcan
- Email: gorur.1.can@gmail.com

## Referanslar

- MediaPipe Face Mesh: https://google.github.io/mediapipe/solutions/face_mesh
- OpenCV Documentation: https://docs.opencv.org/
- PyAutoGUI Documentation: https://pyautogui.readthedocs.io/

Son Güncelleme: Ocak 2025
```

Kaydet.

---

venv/
env/
__pycache__/
*.pyc
.DS_Store
.vscode/
config.json