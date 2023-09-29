def ortakharf(kelime1, kelime2):
    set1 = set(kelime1)
    set2 = set(kelime2)
    ortak = set1.intersection(set2)



    for harf in ortak:
        sayi = min(kelime1.count(harf), kelime2.count(harf))
        print(f"'{harf}, {sayi} kere kullanildi.")


ortakharf("kelimeaaa", "kelime2")

