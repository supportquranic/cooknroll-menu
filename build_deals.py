import os
from PIL import Image, ImageDraw, ImageFont, ImageOps

IMAGES_DIR = r"d:\ai\cook n roll\images"

# 1. Create a clean drink image if it doesn't exist
drink_path = os.path.join(IMAGES_DIR, "drink.jpg")
if not os.path.exists(drink_path):
    img = Image.new("RGB", (400, 400), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    # Draw bottle shape
    # Cap
    draw.rectangle([170, 40, 230, 70], fill=(220, 38, 38))
    # Neck
    draw.polygon([(180, 70), (220, 70), (240, 140), (160, 140)], fill=(30, 41, 59))
    # Body
    draw.rounded_rectangle([150, 140, 250, 360], radius=20, fill=(30, 41, 59))
    # Label
    draw.rectangle([150, 200, 250, 280], fill=(220, 38, 38))
    # Text
    draw.text((165, 225), "COLD\nDRINK", fill=(255, 255, 255))
    img.save(drink_path)
    print("Created drink.jpg")

DEALS_CONFIG = [
    {
        "id": "deal_01",
        "title": "DEAL 01",
        "items": [("shawarma.jpg", "5x Chicken Shawarma"), ("drink.jpg", "1.5L Cold Drink")],
        "desc": "5 Shawarmas + 1.5L Drink"
    },
    {
        "id": "deal_02",
        "title": "DEAL 02",
        "items": [("shawarma.jpg", "2x Zinger Shawarma"), ("drink.jpg", "500ml Cold Drink")],
        "desc": "2 Zinger Shawarma + 500ml Drink"
    },
    {
        "id": "deal_03",
        "title": "DEAL 03",
        "items": [("zinger_burger.jpg", "2x Zinger Burger"), ("fries.jpg", "1x Regular Fries"), ("drink.jpg", "500ml Cold Drink")],
        "desc": "2 Zinger + Fries + 500ml Drink"
    },
    {
        "id": "deal_04",
        "title": "DEAL 04",
        "items": [("zinger_burger.jpg", "5x Zinger Burger"), ("fries.jpg", "1x Large Fries"), ("drink.jpg", "1.5L Cold Drink")],
        "desc": "5 Zinger + Large Fries + 1.5L Drink"
    },
    {
        "id": "deal_05",
        "title": "DEAL 05",
        "items": [("zinger_burger.jpg", "2x Zinger Burger"), ("broast.jpg", "Quarter Broast"), ("drink.jpg", "1L Cold Drink")],
        "desc": "2 Zinger + Broast + 1L Drink"
    },
    {
        "id": "deal_06",
        "title": "DEAL 06",
        "items": [("zinger_burger.jpg", "2x Zinger"), ("sandwich.jpg", "1x Sandwich"), ("pizza.jpg", "1x 8\" Pizza"), ("fries.jpg", "1x Fries"), ("drink.jpg", "1.5L Drink")],
        "desc": "2 Zinger + Sandwich + Pizza + Fries + Drink"
    },
    {
        "id": "deal_07",
        "title": "DEAL 07",
        "items": [("paratha_roll.jpg", "1x Wrap"), ("shawarma.jpg", "1x Shawarma"), ("fries.jpg", "1x Fries"), ("drink.jpg", "1L Cold Drink")],
        "desc": "Wrap + Shawarma + Fries + 1L Drink"
    },
    {
        "id": "deal_08",
        "title": "DEAL 08",
        "items": [("pizza.jpg", "10\" Medium Pizza"), ("shawarma.jpg", "4x Shawarma"), ("fries.jpg", "1x Fries"), ("drink.jpg", "1.5L Cold Drink")],
        "desc": "Pizza + 4 Shawarma + Fries + Drink"
    },
    {
        "id": "deal_09",
        "title": "DEAL 09",
        "items": [("shawarma.jpg", "5x Zinger Shawarma"), ("drink.jpg", "1.5L Cold Drink")],
        "desc": "5 Zinger Shawarma + 1.5L Drink"
    },
    {
        "id": "deal_10",
        "title": "DEAL 10",
        "items": [("zinger_burger.jpg", "2x Zinger"), ("shawarma.jpg", "2x Zinger Shawarma"), ("pizza.jpg", "8\" Pizza"), ("fries.jpg", "1x Fries"), ("drink.jpg", "1.5L Drink")],
        "desc": "2 Zinger + 2 Shawarma + Pizza + Fries + Drink"
    },
    {
        "id": "deal_11",
        "title": "DEAL 11",
        "items": [("zinger_burger.jpg", "2x Zinger"), ("pizza.jpg", "2x Pizzas (8\" & 10\")"), ("fries.jpg", "Large Fries"), ("nuggets.jpg", "5x Nuggets"), ("drink.jpg", "2.25L Drink")],
        "desc": "2 Zinger + 2 Pizzas + Fries + Nuggets + Drink"
    },
    {
        "id": "deal_12",
        "title": "DEAL 12",
        "items": [("zinger_burger.jpg", "4x Zinger"), ("pizza.jpg", "13\" Large Pizza"), ("fries.jpg", "Large Fries"), ("nuggets.jpg", "5x Nuggets"), ("drink.jpg", "2.25L Drink")],
        "desc": "4 Zinger + 13\" Pizza + Fries + Nuggets + Drink"
    },
    {
        "id": "deal_13",
        "title": "DEAL 13",
        "items": [("shawarma.jpg", "2x Shawarma Platter"), ("nuggets.jpg", "5x Hot Wings"), ("pizza.jpg", "8\" Pizza"), ("fries.jpg", "1x Fries"), ("drink.jpg", "1.5L Drink")],
        "desc": "2 Platters + 5 Wings + Pizza + Fries + Drink"
    },
    {
        "id": "deal_14",
        "title": "DEAL 14",
        "items": [("pizza.jpg", "3x 6\" Small Pizzas"), ("drink.jpg", "1.5L Cold Drink")],
        "desc": "3 Small Pizzas + 1.5L Drink"
    },
    {
        "id": "deal_15",
        "title": "DEAL 15",
        "items": [("pizza.jpg", "3x 8\" Regular Pizzas"), ("drink.jpg", "1.5L Cold Drink")],
        "desc": "3 Regular Pizzas + 1.5L Drink"
    },
    {
        "id": "deal_16",
        "title": "DEAL 16",
        "items": [("pizza.jpg", "3x 10\" Medium Pizzas"), ("drink.jpg", "1.5L Cold Drink")],
        "desc": "3 Medium Pizzas + 1.5L Drink"
    },
    {
        "id": "deal_17",
        "title": "DEAL 17",
        "items": [("pizza.jpg", "3x 13\" Large Pizzas"), ("drink.jpg", "2.5L Cold Drink")],
        "desc": "3 Large Pizzas + 2.5L Drink"
    },
    {
        "id": "deal_18",
        "title": "DEAL 18",
        "items": [("pizza.jpg", "3x 16\" Family Pizzas"), ("drink.jpg", "2.25L Cold Drink")],
        "desc": "3 Family Pizzas + 2.25L Drink"
    }
]

# Try loading a system font
try:
    font_large = ImageFont.truetype("arial.ttf", 28)
    font_bold = ImageFont.truetype("arialbd.ttf", 22)
    font_small = ImageFont.truetype("arial.ttf", 16)
except:
    font_large = font_bold = font_small = ImageFont.load_default()

def create_deal_image(deal):
    canvas = Image.new("RGB", (600, 600), (255, 255, 255))
    draw = ImageDraw.Draw(canvas)
    
    # 1. Top Red Header Bar
    draw.rectangle([0, 0, 600, 70], fill=(220, 38, 38))
    draw.text((25, 18), deal["title"], fill=(255, 255, 255), font=font_large)
    draw.text((180, 24), "SPECIAL COMBO DEAL", fill=(254, 202, 202), font=font_small)

    # 2. Outer Border
    draw.rectangle([0, 0, 599, 599], outline=(226, 232, 240), width=3)
    
    items = deal["items"]
    num_items = len(items)
    
    # Layout item grid
    if num_items <= 2:
        cols, rows = num_items, 1
    elif num_items <= 4:
        cols, rows = 2, 2
    else:
        cols, rows = 3, 2

    box_w = 540 // cols
    box_h = 420 // rows

    start_x = (600 - (cols * box_w)) // 2
    start_y = 90

    for idx, (img_name, label) in enumerate(items):
        r = idx // cols
        c = idx % cols

        x = start_x + c * box_w
        y = start_y + r * box_h

        # Load item image
        img_file = os.path.join(IMAGES_DIR, img_name)
        if os.path.exists(img_file):
            item_img = Image.open(img_file).convert("RGB")
            # Resize keeping ratio
            thumb_size = min(box_w - 30, box_h - 60)
            item_img = ImageOps.fit(item_img, (thumb_size, thumb_size), Image.Resampling.LANCZOS)
            
            # Center item image
            img_x = x + (box_w - thumb_size) // 2
            img_y = y + 10
            canvas.paste(item_img, (img_x, img_y))

        # Item Card Background / Badge
        text_bbox = draw.textbbox((0, 0), label, font=font_small)
        text_w = text_bbox[2] - text_bbox[0]
        text_h = text_bbox[3] - text_bbox[1]
        
        lbl_x = x + (box_w - text_w - 20) // 2
        lbl_y = y + box_h - 35
        
        # Pill badge for label
        draw.rounded_rectangle([lbl_x, lbl_y, lbl_x + text_w + 20, lbl_y + 26], radius=8, fill=(241, 245, 249), outline=(203, 213, 225))
        draw.text((lbl_x + 10, lbl_y + 3), label, fill=(15, 23, 42), font=font_small)

    # Footer Banner
    draw.rectangle([0, 530, 600, 600], fill=(248, 250, 252))
    draw.line([(0, 530), (600, 530)], fill=(226, 232, 240), width=1)
    
    desc_bbox = draw.textbbox((0, 0), deal["desc"], font=font_bold)
    desc_w = desc_bbox[2] - desc_bbox[0]
    draw.text(((600 - desc_w) // 2, 550), deal["desc"], fill=(220, 38, 38), font=font_bold)

    save_path = os.path.join(IMAGES_DIR, f"{deal['id']}.jpg")
    canvas.save(save_path, "JPEG", quality=95)
    print(f"Generated {deal['id']}.jpg")

for deal in DEALS_CONFIG:
    create_deal_image(deal)

print("ALL DEAL IMAGES GENERATED SUCCESSFULLY!")
