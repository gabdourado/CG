#!/home/gab/BCC/CG/env/bin/python

import pygame

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
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1]
]

AMARELO = (255, 255, 0)

VELOCIDADE = 5

SIZE_TILE = 32

LARGURA, ALTURA = SIZE_TILE * len(mapa[0]), SIZE_TILE * len(mapa) 

pygame.init()

screen = pygame.display.set_mode((LARGURA, ALTURA))

tileset = pygame.image.load("./tileset-fundo.png").convert_alpha()

def get_tile(x, y):
    tile = tileset.subsurface((x * SIZE_TILE, y * SIZE_TILE, SIZE_TILE, SIZE_TILE))
    return tile
tiles = {
    1: get_tile(0, 0),  # grama (área acessível)
    0: get_tile(1, 0),  # pedra (área inacessível)
}

def inicializar():
  pygame.init()
  tela = pygame.display.set_mode((LARGURA, ALTURA))
  pygame.display.set_caption("Jogo em desenvolvimento")
  return tela

def desenhar_mapa(tela, mapa):
    for y, linha in enumerate(mapa):
        for x, tile_id in enumerate(linha):
            tela.blit(tiles[tile_id], (x * SIZE_TILE, y * SIZE_TILE))

def criar_jogador(x, y, largura, altura):
  return pygame.Rect(x, y, largura, altura)

def desenhar_tela(tela, jogador, cor):
  desenhar_mapa(tela, mapa)
  pygame.draw.rect(tela, cor, jogador)
  pygame.display.flip()

def sprite_valido(x, y):
  tile_coluna = x // SIZE_TILE
  tile_linha = y // SIZE_TILE

  if 0 <= tile_linha < len(mapa) and 0 <= tile_coluna < len(mapa[0]):
    return mapa[tile_linha][tile_coluna] == 0
  return False

def mover_jogador(jogador):
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
      sprite_valido(novo_jogador.left, novo_jogador.top) and
      sprite_valido(novo_jogador.right - 1, novo_jogador.top) and
      sprite_valido(novo_jogador.left, novo_jogador.bottom - 1) and
      sprite_valido(novo_jogador.right - 1, novo_jogador.bottom - 1)
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

    mover_jogador(jogador)
    desenhar_tela(tela, jogador, AMARELO)
    clock.tick(60)

  pygame.quit()

def main():
  altura, largura = 10, 10
  tela = inicializar()
  jogador = criar_jogador(LARGURA // 2, ALTURA // 2, altura, largura)
  loop_jogo(tela, jogador)

if __name__ == "__main__":
  main()