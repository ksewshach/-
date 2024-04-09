
"""                                                                                -->>>      !  НАСЛЕДОВАНИЕ  !      <<<--
"""

# dir() <- функция, которая возвращает список методов объекта (передать любой объект)

# Если аргумент нужен дефолтный, то надо менять аргументы местами чтобы дефолт был в конце, также можно внутри присваивать значению тру или фолс


class Phone: # Родительский класс

    def __init__(self, color:str, speaker:bool, mic:bool) -> None:
        self.color: str = color
        self.speaker: bool = speaker
        self.mic: bool = mic

    def call(self):
        print('Класс Phone')

    
class MobilePhone(Phone):
    def __init__(self, color: str, speaker: bool, mic: bool, battery: int) -> None:
        super().__init__(color, speaker, mic) # Super для явного указывания, что переносим. УНИВЕРСАЛЬНАЯ. Безопасно создаст временный объект класса, после того как всё сделдали в родительском, уже будет в дочернем. Можно заменить 'super()' на 'MobilePhone'
        self.battery: int = battery

    def call(self):
        print('Класс MobilePhone') # Перегрузка метода, адаптируем метод для нового класса
    
    def send_message(self):
        print('Отправил сообщение с класса MobilePhone')

# Конструкция общая, но у каждого будут свои особенности. Такой принцип неследования
class Nokia(MobilePhone):
    def __init__(self, color: str, speaker: bool, mic: bool, battery: int, memory: int, id: int) -> None:
        super().__init__(color, speaker, mic, battery)
        self.memory: int = memory
        self.flashlight: bool = False
        self.id: int = id

    def play(self):
        print('Играть в змейку')

    def flashlight_on(self):
        if self.flashlight == False:
            self.flashlight = True
            print('Фонарик включился')

    def flashlight_off(self):
        if self.flashlight == True:
            self.flashlight = False

    def __repr__(self) -> str: # Чтобы STORAGE вывелся в терминал удобоваримо
        return f'Nokia id = {self.id}'
    
STORAGE: list = []

for i in range(1000):
    phone = Nokia('black', True, True, 500, 100, i)
    STORAGE.append(phone)

print(STORAGE)


for i in range(len(STORAGE)):     # Включили фонарик на каждом втором телефоне
    if i % 2 == 0:
        STORAGE[i].flashlight_on()
        print(STORAGE[i])
