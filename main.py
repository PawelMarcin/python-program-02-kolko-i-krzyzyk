# Kolko i krzyzyk:
# Zalozenia.
#     - Komputer rozpoczyna gre - symbol: X
#     - Uzytkownik - symbol: O
#     - Komputer nie moze przegrac
#     - Identyfikatory pol:
#             1 2 3
#             4 5 6
#             7 8 9
#     - Koniec gry:
#         -- wygrana komputera: wyswietlony napis Przegrana
#         -- wszystkie pola zapelnione: wyswietlony napis Remis
# Zmienne do wyswietlania plaszy:
#   p1, p2, p3, p4, p5, p6, p7, p8, p9 - wartosci: 'O', 'X', '-'
# Analiza plaszy:
#   linia l1 - pola: 1, 2, 3
#   linia l2 - pola: 4, 5, 6
#   linia l3 - pola: 7, 8, 9
#   linia l4 - pola: 1, 4, 7
#   linia l5 - pola: 2, 5, 8
#   linia l6 - pola: 3, 6, 9
#   linia l7 - pola: 1, 5, 9
#   linia l8 - pola: 3, 5, 7
# Wartosci linii:
#       10 - pusta linia
#        3 - trzy krzyzyki w linii (komputer wygral)
#        2 - dwa krzyzyki w linii (szansa na wygrana komputera)
#        1 - jeden krzyzyk w linii
#       -1 - jedno kolko w linii
#       -2 - dwa kolka w linii (blokowac linie)
#       -3 - trzy kolka w linii - niedopuszczalne (wygrana gracza)
#       -5 - kolko i krzyzyk w linii (w tej linii nie da sie wygrac)
#      -10 - 2 kolka i krzyzyk lub kolko i 2 krzyzyki w linii, linia pelna


print('--------------------------------------------------------------------')
print('Kolko i krzyzyk')
print('--------------------------------------------------------------------')
print('Identyfikatory pol:')
print('1  2  3')
print('4  5  6')
print('7  8  9')
print('--------------------------------------------------------------------')
print('Zaczynamy!')

p1 = p2 = p3 = p4 = p6 = p7 = p8 = p9 = '-'
l1 = l2 = l3 = l4 = l5 = l6 = l7 = l8 = 10

p5 = 'X'
# l2 = 1
# l5 = 1
# l7 = 1
# l8 = 1
nr_ruchu = 1

max_liczba_ruchow = 9
koniec_gry = False

