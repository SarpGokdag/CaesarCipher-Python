##Sarp Gökdağ [Caesar Cipher]
##Youtube Video Link --> 
plaintext = input('Çevrilecek Metin : ')
alfabe = "abcçdefghıijklmnoöprsştuüvyz"
yanakaydırma = 3
kripto = ''

for c in plaintext :
    if c in alfabe:
        kripto += alfabe[(alfabe.index(c)-yanakaydırma)%(len(alfabe))]

print('İşte Kriptolu Mesajınız :' + kripto)