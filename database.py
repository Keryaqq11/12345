import sqlite3


connection = sqlite3.connect("database.sqlite")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS brawler")


request = ("CREATE TABLE IF NOT  EXISTS brawler"
           "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
           "name VARCHAR(255),"
           "rares VARCHAR(255),"
           "description VARCHAR(255),"
           "hp INTEGER,"
           "yron INTEGER,"
           "photo VARCHAR(255),"
           "build_icon1 VARCHAR(255),"
           "build_icon2 VARCHAR(255),"
           "build_icon3 VARCHAR(255),"
           "build_icon4 VARCHAR(255),"
           "hypercharge VARCHAR(255))")
cursor.execute(request)

insert_request = "INSERT INTO brawler" "(name, rares, description, hp, yron, photo, build_icon1, build_icon2, build_icon3, build_icon4, hypercharge) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

cursor.execute(insert_request, ("Шелли", "common", "Шелли — идеальный рейнджер. Она ответственная, выносливая и непревзойдённо обращается с ружьём, и ей непонятно, как Кольт перетянул всё внимание на себя", "7400", "600", "Shelly.webp", "1.webp", "gadget1.webp", "yron.webp", "dop.webp", "yes"))
cursor.execute(insert_request, ("Нита", "rare", "Нита — совсем малышка, но рвётся в бой с недетской яростью! Её шапка в виде плюшевого мишки как бы намекает: не будите спящего медведя", "8000", "1920", "Nita.webp", "2.png", "22.webp", "compan.png", "yron.webp", "yes"))
cursor.execute(insert_request, ("Кольт", "rare", "Кольт — настоящая звезда парка Старр! Его стиль, обаяние и трюки с пистолетами покорят любого (за исключением Шелли)", "5600", "720", "colt.webp", "3.jpg", "33.webp", "reload.jpg", "dop.webp", "yes"))
cursor.execute(insert_request, ("Булл", "rare", "Булл уже не такой бесшабашный, как в юности, но это ещё не значит, что он не наваляет любому, кто явно напрашивается", "10000", "880", "bull.webp", "6.webp", "66.webp", "dop.webp", "zaryad_supera.webp", "yes"))
cursor.execute(insert_request, ("Брок", "rare", "Брок — геймер и тролль. Вообще-то он романтичный интроверт, но ради победы он готов выйти из зоны комфорта", "5400", "2320", "Brok.webp", "5.webp", "55.webp", "shit.png", "reload.jpg", "yes"))
cursor.execute(insert_request, ("Эль Примо", "rare", "Эль Примо всегда в центре внимания, и он это просто обожает! Публика в восторге от него, а вот коллеги – не очень", "12000", "760", "el_primo.webp", "4.webp", "44.webp", "hit.png", "yron.webp", "yes"))
cursor.execute(insert_request, ("Барли", "rare", "Барли — робот для приготовления напитков и разговоров с посетителями. Он помешан на чистоте, и это сразу поймёт любой, кто прольёт напиток на его барную стойку", "4800", "1600", "Barli.webp", "8.webp", "88.webp", "dop.webp", "shit.png", "yes"))
cursor.execute(insert_request, ("Поко", "rare", "Поко верит в чудотворную силу музыки и так любит свою гитару, что ни на минуту не прекращает играть. Даже когда его очень просят", "7400", "1520", "Poco.webp", "7.webp", "77.webp", "dop.webp", "yron.webp", "yes"))
cursor.execute(insert_request, ("Роза", "rare", "Роза одинаково увлекается и ботаникой, и боксом. Она обожает свой сад, но если какое-то растение обнаглеет, то получит и по вершкам, и по корешкам", "10000", "920", "Rosa.webp", "9.webp", "99.webp", "yron.webp", "speed.webp", "yes"))
cursor.execute(insert_request, ("Джесси", "superrare", "Джесси — изобретательница-вундеркинд. Она мастерит оружие и гаджеты из хлама, чтобы доказать своей матери Пэм, что может постоять за себя", "6000", "2120", "Jessi.webp", "10.webp", "1010.webp", "dop.webp", "compan.png", "yes"))
cursor.execute(insert_request, ("Диномайк", "superrare", "Динамайк — старый шахтёр и золотоискатель, который обожает всё взрывать. Ничто не радует его так, как запах дыма и грохот камней!", "5600", "1600", "Dino.webp", "11.webp", "1111.webp", "dop.webp", "yron.webp", "yes"))
cursor.execute(insert_request, ("Тик", "superrare", "Тик хвостиком ходит за Пенни и участвует во всех её затеях. Единственное, что он умеет — это взрывать всё вокруг, но другого от него обычно и не требуется", "4400", "1280", "Tic.webp", "12.webp", "1212.webp", "dop.webp", "tickm.webp", "yes"))
cursor.execute(insert_request, ("8-бит", "superrare", "8-БИТ — игровой автомат, ненавидящий игроков. Всё потому, что однажды кто-то разозлился из-за проигрыша и украл один из его пистолетов", "10000", "640", "Bit.webp", "13.webp", "1313.webp", "dop.webp", "yron.webp", "yes"))
cursor.execute(insert_request, ("Рико", "superrare", "Рико — совершенно точно самый настоящий межгалактический охотник за головами, а не автомат со жвачкой, который пытается круто выглядеть", "5600", "640", "Rico.webp", "14.webp", "1414.webp", "dop.webp", "reload.jpg", "yes"))
cursor.execute(insert_request, ("Дэррил", "superrare", "Дэррил пошёл в пираты, потому что устал работать, но теперь ему приходится вкалывать ещё больше, защищая корабль. Какая ирония", "10600", "480", "derril.webp", "15.webp", "1515.webp", "hil.png", "yron.webp", "yes"))
cursor.execute(insert_request, ("Пенни", "superrare", "Пенни не разбирается в старых картах и морских легендах. Быть пираткой для неё означает палить из пушек и брать всё, что приглянулось!", "6400", "1960", "Penni.webp", "16.webp", "1616.webp", "shit.webp", "yron.webp", "yes"))
cursor.execute(insert_request, ("Карл", "superrare", "Карл — робот-шахтёр, который без ума от камней и горных пород, а в последнее время серьёзно увлёкся изучением кристаллов!", "8000", "1480", "Carl.webp", "17.webp", "1717.webp", "dop.webp", "yron.webp", "no"))
cursor.execute(insert_request, ("Джеки", "superrare", "Джеки любит рассказывать всякие байки из своей шахтёрской жизни, не стесняясь в выражениях. К счастью, шум отбойного молотка заглушает ругательства", "10000", "2480", "Jeki.webp", "18.webp", "1818.webp", "hil.png", "yron.webp", "yes"))
cursor.execute(insert_request, ("Гас", "superrare", "Малыш Гас такой бледный, что его часто принимают за привидение. Впрочем, ему это нравится, ведь он обожает всё жуткое и сверхъестественное", "6400", "2240", "Gas.webp", "19.webp", "1919.webp", "dop.webp", "yron.webp", "no"))
cursor.execute(insert_request, ("Бо", "Epic", "Бо уже долгое время выживает в джунглях. Впечатляет, учитывая, что у него при себе нет ничего, кроме игрушек из магазина сувениров", "7200", "1280", "Bo.webp", "20.webp", "2020.webp", "dop.webp", "yron.webp", "no"))
cursor.execute(insert_request, ("Эмз", "Epic", "Вообще-то Эмз работает в морге у своего дяди Мортиса, но редко там появляется. Она слишком занята рекламой своего бренда лака для волос.", "7200", "1040", "Emz.webp", "21.webp", "2121.webp", "dop.webp", "yron.webp", "yes"))
cursor.execute(insert_request, ("Сту", "Epic", "За свою карьеру каскадёра Сту пережил столько ударов и падений и так надышался бензином, что просто удивительно, как он вообще держится на колёсах.", "6400", "1080", "Stu.webp", "222.webp", "2222.webp", "shit.png", "yron.webp", "yes"))
cursor.execute(insert_request, ("Пайпер", "Epic", "Пайпер мечтает открыть пекарню и торговать пирожными, печеньем и другими сладостями. Только не стоит спрашивать её о прошлом, иначе можно очутиться в духовке.", "4600", "3400", "Piper.webp", "233.webp", "2323.webp", "dop.webp", "shit.png", "yes"))
cursor.execute(insert_request, ("Пем", "Epic", "Пэм целыми днями сортирует мусор на свалке. Она отличный работник, но у неё совсем не остаётся времени на родную дочь Джесси.", "9600", "520", "Pem.webp", "244.webp", "2424.webp", "dop.webp", "Pemmm.webp", "no"))
cursor.execute(insert_request, ("Френк", "Epic", "Фрэнк — добродушный великан, который днём работает помощником в морге, а ночью — диджеем в клубе. По нему заметно, что он не высыпается", "13400", "2320", "Frank.webp", "255.webp", "2525.webp", "hil.png", "dop.webp", "yes"))
cursor.execute(insert_request, ("Биби", "Epic", "Биби выглядит как хулиганка и ходит с битой наперевес. Вообще-то она любит читать, но никогда не признается в этом, чтобы не испортить себе репутацию", "9600", "2800", "Bibi.webp", "266.webp", "2626.webp", "dop.webp", "yron.webp", "yes"))
cursor.execute(insert_request, ("Беа", "Epic", "Беа целыми днями наблюдает за разными букашками, представляя, как круто было бы понимать их язык... или даже быть одной из них", "5000", "1600-4400", "Bea.webp", "277.webp", "2727.webp", "shit.png", "yron.webp", "no"))
cursor.execute(insert_request, ("Нани", "Epic", "Нани была простой камерой видеонаблюдения, пока её не модифицировали, чтобы присматривать за Джесси. К сожалению, она не всегда успевает угнаться за подопечной", "4800", "1480", "Nani.webp", "288.webp", "2828.webp", "dop.webp", "yron.webp", "yes"))
cursor.execute(insert_request, ("Эдгар", "Epic", "Эдгара бесит, что его никто не понимает, особенно мама, которая уверена, что это просто переходный возраст. Разве она не видит, что в его душе царит вечная тьма?!", "6600", "1080", "Edgar.webp", "299.webp", "2929.webp", "dop.webp", "yron.webp", "yes"))
cursor.execute(insert_request, ("Анджело", "Epic", "Купидон Анджело обернулся комаром и поселился на болоте. Он кружит по каналам в поисках гуляющих парочек, по привычке сражая их если не своим чарующим обаянием, то стрелами.", "6000", "4000", "angelo.webp", "30.webp", "3030.webp", "dop.webp", "yron.webp", "yes"))
cursor.execute(insert_request, ("Менди", "Epic", "Мэнди управляет магазином сладостей, облачившись в наряд конфетной королевы. Иногда она немного увлекается и ведёт себя, как настоящий деспот.", "5600", "2600", "mandy.webp", "31.webp", "3131.webp", "shit.png", "yron.webp", "no"))
cursor.execute(insert_request, ("Коллет", "Epic", "У Колетт есть плакаты и фигурки всех бойцов Brawl Stars. Можно ли назвать её одержимой фанаткой? Да. Но окончательно ли она сошла с ума? Тоже да.", "6800", "1000", "collet.webp", "32.webp", "3232.webp", "dop.webp", "yron.webp", "yes"))
cursor.execute(insert_request, ("Ларри и Лори", "Epic", "Ларри и Лори — билетёры в парке Старр. Ларри любит правила за то, что они упрощают жизнь, а Лори просто любит усложнять жизнь другим. Они отличная команда.", "5600", "1400", "l2l.webp", "333.webp", "3333.webp", "dop.webp", "yron.webp", "no"))
cursor.execute(insert_request, ("Мейси", "Epic", "Мэйси работает координатором по технике безопасности, но на самом деле ей нравится рисковать. Иногда она как будто нарочно создаёт опасные ситуации...", "7200", "3000", "meisi.webp", "34.webp", "3434.webp", "dop.webp", "yron.webp", "yes"))
cursor.execute(insert_request, ("Белль", "Epic", "Белль — глава банды Золотой руки. Она не только охотится за наживой, но и пытается выяснить всю правду о парке Старр, чтобы добиться его закрытия.", "5200", "2080", "bell.webp", "35.webp", "3535.webp", "yron.webp", "dop.webp", "yes"))
cursor.execute(insert_request, ("Берри", "Epic", "В кондитерской Мэнди вечно всё вверх дном, но Берри не спешит оттуда увольняться. Может показаться, что он ненавидит свою работу, но в конце смены на его лице появляется улыбка.", "5000", "1320", "berry.webp", "36.webp", "3636.webp", "yron.webp", "dop.webp", "yes"))
cursor.execute(insert_request, ("Грифф", "Epic", "«Грифф ведёт себя как успешный бизнесмен, но его магазин сувениров в шаге от банкротства, а сам он бегает от налоговых инспекторов.", "6800", "560", "grif.webp", "37.webp", "3737.webp", "yron.webp", "shit.png", "no"))
cursor.execute(insert_request, ("Бонни", "Epic", "Бонни переполняет безудержная и глубоко разрушительная энергия. Её главная мечта — чтобы ею выстрелили из пушки на Луну!", "9600", "2240", "bonni.webp", "38.webp", "3838.webp", "yron.webp", "dop.webp", "no"))
cursor.execute(insert_request, ("Пёрл", "Epic", "Вопреки всем ожиданиям, Перл удалось растопить суровые сердца Белль и Сэма своим душевным теплом. Да и кто устоит перед шоколадным печеньем?", "7800", "905", "perl.webp", "39.webp", "3939.webp", "yron.webp", "dop.webp", "yes"))
cursor.execute(insert_request, ("Гром", "Epic", "Гром — мощный здоровяк-охранник. Он боится лишь одного: что его уволят и ему придётся вернуться на работу в детском саду. Дети не знают пощады.", "5600", "2280", "grom.webp", "40.webp", "4040.webp", "yron.webp", "dop.webp", "no"))
cursor.execute(insert_request, ("Гейл", "Epic", "Гэйл ответственно относится к своим обязанностям по уборке снега вокруг зимнего отеля мистера П. и не прекращает работу, даже если на пути оказались гости", "7600", "560", "geyl.webp", "41.webp", "4141.webp", "yron.webp", "dop.webp", "yes"))
cursor.execute(insert_request, ("Лола", "Epic", "Лола умеет произвести на себя впечатление с порога. Она не стесняется устраивать скандалы, чтобы добиться своего, и гордится этим талантом!", "7600", "560 * 6", "lola.webp", "42.webp", "4242.webp", "yron.webp", "dop.webp", "no"))
cursor.execute(insert_request, ("Сем", "Epic", "Сэм — бывший фабричный рабочий, вступивший в банду Золотой руки. Он помогает Белль, прикрывая её во время ограблений!", "10800", "1600 * 2", "sem.webp", "43.webp", "4343.webp", "yron.webp", "dop.webp", "no"))
cursor.execute(insert_request, ("Хенк", "Epic", "Пусть Хэнк всего лишь креветка, но у него есть танк и благородная цель: вызволить всю морскую живность с рынков и кухонь мира. Повара, берегитесь!", "11200", "4200", "henk.webp", "444.webp", "4444.webp", "yron.webp", "hil.png", "no"))
cursor.execute(insert_request, ("Эш", "Epic", "Эш занимается самой грязной работой — уборкой парка. Мусорный бак служит ему доспехом, защищая от крысиных укусов и битого стекла, но не улучшает настроения.", "10800", "1600", "esh.webp", "45.webp", "4545.webp", "yron.webp", "dop.webp", "yes"))
cursor.execute(insert_request, ("Мортис", "Mythic", "Мортис мечтал о карьере гробовщика и по совместительству вампира, но его планам помешало то, что в парке Старр никто не умирает.", "7600", "2000", "mortis.webp", "46.webp", "4646.webp", "mort_myt.webp", "dop.webp", "yes"))
cursor.execute(insert_request, ("Тара", "Mythic", "Карты Тары предрекают тебе суровые испытания! Но не волнуйся, у неё полно волшебных талисманов, которые она готова продать по выгодной цене.", "6200", "960 * 3", "tara.webp", "47.webp", "4747.webp", "yron.webp", "dop.webp", "yes"))
cursor.execute(insert_request, ("Джин", "Mythic", "Глядя на Джина, многие видят просто маленького человечка в странном костюме. Но им стоит повнимательнее присмотреться к его чайнику. Или это лампа?..", "7200", "2000", "jin.webp", "48.webp", "4848.webp", "shit.png", "dop.webp", "yes"))
cursor.execute(insert_request, ("Макс", "Mythic", "Макс полна сил благодаря энергетическим напиткам. Она первая спешит на помощь, если кто-то в беде... Но часто так разгоняется, что пробегает мимо.", "6600", "640 * 4", "max.webp", "49.webp", "4949.webp", "yron.webp", "dop.webp", "yes"))
cursor.execute(insert_request, ("Мистер Пи", "Mythic", "Директор отеля мистер П. постоянно кричит и подгоняет своих сотрудников. Это не помогает — они вообще не понимают, что он говорит.", "6800", "1520", "mp.webp", "50.webp", "5050.webp", "petm.webp", "dop.webp", "no"))
cursor.execute(insert_request, ("Спраут", "Mythic", "Спраут выглядит как милый робот, помогающий Розе в «Биокуполе», но на самом деле это инкубатор на колёсах для странного розового семечка.", "6000", "2080", "sprout.webp", "51.webp", "5151.webp", "zaryad_supera.webp", "shit.png", "yes"))
cursor.execute(insert_request, ("Байрон", "Mythic", "Байрон изобрёл множество микстур и эликсиров, как целебных, так и ядовитых. Но в основном ядовитых. Да что уж там, почти все его зелья — страшная отрава.", "4800", "710 * 3", "byron.webp", "52.webp", "5252.webp", "shit.png", "dop.webp", "no"))
cursor.execute(insert_request, ("Сквик", "Mythic", "Скуик — ходячий сгусток позитива, обожающий своего создателя Гавса. Все его любят, по крайней мере, пока не поймут, что он сделан из собачьих слюней.", "7200", "2320", "sqwick.webp", "53.webp", "5353.webp", "shit.png", "dop.webp", "yes"))
cursor.execute(insert_request, ("Лу", "Mythic", "Лу — робот-автомат с мороженным, у которого никто ничего не покупает. Возможно, ему стоило бы спуститься с заснеженного горного пика, куда не добраться пешком.", "6400", "880 * 3", "lu.webp", "54.webp", "5454.webp", "shit.png", "dop.webp", "yes"))
cursor.execute(insert_request, ("Р-Т", "Mythic", "R-T задумывался, как стойка информации, но потом к его обязанностям добавилась слежка за всем, что происходит в парке Старр. Исключительно в целях безопасности.", "7800", "1400", "r-t.webp", "555.webp", "5555.webp", "yron.webp", "dop.webp", "no"))
cursor.execute(insert_request, ("Лили", "Mythic", "Тяга к запретным знаниям и чёрной магии привела Лили в зачарованный лес, где происшествие с участием светлячка и хищного растения навсегда изменило её жизнь.", "8200", "2120", "lily.webp", "56.webp", "5656.webp", "yron.webp", "dop.webp", "no"))
cursor.execute(insert_request, ("Базз", "Mythic", "Базз работает спасателем на водных аттракционах Велоцираптопарка и следит за соблюдением правил настолько строго, что это граничит с синдромом вахтёра", "9600", "840 * 5", "bazz.webp", "57.webp", "5757.webp", "yron.webp", "dop.webp", "yes"))
cursor.execute(insert_request, ("Бастер", "Mythic", "Бастер стащил проектор из кинотеатра, где подрабатывает механиком, и использует его в качестве реквизита, что не только опасно, но и непрофессионально!", "10000", "2760 * 3", "baster.webp", "58.webp", "5858.webp", "hil.png", "dop.webp", "no"))
cursor.execute(insert_request, ("Мелоди", "Mythic", "Когда дело касается караоке, Мелоди не знает пощады. Сочетание кавайного очарования с мощным голосом обеспечивает ей внимание зрителей.", "8200", "920", "melodie.webp", "59.webp", "5959.webp", "yron.webp", "dop.webp", "yes"))
cursor.execute(insert_request, ("Мико", "Mythic", "Мико работает звукооператором в Броуливуде, но его легко принять за знаменитость, учитывая, сколько он хвастается. У него крутой нрав, а вот чувства юмора нет, так что лучше не шути с ним!", "6600", "2180", "Miko.webp", "60.webp", "6060.webp", "yron.webp", "dop.webp", "yes"))
cursor.execute(insert_request, ("Мо", "Mythic", "Однажды Гром нашёл в канализации слепого крысёнка по имени Мо. Теперь Мо живёт у него и занимается обслуживанием парка Старр, передвигаясь под землёй на своём верном дырокопе. Мо верит, что однажды, его бур пронзит небеса, но пока он добавляет работы Эшу.", "6800", "1000 * 8", "mo.webp", "61.webp", "6161.webp", "yron.webp", "dop.webp", "no"))
cursor.execute(insert_request, ("Гавс", "Mythic", "Генерал Гавс — хладнокровный покоритель космоса, поддерживающий на корабле железную дисциплину. Но в душе он мечтает, чтобы его просто погладили...", "5600", "1120 * 2", "gavs.webp", "62.webp", "6262.webp", "shit.png", "dop.webp", "yes"))
cursor.execute(insert_request, ("Грей", "Mythic", "Грей изображает из себя героя немого кино, но иногда он забывается, когда делает вид, что стреляет из пальцев.", "6600", "2320", "grey.webp", "63.webp", "6363.webp", "shit.png", "dop.webp", "yes"))
cursor.execute(insert_request, ("Виллоу", "Mythic", "Виллоу катает влюблённые парочки в гондоле по болоту. Может быть, это не особо романтично, но уж точно незабываемо.", "5600", "800 * 3", "willoy.webp", "64.webp", "6464.webp", "shit.png", "dop.webp", "no"))
cursor.execute(insert_request, ("Отис", "Mythic", "Отис — подающий надежды уличный художник, который пользуется чернилами вместо краски. Никто не знаком с ним лично, но загадочность — часть его имиджа!", "6400", "920 * 3", "otis.webp", "65.webp", "6565.webp", "yron.webp", "dop.webp", "yes"))
cursor.execute(insert_request, ("Даг", "Mythic", "Хот-доги Дага продлевают жизнь друзьям.", "10000", "2400", "dag.webp", "666.webp", "6666.webp", "yron.webp", "dop.webp", "no"))
cursor.execute(insert_request, ("Джанет", "Mythic", "Джанет готова на всё ради успеха, а её акробатические навыки приходятся кстати, когда нужно вызволить сестру Бонни из неприятностей.", "6400", "2000", "janet.webp", "67.webp", "6767.webp", "yron.webp", "dop.webp", "yes"))
cursor.execute(insert_request, ("Джу Джу", "Mythic", "Джуджу — хозяйка лавки странностей, неразлучная с куклой вуду Гри-Гри (произносится как «Грегори»). Джуджу не только повелевает стихиями, но и мастерски делает кукол на радость многочисленным посетителям парка Старр.", "6000", "1600-2000", "juju.webp", "68.webp", "6868.webp", "shit.png", "dop.webp ", "no"))
cursor.execute(insert_request, ("Ева", "Mythic", "Смысл жизни Евы в том, чтобы позаботиться о своих драгоценных детёнышах и обеспечить им тёплую и сытую жизнь — например, в густой шерсти Гавса.", "5800", "800 + 1040 + 1280", "eva.webp", "69.webp", "6969.webp", "yron.webp", "dop.webp", "yes"))
cursor.execute(insert_request, ("Кленси", "Mythic", "Клэнси никогда не идёт на попятную. Если, конечно, ему не прикажет Хэнк. Он полностью смирился с судьбой ракообразного и готов на всё ради своих друзей.", "6600", "1200-1600 * 1-4", "clansy.webp", "70.webp", "7070.webp", "yron.webp", "dop.webp", "no"))
cursor.execute(insert_request, ("Фенг", "Mythic", "Фэнг смотрел так много фильмов про кунг-фу, что ведёт себя как герой одного из них. Он никогда не распускает руки... если вопрос можно решить ногами.", "8600", "680-2720", "fang.webp", "71.webp", "7171.webp", "yron.webp", "dop.webp", "yes"))
cursor.execute(insert_request, ("Чак", "Mythic", "Некогда выдающийся маэстро, Чак променял симфонии концертных залов на какофонию Станции призраков в поиске вдохновения и новых музыкальных форм!", "9000", "1080 * 3", "chak.webp", "72.webp", "7272.webp", "yron.webp", "dop.webp", "no"))
cursor.execute(insert_request, ("Чарли", "Mythic", "Чарли в цирке выступала,Посмотреть всех зазывала.Распустила локоны,Оплела всех коконом.Публика возмутилась,А Чарли с деньгами смылась!", "7000", "1600", "charlie.webp", "73.webp", "7373.webp", "yron.webp", "dop.webp", "yes"))
cursor.execute(insert_request, ("Спайк", "Legendary", "Все считают Спайка просто милым помощником Кольта и Шелли на ранчо, и никто не подозревает, какая боль живёт в его израненной душе.", "5600", "1080", "spike.webp", "74.webp", "7474.webp", "spikegirs.webp", "yron.webp", "yes"))
cursor.execute(insert_request, ("Ворон", "Legendary", "Ворон никому не доверяет и предпочитает одиночество, но иногда его можно увидеть в закусочной вместе с Буллом и Биби.", "4800", "640 * 3", "voron.webp", "75.webp", "7575.webp", "vorongirs.webp", "dop.webp", "yes"))
cursor.execute(insert_request, ("Леон", "Legendary", "Леон не любит общаться, так что его умение становиться невидимым весьма кстати. Не прячется он только от своей сестры Ниты.", "6800", "960 * 4", "leon.webp", "76.webp", "7676.webp", "leongirs.webp", "dop.webp", "yes"))
cursor.execute(insert_request, ("Сенди", "Legendary", "В те редкие моменты, когда Сэнди бодрствует, он старается помогать своей старшей сестре Таре в магазине. Но обычно его хватает ненадолго.", "7600", "1800", "sandy.webp", "777.webp", "7777.webp", "sandygirs.webp", "dop.webp", "yes"))
cursor.execute(insert_request, ("Амбер", "Legendary", "Амбер любит играть с огнём в буквальном смысле. А ещё часто пренебрегает техникой безопасности, так что лучше держаться от неё на расстоянии.", "6400", "420 * 40", "amber.webp", "78.webp", "7878.webp", "yron.webp", "dop.webp", "no"))
cursor.execute(insert_request, ("Вольт", "Legendary", "Вольт — это торговый автомат с бесконечным запасом энергетических напитков, так что он всегда готов зажигать, искрить и пепелить на танцполе.", "6000", "2360", "volt.webp", "80.webp", "8080.webp", "yron.webp", "dop.webp", "yes"))
cursor.execute(insert_request, ("Честер", "Legendary", "Честер любит жестокие шутки и розыгрыши. Чем сильнее злится его жертва, тем лучше... особенно если это Мэнди!", "7000", "1280 1-4", "chester.webp", "81.webp", "8181.webp", "yron.webp", "dop.webp", "no"))
cursor.execute(insert_request, ("Мэг", "Legendary", "Пока Макс и Вольт развлекают посетителей, Мэг ремонтирует всё, что сломано, облачившись в надёжный меха-костюм. Впрочем, её устраивает такой расклад.", "4600", "600 * 2", "meg.webp", "79.webp", "7979.webp", "hil.png", "dop.webp", "no"))
cursor.execute(insert_request, ("Корделиус", "Legendary", "Садовник, ухаживающий за Зачарованным лесом. Обожает грибы и враждебно относится к незнакомцам.", "6400", "1400 * 2", "cordelius.webp", "82.webp", "8282.webp", "yron.webp", "dop.webp", "no"))
cursor.execute(insert_request, ("Драко", "Legendary", "Каждый вечер Драко устраивает незабываемое фэнтезийное шоу, выезжая верхом на огнедышащем надувном драконе. Зрители в восторге от его фейерверков и рёва электрогитары!", "11000", "1400-2800", "draco.webp", "83.webp", "8383.webp", "yron.webp", "dop.webp", "no"))
cursor.execute(insert_request, ("Кит", "Legendary", "Кит — звезда старых мультфильмов. Втайне он мечтает сняться в новом проекте, где его будут ценить не только за милый вид, но и за актёрский талант.", "6000", "2000", "cit.webp", "84.webp", "8484.webp", "yron.webp", "dop.webp", "no"))
cursor.execute(insert_request, ("Кендзи", "Legendary", "Кэндзи держит суши-ресторан в парке Старр. Он подозрительно мало рассказывает о своём прошлом, но так хорошо готовит суши, что посетителям всё равно...", "7600", "1500-2000", "kendzi.webp", "85.webp", "8585.webp", "yron.webp", "dop.webp", "no"))

connection.commit()
connection.close()
