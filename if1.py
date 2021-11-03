#juft = float(input('juft sonni kiriting?>>>'))
#if juft%2:
 #   print('bu son juft emas')
#else:
#    print('raxmat')


#yosh = int(input('iltimos yoshingizni kirting? >>>'))

#if yosh <= 4 or yosh >= 60:
#    narx = 'bepul'
#elif yosh < 18:
#    narx = '10 000 som'
#else:
#    narx = '8000 som'
#print(f'Konsetga kirish  {narx}')

#x = float(input('Birinchi sonni kiriting? >>>'))
#y = float(input('ikkinchi sonni kiriting? >>>'))

#if x ==y:
#    print(f'{x} = {y}')
#elif x > y:
#    print(f"{x} > {y}")
#else:
#    print(f'{x}<{y}')\
    

#mahsulotlar = ['sabzi','piyoz','kartoshka','qalanpir']
#savat = []
#for n in range(3):
#  savat.append(input(f'savatga {n+1} mahsulot qoshing: '))
  
#  for mahsulot in savat:
#      if mahsulot in mahsulotlar:
#          print(f'{mahsulot} mavjud')
#      else:
#           print(f'{mahsulot} mavjud emas')

son = int(input('istagan sonni kiritng'))

for n in range(2 ,11):
    if not (son % n):
        print(f'{son} soni {n} ga qoldiqsiz bolinadi')