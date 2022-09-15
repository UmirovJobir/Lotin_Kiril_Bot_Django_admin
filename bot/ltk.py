kril=["А","а","Б","б","В","в","Г","г","Д","д","Е","е","Ё","ё","Ж","ж",
"З","з","И","и","Й","й","К","к","Л","л","М","м","Н","н","О","о",
"П","п","Р","р","С","с","Т","т","У","у","Ф","ф","Х","х","Ц","ц",
"Ч","ч","Ш","ш","ъ","ь","Э","э","Ю","ю","Я","я","Ў","ў",
"Қ","қ","Ғ","ғ","Ҳ","ҳ", " ",'"',"#","$","%","&","(",")","*","+",",","-",".","/",
"0","1","2","3","4","5","6","7","8","9",":",";","<","=",">","?","@","[","]","^","_","`"]

lotin=["A","a","B","b","V","v","G","g","D","d","Ye","ye","Yo","yo","J","j",
"Z","z","I","i","Y","y","K","k","L","l","M","m","N","n","O","o",
"P","p","R","r","S","s","T","t","U","u","F","f","X","x","S","s",
"Ch","ch","Sh","sh","’","","E","e","Yu","yu","Ya","ya","O‘","o‘",
"Q","q","G‘","g‘","H","h"," ",'"',"#","$","%","&","(",")","*","+",",","-",".","/","\\",
"0","1","2","3","4","5","6","7","8","9",":",";","<","=",">","?","@","[","]","^","_","`"]

def translate(text):
    n = ''
    for j, i in enumerate(text):
        for index, (l, k) in enumerate(zip(lotin, kril)):
            if (i == 'e' and i == l) or (i == 'E' and i == l):
                if (text[j-1] == ' ') or (j-1 < 0):
                    n = f"{n}{k}"
                    break
                else:
                    n = f"{n}{i}"
                    break
            if i == l:
                n = f"{n}{kril[index]}"
                break
            elif i == k:
                n = f"{n}{k}"
                break
    print(n)

text = input("Lotincha yoki krilcha so'z kiriting: ")
text = text.replace("Yo'", "Йў").replace("yo'", 'йў').replace("Yo‘","Йў").replace("yo‘",'йў')
text = text.replace("Ye", "Е").replace("ye","е").replace("Yo", "Ё").replace("yo","ё").replace("Ch","Ч").replace("ch","ч").replace("Sh","Ш").replace("sh","ш").replace("Yu","Ю").replace("yu","ю").replace("Ya","Я").replace("ya","я").replace("O‘","Ў").replace("o‘","ў").replace("G‘","Ғ").replace("g‘","ғ")
text = text.replace("oʻ", 'ў').replace("Oʻ", "Ў").replace("gʻ", "ғ").replace("Gʻ", "Ғ")
text = text.replace("O'","Ў").replace("o'","ў").replace("G‘","Ғ").replace("g'","ғ")
text = text.replace("'", "ъ").replace("`", "ъ")

t = []
for i in text:
    t.append(i)
print(t)

translate(text=t)