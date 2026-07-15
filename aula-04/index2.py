import math
# Entrada de dados do jogador
velocidade_inicial = 15  # Força do arremesso
angulo_graus = 45  # Ângulo da mira

# Converter o ângulo de graus para radianos (Python trabalha em radianos)
angulo_radianos = math.radians(angulo_graus)

# Decomposição da velocidade
vx = velocidade_inicial * math.cos(angulo_radianos)
vy = velocidade_inicial * math.sin(angulo_radianos)

print(f"Velocidade Horizontal (Vx): {round(vx, 2)} m/s")
print(f"Velocidade Vertical (Vy): {round(vy, 2)} m/s")
