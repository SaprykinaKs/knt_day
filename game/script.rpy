﻿define m = Character(color="#E6E6FA")
define main = Character ("Я", color="#E6E6FA")
define g = Character("Студент", color="#d0143a") 
define DEFENDER = Character ("Охранник", color="#1E90FF")


label start:
    $ good=0
    $ bad=0
    $ avtaz=0
    $ crow=0
    $ geo=0
    $ late_t81=0
    $ late_DEFENDER=0
    $ d=0
    $ late=0
    $ matan=0

    scene sky with fade

    m "Утро. {w} Какой прекрасный сегодня день."
    m "Нет никаких сожалений, невзгод и заполненных т81…"

    scene t81

    m "Где я…? {w} Что произошло…?"
    m "Ах, ну конечно. {w} Обычный учебный день, обычное серое небо и обычная, наполовину погибшая от бесконечного потока людей т81."
    m "А вот и она…"

    menu:
        "Поехать на ней":

            m "Да начнутся приключения!"

            $ good+=1
            jump t81_later
            
        "Подождать следующую":

            m "Пожалуй, я могу подождать следующую…"

            scene sky

            m "Еще есть шанс не опоздать..."

            scene t81

            menu:
                "Ситуация лучше не стала, но я хотя бы все еще не опаздываю…":

                    $ good+=1
                    jump t81_later

                "Нет, я не хочу…":

                    $ bad+=1
                    $ late+=1

                    scene sky

                    m "..."
                    m "И все-таки у меня больше нет времени. {w} Придется принять суровую реальность…"

                    scene t81

                    menu:

                        "Поехать на ней":
                            pass
                        "Поехать на ней":
                            pass

                    $ late_t81+=1
                    jump t81_later

        "Поехать на метро":

            m "Нет уж, я себя уважаю и не поеду на этом."

            scene sky

            $ bad+=1
            $ late+=1

            m "Это было неплохо, но стоило ли это того, чтобы я опоздал на пару?"
            m "Ладно уж."
            m "Ничего уже не изменить."

            jump hse
    return
label t81_later:

    scene bus

    m "Жизнь полна разочарований {w}и одно из них – т81."
    if late_t81==1:
        m "Между тем я еще и опаздываю."

    jump hse
    return
label hse:

    scene hse_ent with fade

    m "Наконец я доехал до корпуса."
    m "Если существует проход в преисподнюю, то он находится здесь…"

    scene hse_sec 

    m "Так. {w} Где моя волшебная карта?"
    m "Этот цербер скоро насквозь прожжет меня взглядом."
    m "Эм."
    m ".{w}.{w}."
    m "Кажется, я забыл пропуск дома…"

    menu:
        "Договориться со студентом и пройти по чужому пропуску":

            m "Выйду-ка я на улицу и по старинке отыщу доброго человека…"
            m "Ловкость рук в этом деле еще никогда не подводила меня."

            $ good+=1

        "Договориться с охранником":

            main "Извините…"
            DEFENDER "Что?"
            main "Я забыл пропуск, не могли бы вы меня впустить…"
            m "..."
            m "Это было долго и мучительно, но все-таки он пропустил меня."
            m "Благо у меня оказался с собой студенческий."
            m "Почему у меня он был, а пропуск остался дома?"
            m "..."
            m "История умалчивает."
            
            $ bad+=1
            $ late_DEFENDER+=1
            $ late+=1
            
    jump bench
    return
