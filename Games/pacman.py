#!/home/gab/BCC/CG/env/bin/python

import pygame

AMARELO = (255, 255, 0)
AZUL = (0, 0, 255)
PRETO = (0, 0, 0)

LARGURA = 800
ALTURA = 600
TAMANHO_TILE = 50

VELOCIDADE = 5


mapa = [
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],

]

def inicializar():
  pygame.init()
  tela = pygame.display.set_mode((LARGURA, ALTURA))
  pygame.display.set_caption("Jogo em desenvolvimento")
  return tela

def desenhar_mapa(tela, mapa):
  for linha in range(len(mapa)):
    for coluna in range(len(mapa[linha])):
      x = coluna * TAMANHO_TILE
      y = linha * TAMANHO_TILE

      if mapa[linha][coluna] == 1:
        cor = AZUL
      else:
        cor = PRETO

      pygame.draw.rect(tela, cor, (x, y, TAMANHO_TILE, TAMANHO_TILE))
      pygame.draw.rect(tela, PRETO, (x, y, TAMANHO_TILE, TAMANHO_TILE), 1)

def criar_jogador(x, y, largura, altura):
  return pygame.Rect(x, y, largura, altura)

def desenhar_tela(tela, jogador, cor):
  desenhar_mapa(tela, mapa)
  pygame.draw.rect(tela, cor, jogador)
  pygame.display.flip()

def valida(x, y):
  tile_coluna = x // TAMANHO_TILE
  tile_linha = y // TAMANHO_TILE

  if 0 <= tile_linha < len(mapa) and 0 <= tile_coluna < len(mapa[0]):
    return mapa[tile_linha][tile_coluna] == 0
  return False

def mover_jogador(jogador, mapa):
  teclas = pygame.key.get_pressed()

  dx = dy = 0
  
  if teclas[pygame.K_LEFT]:
    dx = -VELOCIDADE
  if teclas[pygame.K_RIGHT]:
    dx = VELOCIDADE
  if teclas[pygame.K_UP]:
    dy = -VELOCIDADE
  if teclas[pygame.K_DOWN]:
    dy = VELOCIDADE

  novo_jogador = jogador.move(dx, dy)

  if (
      valida(novo_jogador.left, novo_jogador.top) and
      valida(novo_jogador.right - 1, novo_jogador.top) and
      valida(novo_jogador.left, novo_jogador.bottom - 1) and
      valida(novo_jogador.right - 1, novo_jogador.bottom - 1)
    ):
    jogador.x += dx
    jogador.y += dy

def loop_jogo(tela, jogador):
  clock = pygame.time.Clock()
  rodando = True

  while rodando:
    for evento in pygame.event.get():
      if evento.type == pygame.QUIT:
          rodando = False

    mover_jogador(jogador, mapa)
    desenhar_tela(tela, jogador, AMARELO)
    clock.tick(60)

  pygame.quit()

def main():
  altura, largura = 20, 20
  tela = inicializar()
  jogador = criar_jogador(400, 300, altura, largura)
  loop_jogo(tela, jogador)

if __name__ == "__main__":
  main()