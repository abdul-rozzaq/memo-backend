words_str = '''

아이: bola,오이: bodring,아우: uka,이마: peshona,
나이: yosh,오리: o'rdak,너무: juda,누나: opa(erkaklar uchun),
나무: daraxt,어머니: ona,머리: bosh,미리: oldindan
,어느 나라: qaysi davlat,우리 나라: bizning davlat


'''


for x in words_str.split(','):
    y = x.split(':')

    korean = y[0].strip()
    uzbek = y[1].strip()

    
