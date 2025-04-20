import cairo
from colorsys import rgb_to_hls, hls_to_rgb
from random import uniform, randint

def gen_parameters (tam):
    parameters = []
    
    while len(parameters) < tam:
        num = round(uniform(-0.4, 0.4), 1)
        if num not in parameters:
            parameters.append(num)

    return parameters

def random_squares (contexto, screen_w, rgb, num_squares, space = 10):

    side_square = int((screen_w - (num_squares + 1) * space) / num_squares)

    total_space = num_squares * side_square + (num_squares - 1) * space

    x_inicio = y_inicio = (screen_w - total_space) / 2

    r, g, b = rgb
    h, l, s = rgb_to_hls(r, g, b)
    
    parameters = gen_parameters(num_squares)

    for i in range(num_squares):
      
      new_l = min(max(l + parameters[i], 0), 1)
      new_s =  min(max(s + parameters[i], 0), 1)

      new_r, new_g, new_b = hls_to_rgb(h, new_l, new_s)

      for j in range(num_squares):

          contexto.set_source_rgb(new_r, new_g, new_b)
          x = x_inicio + j * (side_square + space)
          y = y_inicio + i * (side_square + space)
          contexto.rectangle(x, y, side_square, side_square)
          contexto.fill()

width = height = 200
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
ctx = cairo.Context(surface)

ctx.set_source_rgb(1, 1, 1)
ctx.paint()

# Some Colors
colors = [ 
    [1, 0, 0],
    [1, 1, 0],
    [0, 0, 1],
    [0, 1, 0],
    [0, 1, 1],
    [1, 0, 1]
]
random_color = colors[randint(0, len(colors) - 1)]

random_squares(ctx, width, random_color, 5) 

surface.write_to_png("./outputs/colors-tones.png")