import pyautogui
from PIL import Image

myScreenshot = pyautogui.screenshot() # take a screenshot

myScreenshot.save(r'vscode.png') # save screenshot

Image.open(r'vscode.png') # open screenshot
