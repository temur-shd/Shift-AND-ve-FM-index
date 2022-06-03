 #Text içinde GAATTCATTTCTCCCGCTGCCCCATCTCT, TCACG ve TCTCG örüntülerinin arama zamanları hesaplanacaktır.
#Örüntü aramaları Shift AND ve FM index ile yapılacaktır.
#Her iki algoritmanın arama ve önişleme süreleri kıyaslanacaktır.

import timeit  #Çalışma zamanını ölçmek için kullanılmıştır.

#ShiftAND işlemi için oluşturulmuştur.
def shift_and(oruntu, text):
    m = len(oruntu)  #örüntü uzunluğu
    n = len(text)    #fna dosyasındaki texy uzunluğu

    # Soruda verilen örüntüleri kümeye atma işlemi
    B = {}
    for i in range(m):
        B[oruntu[i]] = (B.get(oruntu[i], 0) | (1 << i))

    # arama işlemi
    D = 0
    for i in range(n):
        D = ((D << 1) | 1) & (B.get(text[i], 0))
        if D & (1 << (m - 1)):
            print("BULUNDUGU YER: %d" % (i - m + 1))

#Verilen fna dosyasını açma işlemi
fh = open('gene.fna')
text= fh.read()
oruntu = ['GAATTCATTTCTCCCGCTGCCCCATCTCT','TCACG','TCTCG']

for x in range(3):      # 3 tane örüntü olduğu için for ddöngüsü açılmıştır.
    print("{}".format(oruntu[x]))
    shift_and(oruntu[x], text)
    print('ARAMA ZAMANI: ',
          timeit.timeit(),"\n"
          '***************',
          )

"""
Syntax: timeit.timeit(stmt, setup,timer, number)
Parameters
stmt: This will take the code for which you want to measure the execution time. The default value is “pass”.
setup: This will have setup details that need to be executed before stmt. The default value is “pass.”
timer: This will have the timer value, timeit() already has a default value set, and we can ignore it.
number: The stmt will execute as per the number is given here. The default value is 1000000."""














