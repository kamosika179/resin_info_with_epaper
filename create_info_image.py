import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

def create_info_image(genshin_resin,is_genshin_expedition,is_genshin_daily,starrail_stamina,is_starrail_expedition,is_starrail_daily):

    # genshin,starrail,stamina information
    max_genshin_resin = 160
    max_starrail_stamina = 180

    # Load image
    base_img = Image.new('RGB', (250,128), 'white') .convert("RGB")
    paimon_icon = Image.open('images/paimon_icon.png')
    pam_icon = Image.open('images/pam_icon.png')
    daily_icon = Image.open('images/daily_icon.png')
    exclamation_mark = Image.open('images/exclamation_mark.png')
    person_icon = Image.open('images/person_icon.png')

    
    # Resize image
    paimon_icon = paimon_icon.resize((43,43))
    pam_icon = pam_icon.resize((43,43))
    genshin_daily_icon = daily_icon.resize((43,43))
    genshin_person_icon = person_icon.resize((43,43))
    starrail_daily_icon = daily_icon.resize((43,43))
    starrail_person_icon = person_icon.resize((43,43))
    exclamation_mark = exclamation_mark.resize((43,43))
    
        
    # Paste image
    base_img.paste(paimon_icon, (62,0),mask=paimon_icon)
    base_img.paste(pam_icon, (168,0),mask=pam_icon)
    base_img.paste(genshin_daily_icon, (42,85),mask=genshin_daily_icon)
    base_img.paste(genshin_person_icon, (82,85),mask=genshin_person_icon)
    base_img.paste(starrail_daily_icon, (148,85),mask=starrail_daily_icon)
    base_img.paste(starrail_person_icon, (188,85),mask=starrail_person_icon)

    # exclamation_mark
    if is_genshin_daily == False:
        base_img.paste(exclamation_mark, (52,75),mask=exclamation_mark)
    if is_genshin_expedition:
        base_img.paste(exclamation_mark, (92,75),mask=exclamation_mark)
    if is_starrail_daily == False:
        base_img.paste(exclamation_mark, (158,75),mask=exclamation_mark)
    if is_starrail_expedition:
        base_img.paste(exclamation_mark, (198,75),mask=exclamation_mark)
    
    # Draw text
    draw = ImageDraw.Draw(base_img) 
    #font = ImageFont.load_default()
    font = ImageFont.truetype('IPAexfont00401/ipaexg.ttf',20)
    #genshin resin information
    draw.text((82, 55), f"/{max_genshin_resin}", (0, 0, 0), font=font)
    if genshin_resin == max_genshin_resin:
        draw.text((42, 55), f"{genshin_resin}", (255, 0, 0), font=font)
    else:
        draw.text((42, 55), f"{genshin_resin}", (0, 0, 0), font=font)
    #starrail stamina information
    draw.text((188, 55), f"/{max_starrail_stamina}", (0, 0, 0), font=font)
    if starrail_stamina == max_starrail_stamina:
        draw.text((148, 55), f"{starrail_stamina}", (255, 0, 0), font=font)
    else:
        draw.text((148, 55), f"{starrail_stamina}", (0, 0, 0), font=font)
    
               
   

    # Save image
    base_img.save('info.png')
    return 'info.png'

if __name__ == "__main__":
    create_info_image(genshin_resin=160,is_genshin_daily=True,is_genshin_expedition=True,starrail_stamina=180,is_starrail_daily=True,is_starrail_expedition=True)
