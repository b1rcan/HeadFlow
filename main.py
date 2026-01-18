"""
HeadFlow - AI Tabanlı Temassız Mouse Kontrolü
Geliştirici: [Senin Adın]
Başlangıç: Ocak 2025
"""

import cv2

print(" HeadFlow - Kamera Testi")
print("=" * 40)

# Kamerayı aç (0 = varsayılan kamera)
cap = cv2.VideoCapture(0)

# Kamera açıldı mı kontrol et
if not cap.isOpened():
    print(" HATA: Kamera açılamadı!")
    print("Çözüm: Başka uygulamalar kamerayı kullanıyor olabilir.")
    exit()

print(" Kamera başarıyla açıldı!")
print(" Pencereyi kapatmak için ESC tuşuna bas")
print()

while True:
    success, frame = cap.read()
    
    if not success:
        print("⚠️ Kamera görüntüsü alınamadı!")
        break
    
    # Ekrana göster
    cv2.imshow("HeadFlow - Kamera Testi", frame)
    
    # ESC tuşu (27) ile çık
    if cv2.waitKey(1) & 0xFF == 27:
        print("\n👋 Program kapatılıyor...")
        break

# Temizlik
cap.release()
cv2.destroyAllWindows()
print(" Kamera kapatıldı. Görüşürüz!")