label bench:

    scene bench with fade
    
    if late_DEFENDER==1:
        m "Опаздывать мне не в первой…"
    m "Это место легендарно.{w} Вся элита и весь сброд собирается в одном месте после пары, чтобы сбросить напряжение…"
    if late_DEFENDER==0:
        m "Но сейчас всеобщая печаль развеяна, ведь пара уже началась."
    if late_DEFENDER==1:
        "Но сейчас всеобщая печаль развеяна, ведь пара уже давно идет."
    m "…"
    m "Но что-то не так.{w} Я вижу нечто, подающее признаки жизни…"
    m "Незнакомый студент одиноко сидит на скамейке."
    show geo_neutral with fade
    menu:
        "Поговорю-ка я с ним…":
            main "Привет, а ты почему сидишь сейчас здесь?"
            show geo_speaking
            g "Таков путь."
            main "А…?"
            g "Мою пару отменили, и я коротаю время до следующей."
            hide geo_speaking
            main "…"
            show geo_speaking
            g "Слушай, студент."
            main "Чего?"
            g "Я вижу ты в наших рядах новенький."
            g "Я бы посоветовал тебе пойти на пары, у тебя то они хотя бы есть."
            hide geo_speaking
            menu:
                "Куда я вообще попал?":
                    $ avtaz+=1
                    show geo_speaking    
                    g "Это проклятое место – район Автозаводский.{w} В простонародье – автаз."
                    hide geo_speaking
                    g "Здесь обитают подобия людей, которых изрядно потрепала нелегкая жизнь."
                    g "Дома здесь бесконечно серы, как и небо."
                    show geo_speaking
                    g "Согласись, не найдешь прекраснее места для того, чтобы поставить корпус одного из лучших вузов этой страны."
                    g "Ладно, иди своей дорогой, студент. {w}Может быть, судьба еще однажды сведет нас."
                    hide geo_speaking
                    jump para_1
                "В другой раз":
                    pass    
        "В другой раз":
            pass
    jump para_1 
    return
label para_1:
    scene para_1 with fade
    m "Первая пара – лекция по программированию."
    m "Я думал о том, чтобы поспать, но бесконечные упоминания абстракции вызывали во мне неприятные воспоминания."
    scene hse_cor
    m "Пара завершилась, и я вышел в коридор."
    m "Идти на следующую пару не хочется совсем."
    m "Тем более это дискретка, а об ее существовании я решил забыть вплоть до сессии, да и домашнее задание по ней никто не проверяет."
    m "..."
    m "Чем бы заняться?"
    m "Вопрос быстро отпал, когда я заметил ее…"
    show crow with fade
    m "Я вспомнил, что где-то слышал об этой вороне как о символе вышки."
    m "И. {w}Она выглядит ужасающе…"
    m "..."
    m "Но между тем так маняще…"
    menu:
        "Пойти за ней":
            $ crow+=1
            jump tur_crow
        "Проигнорировать":
            m "Пожалуй, жизнь мне еще дорога…"
            jump tur_alone
    return
label tur_crow:
    scene hse_k with fade
    show crow at right
    m "Произошло нечто удивительное и она показала мне корпус…"
    m "Если честно, я даже не знаю, что об этом и думать"
    m "Благо пара закончилась, и я могу пойти уже на третью."
    jump para_3
    return
label tur_alone:
    scene hse_k with fade
    m "Спустя час бесцельных блужданий по корпусу я вернулся к третьей паре."
    jump para_3
    return
label para_3:
    scene para_3 with fade
    m "На линале ничего не произошло."
    m "Ну. {w}Кроме того, что я вспомнил, что забыл позавтракать, и теперь мой живот бьет тревогу."
    m "Куда же мне сходить поесть сейчас?"
    menu:
        "Булочка из пятерочки":
            scene hse_k
            m "Классика. {w}Правда, здесь на квартал целых четыре пятерочки."
            m "Те, что справа по курсу, мне не импонируют."
            m "Значит выбор между двумя оставшимися."
            m "Если пойду в ближайшую, велик шанс опоздать.{w} Но…"
            menu:
                "Пойти в ближайшую":
                    m "Пятерочка, битком забитая людьми и всего лишь с одной работающей кассой – главный спонсор моих опозданий."
                    $ bad+=1
                    $ late+=1
                    jump para_4
                "Пойти через дорогу":
                    $ good+=1
                    m "Я больше не хочу опаздывать, так что не буду рисковать."
                    jump para_4
        "Шаурма на львовке":
            scene shaurma
            $ avtaz+=1
            m "Говорят крутости этой шаурме нет предела."
            m "Думаю, стоит оценить.{w} Так сказать, проникнуться духом этого места."
            jump para_4
        "Столовая":
            scene stolovka
            m "Банально, но сейчас нет желания придумывать ничего необычного."
            jump para_4
    return
