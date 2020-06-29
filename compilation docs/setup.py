import cx_Freeze
from cx_Freeze import *


# CONFIGURAÇÕES DO MSI
# shortcut_table = [
#     ("Unicorn Mazer",        # Shortcut
#      "DesktopFolder",          # Directory_
#      "Unicorn Mazer",           # Name
#      "C:/Program Files (x86)/Unicorn Mazer",              # Component_
#      "C:/Program Files (x86)/Unicorn Mazer/Unicorn Mazer.exe",# Target
#      None,                     # Arguments
#      None,                     # Description
#      None,                     # Hotkey
#      None,                     # Icon
#      None,                     # IconIndex
#      None,                     # ShowCmd
#      "C:/Program Files (x86)/Unicorn Mazer"               # WkDir
#      )
#     ]


# shortcut_table = [
#     ("DesktopShortcut",        # Shortcut
#      "DesktopFolder",          # Directory_
#      "Unicorn Mazer",           # Name
#      "TARGETDIR",              # Component_
#      "[TARGETDIR]Unicorn Mazer.exe",# Target
#      None,                     # Arguments
#      None,                     # Description
#      None,                     # Hotkey
#      None,                     # Icon
#      None,                     # IconIndex
#      None,                     # ShowCmd
#      'ProgramFiles64Folder'               # WkDir
#      )
# ]


# # CONFIGURAÇÕES DO EXE
# build_exe_options = {
#     'packages': ['pygame', 'random','sys'],

#     'include_files': ['big_cof.png','big_cup.png','big_mino.png','big_uni.png','big_uni_right.png','big_uni_left.png',
#     'build_sound.wav','cof.png','cof_sound.wav','cup.png','dead.png','death.wav','giant_cup.png','icone.ico','intro.wav',
#     'lose.wav','mino.png','start_image.png','tema.wav','uni.png','uni.png','uni_left.png','uni_right.png','win.wav'],
    
#     'include_msvcr': True,
# }



# GERADOR
setup(

    name = "Perfect Aim",
    version = "1.0",
    author = "Gustavo Pimenta",
    description='[gustavopimenta.gp@gmail.com]',
    # options = {"build_exe":build_exe_options, "build_msi":build_msi_options},
    executables=[

            Executable(

                "perfect_aim.pyw",
                icon="icone.ico",
                # base = "Win32GUI",
                # shortcutName="Unicorn Mazer",
                # shortcutDir="DesktopFolder"

            )
    ]

)
