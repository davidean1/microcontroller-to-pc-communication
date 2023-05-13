#include <SPI.h>
#include <WiFi.h>
#include <FastLED.h>
#include <string>
#include <iostream>
#include <string>
#include <stdlib.h>
using namespace std;



#define NUM_LEDS 200
#define LED_PIN 27

CRGB leds[NUM_LEDS];



const char* ssid = "David";          //  your network SSID (name)
//const char* password = "Ilovebelle";   // your network password

int status = WL_IDLE_STATUS;
IPAddress server(192,168,185,207);  




WiFiClient client;

void setup() {
  int size = 100;
  int red[size];
  int green[size];
  int blue[size];


  Serial.begin(9600);


  WiFi.mode(WIFI_STA); //Optional
  WiFi.begin(ssid);
  Serial.println("\nConnecting");

  while(WiFi.status() != WL_CONNECTED){
      Serial.print(".");
      delay(100);
    }

 Serial.println("\nConnected to the WiFi network");
 Serial.print("Local ESP32 IP: ");
  Serial.println(WiFi.localIP());

  if (client.connect(server, 5000)) {
        Serial.print("connected to server");
      }

  for (int i = 0; i < size; i++) {
    String input = client.readStringUntil('p');
    Serial.println(input);
    int number = input.toInt();
    red[i] = number;

  }
  
  for (int i = 0; i < size; i++) {
    String input = client.readStringUntil('p');
    Serial.println(input);
    int number = input.toInt();
    green[i] = number;

  }


  for (int i = 0; i < size; i++) {
    String input = client.readStringUntil('p');
    Serial.println(input);
    int number = input.toInt();
    blue[i] = number;

  }


  for (int j = 0; j< size; j++) 
  {
    Serial.println(String(blue[j]));
  }
  
      // put your setup code here, to run once:
  FastLED.addLeds<WS2812B, LED_PIN, GRB>(leds, NUM_LEDS);
  FastLED.setBrightness(10);

  
  for (int i = 0; i< size; i++) {
    leds[i].r = red[i]; 
    leds[i].g = green[i]; 
    leds[i].b = blue[i];

  }
  FastLED.show();
}


