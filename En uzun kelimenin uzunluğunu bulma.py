#  2. ÖDEV 1. SORU

A = ("cat", "bird", "dolphin", "giraffe", "elephant", "dog")

en_uzun_kelime = ""
en_uzun_uzunluk = 0

for kelime in A:
    uzunluk = 0
    for harf in kelime:
        uzunluk += 1
    if uzunluk > en_uzun_uzunluk:
        en_uzun_uzunluk = uzunluk
        en_uzun_kelime = kelime

print("En uzun kelime:", en_uzun_kelime)
print("Kelimenin uzunluğu:", en_uzun_uzunluk)
