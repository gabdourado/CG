import cairo
import pygame

def CantorSet(init_x, end_x, y, iterations):
    
    if iterations < 0:
        return

    context.move_to(init_x, y)
    context.line_to(end_x, y)
    context.stroke()

    v = (end_x - init_x)/3.0

    y += 10

    iterations -= 1

    CantorSet(init_x, init_x + v, y, iterations) # Right
    CantorSet(end_x - v, end_x, y, iterations) # Left

# Create an image surface (RGBA format)
width, height = 1000, 200
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
context = cairo.Context(surface)

context.set_line_width(3)

# Set the background to be white
context.set_source_rgb(1, 1, 1)
context.paint()

context.set_source_rgb(0,0,0) # Black

init_x = y = 10
end_x = width - init_x

# Line 1 (1 line - main)
CantorSet(init_x, end_x, y, 7)

surface.write_to_png("../outputs/cantor-set.png")

# Opens a window with the drawing
pygame.init()
screen = pygame.display.set_mode((width, height))
image = pygame.image.load("../outputs/cantor-set.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(image, (0, 0))
    pygame.display.flip()

pygame.quit()
