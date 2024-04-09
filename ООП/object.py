
"""                                                                                -->>>      !  НАСЛЕДОВАНИЕ  !      <<<--
"""


class Metal: # Поджанры метал-музыки

    def __init__(self, id: int, character:str, speed:str, vocals:bool = True) -> None:
        self.id = id
        self.character: str = character
        self.speed: str = speed
        self.vocals: bool = vocals

    def play(self):
        print('Музыка играет.')

    def write(self):
        print('Музыка пишется!')

    def __repr__(self) -> str: # Чтобы СПИСОК вывелся в терминал удобоваримо
        return f'Песня {self.id}: {self.character}, {self.speed}, вокал: {self.vocals}'

    

 


# Проблемки начинаются отсюда:

class NuMetal(Metal):
    def __init__(self, id: int, character: str, speed: str, vocals: bool, rapping: bool = True) -> None:
        NuMetal.__init__(id, character, speed, vocals, rapping) 
        self.rapping: bool = rapping
    def __repr__(self) -> str:
        return f'Песня {self.id}: {self.character}, {self.speed}, вокал: {self.vocals}, читка: {self.rapping}'









class Progressive(Metal):
    def __init__(self, id: int, character: str, speed: str, vocals: bool, djent: bool = True) -> None:
        super().__init__(character, speed, vocals)
        self.djent: bool = djent

class Instrumental(Progressive):
    def __init__(self, id: int, character: str, speed: str, djent: bool, vocals: bool = False) -> None:
        super().__init__(character, speed, vocals, djent)
        self.vocals = False # ??????????? дублирование ????????????????? 
    
class Christian(Metal):
    def __init__(self, id: int, character: str, speed: str, vocals: bool, Jesus: bool = True) -> None:
        super().__init__(character, speed, vocals)
        self.Jesus: bool = Jesus

PLAYLIST: list = []




for i in range(1,5):
    song = Metal(i, 'Мелодичная', 'быстрая', True)
    PLAYLIST.append(song)
    print(song)

# Вывод:
"""
Песня 1: Мелодичная, быстрая, вокал: True
Песня 2: Мелодичная, быстрая, вокал: True
Песня 3: Мелодичная, быстрая, вокал: True
Песня 4: Мелодичная, быстрая, вокал: True
"""

# Не работает:
    
# for i in range(6,10):
#     song = NuMetal(i, 'Качовая', 'умеренная', True, True)
#     PLAYLIST.append(song)
#     print(song)


