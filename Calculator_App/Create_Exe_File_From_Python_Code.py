
import PyInstaller.__main__


# Use this python program to create exe files from python pgograms

PyInstaller.__main__.run([
    'Calculator.py',
    '--onefile',
    '--windowed'
])