import random
import math
# Pacote que suporta geração de processos usando uma API semelhante ao módulo de threading
import multiprocessing
from multiprocessing import Pool


# Calcula o número de pontos dentro do circulo de x e y
def calculoDePontos(n):
    
    pontosCirc = 0
    n = int(n)
    for i in range(n):

        deltaX = random.random()
        deltaY = random.random()

        distancia = math.sqrt(deltaX**2 + deltaY**2)

        
        # Verifica se o ponto ta dentro do circulo
        if distancia <= 1:
            pontosCirc += 1
    return pontosCirc


if __name__=='__main__':
    
    np = multiprocessing.cpu_count()
    print(F'Você tem {np} CPUs')

    # Número de pontos
    n = 10000000
    
    # Pega um array de numero de pontos dividindo pelo numero de cpu e multiplica pela cpu
    # Cada worker vai pegar uma parte do array gerado
    
    totalPontos = [n/np] * np

    # Cria os workers com base no número de cpu encontrados pela cpu_count
    pool = Pool(processes=np)   

    # pontosCirc vai pegar os workers do pool e interagir fazendo comq a função seja executada para cada totalPontos
    # pool.map = função + iteração
    pontosCirc = pool.map(calculoDePontos, totalPontos)
    pool.close()
    pool.join()
    print("Pontos de cada worker:", totalPontos)
    print("Pontos de cada worker que esta dentro do circulo:", pontosCirc)

    pi = sum(pontosCirc) / n * 4
    print("Valor aproximado de PI: ", pi) 