#include <FastLED.h>

#define NUM_LEDS 200
#define LED_PIN 27

CRGB leds[NUM_LEDS];

void setup() {
  // put your setup code here, to run once:
FastLED.addLeds<WS2812B, LED_PIN, GRB>(leds, NUM_LEDS);
FastLED.setBrightness(10);
}

void loop() {
  // put your main code here, to run repeatedly:

  for (int i = 0; i< 200; i++) {
      leds[i] = CRGB::Green;
  }
  leds[0] = CRGB::Green;    
  FastLED.show();
}
