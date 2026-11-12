import unittest

from gdo.tiktok.module_tiktok import module_tiktok


class TestTikTokSkeleton(unittest.TestCase):
    def test_creator_setting_exists(self):
        settings = module_tiktok().gdo_module_config()
        self.assertEqual(['tiktok_live_user'], [setting.get_name() for setting in settings])
