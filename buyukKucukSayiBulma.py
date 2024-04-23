a = input('a sayısını giriniz :')
b = input('b sayısını giriniz :')
c = input('c sayısını giriniz :')

if a == b != c:
  print('a ve b eşit, c farklı')
  enBuyuk = max(a, b, c)
  enKucuk = min(a, b, c)
  print("En büyük sayı: ", enBuyuk)
  print('En küçük sayı: ', enKucuk)

elif a == c != b:
  print('a ve c eşit, b farklı')
  enBuyuk = max(a, b, c)
  enKucuk = min(a, b, c)
  print("En büyük sayı: ", enBuyuk)
  print('En küçük sayı: ', enKucuk)

elif b == c != a:
  print('b ve c eşit, a farklı')
  enBuyuk = max(a, b, c)
  enKucuk = min(a, b, c)
  print("En büyük sayı: ", enBuyuk)
  print('En küçük sayı: ', enKucuk)

elif a == b == c:
  print('a, b ve c eşittir. Farklı değildir.')

else:
  print('a, b ve c farklı sayılardır.')
  enBuyuk = max(a, b, c)
  enKucuk = min(a, b, c)
  print("En büyük sayı: ", enBuyuk)
  print('En küçük sayı: ', enKucuk)
