from PIL import Image, ImageFilter, ImageEnhance, ImageDraw
import os

try:
    if os.path.exists("FOndo.png"):
        img = Image.open("FOndo.png").convert("RGBA")
        
        # 1. Oscurecer la imagen al 40% (0.4)
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(0.4)
        
        # 2. Difuminar los bordes ligeramente (vignette effect).
        # We will create an alpha mask that is blurred and use it to blend with black
        width, height = img.size
        mask = Image.new('L', (width, height), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((width*0.1, height*0.1, width*0.9, height*0.9), fill=255)
        mask = mask.filter(ImageFilter.GaussianBlur(100))
        
        black_bg = Image.new('RGBA', (width, height), (0, 0, 0, 255))
        result = Image.composite(img, black_bg, mask)
        
        # Save as png
        result.save("FOndo_dark.png")
        print("Fondo dark creado exitosamente.")
    else:
        print("FOndo.png no encontrado.")
except Exception as e:
    print("Error:", e)
