number=int(input('put your number:'))
while number!=9:
    print('try again')
    number=int(input('put your number:'))
print('enter your number')
text='AbbaBAaAb'
counter=0
count=0
for i in range(len(text)):
    if text[i]=='a' or text[i]=='A':
        counter+=1
    if text[i]=='b':
        count+=1
print('A and a:',counter)
print('b:',count)
texts='AbbaBAaAb'
counter=0
count=0
for text in texts:
    if text. lower()=='a':
        counter+=1
    if text=='b':
        count+=1
print('A and a:',counter,'b:',count)

