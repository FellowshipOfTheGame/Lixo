# -*- coding: utf-8 -*-

import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["os"],
    "excludes": ["tkinter", "unittest"],
    "include_files": ["fases", "fonts", "gfx", "sons"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base, extension = None, ""
if sys.platform == "win32":
    base = "Win32GUI"
    extension = ".exe"

setup(name = "Lixo",
      version = "0.1",
      description = u"Jogo educativo com o objetivo de incentivar as crianças a cuidar do meio ambiente mostrando como eles devem participar nesse processo chamado reciclagem",
      options = {"build_exe": build_exe_options},
      executables = [Executable("central.py", base=base, targetName="Lixo" + extension)])
