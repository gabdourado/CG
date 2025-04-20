import cairo
import colorsys
import pygame

# Function to draw a triangle with specified vertices
def draw_triangle(context, vertices):

    # Start drawing the triangle based on the vertices
    context.move_to(vertices[0][0], vertices[0][1])
    context.line_to(vertices[1][0], vertices[1][1])
    context.line_to(vertices[2][0], vertices[2][1])
    context.close_path()  # Close the path to complete the triangle

# Linear Interpolation Function (LERP)
def lerp(a,b,t):
  return a*(1.0-t) + b*t

# Linear Interpolation Function + RGB
def lerp_rgb(rgb1, rgb2, t):
  return [lerp(rgb1[0], rgb2[0], t), lerp(rgb1[1], rgb2[1], t), lerp(rgb1[2], rgb2[2], t)]

def rainbow_triangles(context):
   
   h = 0.0 # h initial (red)

   for j in range(1, 1201, 200):

    rgb_init = colorsys.hls_to_rgb(h, 0.5, 1.0)
        
    h = (h + 0.166) % 1.0

    rgb_end = colorsys.hls_to_rgb(h, 0.5, 1.0)

    for i in range(10, 110, 10):

      # Call the Linear Interpolation Function
      [r,g,b] = lerp_rgb([rgb_init[0], rgb_init[1], rgb_init[2]], [rgb_end[0], rgb_end[1], rgb_end[2]], float(i)/100)

      # Set the color for the triangle
      context.set_source_rgba(r, g, b, 1)

      # The vertices
      vertices = [(0+i+j, 100+i), (50+i+j, 0+i), (100+i+j, 100+i)]

      # Call the function to draw a triangle with specified vertices
      draw_triangle(context, vertices)
      # Fill the triangle
      context.fill_preserve()
      
      # Line width
      context.set_line_width(0)
      
      # contour black
      context.set_source_rgb(0, 0, 0)  # RGB para preto
      context.stroke()


# Create an image surface (RGBA format)
width, height = 1220, 220
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
context = cairo.Context(surface)

# Set the background to be white
context.set_source_rgb(1, 1, 1)
context.paint()

rainbow_triangles(context)

# Save the image with multiple shapes
surface.write_to_png("../outputs/rainbow-triangles.png")

# Opens a window with the drawing
pygame.init()
screen = pygame.display.set_mode((width, height))
image = pygame.image.load("../outputs/rainbow-triangles.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(image, (0, 0))
    pygame.display.flip()

pygame.quit()
