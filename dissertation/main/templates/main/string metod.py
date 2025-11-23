#туыстық атаулары
atatek_ataulary = "ата, әке, бала, немере, шөбере, шөпшек, немене"
print (atatek_ataulary.upper())

tuystyk_ataulary = "ЖҮРЕЖАТ, ТУАЖАТ, ЖҰРАҒАТ, ЖАТ ЖҰРАҒАТ, ЖЕГЖАT, ЖАМАҒАЙЫН"
print (tuystyk_ataulary.lower())

s = 'Қазақстанның астанасы - Нұрсұлтан'
new_s = s.replace('Нұрсұлтан', 'Астана')
print(new_s)


#Қазақша әлеуметтік желі
rus = 'лайк'
kz = rus.replace('лайк', 'лүпіл')
print(kz)

rus = 'комментарий'
kz = rus.replace('комментарий', 'пікір')
print(kz)

rus = 'подписчик'
kz = rus.replace('подписчик', 'жазылушы')
print(kz)

rus = 'поделиться'
kz = rus.replace('поделиться', 'бөлісу')
print(kz)

rus = 'сoхранить'
kz = rus.replace('сохранить', 'сақтау')
print(kz)

rus = 'поиск'
kz = rus.replace('поиск', 'іздеу')
print(kz)


rus = 'прямой эфир'
kz = rus.replace('прямой эфир', 'тікелей эфир')
print(kz)


rus = 'просмотры'
kz = rus.replace('просмотры', 'қаралым')
print(kz)

rus = 'блокировать'
kz = rus.replace('блокировать', 'бұғаттау')
print(kz)

rus = 'селфи'
kz = rus.replace('селфи', 'селфи жасау')
print(kz)
#ұлттыққорықтар
koryk = "Ақсу-Жабағылы, Алакөл, Алматы, Барсакелмес, Батыс Алтай, Қаратау, Қорғалжын, Марқакөл, Наурызым, Үстірт"
print (koryk.find('Алакөл'))
print (koryk.find('Алакөл'))
print (sorted(koryk))

string1 = 'Hello, hello, hello, hello'
print (string1.count(' '))


string1 = 'БОТАМ АЙНАЛАЙЫН  БАЛАПАНЫМ  БОТАҚАНЫМ БӨЛТІРІГІМ ЕЛІГІМ  КӨЖЕГІМ ТАЙЛАҒЫМ ШӨЖЕМ  ҚОШАҚАНЫМ ҚҰЛЫНШАҒЫМ'
commands = string1.split()
print(commands)
print (sorted(commands))
print (ord ('A'))


string1 = 'Hello, hello, hello, hello'
print (string1.strip('hello'))