label para_4:
    scene para_4 with fade
    m "Последняя пара – матан…"
    m "Хочу просто отсидеть ее, ни о чем не думая."
    m "..."
    m "Спустя несколько фраз я осознал, что препод обращается ко мне…"
    m "Наш препод, Грязняков, - гроза матанализа."
    m "Что же мне делать? Его явно не стоит злить."
    if crow==1:
        menu:
            "Попытаться ответить":
                main "Эм. Эээээ. Для любого эпсилон больше нуля…"
                m "Дальше я безудержно начал нести полный бред."
                menu:                    
                    "Продолжить ответ":
                        m "Он попросил меня прекратить нести чушь. Зря я вообще это начал…"
                        $ bad+=1
                    "Остановиться":
                        m "Я решил прекратить и принять поражение."
                        pass
            "Проигнорировать":
                m "Я проигнорировал его и он отстал, но ему явно не понравилось мое поведение…"
                $ bad+=1
            "Рассказать о приключении с вороной": 
                m "Ему показалась забавной моя история, и он перестал меня спрашивать."
                m "Не знаю, откуда появилась эта ворона, но если мне удастся повстречать ее еще раз, то я должен ее поблагодарить."
                $ good+=1
    else:
        menu:
            "Попытаться ответить":
                main "Эм. Эээээ. Для любого эпсилон больше нуля…"
                m "Дальше я безудержно начал нести полный бред."
                menu:                    
                    "Продолжить ответ":
                        m "Он попросил меня прекратить нести чушь. Зря я вообще это начал…"
                        $ bad+=1
                    "Остановиться":
                        m "Я решил прекратить и принять поражение."
                        pass
            "Проигнорировать":
                m "Я проигнорировал его и он отстал, но ему явно не понравилось мое поведение…"
                $ bad+=1
    scene hse_cor with fade
    m "Я смог пережить все пары и даже остался цел."
    m "Дальше меня ждет путешествие в боталку с целью сделать домашку…"
    jump coworking 
    return
label coworking:    
    scene coworking with fade 
    m "Все сделать я не успею, так что вновь придется выбирать."
    menu:
        "Матан":
            $ good+=1
            pass
        "Линал":
            $ good+=1
            pass
        "Дискра":
            $ bad+=1
            $ d+=1
    m "Что-то да сделать я успел, пожалуй, закончу на этом."
    jump bus_stop
    return
label bus_stop:
    scene bus_st with fade
    m "На сегодня все. {w}Самое время возвращаться домой."
    m "…"
    m "Так…"
    m "А почему автобусы больше не ходят от этой остановки? {w}Видимо, какая-то авария…"
    m "В любом случае мне это не на руку."
    m "Что же делать?"
    menu: 
        "Отправиться на поиски другой остановки":
            m "Думаю, другого выбора нет."
            scene bus_st with fade
            m "Кажется, я вижу знакомое лицо."
            show geo_neutral
            $ geo+=1
            main "Прив…"
            show geo_speaking
            g "Так или иначе мы уже виделись."
            main "Тоже пытаешься покинуть это место?"
            g "Да, и пока безуспешно."
            g "Я думаю дойти до метро и не думаю, что у тебя есть выбор лучше, чем пойти со мной."
            show geo_speaking
            main "Пожалуй, ты прав…"
        "Пойти гулять по автазу":
            $ avtaz+=1
            scene avtaz1
            m "Пожалуй, мне стоит ознакомиться с этим районом."
            scene avtaz2
            m "Пройдусь немного, а затем сразу на метро."
    hide geo_speaking
    hide geo_neutral
    m "..."
    m "Что-то пришло на корпоративную почту."
    m "Письма… Они могу нести в себе как счастье, так и бесконечную печаль."
    m "В этот раз меня просят отправить что-то из домашки. {w}Линал или матан…"
    m "Отправлю то, что сделал сегодня."
    if d==1:
        "Кто-нибудь объяснит мне, зачем я делал дискретку?"

    jump metro
    return
