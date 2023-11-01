from contextlib import AbstractContextManager
from typing import Any
import unittest
from statistics_service import StatisticsService
from player import Player
from statistics_service import SortBy

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_haku_toimii(self):
        self.assertEqual(self.stats.search("Kurri").name, "Kurri")
        self.assertEqual(self.stats.search("Kurri").team, "EDM")
        self.assertEqual(self.stats.search("Kurri").goals, 37)
        self.assertEqual(self.stats.search("Kurri").assists, 53)
    
    def test_vaaralla_nimella_pelaajaa_ei_loydy(self):
        self.assertEqual(self.stats.search("abc"), None)
    
    def test_tiimin_haku_toimii(self):
        self.assertEqual(self.stats.team("EDM")[0].name, "Semenko")
        self.assertEqual(self.stats.team("EDM")[1].name, "Kurri")
        self.assertEqual(self.stats.team("EDM")[2].name, "Gretzky")
    
    def test_tiimia_ei_loydy(self):
        self.assertEqual(self.stats.team("abc"), [])
    
    def test_pelaajien_jarjestaminen_pisteiden_mukaan(self):
        self.assertEqual(len(self.stats.top(2)), 3)
        self.assertEqual(self.stats.top(2)[0].name, "Gretzky")
        self.assertEqual(self.stats.top(2)[1].name, "Lemieux")
        self.assertEqual(self.stats.top(2)[2].name, "Yzerman")
    
    def test_pelaajien_jarjestaminen_nolla_pelaajaa(self):
        self.assertEqual(self.stats.top(-1), [])
    
    def test_pelaajien_jarjestaminen_maalien_mukaan(self):
        self.assertEqual(len(self.stats.top(2, SortBy.GOALS)), 3)
        self.assertEqual(self.stats.top(2, SortBy.GOALS)[0].name, "Lemieux")
        self.assertEqual(self.stats.top(2, SortBy.GOALS)[1].name, "Yzerman")
        self.assertEqual(self.stats.top(2, SortBy.GOALS)[2].name, "Kurri")
    
    def test_pelaajien_jarjestaminen_syottojen_mukaan(self):
        self.assertEqual(len(self.stats.top(2, SortBy.ASSISTS)), 3)
        self.assertEqual(self.stats.top(2, SortBy.ASSISTS)[0].name, "Gretzky")
        self.assertEqual(self.stats.top(2, SortBy.ASSISTS)[1].name, "Yzerman")
        self.assertEqual(self.stats.top(2, SortBy.ASSISTS)[2].name, "Lemieux")