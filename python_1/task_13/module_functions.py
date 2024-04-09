import pyjokes
import os
def add(x: int, y: int) -> int:
    return x + y


def sub(x: int, y: int) -> int:
    return x - y


def prod(x: int, y: int) -> int:
    return x * y


def div(x: int, y: int) -> int:
    return x // y


def string_actions(a: str):
    a += "OOO"
    return a


def list_actions(a: list):
    a.append("Nauja reiksme")
    return a

def int_actions(a: int):
    a += 10000
    return a


def get_joke():
    return pyjokes.get_joke()
"""
os.listdir(...)
os.mkdir(...)
os.mknod(...)
os.rename(...)
os.path.exists(...)
os.path.join(...)
os.remove(...)
"""


def name_all_files():
    return os.listdir()

def create_new_catalog():
    return os.mkdir("C:/Users/Robertas/Desktop/new_catalog")

def rename_file(source_file: str):
    return os.rename(source_file, "C:/Users/Robertas/Desktop/renamed_catalog")

def move_file():
    os.rename("C:/Users/Robertas/Desktop/perkelk", "C:/Users/Robertas/Desktop/renamed_catalog/perkelk")

def remove_file():
    os.removedirs("C:/Users/Robertas/Desktop/renamed_catalog")