class DominoLine:
    def __init__(self, domino_str):
        correct_literals = set("\|/")
        self.iterations = list()
        if not (set(domino_str) - correct_literals) and domino_str:
            self.dominoes = list(domino_str)
        else:
            print('input is not correct')

    def __str__(self):
        return ''.join(self.dominoes)

    def step_forward(self, steps=1):
        if steps > 0:
            prev_dominoes = []
            self.iterations.append(self.dominoes.copy())
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
                return ''.join(self.dominoes)
            if steps > 1:
                self.step_forward(steps-1)
        else:
            print('input is not correct')

    def step_backward(self, steps=1):
        if steps > 0:
            if steps <= len(self.iterations):
                print(''.join(self.iterations[-steps-1]))
            else:
                if self.iterations:
                    line = self.iterations[0].copy()
                else:
                    line = self.dominoes.copy()
                steps = steps - len(self.iterations)
                for step in range(steps):
                    print('dupa')
                    if len(self.dominoes) > 1:
                        prev_domino = ''
                        for domino_id in range(len(line)):
                            domino = line[domino_id]
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
                    if step == steps-1:
                        print(''.join(line))
                        return ''.join(line)
        else:
            print('input is not correct')
            return None
