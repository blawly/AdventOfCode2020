class Combat:
    def __init__(self, pOneDeck, pTwoDeck, recursive):
        self.pOneDeck = pOneDeck.copy()
        self.pTwoDeck = pTwoDeck.copy()
        self.recursive = recursive
        self.pOneHistory = set()
        self.pTwoHistory = set()
        self.loop = False
    
    def play(self):
        if self.recursive:
            return self.rPlay()
        else:
            return self.nPlay()

    def nPlay(self):
        while True:
            pOne = self.pOneDeck.pop(0)
            pTwo = self.pTwoDeck.pop(0)
            if pOne > pTwo:
                self.pOneDeck.append(pOne)
                self.pOneDeck.append(pTwo)
            else:
                self.pTwoDeck.append(pTwo)
                self.pTwoDeck.append(pOne)
            if len(self.pTwoDeck) == 0:
                score = 0
                for i in range(len(self.pOneDeck)):
                    score += (i + 1) * self.pOneDeck.pop()
                return (score, True)
            elif len(self.pOneDeck) == 0:
                score = 0
                for i in range(len(self.pTwoDeck)):
                    score += (i + 1) * self.pTwoDeck.pop()
                return(score, False)
    
    def rPlay(self):
        while True:
            if str(self.pOneDeck) in self.pOneHistory and str(self.pTwoDeck) in self.pTwoHistory:
                score = 0
                for i in range(len(self.pOneDeck)):
                    score += (i + 1) * self.pOneDeck.pop()
                return (score, True)
            else:
                self.pOneHistory.add(str(self.pOneDeck))
                self.pTwoHistory.add(str(self.pTwoDeck))
                pOne = self.pOneDeck.pop(0)
                pTwo = self.pTwoDeck.pop(0)
                if pOne <= len(self.pOneDeck) and pTwo <= len(self.pTwoDeck):
                    subGame = Combat(self.pOneDeck[:pOne], self.pTwoDeck[:pTwo], True)
                    outcome = subGame.play()
                    if outcome[1]:
                        self.pOneDeck.append(pOne)
                        self.pOneDeck.append(pTwo)
                    else:
                        self.pTwoDeck.append(pTwo)
                        self.pTwoDeck.append(pOne)
                else:
                    if pOne > pTwo:
                        self.pOneDeck.append(pOne)
                        self.pOneDeck.append(pTwo)
                    else:
                        self.pTwoDeck.append(pTwo)
                        self.pTwoDeck.append(pOne)
            if len(self.pTwoDeck) == 0:
                score = 0
                for i in range(len(self.pOneDeck)):
                    score += (i + 1) * self.pOneDeck.pop()
                return (score, True)
            elif len(self.pOneDeck) == 0:
                score = 0
                for i in range(len(self.pTwoDeck)):
                    score += (i + 1) * self.pTwoDeck.pop()
                return (score, False)

with open('input/day22.txt') as f:
    pOneDeck = []
    pTwoDeck = []
    one = True
    for line in f.read().split('\n'):
        if line.isnumeric():
            if one:
                pOneDeck.append(int(line))
            else:
                pTwoDeck.append(int(line))
        elif line == 'Player 2:':
            one = False

partOne = Combat(pOneDeck, pTwoDeck, False)
print(partOne.play())
partTwo = Combat(pOneDeck, pTwoDeck, True)
print(partTwo.play())