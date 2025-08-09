#include <Servo.h>

Servo motor;

void setup() {
  Serial.begin(9600);
  motor.attach(9); // Servo motor on pin 9
  motor.write(115); // Start at center
}

void loop() {
  if (Serial.available()) {
    String command = Serial.readStringUntil('\n');
    command.trim();

    if (command == "recycle") {
      Serial.println("Recycling - Turning right");
      delay(1000);
      motor.write(180);  // Right
      delay(1000);
      motor.write(115); // Back to center

    } else if (command == "non-recycle") {
      Serial.println("Non-Recyclable - Turning left");
      delay(1000);
      motor.write(0); // Left
      delay(1000);
      motor.write(115);  // Back to center
    }
  }
}