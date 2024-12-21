import pyxel
# import numpy as np

WINDOW_ASPECT = 1.33
WINDOW_SCALE = 100
WINDOW_H = int(WINDOW_SCALE * 1)
WINDOW_W = int(WINDOW_SCALE * WINDOW_ASPECT)

KUCHAN = (0, 0, 15, 15)
IWAKI = (16, 0, 15, 15)
SAITO = (32, 0, 15, 15)
TSUKAJI = (48, 0, 15, 15)
LETTER_SHI = (0, 16, 15, 15)
LETTER_O = (16, 16, 15, 15)
LETTER_DO = (32, 16, 15, 15)

LESPAUL = (0, 32, 15, 15)
IBANEZ = (16, 32, 15, 15)
STINGRAY = (32, 32, 15, 15)

DRUM_LEFT = (0, 64, 15, 15)
DRUM_RIGHT = (16, 64, 15, 15)
CYMBAL_A = (0, 48, 15, 15)
CYMBAL_B = (16, 48, 15, 15)

MIC_STAND_SHIMOTE = (32, 64, 15, 15)
MIC_STAND_KAMITE = (48, 64, 15, 15)

# STAGE = (0, 80, 100, 20)
KADOMATSU = (32, 80, 15, 15)

BGM = 0

SCENE_TITLE = 0
SCENE_CONCERT = 1

