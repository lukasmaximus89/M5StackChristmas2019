from m5stack import *
from m5ui import *

setScreenColor(lcd.BLACK)

lcd.font(lcd.FONT_Minya)
lcd.print('Merry Christmas',0,0,lcd.RED)
lcd.fillTriangle(100, 80, 200, 80, 150, 20 , lcd.GREEN)
lcd.fillTriangle(80, 140, 220, 140, 150, 60 , lcd.GREEN)
lcd.fillTriangle(60, 180, 240, 180, 150, 120 , lcd.GREEN)
lcd.fillCircle(102, 144, 15, lcd.BLUE)
lcd.fillCircle(190, 110, 15, lcd.RED)
lcd.fillCircle(152, 50, 15, lcd.NAVY)
lcd.fillRect(142, 181, 30, 60, lcd.MAROON)

