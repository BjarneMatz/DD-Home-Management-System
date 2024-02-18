import serial
import telegram_bot

# Seriellen Port öffnen
ser = serial.Serial('COM1', 9600)  # Hier den entsprechenden Port und Baudrate angeben

while True:
    # Daten vom Arduino lesen
    old_data = ""
    data = ser.readline().decode().strip()
    
    if old_data != data:
        if data == "1":
            telegram_bot.send_water_warning()
        old_data = data
    
    # Beispiel: Daten auf der Konsole ausgeben
    print(data)
    
# Seriellen Port schließen
ser.close()