class App:
    def __init__(self):
        pyxel.init(WINDOW_W, WINDOW_H)
        pyxel.load("./assets/keion.pyxres")
        self.scene = SCENE_TITLE
        self.music_on = False

        self.kuchan_pos = [WINDOW_W//2 - (16 + 2) * -1, WINDOW_H//2 + 5]
        self.iwaki_pos = [WINDOW_W//2 - (16 + 2) * 1, WINDOW_H//2]
        self.saito_pos = [WINDOW_W//2 - 8, WINDOW_H//2 - 20]
        self.tsukaji_pos = [WINDOW_W//2 - (16 + 2) * 2, WINDOW_H//2 + 5]

        self.initial_kuchan_pos = self.kuchan_pos
        self.initial_iwaki_pos = self.iwaki_pos
        self.initial_saito_pos = self.saito_pos
        self.initial_tsukaji_pos = self.tsukaji_pos

        # self.snowflakes = [[np.random.randint(0, WINDOW_W), np.random.randint(0, WINDOW_H)] for _ in range(100)]
        
        # pyxel.playm(0, loop=True)
        pyxel.run(self.update, self.draw)

    def update_title_scene(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) or pyxel.btnp(pyxel.KEY_KP_ENTER):
            self.scene = SCENE_CONCERT

    def update(self):
        # for flake in self.snowflakes:
        #     flake[1] += 1
        #     if flake[1] > WINDOW_H:
        #         flake[0] = np.random.randint(0, WINDOW_W)
        #         flake[1] = 0

        if self.scene == SCENE_TITLE:
            self.update_title_scene()
        elif self.scene == SCENE_CONCERT:
            if self.music_on == False:
                pyxel.playm(0, loop=True)
                self.music_on = True
            # Random walk for each character (Kuchan, Iwaki, Saito, Tsukaji), but stay in the window
            # self.kuchan_pos = np.clip(np.array(self.kuchan_pos) + np.random.randint(-1, 2, 2), 0, [WINDOW_W - 16, WINDOW_H - 16])
            # self.iwaki_pos = np.clip(np.array(self.iwaki_pos) + np.random.randint(-1, 2, 2), 0, [WINDOW_W - 16, WINDOW_H - 16])
            # self.saito_pos = np.clip(np.array(self.saito_pos) + np.random.randint(-1, 2, 2), 0, [WINDOW_W - 16, WINDOW_H - 16])
            # self.tsukaji_pos = np.clip(np.array(self.tsukaji_pos) + np.random.randint(-1, 2, 2), 0, [WINDOW_W - 16, WINDOW_H - 16])

    def draw(self):
        if self.scene == SCENE_TITLE:
            pyxel.text(WINDOW_W//2 - 20, WINDOW_H//2, "音が鳴ります ENTER/CLICK", pyxel.COLOR_WHITE)
            
        elif self.scene == SCENE_CONCERT:
            pyxel.cls(0)

            self.draw_shishiodoshi()

            self.draw_saito(self.saito_pos)
            self.draw_drums(self.initial_saito_pos)
            self.draw_cymbals(self.initial_saito_pos)

            self.draw_kuchan(self.kuchan_pos)
            self.draw_lespaul(self.kuchan_pos)

            self.draw_iwaki(self.iwaki_pos)
            self.draw_ibanez(self.iwaki_pos)

            self.draw_tsukaji(self.tsukaji_pos)
            self.draw_stingray(self.tsukaji_pos)

            self.draw_mic_stand_shimote(self.initial_kuchan_pos)
            self.draw_mic_stand_kamite(self.initial_tsukaji_pos)

            for i in range(WINDOW_H//16 + 1):
                pyxel.blt(0, WINDOW_H - i*16, 0, *KADOMATSU, 0)
                pyxel.blt(WINDOW_W - 16, WINDOW_H - i*16, 0, *KADOMATSU, 0)

            # self.snow()
    
    def draw_kuchan(self, pos: list[int, int]):
        pyxel.blt(int(pos[0]), int(pos[1]), 0, *KUCHAN, 0)
    
    def draw_iwaki(self, pos: list[int, int]):
        pyxel.blt(int(pos[0]), int(pos[1]), 0, *IWAKI, 0)
    
    def draw_saito(self, pos: list[int, int]):
        pyxel.blt(int(pos[0]), int(pos[1]), 0, *SAITO, 0)
    
    def draw_tsukaji(self, pos: list[int, int]):
        pyxel.blt(int(pos[0]), int(pos[1]), 0, *TSUKAJI, 0)
    
    def draw_lespaul(self, pos: list[int, int]):
        pyxel.blt(int(pos[0])-3, int(pos[1])+2, 0, *LESPAUL, 0, 20)
    
    def draw_ibanez(self, pos: list[int, int]):
        pyxel.blt(int(pos[0])-2, int(pos[1])+1, 0, *IBANEZ, 0, 20)

    def draw_stingray(self, pos: list[int, int]):
        pyxel.blt(int(pos[0])-3, int(pos[1])+2, 0, *STINGRAY, 0, 20)
    
    def draw_mic_stand_shimote(self, pos: list[int, int]):
        pyxel.blt(int(pos[0])-3, int(pos[1])+2, 0, *MIC_STAND_SHIMOTE, 0, 0)

    def draw_mic_stand_kamite(self, pos: list[int, int]):
        pyxel.blt(int(pos[0])-3, int(pos[1])+2, 0, *MIC_STAND_KAMITE, 0, 0)
    
    def draw_drums(self, pos: list[int, int]):
        pyxel.blt(int(pos[0])-7, int(pos[1]), 0, *DRUM_LEFT, 0, 0)
        pyxel.blt(int(pos[0])+8, int(pos[1]), 0, *DRUM_RIGHT, 0, 0)
    
    def draw_cymbals(self, pos: list[int, int]):
        pyxel.blt(int(pos[0])-3, int(pos[1]), 0, *CYMBAL_A, 0, 0, 0.6)
        pyxel.blt(int(pos[0])+3, int(pos[1]), 0, *CYMBAL_B, 0, 0, 0.6)
    
    # def draw_stage(self):
    #     pyxel.blt(0, WINDOW_H - 20, 0, *STAGE, 0)

    def draw_kadomatsu(self, pos: list[int, int]):
        pyxel.blt(int(pos[0]), int(pos[1]), 0, *KADOMATSU, 0)

    def draw_shishiodoshi(self):
        # シシオドシ
        pyxel.blt(int(WINDOW_W//2) - int(16 * 2.5), int(10), 0, *LETTER_SHI, 0)
        pyxel.blt(int(WINDOW_W//2) - int(16 * 1.5), int(10), 0, *LETTER_SHI, 0)
        pyxel.blt(int(WINDOW_W//2) - int(16 * 0.5), int(10), 0, *LETTER_O, 0)
        pyxel.blt(int(WINDOW_W//2) - int(16 * -0.5), int(10), 0, *LETTER_DO, 0)
        pyxel.blt(int(WINDOW_W//2) - int(16 * -1.5), int(10), 0, *LETTER_SHI, 0)
    
    # def snow(self):
    #     for flake in self.snowflakes:
    #         pyxel.pset(flake[0], flake[1], pyxel.COLOR_WHITE)

App()