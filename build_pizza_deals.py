import os
from PIL import Image, ImageDraw, ImageFilter, ImageOps, ImageFont

IMAGES_DIR = r"d:\ai\cook n roll\images"
pizza_path = os.path.join(IMAGES_DIR, "pizza.jpg")
drink_path = os.path.join(IMAGES_DIR, "drink.jpg")

# Deal 14: 3x Small Pizza 6" + 1.5L Drink
# Deal 15: 3x Regular Pizza 8" + 1.5L Drink
# Deal 16: 3x Medium Pizza 10" + 1.5L Drink
# Deal 17: 3x Large Pizza 13" + 2.5L Drink
# Deal 18: 3x Family Pizza 16" + 2.25L Drink

pizza_deals = [
    {"id": "deal_14", "size": '3x 6" Small Pizzas', "badge": '6" Small'},
    {"id": "deal_15", "size": '3x 8" Regular Pizzas', "badge": '8" Regular'},
    {"id": "deal_16", "size": '3x 10" Medium Pizzas', "badge": '10" Medium'},
    {"id": "deal_17", "size": '3x 13" Large Pizzas', "badge": '13" Large'},
    {"id": "deal_18", "size": '3x 16" Family Pizzas', "badge": '16" Family XL'},
]

pizza_base = Image.open(pizza_path).convert("RGBA")
drink_base = Image.open(drink_path).convert("RGBA")

try:
    font_bold = ImageFont.truetype("arialbd.ttf", 24)
    font_small = ImageFont.truetype("arialbd.ttf", 18)
except:
    font_bold = font_small = ImageFont.load_default()

for pd in pizza_deals:
    canvas = Image.new("RGBA", (800, 800), (255, 255, 255, 255))
    
    # 3 Pizzas arranged in aesthetic triangle layout + drink
    # Pizza 1: top-left (sz 340)
    # Pizza 2: bottom-left (sz 340)
    # Pizza 3: top-center/right (sz 340)
    # Drink: right-center (height 480)
    
    # Resize drink
    d_w, d_h = int(240 * (drink_base.width / drink_base.height)), 480
    d_img = drink_base.resize((240, 480), Image.Resampling.LANCZOS)
    
    # Resize pizza
    p_img = pizza_base.resize((320, 320), Image.Resampling.LANCZOS)
    
    # Create shadow helper
    def add_shadow_and_paste(canv, item, pos):
        w, h = item.size
        sh = Image.new("RGBA", (w + 40, h + 40), (0, 0, 0, 0))
        sh_draw = Image.new("RGBA", (w, h), (0, 0, 0, 30))
        sh.paste(sh_draw, (20, 20))
        sh = sh.filter(ImageFilter.GaussianBlur(16))
        canv.paste(sh, (pos[0] - 20, pos[1] - 10), sh)
        canv.paste(item, pos, item)

    # Paste pizzas
    add_shadow_and_paste(canvas, p_img, (30, 40))
    add_shadow_and_paste(canvas, p_img, (240, 40))
    add_shadow_and_paste(canvas, p_img, (130, 380))
    
    # Paste drink on the right
    add_shadow_and_paste(canvas, d_img, (520, 240))
    
    # Add modern sleek badge in bottom left
    draw = ImageDraw.Draw(canvas)
    
    # Draw pill badge
    badge_text = pd["size"] + " + 1.5L Drink"
    bbox = draw.textbbox((0, 0), badge_text, font=font_bold)
    bw = bbox[2] - bbox[0]
    
    draw.rounded_rectangle([30, 720, 30 + bw + 36, 770], radius=12, fill=(220, 38, 38, 255))
    draw.text((48, 732), badge_text, fill=(255, 255, 255, 255), font=font_bold)

    final_rgb = canvas.convert("RGB")
    out_file = os.path.join(IMAGES_DIR, f"{pd['id']}.jpg")
    final_rgb.save(out_file, "JPEG", quality=95)
    print(f"Generated clean photographic {pd['id']}.jpg")

print("Deals 14-18 generated successfully!")
