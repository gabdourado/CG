import cairo

# Linear Interpolation Function (LERP)
def lerp(a,b,t):
  return a*(1.0-t) + b*t

# Linear Interpolation Function + RGB
def lerp_rgb(rgb1, rgb2, t):
  return [lerp(rgb1[0], rgb2[0], t), lerp(rgb1[1], rgb2[1], t), lerp(rgb1[2], rgb2[2], t)]

# Function to draw a "matrix" of squares
def rainbow_squares(contexto, screen_w, rgbA, rgbB, rgbC, rgbD, num_squares, space = 10):
    
    side_square = int((screen_w - (num_squares + 1) * space) / num_squares)

    total_space = num_squares * side_square + (num_squares - 1) * space

    x_inicio = y_inicio = (screen_w - total_space) / 2
 
    for i in range(num_squares):
        
        rgb_init = lerp_rgb([rgbA[0], rgbA[1], rgbA[2]], [rgbC[0], rgbC[1], rgbC[2]], float(i)/(num_squares - 1))
        rgb_end = lerp_rgb([rgbB[0], rgbB[1], rgbB[2]], [rgbD[0], rgbD[1], rgbD[2]], float(i)/(num_squares - 1))

        for j in range(num_squares):
            
            [r, g, b] = lerp_rgb([rgb_init[0], rgb_init[1], rgb_init[2]], [rgb_end[0], rgb_end[1], rgb_end[2]], float(j)/(num_squares - 1))
            
            contexto.set_source_rgb(r, g, b)

            x = x_inicio + j * (side_square + space)
            y = y_inicio + i * (side_square + space)
            contexto.rectangle(x, y, side_square, side_square)
            contexto.fill()

# Create an image surface (RGBA format)
width = height = 200
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
ctx = cairo.Context(surface)

# Set the background to be white
ctx.set_source_rgb(1, 1, 1)
ctx.paint()

# Colors A, B, C, D
rgbA = [1, 0, 0] # Red
rgbB = [1, 1, 0] # Yellow
rgbC = [0, 0, 1] # Blue
rgbD = [0, 1, 0] # Gree

# Draw mutiples squares
rainbow_squares(ctx, width, rgbA, rgbB, rgbC, rgbD, 7, 5)

# Save the image
surface.write_to_png("./outputs/rainbow-squares.png")