#!/home/gab/BCC/CG/env/bin/python

import pygame
from time import sleep

mapa = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

AMARELO = (255, 255, 0)
VERMELHO = (255, 0, 0)

DESLOCAMENTO = 5

SIZE_TILE = 32

LARGURA, ALTURA = SIZE_TILE * len(mapa[0]), SIZE_TILE * len(mapa) 

pygame.init()

screen = pygame.display.set_mode((LARGURA, ALTURA))

tileset = pygame.image.load("./tileset-fundo.png").convert_alpha()

def get_tile(x, y):
    tile = tileset.subsurface((x * SIZE_TILE, y * SIZE_TILE, SIZE_TILE, SIZE_TILE))
    return tile

tiles = {
    0: get_tile(0, 0),  # (área inacessível)
    1: get_tile(1, 0),  # (área acessível)
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

def desenhar_tela(tela, jogador, cor_jogador, vilao, cor_vilao):
  desenhar_mapa(tela, mapa)
  pygame.draw.rect(tela, cor_jogador, jogador)
  pygame.draw.rect(tela, cor_vilao, vilao)
  pygame.display.flip()

def sprite_valido(x, y):
  tile_coluna = x // SIZE_TILE
  tile_linha = y // SIZE_TILE

  if 0 <= tile_linha < len(mapa) and 0 <= tile_coluna < len(mapa[0]):
    return mapa[tile_linha][tile_coluna] == 1
  return False

def move_personagem(personagem, classe):
  teclas = pygame.key.get_pressed()

  dx = dy = 0
  
  
  match (classe):
    case 'player1':
      if teclas[pygame.K_LEFT]:
        dx = -DESLOCAMENTO
      if teclas[pygame.K_RIGHT]:
        dx = DESLOCAMENTO
      if teclas[pygame.K_UP]:
        dy = -DESLOCAMENTO
      if teclas[pygame.K_DOWN]:
        dy = DESLOCAMENTO
        
    case 'player2':
      if teclas[pygame.K_w]:
        dy -= DESLOCAMENTO
      if teclas[pygame.K_s]:
          dy += DESLOCAMENTO
      if teclas[pygame.K_a]:
          dx -= DESLOCAMENTO
      if teclas[pygame.K_d]:
          dx += DESLOCAMENTO

  novo_personagem = personagem.move(dx, dy)

  if (
      sprite_valido(novo_personagem.left, novo_personagem.top) and
      sprite_valido(novo_personagem.right - 1, novo_personagem.top) and
      sprite_valido(novo_personagem.left, novo_personagem.bottom - 1) and
      sprite_valido(novo_personagem.right - 1, novo_personagem.bottom - 1)
    ):
    personagem.x += dx
    personagem.y += dy


def morte (jogador, vilao):
  return jogador.colliderect(vilao)

def loop_jogo(tela, jogador, vilao):
  clock = pygame.time.Clock()
  rodando = True

  while rodando:
    for evento in pygame.event.get():
      if evento.type == pygame.QUIT:
          rodando = False

    move_personagem(jogador, 'player1')
    move_personagem(vilao, 'player2')
    desenhar_tela(tela, jogador, AMARELO, vilao, VERMELHO)
    
    if morte(jogador, vilao):
      sleep(0.5)
      rodando = False

    clock.tick(60)

  pygame.quit()

def main():
  altura, largura = 10, 10
  tela = inicializar()
  jogador = criar_jogador(LARGURA // 2, ALTURA // 2, altura, largura) # Programador
  vilao = criar_jogador(LARGURA // 4, ALTURA // 2, altura, largura) # Bug
  loop_jogo(tela, jogador, vilao)

if __name__ == "__main__":
  main()