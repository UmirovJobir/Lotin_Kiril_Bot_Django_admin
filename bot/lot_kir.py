from backend import Analiz

data = Analiz()

class translate:
    def __init__(self):
        self.kril = ["А", "а", "Б", "б", "В", "в", "Г", "г", "Д", "д", "Е", "е", "Ё", "ё", "Ж", "ж",
                "З", "з", "И", "и", "Й", "й", "К", "к", "Л", "л", "М", "м", "Н", "н", "О", "о",
                "П", "п", "Р", "р", "С", "с", "Т", "т", "У", "у", "Ф", "ф", "Х", "х", "Ц", "ц",
                "Ч", "ч", "Ш", "ш", "Э", "э", "Ю", "ю", "Я", "я", "Ў", "ў",
                "Қ", "қ", "Ғ", "ғ", "Ҳ", "ҳ", "ъ", "ь",
                " ", '"', "#", "$", "%", "&", "(", ")", "*", "+", ",", "-", ".", "/",":", ";", "<", "=", ">", "?", "@", "[", "]", "^", "_",
                "`", "❇", "📱", "🌐", "✅", "!", "–"]

        self.lotin = ["A", "a", "B", "b", "V", "v", "G", "g", "D", "d", "Ye", "ye", "Yo", "yo", "J", "j",
                "Z", "z", "I", "i", "Y", "y", "K", "k", "L", "l", "M", "m", "N", "n", "O", "o",
                "P", "p", "R", "r", "S", "s", "T", "t", "U", "u", "F", "f", "X", "x", "S", "s",
                "Ch", "ch", "Sh", "sh",  "E", "e", "Yu", "yu", "Ya", "ya", "O‘", "o‘",
                "Q", "q", "G‘", "g‘", "H", "h", "’", "",
                " ", '"', "#", "$", "%", "&", "(", ")", "*", "+", ",", "-", ".", "/",":", ";", "<", "=", ">", "?", "@", "[", "]", "^", "_",
                "`", "❇", "📱", "🌐", "✅", "!", "–"]

        self.digit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def lotin_to_kril(self, text= 'Matin kiriting..'):

        dic_text = data.replay_dictionary_words()
        for i in dic_text:
            text = text.replace(f'{i[0]}',f'{i[1]}')

        text = text.replace('ksiya', 'кция').replace('KSIYA', 'КЦИЯ')
        text = text.replace('tsiya', 'ция').replace('TSIYA', 'ЦИЯ')
        text = text.replace('ksion', 'кцион').replace('KSION', 'КЦИОН')
        text = text.replace('tsion', 'цион').replace('TSION', 'ЦИОН')
        text = text.replace('bsiya', 'бция').replace('BSIYA', 'БЦИЯ')
        text = text.replace('sion', 'цион').replace('SION', 'ЦИОН')
        text = text.replace('siya', 'ция').replace('SIYA', 'ЦИЯ')

        text = text.replace('tsey', 'цей').replace('TSEY', 'ЦЕЙ')

        text = text.replace('fakultet', 'факультет').replace('Fakultet', 'Факультет').replace('FAKULTET', 'ФАКУЛЬТЕТ')
        text = text.replace('neft','нефть').replace('Neft','Нефть').replace('NEFT','НЕФТЬ')
        text = text.replace('reket', 'рэкет')

        text = text.replace("Yo'", "Йў").replace("yo'", 'йў').replace("Yo‘", "Йў").replace("yo‘", 'йў').replace("yoʻ",'йў').replace("Yoʻ", "Йў").replace("yo`",'йў').replace("Yo`", "Йў").replace("Yo’", "Йў").replace("yo’", 'йў')
        text = text.replace("YO'", "Йў").replace("YO‘", "Йў").replace("YOʻ", "Йў").replace("YO`", "Йў").replace("YO’", "Йў")
        text = text.replace("Ye", "Е").replace("ye", "е").replace("Yo", "Ё").replace("yo", "ё").replace("Ch","Ч").replace("ch", "ч").replace("Sh", "Ш").replace("sh", "ш").replace("Yu", "Ю").replace("yu", "ю").replace("Ya","Я").replace("ya", "я").replace("O‘", "Ў").replace("o‘", "ў").replace("G‘", "Ғ").replace("g‘", "ғ")
        text = text.replace("YE", "Е").replace("YO", "Ё").replace("CH","Ч").replace("SH", "Ш").replace("YU", "Ю").replace("YA","Я")
        text = text.replace("oʻ", 'ў').replace("Oʻ", "Ў").replace("gʻ", "ғ").replace("Gʻ", "Ғ").replace("О‘", "Ў").replace("o‘", 'ў').replace("О`", "Ў").replace("o`", 'ў').replace("О’", "Ў").replace("o’", 'ў').replace("O’", "Ў").replace("oʼ", "ў").replace("Oʼ", "Ў")
        text = text.replace("O'", "Ў").replace("o'", "ў").replace("G'", "Ғ").replace("g'", "ғ").replace("G`", "Ғ").replace("g`", "ғ").replace("G’", "Ғ").replace("g’", "ғ").replace("gʼ", "ғ").replace("Gʼ", "Ғ")
        text = text.replace("'", "ъ").replace("`", "ъ")

        t = []
        for i in text:
            t.append(i)
        #print(t)
        n = ''
        for j, i in enumerate(t):
            for index, (l, k) in enumerate(zip(self.lotin, self.kril)):
                if i not in self.lotin:
                    n = f"{n}{i}"
                    break
                if i == '\n':
                    n = f"{n}{i}"
                    break
                if (i == 'e' and i == l) or (i == 'E' and i == l):
                    if (text[j - 1] == ' ') or (j - 1 < 0) or (text[j-1] == '\n') or ((text[j-1] not in self.kril[:68]) and (text[j-1] not in self.lotin[:66])):
                        n = f"{n}{k}"
                        break
                    else:
                        n = f"{n}{i}"
                        break
                if i == l:
                    n = f"{n}{self.kril[index]}"
                    break
                elif i == k:
                    n = f"{n}{k}"
                    break
        #print(n)
        return n

    def kril_to_lotin(self, text= 'Matin kiriting..'):

        dic_text = data.replay_dictionary_words()
        for i in dic_text:
            text = text.replace(f'{i[0]}', f'{i[1]}')

        text = text.replace('кция','ksiya').replace('КЦИЯ', 'KSIYA')
        text = text.replace('ция','tsiya').replace('ЦИЯ', 'TSIYA')
        text = text.replace('кцион','ksion').replace('КЦИОН','KSION')
        text = text.replace('цион', 'tsion').replace('ЦИОН','TSION')

        text = text.replace('цей', 'tsey').replace('ЦЕЙ','TSEY')

        text = text.replace('факультет', 'fakultet').replace('Факультет','Fakultet').replace('ФАКУЛЬТЕТ', 'FAKULTET')
        text = text.replace('нефть', 'neft').replace('Нефть', 'Neft').replace('НЕФТЬ', 'NEFT')

        # text = text.replace("Йў", "Yo'").replace('йў',"yo'").replace("Йў", "Yo‘").replace('йў', "yo‘").replace('йў', "yoʻ").replace("Йў", "Yoʻ").replace('йў', "yo`").replace("Йў","Yo`").replace("Йў","Yo’").replace('йў',"yo’")
        # text = text.replace("Йў", "YO'").replace("Йў", "YO‘").replace("Йў","YOʻ").replace("Йў", "YO`").replace("Йў", "YO’")
        # text = text.replace("Е", "Ye").replace("е", "ye").replace("Ё", "Yo").replace("ё", "yo").replace("Ч", "Ch").replace("ч", "ch").replace("Ш", "Sh").replace("ш", "sh").replace("Ю", "Yu").replace("ю", "yu").replace("Я","Ya").replace("я", "ya").replace("Ў", "O‘").replace("ў", "o‘").replace("Ғ", "G‘").replace("ғ", "g‘")
        # text = text.replace("Е", "YE").replace("Ё", "YO").replace("Ч", "CH").replace("Ш", "SH").replace("Ю", "YU").replace("Я", "YA")
        # text = text.replace('ў',"oʻ").replace("Ў", "Oʻ").replace("gʻ", "ғ").replace("Gʻ", "Ғ").replace("О‘", "Ў").replace("o‘", 'ў').replace("О`", "Ў").replace("o`", 'ў').replace("О’", "Ў").replace("o’", 'ў').replace("O’", "Ў").replace("oʼ", "ў").replace("Oʼ", "Ў")
        # text = text.replace('ў', "oʻ").replace("Ў", "Oʻ").replace("gʻ", "ғ").replace("Gʻ", "Ғ")
        # text = text.replace("O'", "Ў").replace("o'", "ў").replace("G'", "Ғ").replace("g'", "ғ").replace("G`", "Ғ").replace("g`", "ғ").replace("G’", "Ғ").replace("g’", "ғ").replace("gʼ", "ғ").replace("Gʼ", "Ғ")
        # text = text.replace("'", "ъ").replace("`", "ъ")

        t = []
        for i in text:
            t.append(i)
        #print(t)
        n = ''
        for j, i in enumerate(t):
            for index, (l, k) in enumerate(zip(self.lotin, self.kril)):
                if i not in self.kril:
                    n = f"{n}{i}"
                    break
                if i == '\n':
                    n = f"{n}{i}"
                    break
                if i == k:
                    if ((i == 'е' and i == k) or (i == 'Е' and i == k)) and (text[j - 1] != ' ') and (text[j - 1] != '\n') and (j-1 > 0):
                        n = f"{n}{i}"
                        break
                    else:
                        n = f"{n}{self.lotin[index]}"
                        break
                # if (i == 'e' and i == l) or (i == 'E' and i == k):
                #     if (text[j - 1] == ' ') or (j - 1 < 0) or (text[j-1] == '\n') or ((text[j-1] not in self.kril[:68]) and (text[j-1] not in self.lotin[:66])):
                #         n = f"{n}{l}"
                #         break
                #     else:
                #         n = f"{n}{i}"
                #         break

                elif i == l:
                    n = f"{n}{l}"
                    break
        #print(n)
        return n

