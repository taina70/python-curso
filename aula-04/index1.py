def calcular_posicao(posicao_inicial, velocidade, tempo):
    posicao_atual = posicao_inicial + (velocidade * tempo)
    return posicao_atual


# Exemplo de uso
posicao_bola = calcular_posicao(posicao_inicial=10, velocidade=5, tempo=3)
print(f"A bola está na posição x = {posicao_bola}")
