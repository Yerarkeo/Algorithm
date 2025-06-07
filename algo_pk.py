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
texts='AaBabaCcDdafe'
counter=0
for text in texts:
    if text.lower()=='b' or text.lower()=='c' or text.lower()=='d':
        counter+=1
print('total:',counter)
texts='AaBabaCcDdafe'
count=0
for text in texts:
    if text.upper()=='B':
        count+=1
    elif text.upper()=='C':
        count+=1
    elif text.upper()=='D':
        count+=1
print('total',count)