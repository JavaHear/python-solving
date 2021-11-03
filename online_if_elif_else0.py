# yosh = int(input('yoshingizni kiriting ?')) 
# if yosh <= 4:
#     narx = 'bepul'
# elif yosh >= 18:
#     narx = '5000 som'
# else:
#     narx = '8000 som'
# print(f'{yosh} yosh uchun kirish {narx} ')

# kun = input('bugun qanday kun?>>')
# if kun == 'shanba' or kun == 'yakshanba':
#     print('bugun dam olish kuni')
# else:
#     print('bugun ish kuni')
    

# kun = input('kunni kiriting?>>> ')
# dars = input('bugun dars bormi?>>')

# if kun.lower() == 'yakshanba' and dars.lower() == 'yoq':
#     print('bugun ishga chiqmiz')
# else:
#     print('bugun darsku')


# kun = input('kunni kiriting?>>')
# dars = input('bugun dars bormi?>>>')

# if kun.lower() == 'shanba' or kun.lower() == 'yakshanba' and dars.lower() == 'bor':
#     print('bugun fudbol oynaymiz')
# else:
#     print('bugun darslar bor')

# narx = 15000
# salat = True
# choy = False

# if salat or choy:
#    narx = narx +5000
# elif choy and salat:
#    narx = narx + 5000
# print(f'jami narxi {narx}')

# narx = 10000
# telefon = True
# fleshka = True
# Ipad = False

# if telefon:
#     print(f'mijoz telefon sotib oldi')
#     narx = narx + 1500000

# if fleshka:
#     print(f'mijoz fleshka sotib oldi')
#     narx = narx + 240000
# if Ipad:
#     print(f'mijoz Ipad sotib oldi')
#     narx = narx + 134000
# print(f'umumiy qiymati {narx} som boldi')

# mahsulotlar = ['sabzi','piyoz','qalampir','kartoshka']

# menu = ['osh','kabob', 'shorva', 'manti']
# mijoz = input('nima ovqat yeysiz?>>')

# if mijoz in menu:
#     print(f'{mijoz} qabul qilindi')
# else:
#     print('bu ovqat mavjud emas uzr')

brands = ['fila','adidas','nike','puma']
sales = ['fila','northface','nike']
if sales:
  for thing in sales:
   if thing  in brands:
     print(f'siz {thing} sotib olishingiz mumkin')
  else:
     print(f'siz {thing} mavjud emas')
else:
    print('savat bosh')
  
