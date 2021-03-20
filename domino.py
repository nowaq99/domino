class DominoLine:
    def __init__(self, domino_str):
        correct_literals = set("\|/")
        if not (set(domino_str) - correct_literals):
            self.dominoes = list(domino_str)

    def step_forward(self, steps=1):
        prev_dominoes = []
        for domino_id in range(len(self.dominoes)):
            domino = self.dominoes[domino_id]
            if len(prev_dominoes) == 2:
                if domino == '|':
                    if prev_dominoes == ['/', '|']:
                        self.dominoes[domino_id-1] = '/'
                elif domino == '\\':
                    if prev_dominoes == ['|', '|']:
                        self.dominoes[domino_id-1] = '\\'
            if len(prev_dominoes) == 1 and len(self.dominoes) == 2:
                if domino == '|' and prev_dominoes[0] == '/':
                    self.dominoes[domino_id] = '/'
                elif domino == '\\' and prev_dominoes[0] == '|':
                    self.dominoes[domino_id-1] = '\\'
            prev_dominoes.pop(0)
            prev_dominoes.append(domino)
        print(str(self.dominoes))
