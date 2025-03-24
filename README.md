# 🚇 Metro Rota Optimizasyonu Projesi

Bu proje, sürücüsüz metro sistemlerinde **en az aktarmalı** ve **en hızlı** rotayı bulmak amacıyla geliştirilmiştir.  
**BFS** (Breadth-First Search) ve **A\*** (A-Star) algoritmaları kullanılarak metro ağı üzerinde rota optimizasyonu sağlanmıştır.

---

## 📌 Proje Amacı

Bu projede:

- Metro istasyonlarını bir **graf veri yapısı** şeklinde modellemek,
- **Genişlik Öncelikli Arama (BFS)** algoritması ile en az aktarmalı rotayı bulmak,
- **A\*** algoritması ile en kısa sürede hedefe ulaşan rotayı bulmak amaçlanmıştır.

---

## 🧠 Kullanılan Algoritmalar

### 🔹 BFS (Breadth-First Search)
- Bir istasyondan diğerine **en az sayıda aktarma** ile gidilen rotayı bulmak için kullanılmıştır.
- **Kuyruk (deque)** ve **ziyaret kontrolü (set)** ile uygulanmıştır.

### 🔹 A\* (A-Star) Algoritması
- İstasyonlar arası **süreyi dikkate alarak** en hızlı rotayı bulmak için kullanılmıştır.
- **Heap queue (heapq)** ile öncelik kuyruğu oluşturularak uygulanmıştır.

---

## 🧰 Kullanılan Teknolojiler ve Kütüphaneler

- **Python 3**: Proje dili.
- **collections.deque**: BFS algoritmasındaki kuyruk yapısı için kullanıldı.
- **collections.defaultdict**: Metro hatlarını gruplayarak istasyonları saklamak için kullanıldı (örneğin: aynı hatta bağlı istasyonları listelemek).
- **heapq**: A* algoritmasında öncelik sırası olan istasyonları verimli şekilde işlemek için kullanıldı.
- **typing**: Tip ipuçları (type hints) kullanarak kodun okunabilirliği ve bakımı artırıldı. (`List`, `Dict`, `Tuple`, `Optional`, `Set` vs.)

---

## 🔍 Örnek Kullanım ve Test Sonuçları

```python
metro.en_az_aktarma_bul("M1", "K4")
# Çıktı: AŞTİ -> Kızılay -> Ulus -> Demetevler -> OSB

metro.en_hizli_rota_bul("M1", "K4")
# Çıktı: AŞTİ -> Kızılay -> Ulus -> Demetevler -> OSB (15 dakika)
```
---

## 💡 Projeyi Geliştirme Fikirleri

- 🚉 **Grafiksel arayüz (GUI)** eklenerek kullanıcıların durakları görsel olarak seçmesi sağlanabilir.
- 📍 **Harita veya ağ görselleştirmesi** eklenebilir.
- 🧭 **Yoğunluk, trafik durumu** gibi faktörler eklenerek daha gerçekçi rota seçimi yapılabilir.
- 🗺️ İstasyon verileri dışarıdan (JSON/CSV/Veritabanı) okunabilir hale getirilebilir.

---

## 👨‍💻 Geliştirici

**Göksenin İrem Baş**  
Akbank & Global AI Hub  
Python ve Yapay Zekaya Giriş Bootcamp – Mart 2025

