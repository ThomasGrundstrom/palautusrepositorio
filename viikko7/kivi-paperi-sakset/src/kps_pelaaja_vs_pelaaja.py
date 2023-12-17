from kps import KiviPaperiSakset


class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def __init__(self):
        self.peli = KiviPaperiSakset()

    def pelaa(self):
        return super().pelaa()

    def _toisen_siirto(self, ensimmaisen_siirto):
        return input("Toisen pelaajan siirto: ")
