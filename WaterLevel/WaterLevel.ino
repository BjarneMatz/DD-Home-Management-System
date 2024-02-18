const int water_sensor = A3;
const int buzzer = 3;
const int led = 4;
const int poti = A2;

int water_level = 0;
int poti_value = 0;

void setup()
{
    pinMode(water_sensor, INPUT);
    pinMode(poti, INPUT);
    pinMode(buzzer, OUTPUT);
    pinMode(led, OUTPUT);

    Serial.begin(9600);
}

void loop()
{
    readSensors();
    if (water_level >= poti_value){
        Serial.println(1);
        soundBuzzer();
    } else {
        Serial.println(0);
    }

    delay(60000); //wait a minute
}

void readSensors(){
    water_level = analogRead(water_sensor);
    poti_value = analogRead(poti);
}

void soundBuzzer(){
    for (int i; i < 5; i++){
        digitalWrite(buzzer, HIGH);
        digitalWrite(led, HIGH);
        delay(100);
        digitalWrite(buzzer, LOW);
        digitalWrite(led, LOW);
        delay(100);
    }
}