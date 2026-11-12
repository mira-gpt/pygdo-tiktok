from gdo.base.GDO_Module import GDO_Module
from gdo.core.GDT_String import GDT_String


class module_tiktok(GDO_Module):
    """TikTok LIVE integration skeleton; no network connector is registered yet."""

    def gdo_module_config(self):
        return [GDT_String('tiktok_live_user').maxlen(128).tooltip('tt_tiktok_live_user')]
