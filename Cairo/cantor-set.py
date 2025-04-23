#!/home/gab/BCC/CG/env/bin/python

import cairo

def CantorSet(init_x, end_x, y, iterations):
    
    if iterations < 0:
        return

    context.move_to(init_x, y)
    context.line_to(end_x, y)
    context.stroke()

    v = (end_x - init_x)/3.0

    y += 10

    iterations -= 1

    CantorSet(init_x, init_x + v, y, iterations)
    CantorSet(end_x - v, end_x, y, iterations)

width, height = 1000, 100
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
context = cairo.Context(surface)

context.set_line_width(3)

context.set_source_rgb(1, 1, 1)
context.paint()

context.set_source_rgb(0,0,0)

init_x = y = 10
end_x = width - init_x

CantorSet(init_x, end_x, y, 7)

surface.write_to_png("./outputs/cantor-set.png")