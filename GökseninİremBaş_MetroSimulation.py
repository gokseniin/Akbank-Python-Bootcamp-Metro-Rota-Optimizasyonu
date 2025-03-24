from collections import defaultdict, deque
import heapq
from typing import Dict, List, Set, Tuple, Optional

print("🚇 Sürücüsüz Metro Simülasyonu \nBu projede, BFS ile en az aktarmalı, A* algoritmasıyla en hızlı rotalar bulunur. \nGeliştirici: Göksenin İrem Baş | Mart 2025 | Akbank x GAIH Bootcamp")

class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx
        self.ad = ad
        self.hat = hat
        self.komsular: List[Tuple['Istasyon', int]] = []  # (istasyon, süre) tuple'ları

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        self.komsular.append((istasyon, sure))

class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        if id not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)

    def istasyonlari_goster(self): #İstasyonları listeler
            print("\n Mevcut İstasyonlar:")
            for istasyon in self.istasyonlar.values():
                print(f"{istasyon.idx}: {istasyon.ad} ({istasyon.hat})")
    
    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar: #Başlangıç ve hedef istasyonlarının geçerli olup olmadığı kontrol edilir
            print("Hata: Geçersiz istasyon kodu girdiniz! En az aktarmalı rota bulunamadı.")
            return None
        
        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        ziyaret_edildi = {baslangic}     
        kuyruk = deque([(baslangic, [baslangic])]) #Kuyruk oluşturulur
        # Kuyruk boşalana kadar döngü devam eder
        while kuyruk:
            istasyon, rota = kuyruk.popleft() #Kuyruktan eleman çıkarılır ve rota güncellenir
            # Hedef istasyona ulaşıldığında rota döndürülür
            if istasyon == hedef:
                return rota
            # İstasyonun komşuları ziyaret edilmediyse kuyruğa eklenir
            for komsu, _ in istasyon.komsular:
                if komsu not in ziyaret_edildi:
                    ziyaret_edildi.add(komsu)
                    kuyruk.append((komsu, rota + [komsu]))
        print("Uyarı: İki istasyon arasında geçerli bir rota bulunamadı.") #Rota bulunamazsa uyarı mesajı verilir
        return None

    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar: #Başlangıç ve hedef istasyonlarının geçerli olup olmadığı kontrol edilir
            print("Hata: Geçersiz istasyon kodu girdiniz! En hızlı rota bulunamadı.")
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        ziyaret_edildi = set() #Ziyaret edilen istasyonlar set olarak tutulur
        pq = [(0, id(baslangic), baslangic, [baslangic])] #Öncelik kuyruğu oluşturulur
        # Öncelik kuyruğu boşalana kadar döngü devam eder
        while pq:
            sure, _, istasyon, rota = heapq.heappop(pq) #Öncelik kuyruğundan en küçük süreli eleman çıkarılır ve rota güncellenir
            # Hedef istasyona ulaşıldığında rota ve süre döndürülür
            if istasyon == hedef:
                return rota, sure
            # İstasyonun komşuları ziyaret edilmediyse öncelik kuyruğuna eklenir
            if id(istasyon) in ziyaret_edildi:
                continue
            ziyaret_edildi.add(id(istasyon))
            for komsu, komsu_sure in istasyon.komsular:
                if id(komsu) not in ziyaret_edildi: 
                    heapq.heappush(pq, (sure + komsu_sure, id(komsu), komsu, rota + [komsu])) 
        print("Uyarı: İki istasyon arasında geçerli bir rota bulunamadı.") #Rota bulunamazsa uyarı mesajı verilir
        return None

# Örnek Kullanım
if __name__ == "__main__":
    metro = MetroAgi()
    
    # İstasyonlar ekleme
    # Kırmızı Hat
    metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
    metro.istasyon_ekle("K2", "Ulus", "Kırmızı Hat")
    metro.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat")
    metro.istasyon_ekle("K4", "OSB", "Kırmızı Hat")
    
    # Mavi Hat
    metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat")
    metro.istasyon_ekle("M2", "Kızılay", "Mavi Hat")  # Aktarma noktası
    metro.istasyon_ekle("M3", "Sıhhiye", "Mavi Hat")
    metro.istasyon_ekle("M4", "Gar", "Mavi Hat")
    
    # Turuncu Hat
    metro.istasyon_ekle("T1", "Batıkent", "Turuncu Hat")
    metro.istasyon_ekle("T2", "Demetevler", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T3", "Gar", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T4", "Keçiören", "Turuncu Hat")
    
    # Bağlantılar ekleme
    # Kırmızı Hat bağlantıları
    metro.baglanti_ekle("K1", "K2", 4)  # Kızılay -> Ulus
    metro.baglanti_ekle("K2", "K3", 6)  # Ulus -> Demetevler
    metro.baglanti_ekle("K3", "K4", 8)  # Demetevler -> OSB
    
    # Mavi Hat bağlantıları
    metro.baglanti_ekle("M1", "M2", 5)  # AŞTİ -> Kızılay
    metro.baglanti_ekle("M2", "M3", 3)  # Kızılay -> Sıhhiye
    metro.baglanti_ekle("M3", "M4", 4)  # Sıhhiye -> Gar
    
    # Turuncu Hat bağlantıları
    metro.baglanti_ekle("T1", "T2", 7)  # Batıkent -> Demetevler
    metro.baglanti_ekle("T2", "T3", 9)  # Demetevler -> Gar
    metro.baglanti_ekle("T3", "T4", 5)  # Gar -> Keçiören
    
    # Hat aktarma bağlantıları (aynı istasyon farklı hatlar)
    metro.baglanti_ekle("K1", "M2", 2)  # Kızılay aktarma
    metro.baglanti_ekle("K3", "T2", 3)  # Demetevler aktarma
    metro.baglanti_ekle("M4", "T3", 2)  # Gar aktarma

    metro.istasyonlari_goster() #Kullanıcı için duraklar kodlarıyla birlikte listelenir
    #Kullanıcıdan başlangıç ve hedef durak kodları alınır
    baslangic_id = input("Lütfen başlangıç durağının kodunu girin: ")
    hedef_id = input("Lütfen hedef durağının kodunu girin: ")
    
    rota = metro.en_az_aktarma_bul(baslangic_id, hedef_id) #En az aktarmalı rota
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota)) #Rota ekrana yazdırılır

    sonuc = metro.en_hizli_rota_bul(baslangic_id, hedef_id) #En hızlı rota
    if sonuc:
        rota, sure = sonuc 
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota)) #Rota ve süre ekrana yazdırılır