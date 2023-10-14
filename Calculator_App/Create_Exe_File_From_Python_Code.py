
import PyInstaller.__main__


# Use this python program to create an exe files from your python pgograms

PyInstaller.__main__.run([
    'Calculator.py',
    '--onefile',
    '--windowed'
])
