import get_resin_info
import create_info_image
import asyncio
import genshin

genshin_resin,is_genshin_expedition_finished,is_genshin_commission_finished,starrail_stamina,is_starrail_expedition_finished,is_starrail_commission_finished = asyncio.run(get_resin_info.get_resin_info())
create_info_image.create_info_image(genshin_resin,is_genshin_expedition_finished,is_genshin_commission_finished,starrail_stamina,is_starrail_expedition_finished,is_starrail_commission_finished)
#print(genshin_resin,is_genshin_expedition_finished,is_genshin_commission_finished,starrail_stamina,is_starrail_expedition_finished,is_starrail_commission_finished)
