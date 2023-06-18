import get_resin_info
import asyncio
import genshin

genshin_resin,starrail_resin = asyncio.run(get_resin_info.get_resin_info())
print(genshin_resin,starrail_resin)
