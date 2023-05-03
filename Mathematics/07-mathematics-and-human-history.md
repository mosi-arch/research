# Human History & Mathematics
One of the first writing letters invented by humans was the cuneiform writing letters.
- Did you know that the numbers were based on 60 in "Plateau of Iran" 4000 to 2500 years ago?
- Do you know that in **France** the counting system is still based on 60 and logical base is 10?

**Human civilization is more intertwined than you think.**

The famous Iranian poet Saadi has a poem that in the entrance of the United Nations:\
Humans are members of one body - which are one gem in creation\
When one member hurt -  the other members were not spared

### French:
L'une des premières lettres d'écriture inventées par les humains était les lettres d'écriture cunéiformes.
- Saviez-vous que les chiffres étaient basés sur 60 dans le "Plateau d'Iran" il y a 4000 à 2500 ans ?
- Savez-vous qu'en **France** le système de comptage est toujours basé sur 60 et que la base logique est 10 ?

**La civilisation humaine est plus imbriquée que vous ne le pensez.**

Le célèbre poète iranien Saadi a un poème qui, à l'entrée des Nations Unies :\
Les humains sont membres d'un seul corps - qui est un joyau de la création\
Quand un membre a été blessé - les autres membres n'ont pas été épargnés

### Persian/Farsi:
یکی از اولین حروف نوشتاری ابداع بشر، حروف نوشتاری میخی بوده است.

آیا میدانستید اعداد در ۴۰۰۰ تا ۲۵۰۰ سال پیش در "فلات ایران" بر پایه۶۰ بوده اند؟

آیا میدانید که در کشور فرانسه هنوز سیستم شمارش بر مبنای ۶۰ و در پایه منطقی ۱۰ است؟

تمدن بشری بیشتر از چیزی که تصور میکنید در هم تنیده است.

سعدی شاعر معروف ایرانی شعری دارد که بر ورودی سازمان ملل است:

بنی آدم اعضای یک پیکرند - که در آفرینش ز یک گوهرند

چو عضوی به درد آورد روزگار - دگر عضوها را نماند قرار

#history #humanity #mathematics

![img](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/Babylonian_numerals.svg/400px-Babylonian_numerals.svg.png)
the number 60 is a thin vertical square.

---

### Why human love Base10 for counting?
111/3 = 222/6 = 333/9 = 444/12 = 555/15 = 666/18 = 777/21 = 888/24 = 999/27 = 37

#Theorem :
- What happened? `111/1+1+1 = 111/3 = 37` AND [3 + 7 = 10]
- From 1 to 9 this equation answer is 37.
- The Ancestors love to playing by numbers, they know about Base3, Base6, Base12, Base60, But choosing Base10 for helping next generations.

37 is beautiful ever number, divide 37 to 1 to 36 and watching the answers. (pandelerium)\
#mathematics #love #numbers

---

Centuries ago:
- Base 60 used by Australians.
- Denmark, Norway and the island used Base60. (valhalla is big like base60)
- South America used Base60. (Maya loves math)
- Before the first (Persian) empire in the Middle East, Base60 was used in mathematics.

How did they make Base60?
- Base 12 * 5

You see the math used in nature by humans anywhere is 12th grade.\
**Year, season, hour**...

But in these recent centuries we use base10, just for fingers to count!\
The essential beauty of life is that the mindset underlies everything and the philosophy of mathematics.

---

### Base10 to Base12
```py
def base10_to_base12(num):
    digits = "0123456789xe"
    result = ""
    while num > 0:
        remainder = num % 12
        result = digits[remainder] + result
        num //= 12
    return result if result else "0"
```
x = 10\
e = 11

example:
```py
>>> base10_to_base12(255)
"173"
```

---

### Base10 to Base60
The digits used in base 60 are "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYabcdefghijklmnopqrstuvwxy", where the first 10 digits represent the numbers 0-9, the next 25 digits represent the letters A-Y (in uppercase), and the last 25 digits represent the letters a-y (in lowercase).

```py
def base10_to_base60(num):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYabcdefghijklmnopqrstuvwxy"
    result = ""
    while num > 0:
        remainder = num % 60
        result = digits[remainder] + result
        num //= 60
    return result if result else "0"
```

example:
```py
>>> base10_to_base60(1234567890)
"2lkCB"
```
