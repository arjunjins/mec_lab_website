# simple keyword

# imports
import random as r

# the list
keys = [" E "," N "," I "," T "," R "," L "," S "," A "," U "," O "," D "," Y "," C "," H "," G "," M "," P "," T  I  O  N "," B "," L  Y "," K "," V "," W "," F "," Z "," X "," Q "," J "]

for i in range(6,29):
    
    progress = 0
    l = [k for k in range(1,i)] if i < 9 else [k for k in range(1,9)]
    s = ''
    #print(l)
    
    while progress < 500:
        
        #j = r.choice(l)
        for j in range(r.choice(l)):
            
            if i == 6:
                j = r.choice(keys[:i])
                #print(r.choice(keys[:i]),end='')
            else:
                j = r.choices(keys[:i],weights=tuple([50]*(i-1)+[80]),k=1)[0]
                #print(r.choices(keys[:i],weights=tuple([50]*(i-1)+[80]),k=1)[0],end='')
            
            print(j,end='')
            s+=j
        print()
        if s[-2:-1] == 'A':
            s+=' T  I  O  N '
        with open("words.txt",'a+') as f:
            s = s.replace(" ","")
            if s not in f.readlines():
                f.write(s+'\n')
                progress+=1
        s=''
        
        
    '''
    while progress<.80:
        #j = r.choice(l)
        l = []
        #print(j)
        for z in range(r.choice(l)):
            l.append(r.choice(keys[:i+1]))
        print(i for i in l)
      '''  