label metro:
    scene metro
    if geo==0:
        m "Моя прогулка подошла к концу."
        m "Я думал о том, чтобы просто уехать домой, как вдруг заметил знакомое лицо…"
        show geo_neutral with fade
        main "Прив…"
        g "Виделись."
        show geo_speaking
        main "..."
        hide geo_speaking
        g "Пойти сюда было верным решением с твоей стороны."
        show geo_speaking
    show geo_neutral
    show geo_speaking
    g "Это единственный нормальный способ сейчас выбраться из этого проклятого места."
    g "Хотя это место еще не так проклято, как некоторые другие."
    g "Эх, Мончага… Достойный повод закурить."
    hide geo_speaking
    main "..."
    show geo_speaking
    g "Будешь?"
    menu:
        "Согласиться":
            hide geo_speaking
            main "Да, пожалуй."
            show geo_speaking
            g "А ты, паренёк, не промах."
            $ good+=1
        "Отказаться":
            hide geo_speaking
            main "Воздержусь."
            show geo_speaking
            g "Грустно. Сейчас был самый повод."
            g "Не выжить тебе так в этих краях, студент."
            $ bad+=1
        "Расспросить о Мончаге":
            hide geo_speaking
            main "Лучше поведай мне об этой Мончаге."
            show geo_speaking
            g "Интересный вопрос задаёшь."
            g "Такое лучше один раз увидеть, и все сразу станет понятно."
            $ avtaz+=1
    hide geo_speaking
    hide geo_neutral
    jump end
    return
label end:
    if (good>=bad) and avtaz<3:
        scene ending with fade
        m "Ладно, пожалуй, это действительно все." #нужно сделать надписи концовки по центру экрана
        m "…"
        m "Я попрощался со своим новым знакомым и отправился домой."
        m "Вот так и закончился очередной день без отчисления…"
        window hide
        scene end1
        pause
        return
    if (good<bad) and avtaz<3:
        scene ending with fade
        m "Ладно, пожалуй, это действительно все."
        m "…"
        m "Я отправился домой."
        m "…"
        m "Дома меня ждала страшная новость…"
        if late>1:
            m "Мои опоздания уже всем надоели..."
        if matan==1:
            m "На меня пожаловался Грязняков..."
        if d==1:
            m "Я не сдал домашку…"
        m "…"
        m "Меня отчислили."
        window hide
        scene end2
        return
    if avtaz>=3:
        scene ending with fade
        m "Ладно, пожалуй, это действительно все."
        m "..."
        m "Или нет?"
        scene monchaga
        main "Я хочу отправиться дальше исследовать это место."
        show geo_neutral
        show geo_speaking
        g "Ооо, так тебя манит автаз?"
        g "Ну что же, давай я покажу тебе все прелести этого места."
        hide geo_speaking
        hide geo_neutral
        m "Вместе с моим новым другом мы отправились в Мончагу…"
        m "Уже почти ночь на дворе. {w}Темно. {w}Я ощущаю присутствие призраков автаза…"
        m "Или это не призраки…?"
        m "Вдруг из-за угла показывается темный силуэт…"
        show maniac_neutral
        m "Чччччто у него руках??!"
        m "Это был нож…"
        show maniac_attack
        m "Он побежал с ним на моего нового друга."
        menu: 
            "Убежать":
                hide maniac_neutral
                m "Нет…{w} ОН ПЫРНУЛ МОЕГО ДРУГА."
                m "..."
                hide maniac_attack
                m "Как только я захотел бежать, маньяк уже скрылся в подворотне."
                m "..."
                m "Я слышу звуки сирены… {w}Мигалки…"
                m "Они начинают подходить ко мне, а затем валят на пол."
                m "Это что же такое получается…"
                m "Неужели меня ждет такой конец…?"
                window hide
                pause
                scene end3 with fade
            "Вмешаться":
                hide maniac_neutral
                m "Я должен вмешаться."
                m "Без промедления я подбегаю к маньяку, и мне удается блокировать его удар."
                hide maniac_attack
                m "На крик о помощи сбегаются местные жители."
                m "Мы окружаем его, и маньяку ничего не остается, кроме как сдаться."
                m "…"
                m "После того как все закончилось, все стали благодарить меня за помощь в поимке маньяка."
                m "Меня стали называть героем. \n{w}Героем автаза…"
                window hide
                pause
                scene end4 with fade
        return
