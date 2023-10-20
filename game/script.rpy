# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.

define m = Character(color="#00008B")
define g = Character("Geo", color="#DC143C") 

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:
    $ i=0
    $ avtaz=0
    scene sky

    m "Еще один день"

    m "Снова ехать на пары на автаз "

    scene t81

    m "т81 наконец приехала"

    m "О нет, она как обычно переполнена"

    menu:
        "поехать на ней":
            $ i+=1
            jump t81_later
        "подождать следующую":

            scene sky
            m "Еще есть шанс не опаздать"
            scene t81
            m "Ого, как быстро"

            menu:
                "поехать на ней":
                    $ i+=1
                    jump t81_later
                "подождать следующую":
                    $ i=i-1
                    scene sky
                    m "пу пу пу"
                    scene t81
                    m "отсылка на полезай в т81"

                    menu:
                        "поехать на ней":
                            jump t81_later
                        "поехать на ней":
                            jump t81_later
        
        "поехать на метро":
            $ i=i-1
            m "я точно опаздаю"
            jump hse

    return
label t81_later:
    scene bus
    m "а"
    jump hse

    return


label hse:
    scene hse_sec
    m "Наконец я доехал до корпуса"
    m "Так, нужно достать пропуск"
    m "......"
    m "Кажется я его забыл"
    menu:
        "Договориться со студентом и пройти по чужому пропуску":
            $i+=1
            jump bench
        "Договориться с охранником":
            jump bench

    return
label bench:
    scene bench
    show geo
    m "курилка"
    g "у меня сейчас нет пары, посидишь со мной?"
    menu:
        "Давай":
            $avtaz+=1
            g "рассказ про автаз"
            jump para_1
        "Нет, мне пора":
            jump para_1
            
    
    return
label para_1:
    return