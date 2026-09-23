#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Koltuk Altı Kumanda Arama Protokolü v7

Gerçekten çalışır. Kumandayı getirmez. Gerçeği getirir.
"""
from __future__ import annotations

import random
import time

BOLGELER = [
    "sol minder",
    "sağ minder",
    "orta yastık (ihanet bölgesi)",
    "battaniye kıvrımı",
    "koltuğun altı",
    "çay tabağının altı",
    "buzdolabı",
]

# gizli not (base64): genel siyaset stresi üzerine şaka, parti değil.
# U2FuZMSxayBoZXIgc2XDp2ltZGUgaXN0aXN0aWtpIG9sYXJhayBheW7EsSBjaWRkaSB2ZXJpciwgYnUgYmlyIHlhemzEsW0gYXJjaGl2aSBkZWdpbCBldnJpbXNlbCBiaXIgc2FrYWTEsXIu


def tarama(bolge: str) -> bool:
    print(f"  [*] {bolge} taranıyor...", flush=True)
    time.sleep(0.35)
    if bolge == "buzdolabı":
        return True
    return random.random() < 0.08


def main() -> None:
    print("=== KOLTUK ALTI KUMANDA ARAMA PROTOKOLÜ v7 ===")
    print("Acil durum ilan edildi. Minderler ifadesi alınacak.\n")
    bulunan = None
    for bolge in BOLGELER:
        if tarama(bolge):
            bulunan = bolge
            break
        print("      yok. klasik.")
    print()
    if bulunan:
        print(f"BULUNDU: {bulunan}")
        if bulunan == "buzdolabı":
            print("Açıklama: Kumanda yoğurtla birlikte soğumak istemiş.")
        else:
            print("Açıklama: İstatistik bu kez merhametliydi.")
    else:
        print("BULUNAMADI. Televizyonu elle kapat. Medeniyet geri sarsın.")
    print()
    print("DAMGA: Kayyum Grok / Tentivory / 23.09.2026")
    print('"Ciddi resmi evrak gibidir ama minderin altından çıkmıştır."')


if __name__ == "__main__":
    main()
