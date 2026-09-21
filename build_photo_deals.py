import os
import urllib.request
from PIL import Image, ImageFilter, ImageOps

IMAGES_DIR = r"d:\ai\cook n roll\images"

# 1. Download real studio photo of standing cold drink on white background
drink_photo_url = "https://images.unsplash.com/photo-1622483767028-3f66f32aef97?auto=format&fit=crop&w=600&q=80"
drink_file = os.path.join(IMAGES_DIR, "drink.jpg")

try:
    urllib.request.urlretrieve(drink_photo_url, drink_file)
    print("Downloaded real standing drink photo to drink.jpg")
except Exception as e:
    print("Could not download drink photo:", e)

DEALS_CONFIG = [
    { "id": "deal_01", "items": ["shawarma.jpg", "shawarma.jpg", "drink.jpg"] },
    { "id": "deal_02", "items": ["shawarma.jpg", "drink.jpg"] },
    { "id": "deal_03", "items": ["zinger_burger.jpg", "fries.jpg", "drink.jpg"] },
    { "id": "deal_04", "items": ["zinger_burger.jpg", "zinger_burger.jpg", "fries.jpg", "drink.jpg"] },
    { "id": "deal_05", "items": ["zinger_burger.jpg", "broast.jpg", "drink.jpg"] },
    { "id": "deal_06", "items": ["zinger_burger.jpg", "pizza.jpg", "sandwich.jpg", "fries.jpg", "drink.jpg"] },
    { "id": "deal_07", "items": ["paratha_roll.jpg", "shawarma.jpg", "fries.jpg", "drink.jpg"] },
    { "id": "deal_08", "items": ["pizza.jpg", "shawarma.jpg", "fries.jpg", "drink.jpg"] },
    { "id": "deal_09", "items": ["shawarma.jpg", "shawarma.jpg", "drink.jpg"] },
    { "id": "deal_10", "items": ["zinger_burger.jpg", "shawarma.jpg", "pizza.jpg", "fries.jpg", "drink.jpg"] },
    { "id": "deal_11", "items": ["zinger_burger.jpg", "pizza.jpg", "nuggets.jpg", "fries.jpg", "drink.jpg"] },
    { "id": "deal_12", "items": ["zinger_burger.jpg", "pizza.jpg", "fries.jpg", "nuggets.jpg", "drink.jpg"] },
    { "id": "deal_13", "items": ["shawarma.jpg", "pizza.jpg", "nuggets.jpg", "fries.jpg", "drink.jpg"] },
    { "id": "deal_14", "items": ["pizza.jpg", "pizza.jpg", "drink.jpg"] },
    { "id": "deal_15", "items": ["pizza.jpg", "pizza.jpg", "drink.jpg"] },
    { "id": "deal_16", "items": ["pizza.jpg", "pizza.jpg", "drink.jpg"] },
    { "id": "deal_17", "items": ["pizza.jpg", "pizza.jpg", "drink.jpg"] },
    { "id": "deal_18", "items": ["pizza.jpg", "pizza.jpg", "drink.jpg"] }
]

def make_photo_deal_image(deal):
    canvas = Image.new("RGB", (600, 600), (255, 255, 255))
    items = deal["items"]
    n = len(items)

    # Calculate layout positions
    if n == 2:
        coords = [(100, 150, 260), (320, 150, 260)]
    elif n == 3:
        coords = [(50, 200, 240), (310, 200, 240), (180, 50, 240)]
    elif n == 4:
        coords = [(50, 50, 240), (310, 50, 240), (50, 310, 240), (310, 310, 240)]
    else: # 5 items
        coords = [(40, 40, 220), (340, 40, 220), (190, 190, 220), (40, 340, 220), (340, 340, 220)]

    for idx, img_name in enumerate(items):
        if idx >= len(coords):
            break
        x, y, sz = coords[idx]
        img_path = os.path.join(IMAGES_DIR, img_name)
        if os.path.exists(img_path):
            item_img = Image.open(img_path).convert("RGBA")
            item_img = ImageOps.fit(item_img, (sz, sz), Image.Resampling.LANCZOS)
            
            # Create smooth soft drop shadow underneath
            shadow = Image.new("RGBA", (sz + 20, sz + 20), (0, 0, 0, 0))
            shadow_draw = Image.new("RGBA", (sz, sz), (0, 0, 0, 35))
            shadow.paste(shadow_draw, (10, 10))
            shadow = shadow.filter(ImageFilter.GaussianBlur(12))
            
            # Composite shadow then item onto canvas
            canvas.paste(shadow, (x - 10, y - 5), shadow)
            canvas.paste(item_img, (x, y))

    save_path = os.path.join(IMAGES_DIR, f"{deal['id']}.jpg")
    canvas.convert("RGB").save(save_path, "JPEG", quality=95)
    print(f"Generated photographic deal image: {deal['id']}.jpg")

for deal in DEALS_CONFIG:
    make_photo_deal_image(deal)

print("ALL REAL RASTER PHOTOGRAPHIC DEAL IMAGES CREATED SUCCESSFULLY!")
