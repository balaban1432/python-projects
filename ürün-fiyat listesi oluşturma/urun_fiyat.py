# 4. kullanıcıdan alacağınız sınırsız ürün bilgisini ürünler listesinde saklayınız.  ** ürün sayısını kullanıcıya sorun ** dictionary yapısı (name , price) şeklinde olsun **ürün ekleme işlemi bittiğinde ürünleri ekranda for ile listeleyin.


urunler = []

adet = int(input("kaç ürün eklemek istiyorsunuz?  "))
i = 0

while i < adet:
    name = input("ürün ismi: ")
    price = input("ürün fiyatı: ")
    urunler.append({
        "name" : name,
        "price" : price
    })
    i += 1

for i in urunler:
    print(f'ürün adı: {i["name"]} , ürün fiyatı: {i["price"]}')
