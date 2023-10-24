define m = Character(color="#00008B")
define g = Character("Geo", color="#d0143a") 


label start:
    $ good=0
    $ bad=0
    $ avtaz=0
    $ crow=0
    $ geo=0
    scene sky
    m "еще один день"
    m "снова ехать на пары на автаз "
    scene t81
    m "т81 наконец приехала"
    m "о нет, она как обычно переполнена"
    menu:
        "поехать на ней":
            $ good+=1
            jump t81_later
        "подождать следующую":
            scene sky
            m "еще есть шанс не опаздать"
            scene t81
            m "ого, как быстро"
            menu:
                "поехать на ней":
                    $ good+=1
                    jump t81_later
                "подождать следующую":
                    $ bad+=1
                    scene sky
                    m "пу пу пу"
                    scene t81
                    m "отсылка на полезай в т81"
                    menu:
                        "поехать на ней":
                            pass
                        "поехать на ней":
                            pass
                    jump t81_later
        "поехать на метро":
            $ bad+=1
            m "я точно опаздаю"
            jump hse
    return
label t81_later:
    scene bus
    m "пупупу"
    jump hse
    return
label hse:
    scene hse_ent
    m "наконец я доехал до корпуса"
    scene hse_sec
    m "так, нужно достать пропуск"
    m "......"
    m "кажется я его забыл"
    menu:
        "договориться со студентом и пройти по чужому пропуску":
            $ good+=1
        "договориться с охранником":
            $ bad+=1
    jump bench

    return
label bench:
    scene bench
    show geo
    m "курилка"
    g "у меня сейчас нет пары, посидишь со мной?"
    menu:
        "давай":
            $ avtaz+=1
            g "рассказ про автаз"
        "нет, мне пора":
            pass
    jump para_1 
    return
label para_1:
    scene para_1
    m "первая пара матан"
    m "следующая - дискра"
    m "но кажется на нее я не пойду"
    show crow
    m "а это еще кто"
    menu:
        "пойти за ней":
            m "ну пошли вместе"
            $ crow+=1
            jump tur_crow
        "проигнорировать":
            m "пойду-ка я отсюда"
            jump tur_alone
    return
label tur_crow:
    scene hse_k
    show crow at right
    m "пупупу"
    m "пора на линал"
    jump para_3
    return
label tur_alone:
    scene hse_k
    m "пупупу"
    m "пора на линал"
    jump para_3
    return
label para_3:
    scene para_3
    m "пупупу"
    m "хочется кушать, пора идти на поиски еды"
    menu:
        "булочка из пятерочки":
            scene five
            menu:
                "пойти в ближайшую":
                    m "тут слишком большая очередь, кажется я опаздаю на пару"
                    $ bad+=1
                "пойти через дорогу":
                    $ good+=1
                    m "булочка как булочка"
        "шаурма на львовке":
            scene shaurma
            $ avtaz+=1
            m "шаурма - всегда хорошая идея"
        "столовая":
            scene stolovka
            m "ну и чего я ожидал от столовой?"
    m "пора на матан"
    jump para_4
    return
label para_4:
    scene para_4
    m "*о нет, грязноков спросил именно меня, что делать*"
    if crow==1:
        menu:
            "попытаться ответить":
                menu:                    
                    "продолжить кринж ответ":
                        $ bad+=1
                    "остановиться":
                        pass
            "проигнорировать":
                $ bad+=1
            "рассказать о приключении с вороной": 
                $ good+=1
    else:
        menu:
            "попытаться ответить":
                menu:                    
                    "продолжить кринж ответ":
                        $ bad+=1
                    "остановиться":
                        pass
            "проигнорировать":
                    $ bad+=1
    m "пары наконец закончились, пойду ботать"
    jump coworking 
    return
label coworking:    
    scene coworking 
    m "что ботать"
    menu:
        "матан":
            pass
        "линал":
            pass
        "дискра":
            m "а зачем мне ботать дискру, если я на нее не хожу?"
    m "пора домой, пойду на остановку"
    jump bus_stop
    return
label bus_stop:
    scene bus_st
    m "судя по расписанию здесь т81 не останавливается"
    menu: 
        "отправиться на поиски другой остановки":
            show geo
            $ geo+=1
            g "о! пошли вместе на метро"
        "поехать на метро":
            pass
        "пойти гулять по автазу":
            $ avtaz+=1
            scene avtaz1
            scene avtaz2
            scene avtaz3
            m "все же пора домой, как раз метро рядом"
    m "что-то пришло на корпоративную почту"
    m "нужно прислать дз по матану и линалу"
    menu:
        "отправить матан и линал":
            $ good+=1
        "отправить дискру":
            $ bad+=1
    jump metro
    return
label metro:
    scene metro
    show geo  
    if geo==0:
        g "hi"
    g "рассказ про Мончагу"
    g "сигарету?"
    menu:
        "согласиться":
            $ good+=1
        "отказаться":
            $ bad+=1
        "расспросить о Мончаге":
            $ avtaz+=1
    jump end
    return
label end:
    if (good>=bad) and avtaz<3:
        scene end1
        m "вы поехали домой на метро. у вас появился новый друг и вас не отчислили." #нужно сделать надписи концовки по центру экрана
        return
    if (good<bad) and avtaz<3:
        scene end2
        m "вы поехали домой на метро. вам позвонили из учебного офиса: вас отчислили."
        return
    if avtaz>=3:
        scene end3
        m "вы с новым другом отправились в Мончагу"
        m "на друга напал маньяк"
        menu: 
            "убежать":
                m "вашего друга зарезали, из-за угла появилась полиция и вас отправили за решетку"
            "вмешаться":
                m "к вам на помощь прибежали жители автаза. вы отбились от маньяка. теперь вы герой автаза"
        return