while nr_ruchu <= max_liczba_ruchow:
  print(p1 + '  ' + p2 + '  ' + p3)
  print(p4 + '  ' + p5 + '  ' + p6)
  print(p7 + '  ' + p8 + '  ' + p9)

  if nr_ruchu == max_liczba_ruchow or koniec_gry:
    break

  # Ruch gracza:
  print('Twoj ruch: ', end='')

  pole = int(input())

  if pole == 1 and p1 == '-':
    p1 = 'O'
  elif pole == 2 and p2 == '-':
    p2 = 'O'
  elif pole == 3 and p3 == '-':
    p3 = 'O'
  elif pole == 4 and p4 == '-':
    p4 = 'O'
  elif pole == 5 and p5 == '-':
    p5 = 'O'
  elif pole == 6 and p6 == '-':
    p6 = 'O'
  elif pole == 7 and p7 == '-':
    p7 = 'O'
  elif pole == 8 and p8 == '-':
    p8 = 'O'
  elif pole == 9 and p9 == '-':
    p9 = 'O'
  else:
    print('Blad!')
    continue
  nr_ruchu += 1

  # Stan planszy:
  # 1. Linia 1:
  #     zliczanie symboli w linii 1:
  licz_kolka = 0
  licz_krzyzyki = 0
  if p1 == 'O':
    licz_kolka += 1
  elif p1 == 'X':
    licz_krzyzyki += 1
  if p2 == 'O':
    licz_kolka += 1
  elif p2 == 'X':
    licz_krzyzyki += 1
  if p3 == 'O':
    licz_kolka += 1
  elif p3 == 'X':
    licz_krzyzyki += 1
  #     ustalenie wartosci linii 1:
  if licz_kolka == licz_krzyzyki == 0:
    l1 = 10
  elif licz_kolka == licz_krzyzyki == 1:
    l1 = -5
  elif (licz_krzyzyki == 2 and licz_kolka == 1) or (licz_krzyzyki == 1 and licz_kolka == 2):
    l1 = -10
  elif licz_kolka == 0:
    if licz_krzyzyki == 2:
      l1 = 2
    elif licz_krzyzyki == 1:
      l1 = 1
  elif licz_krzyzyki == 0:
    if licz_kolka == 2:
      l1 = -2
    elif licz_kolka == 1:
      l1 = -1
  # 2. Linia 2:
  #     zliczanie symboli w linii 2:
  licz_kolka = 0
  licz_krzyzyki = 1
  if p4 == 'O':
    licz_kolka += 1
  elif p4 == 'X':
    licz_krzyzyki += 1
  if p6 == 'O':
    licz_kolka += 1
  elif p6 == 'X':
    licz_krzyzyki += 1
  #     ustalenie wartosci linii 2:
  if licz_kolka == licz_krzyzyki == 0:
    l2 = 10
  elif licz_kolka == licz_krzyzyki == 1:
    l2 = -5
  elif (licz_krzyzyki == 2 and licz_kolka == 1) or (licz_krzyzyki == 1 and licz_kolka == 2):
    l2 = -10
  elif licz_kolka == 0:
    if licz_krzyzyki == 2:
      l2 = 2
    elif licz_krzyzyki == 1:
      l2 = 1
  elif licz_krzyzyki == 0:
    if licz_kolka == 2:
      l2 = -2
    elif licz_kolka == 1:
      l2 = -1
  # 3. Linia 3:
  #     zliczanie symboli w linii 3:
  licz_kolka = 0
  licz_krzyzyki = 0
  if p7 == 'O':
    licz_kolka += 1
  elif p7 == 'X':
    licz_krzyzyki += 1
  if p8 == 'O':
    licz_kolka += 1
  elif p8 == 'X':
    licz_krzyzyki += 1
  if p9 == 'O':
    licz_kolka += 1
  elif p9 == 'X':
    licz_krzyzyki += 1
  #     ustalenie wartosci linii 3:
  if licz_kolka == licz_krzyzyki == 0:
    l3 = 10
  elif licz_kolka == licz_krzyzyki == 1:
    l3 = -5
  elif (licz_krzyzyki == 2 and licz_kolka == 1) or (licz_krzyzyki == 1 and licz_kolka == 2):
    l3 = -10
  elif licz_kolka == 0:
    if licz_krzyzyki == 2:
      l3 = 2
    elif licz_krzyzyki == 1:
      l3 = 1
  elif licz_krzyzyki == 0:
    if licz_kolka == 2:
      l3 = -2
    elif licz_kolka == 1:
      l3 = -1
  # 4. Linia 4:
  #     zliczanie symboli w linii 4:
  licz_kolka = 0
  licz_krzyzyki = 0
  if p1 == 'O':
    licz_kolka += 1
  elif p1 == 'X':
    licz_krzyzyki += 1
  if p4 == 'O':
    licz_kolka += 1
  elif p4 == 'X':
    licz_krzyzyki += 1
  if p7 == 'O':
    licz_kolka += 1
  elif p7 == 'X':
    licz_krzyzyki += 1
  #     ustalenie wartosci linii 4:
  if licz_kolka == licz_krzyzyki == 0:
    l4 = 10
  elif licz_kolka == licz_krzyzyki == 1:
    l4 = -5
  elif (licz_krzyzyki == 2 and licz_kolka == 1) or (licz_krzyzyki == 1 and licz_kolka == 2):
    l4 = -10
  elif licz_kolka == 0:
    if licz_krzyzyki == 2:
      l4 = 2
    elif licz_krzyzyki == 1:
      l4 = 1
  elif licz_krzyzyki == 0:
    if licz_kolka == 2:
      l4 = -2
    elif licz_kolka == 1:
      l4 = -1
  # 5. Linia 5:
  #     zliczanie symboli w linii 5:
  licz_kolka = 0
  licz_krzyzyki = 1
  if p2 == 'O':
    licz_kolka += 1
  elif p2 == 'X':
    licz_krzyzyki += 1
  if p8 == 'O':
    licz_kolka += 1
  elif p8 == 'X':
    licz_krzyzyki += 1
  #     ustalenie wartosci linii 5:
  if licz_kolka == licz_krzyzyki == 0:
    l5 = 10
  elif licz_kolka == licz_krzyzyki == 1:
    l5 = -5
  elif (licz_krzyzyki == 2 and licz_kolka == 1) or (licz_krzyzyki == 1 and licz_kolka == 2):
    l5 = -10
  elif licz_kolka == 0:
    if licz_krzyzyki == 2:
      l5 = 2
    elif licz_krzyzyki == 1:
      l5 = 1
  elif licz_krzyzyki == 0:
    if licz_kolka == 2:
      l5 = -2
    elif licz_kolka == 1:
      l5 = -1
  # 6. Linia 6:
  #     zliczanie symboli w linii 6:
  licz_kolka = 0
  licz_krzyzyki = 0
  if p3 == 'O':
    licz_kolka += 1
  elif p3 == 'X':
    licz_krzyzyki += 1
  if p6 == 'O':
    licz_kolka += 1
  elif p6 == 'X':
    licz_krzyzyki += 1
  if p9 == 'O':
    licz_kolka += 1
  elif p9 == 'X':
    licz_krzyzyki += 1
  #     ustalenie wartosci linii 6:
  if licz_kolka == licz_krzyzyki == 0:
    l6 = 10
  elif licz_kolka == licz_krzyzyki == 1:
    l6 = -5
  elif (licz_krzyzyki == 2 and licz_kolka == 1) or (licz_krzyzyki == 1 and licz_kolka == 2):
    l6 = -10
  elif licz_kolka == 0:
    if licz_krzyzyki == 2:
      l6 = 2
    elif licz_krzyzyki == 1:
      l6 = 1
  elif licz_krzyzyki == 0:
    if licz_kolka == 2:
      l6 = -2
    elif licz_kolka == 1:
      l6 = -1
  # 7. Linia 7:
  #     zliczanie symboli w linii 7:
  licz_kolka = 0
  licz_krzyzyki = 1
  if p1 == 'O':
    licz_kolka += 1
  elif p1 == 'X':
    licz_krzyzyki += 1
  if p9 == 'O':
    licz_kolka += 1
  elif p9 == 'X':
    licz_krzyzyki += 1
  #     ustalenie wartosci linii 7:
  if licz_kolka == licz_krzyzyki == 0:
    l7 = 10
  elif licz_kolka == licz_krzyzyki == 1:
    l7 = -5
  elif (licz_krzyzyki == 2 and licz_kolka == 1) or (licz_krzyzyki == 1 and licz_kolka == 2):
    l7 = -10
  elif licz_kolka == 0:
    if licz_krzyzyki == 2:
      l7 = 2
    elif licz_krzyzyki == 1:
      l7 = 1
  elif licz_krzyzyki == 0:
    if licz_kolka == 2:
      l7 = -2
    elif licz_kolka == 1:
      l7 = -1
  # 8. Linia 8:
  #     zliczanie symboli w linii 8:
  licz_kolka = 0
  licz_krzyzyki = 1
  if p3 == 'O':
    licz_kolka += 1
  elif p3 == 'X':
    licz_krzyzyki += 1
  if p7 == 'O':
    licz_kolka += 1
  elif p7 == 'X':
    licz_krzyzyki += 1
  #     ustalenie wartosci linii 8:
  if licz_kolka == licz_krzyzyki == 0:
    l8 = 10
  elif licz_kolka == licz_krzyzyki == 1:
    l8 = -5
  elif (licz_krzyzyki == 2 and licz_kolka == 1) or (licz_krzyzyki == 1 and licz_kolka == 2):
    l8 = -10
  elif licz_kolka == 0:
    if licz_krzyzyki == 2:
      l8 = 2
    elif licz_krzyzyki == 1:
      l8 = 1
  elif licz_krzyzyki == 0:
    if licz_kolka == 2:
      l8 = -2
    elif licz_kolka == 1:
      l8 = -1

  # Ruch komputera:
  while True:
    # 1. Czy mozna wygrac w tym ruchu (l = 2)
    #    lub czy trzeba zablokowac gracza (l = -2)
    if l1 == 2 or l1 == -2:
      if p1 == '-':
        p1 = 'X'
      elif p2 == '-':
        p2 = 'X'
      elif p3 == '-':
        p3 = 'X'
      if l1 == 2:
        l1 = 3
        koniec_gry = True
      break
    if l2 == 2:
      if p4 == '-':
        p4 = 'X'
      elif p6 == '-':
        p6 = 'X'
      l2 = 3
      koniec_gry = True
      break
    if l3 == 2 or l3 == -2:
      if p7 == '-':
        p7 = 'X'
      elif p8 == '-':
        p8 = 'X'
      elif p9 == '-':
        p9 = 'X'
      if l3 == 2:
        l3 = 3
        koniec_gry = True
      break
    if l4 == 2 or l4 == -2:
      if p1 == '-':
        p1 = 'X'
      elif p4 == '-':
        p4 = 'X'
      elif p7 == '-':
        p7 = 'X'
      if l4 == 2:
        l4 = 3
        koniec_gry = True
      break
    if l5 == 2:
      if p2 == '-':
        p2 = 'X'
      elif p8 == '-':
        p8 = 'X'
      l5 = 3
      koniec_gry = True
      break
    if l6 == 2 or l6 == -2:
      if p3 == '-':
        p3 = 'X'
      elif p6 == '-':
        p6 = 'X'
      elif p9 == '-':
        p9 = 'X'
      if l6 == 2:
        l6 = 3
        koniec_gry = True
      break
    if l7 == 2:
      if p1 == '-':
        p1 = 'X'
      elif p9 == '-':
        p9 = 'X'
      l7 = 3
      koniec_gry = True
      break
    if l8 == 2:
      if p3 == '-':
        p3 = 'X'
      elif p7 == '-':
        p7 = 'X'
      l8 = 3
      koniec_gry = True
      break
    # 2. Czy ktoras linia jest rozpoczeta (l = -1 lub l = 1)
    if l1 == -1 or l1 == 1:
      if p1 == '-':
        p1 = 'X'
      elif p3 == '-':
        p3 = 'X'
      elif p2 == '-':
        p2 = 'X'
      break
    if l4 == -1 or l4 == 1:
      if p1 == '-':
        p1 = 'X'
      elif p7 == '-':
        p7 = 'X'
      elif p4 == '-':
        p4 = 'X'
      break
    if l3 == -1 or l3 == 1:
      if p7 == '-':
        p7 = 'X'
      elif p9 == '-':
        p9 = 'X'
      elif p8 == '-':
        p8 = 'X'
      break
    if l6 == -1 or l6 == 1:
      if p3 == '-':
        p3 = 'X'
      elif p9 == '-':
        p9 = 'X'
      elif p6 == '-':
        p6 = 'X'
      break
    if l2 == 1:
      if p4 == '-':
        p4 = 'X'
      elif p6 == '-':
        p6 = 'X'
      break
    if l5 == 1:
      if p2 == '-':
        p2 = 'X'
      elif p8 == '-':
        p8 = 'X'
      break
    if l7 == 1:
      if p1 == '-':
        p1 = 'X'
      elif p9 == '-':
        p9 = 'X'
      break
    if l8 == 1:
      if p3 == '-':
        p3 = 'X'
      elif p7 == '-':
        p7 = 'X'
      break
    # 3. whatever, byle do konca
    if l1 == -5:
      if p1 == '-':
        p1 = 'X'
      elif p2 == '-':
        p2 = 'X'
      elif p3 == '-':
        p3 = 'X'
      break
    if l2 == -5:
      if p4 == '-':
        p4 = 'X'
      elif p6 == '-':
        p6 = 'X'
      break
    if l3 == -5:
      if p7 == '-':
        p7 = 'X'
      elif p8 == '-':
        p8 = 'X'
      elif p9 == '-':
        p9 = 'X'
      break
    if l4 == -5:
      if p1 == '-':
        p1 = 'X'
      elif p4 == '-':
        p4 = 'X'
      elif p7 == '-':
        p7 = 'X'
      break
    if l5 == -5:
      if p2 == '-':
        p2 = 'X'
      elif p8 == '-':
        p8 = 'X'
      break
    if l6 == -5:
      if p3 == '-':
        p3 = 'X'
      elif p6 == '-':
        p6 = 'X'
      elif p9 == '-':
        p9 = 'X'
      break
    if l7 == -5:
      if p1 == '-':
        p1 = 'X'
      elif p9 == '-':
        p9 = 'X'
      break
    if l8 == -5:
      if p3 == '-':
        p3 = 'X'
      elif p7 == '-':
        p7 = 'X'
      break
  nr_ruchu += 1

# Zakonczenie gry:

if l1 == 3 or l2 == 3 or l3 == 3 or l4 == 3 or \
    l5 == 3 or l6 == 3 or l7 == 3 or l8 == 3:
  print('Przegrana')
else:
  print('Remis')

