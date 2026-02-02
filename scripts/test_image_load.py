#!/usr/bin/env python3
import os
import pygame

path = os.path.join("imgs", "dungeon_crawl", "misc", "cursor.png")
print("CWD:", os.getcwd())
print("Exists:", os.path.exists(path))

pygame.init()
# create a small hidden display to allow convert_alpha()
pygame.display.set_mode((1, 1))
try:
    surf = pygame.image.load(path)
    print("Loaded OK (before convert):", type(surf))
    try:
        surf = surf.convert_alpha()
        print("convert_alpha OK")
    except Exception as e:
        print("convert_alpha failed:", repr(e))
except Exception as e:
    print("load failed:", repr(e))

pygame.quit()
