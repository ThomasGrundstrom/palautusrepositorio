from tekoaly import Tekoaly
from kps import KiviPaperiSakset


class KPSTekoaly(KiviPaperiSakset):
    def __init__(self):
        self.peli = KiviPaperiSakset()
        self.tekoaly = Tekoaly()

    def pelaa(self):
        return super().pelaa()

    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        return tokan_siirto
