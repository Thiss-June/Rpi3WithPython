#-*-coding:utf-8-*-

# 필요한 라이브러리를 불러옵니다. 
import time
import Adafruit_GPIO.SPI as SPI #oled spi 
import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont
import Adafruit_DHT

# OLED 128X64 ( spi_address = 연결된 OLED 주소 ) 인스턴스 disp 생성
disp = Adafruit_SSD1306.SSD1306_128_64(rst=24, dc=23, spi=SPI.SpiDev(0, 0, max_speed_hz=8000000))

# disp 초기화 
disp.begin()

# 화면 클리어 
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# 디폴트 폰트 불러오기
#font = ImageFont.load_default()
font = ImageFont.truetype('VCR_OSD_MONO.ttf', 16)

sensor = Adafruit_DHT.DHT11
pin = 14  #BCM 14


while True:
    # 온도, 압력, 고도 값을 읽어서 변수에 저장
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    
    # 측정값을 출력 (터미널) 
    print('Temp = {0:0.2f} *C'.format(temperature))
    print('Humi = {0:0.2f} %'.format(humidity))

    # OLED에 화면 표시 내용 
    draw.text((x,top),   'Temp = {0:0.2f} *C'.format(temperature), font=font, fill=255)
    draw.text((x,top+16), 'Humi = {0:0.2f} %'.format(humidity),font=font, fill=255)

    # 화면 표시 
    disp.image(image)
    disp.display()
    # 딜레이 시간 2초 
    time.sleep(2) 


