class Ship:

    def __init__(self, screenWidth, screenHeight, pyGameData, win):
        width = 40
        height = 60
        self.win = win
        self.pyGameData = pyGameData
        self.screenHeight = screenHeight
        self.screenWidth = screenWidth
        y = screenHeight - height

        x = int(screenWidth / 2)
        pyGameData.draw.rect(win, (255, 0, 0), (x, y, width, height))
