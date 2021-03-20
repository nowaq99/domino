class DominoLine:
    def __init__(self, domino_str):
        correct_literals = set("\|/")
        if not (set(domino_str) - correct_literals) and domino_str:
            self.dominoes = list(domino_str)
        else:
            print('input is not correct')

    def __str__(self):
        return ''.join(self.dominoes)

    def step_forward(self, steps=1):
        if steps > 0:
            prev_dominoes = []
            for domino_id in range(len(self.dominoes)):
                domino = self.dominoes[domino_id]
                if len(prev_dominoes) == 2:
                    if domino in ('|', '/'):
                        if prev_dominoes == ['/', '|']:
                            self.dominoes[domino_id-1] = '/'
                    elif domino == '\\':
                        if prev_dominoes in (['|', '|'], ['\\', '|']):
                            self.dominoes[domino_id-1] = '\\'
                    prev_dominoes.pop(0)
                if len(prev_dominoes) == 1 and len(self.dominoes) == 2:
                    if domino == '|' and prev_dominoes[0] == '/':
                        self.dominoes[domino_id] = '/'
                    elif domino == '\\' and prev_dominoes[0] == '|':
                        self.dominoes[domino_id-1] = '\\'
                prev_dominoes.append(domino)
            if steps == 1:
                print(self)
                return None
            if steps > 1:
                self.step_forward(steps-1)
        else:
            print('input is not correct')

    def step_backward(self, steps=1):
        if steps > 0:
            if len(self.dominoes) > 1:
                prev_domino = ''
                line = self.dominoes.copy()
                for domino_id in range(len(line)):
                    domino = self.dominoes[domino_id]
                    if prev_domino == '/' and domino == '|':
                        line[domino_id-1] = '|'
                    elif prev_domino == '|' and domino == '\\':
                        line[domino_id] = '|'
                    elif prev_domino == '/' and domino == '\\':
                        line[domino_id-1] = '|'
                        line[domino_id] = '|'
                    prev_domino = domino
            else:
                line = '|'
            if steps == 1:
                print(''.join(line))
                return None
            if steps > 1:
                self.step_backward(steps-1)
        else:
            print('input is not correct')
