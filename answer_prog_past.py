import time

while True:
    time.sleep(1)

    present = input('動詞を入力してネ>')

    if (present == 'OK'):
        print('またね～')
        break
    
    ## 現在分詞を作る ##
    
    # 例外的に扱う動詞⑥
    prog = ''
    if present == 'visit' or\
       present == 'limit' or\
       present == 'play' or\
       present == 'enjoy' or\
       present == 'listen' or\
       present == 'see' or\
       present == 'dye' or\
       present == 'enter':
        prog = present + 'ing'

    # ieで終わる語はieを取ってyingにする①
    elif present[-2:] == 'ie':
        prog = present.replace(present[-2:], 'ying')

    # eで終わる語はeを取ってingを付ける②
    elif present[-1] == 'e':
        prog = present.replace(present[-1], 'ing')
        
    # cで終わる語はkingを付ける③
    elif present[-1] == 'c':
        prog = present + 'king'
        
    # 「長母音＋子音」は原形にingを付ける 先に書かないといけない④
    elif (present[-3] == 'a' or \
          present[-3] == 'i' or \
          present[-3] == 'u' or \
          present[-3] == 'e' or \
          present[-3] == 'o') and\
         (present[-2] == 'a' or \
          present[-2] == 'i' or \
          present[-2] == 'u' or \
          present[-2] == 'e' or \
          present[-2] == 'o'):
        prog = present + 'ing'

    # 「短母音＋ 子音」は子音字を重ねてingを付ける⑤
    elif present[-2] == 'a' or \
         present[-2] == 'i' or \
         present[-2] == 'u' or \
         present[-2] == 'e' or \
         present[-2] == 'o':
        prog = present + present[-1] + 'ing'
    # どれにも一致しない⑦
    else:
        prog = present + 'ing'
    print('現在分詞はコレ->' + prog)




    ## 過去形を作る ##

    past = ''
    # 例外的に扱う動詞⑦
    if present == 'visit' or\
       present == 'limit' or\
       present == 'play' or\
       present == 'enjoy' or\
       present == 'listen' or\
       present == 'enter':
        past = present + 'ed'

    # 例外的に扱う動詞⑧
    elif present == 'dye':
        past = present + 'd'

    # 不規則動詞
    elif present == 'get':
        past = 'got-got'

    # 不規則動詞
    elif present == 'run':
        past = 'ran-run'

    # 不規則動詞
    elif present == 'swim':
        past = 'swam-swumt'

    # 不規則動詞
    elif present == 'begin':
        past = 'began-begun'

    # 不規則動詞
    elif present == 'read':
        past = 'read-read'
        
    # e で終わる語はdを付ける①
    elif present[-1] == 'e':
        past = present + 'd'

    # 語尾がpで終わる動詞②
    elif present[-1:] == 'p':
        # 語尾が「母音＋p」）で終わる場合はpを加えてからedを付ける
        if present[-2] == 'a' or \
           present[-2] == 'i' or \
           present[-2] == 'u' or \
           present[-2] == 'e' or \
           present[-2] == 'o':
            past = present + 'ped'
        # それ以外はedのみを付ける
        else:
            past = present + 'ed'

    # 語尾がyで終わる動詞③
    elif present[-1:] == 'y':
        # 語尾が「母音+y」で終わる場合はedのみを付ける
        if present[-2] == 'a' or \
           present[-2] == 'i' or \
           present[-2] == 'u' or \
           present[-2] == 'e' or \
           present[-2] == 'o':
            past = present + 'ed'
        # それ以外はyをiに変えてedを付ける
        else:
            past = present.replace(present[-1], 'ied')

    # cで終わる動詞はkを加えてからedを付ける④
    elif present[-1] == 'c':
        past = present + 'ked'

    # ir、er、urで終わる動詞は最後の子音を加えてからedを付ける⑤
    elif present[-2:] == 'ir' or \
         present[-2:] == 'er' or \
         present[-2:] == 'ur':
        past = present + present[-1] + 'ed'

    # 「長母音＋子音」はedを付ける⑥
    elif (present[-3] == 'a' or \
          present[-3] == 'i' or \
          present[-3] == 'u' or \
          present[-3] == 'e' or \
          present[-3] == 'o') and\
         (present[-2] == 'a' or \
          present[-2] == 'i' or \
          present[-2] == 'u' or \
          present[-2] == 'e' or \
          present[-2] == 'o'):
        past = present + 'ed'

    
    # 「母音＋ 子音」は子音字を重ねてedを付ける⑦
    elif present[-2] == 'a' or \
         present[-2] == 'i' or \
         present[-2] == 'u' or \
         present[-2] == 'e' or \
         present[-2] == 'o':
        past = present + present[-1] + 'ed'


    # どれにも当てはまらない場合はedを付ける⑩
    else:
        past = present + 'ed'


    print('過去形はコレ  ->' + past)

