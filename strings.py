while True:
    word=input()
    if not word:
        break
    l=len(word)
    b=""
    i=0
    while i<l:
        if word[i]=='-' and word[i+1]=='>':
            b+="."
            i+=1
        elif word[i]=='/' and word[i+1]=='/':
            b+="//"
            i+=1
            for j in range(i+1,l):
                b+=word[j]
            break
        else:
            b+=word[i]
        i+=1
    print(b)
