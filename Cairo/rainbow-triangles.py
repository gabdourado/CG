#!/home/gab/BCC/CG/env/bin/python

import cairo
import colorsys

def draw_triangle(context, vertices):

    context.move_to(vertices[0][0], vertices[0][1])
    context.line_to(vertices[1][0], vertices[1][1])
    context.line_to(vertices[2][0], vertices[2][1])
    context.close_path()

def lerp(a,b,t):
  return a*(1.0-t) + b*t

def lerp_rgb(rgb1, rgb2, t):
  return [lerp(rgb1[0], rgb2[0], t), lerp(rgb1[1], rgb2[1], t), lerp(rgb1[2], rgb2[2], t)]

def rainbow_triangles(context):
   
   h = 0.0

   for j in range(1, 1201, 200):

    rgb_init = colorsys.hls_to_rgb(h, 0.5, 1.0)
        
    h = (h + 0.166) % 1.0

    rgb_end = colorsys.hls_to_rgb(h, 0.5, 1.0)

    for i in range(10, 110, 10):

      [r,g,b] = lerp_rgb([rgb_init[0], rgb_init[1], rgb_init[2]], [rgb_end[0], rgb_end[1], rgb_end[2]], float(i)/100)

      context.set_source_rgba(r, g, b, 1)

      vertices = [(0+i+j, 100+i), (50+i+j, 0+i), (100+i+j, 100+i)]

      draw_triangle(context, vertices)

      context.fill_preserve()
      
      context.set_line_width(0)
      
      context.set_source_rgb(0, 0, 0)
      context.stroke()


width, height = 1220, 220
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
context = cairo.Context(surface)

context.set_source_rgb(1, 1, 1)
context.paint()

rainbow_triangles(context)

surface.write_to_png("./outputs/rainbow-triangles.png")