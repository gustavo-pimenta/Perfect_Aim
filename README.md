# Perfect Aim

Perfect Aim is a hack tool for FPS games.
You can stabilize your aim controlling tha recoil and the fire rate.

3 different versions to use:

Version 1 Perfect Aim (VK version) - uses virtual keys, for simple games (faster than other versions) 
Version 2 Perfect Aim (Ctypes) - uses C language to call DirectInput commands for DirectX games (the best version)
Version 3 Perfect Aim (PyDirectInput) - uses DirectInput commands for DirectX games (slow version)

All versions works fine, you can use the EXE file or the python script.
Test wich one is the best for you.

---------------------------------------------------------------------------------------------------------------------

The first version was made using the libs:
Pynput - Mouse events listener and automation control
PySimpleGUI - User interface

But this first version can't control the mouse inside games because of DirectX.
Automation libs as Pynput and PyAutoGUI send commands as VK (virtual keys). 
New games ignore VK commands to avoid bots, they just accept DirectInput commands.

Two new versions were made to get DirectInput commands, using two different libs: PyDirectInput and Ctypes
PyDirectInput just take the PyAutoGUI VK commands and make DirectInput commands.
Ctypes ensures compatibility with C and allow to call functions in DDL.






