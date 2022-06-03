#Text içinde GAATTCATTTCTCCCGCTGCCCCATCTCT, TCACG ve TCTCG örüntülerinin arama zamanları hesaplanacaktır.
#Örüntü aramaları Shift AND ve FM index ile yapılacaktır.
#Her iki algoritmanın arama ve önişleme süreleri kıyaslanacaktır.
import timeit


def arama(text, pattern):

    begin = 0
    end = len(text)
    for c in pattern[::-1]:
        offset = text.rank_lt(c)
        if offset is None:
            begin, end = None, None
            break
        begin = offset + text.rank(c, begin)
        end = offset + text.rank(c, end)
        if begin >= end:  # no results
            begin, end = None, None
            break
    print('[bwt] (begin, end)', begin, end)
    match = []
    if begin is not None and end is not None:
        for i in range(begin, end):
            match.append((text.sa[i], text.sa[i] + len(pattern)))
    return match















fh = open('gene.fna')
text= fh.read()
pattern = ['GAATTCATTTCTCCCGCTGCCCCATCTCT','TCACG','TCTCG']

for x in range(3):
    arama(pattern[x], text)
    print('*************** ')


print(timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))
