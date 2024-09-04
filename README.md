# MazeSolvingNetworkX

A ideia deste projeto é a implementação do BFS, DFS e o A* com quatro heurística diferentes, para realizar a comparação dos mesmos, para o problema clássico do labirinto. O problema do labirinto se consiste em achar um caminho do ponto inicial até chegar ao ponto final do labirinto, passando por uma serie de corredores em um mapa. Além disso, tam-
bém foi implementado uma simulação para mostrar os caminhos encontrados pelos algoritmos num labirinto aleatório.

# Execução

Para gerar um labirinto basta executar o arquivo *maze-generator.py* passando junto a quantidade de labirintos a ser gerados de tamanhos 11x11, 21x21, 31x31, 41x41, 51x51. Os labirintos serão guardados na pasta *mazes*. Exemplo:

```
python src/maze-generator.py 50
```

Para testar todos os algoritmos basta executar o arquivo *main.py* passando junto a quantidade de labirintos a ser testados de tamanhos 11x11, 21x21, 31x31, 41x41, 51x51. No final da execução será perguntado o nome do arquivo para guardar os resultados, que sera armazenado na pasta *datas*. Exemplo:

```
python src/main.py 50
```

Para ver a simulação dos caminhos basta executar o arquivo *maze-show-path.py* passando junto o tamanho do labirinto quadrado, ou seja, passar o tamanho de um lado. Exemplo:

```
python src/maze-show-path.py 51
```