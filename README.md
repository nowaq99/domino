# Zadanie rekrutacyjne - domino
#### _Opis zadania_

Kostki domina są reprezentowane w formie Stringa, który składa się z poniższych znaków:

| - kostka domina stoi nienaruszona
/ - kostka domina przewraca się w prawą stronę
\ - kostka domina przewraca się w lewą stronę

Twoim zadaniem jest napisanie algorytmu wyznaczającego nowy literał zawierający powyższe znaki po X iteracjach, podczas których zachodzą zmiany w sąsiednich kostkach X jest parametrem wejściowym. Przykładowo dla ciągu wejściowego:

```sh
||//||\||/\|
```
Zastosowanie 1 iteracji algorytmu powinno dać wynik:
```sh
||///\\||/\|
```
Dodatkowo: Napisz algorytm wsteczny, pokazujący jak wyglądał ciąg kostek domina przed zastosowaniem X iteracji algorytmu z pierwszej części zadania Przykładowo dla ciągu wejściowego:
```sh
||////\\\|////|
```
Zastosowanie 2 iteracji algorytmu wstecznego powinno dać wynik:
```sh
||//||||\|//|||
```
#### Rozwiązanie problemu

Klasa ```DominoLine``` reprezentuje ułożone domino. Kostki domina zapisane za pomocą stringów, które trzymane są w liście ```self.dominoes```. Aby stworzyć obiekt tej klasy należy wprowadzić do konstruktora ciąg znaków np.
```sh
dominoes = DominoLine('///\\\|\//|||\\/||\')
```
Aby wykonać iterację algorytmu przewracania kostek, należy wywołać metodę ```step_forward()```. Np.:
```sh
dominoes.step_forward()
dominoes.step_forward(3) #wykonuje ruch o 3 iteracje do przodu
```

Metoda ta zwraca stringa reprezentującego stan domino po iteracjach oraz go wyświetla na konsoli.

Algorytm zastosowany w tej metodzie iteruje po liście ```self.dominoes``` i ją zmienia. Wykorzystywana jest dodatkowa pamięć, która przechowuje 2 poprzednie kostki, by móc ocenić jak zachowają się te, które się jeszcze nie przewróciły.

Aby zobaczyć co się działo przed wykonaniem ruchów używamy funkcji ```step_backward()```. Np.
```sh
dominoes.step_backward()
dominoes.step_forward(3) #sprawdza co się działo 3 iteracje temu
```

Podczas trwania algorytmu z funkcji ```step_forward()```, kolejne stany planszy są zapisywane do listy ```iterations```. Algorytm wsteczny pobiera dane z tej tablicy. Jeśli chcemy zajrzeć do iteracji która wykracza poza zakres tej tablicy, to stosowana jest heurystyka, która działa z dokładnością do przypadów typu /|/ -> ///.

#### Pobieranie i uruchamianie projektu
Należy sklonować projekt z githuba:
```sh
$ git clone https://github.com/nowaq99/domino.git
```

Pojawi się folder z całym projektem. Interesuje nas plik ```domino.py```. Należy go wrzucić do swojego projektu i zaimportować.

```sh
import .../domino.py
```
