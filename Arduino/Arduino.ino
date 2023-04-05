// D7 is servo

#include <Servo.h>
#include <U8x8lib.h>

Servo myservo;  // create servo object to control a servo

U8X8_SSD1306_128X64_ALT0_HW_I2C u8x8(/* reset=*/ U8X8_PIN_NONE);

enum Status
{
  lock, unlock
};

Status status = lock;

void setup()
{
  Serial.begin(115200);
  myservo.attach(7);
  if (myservo.read() <= 70)
  {
    myservo.write(0);
    u8x8.begin();
    u8x8.setFlipMode(1);
    u8x8.setFont(u8x8_font_chroma48medium8_r);
    u8x8.print("CLOSED");
  }
  else
  {
    myservo.write(80);
    u8x8.begin();
    u8x8.setFlipMode(1);
    u8x8.setFont(u8x8_font_chroma48medium8_r);
    u8x8.print("OPEN");
  }
  Serial.print("Setup done!");
}

void loop()
{
  dostuff();
}

void dostuff()
{
  if (Serial.available())
  {
    u8x8.clear();
    char msg = Serial.read();
    Serial.print(msg);
    Serial.print('\n');
    Serial.print(status);
    if (msg == 'A')
    {
      int pos;
      for (pos = 0; pos <= 80; pos++)
      {
        myservo.write(pos);
      }
      status = Status::unlock;
      u8x8.clear();
      u8x8.print("OPEN");
      Serial.print('\n');
      Serial.print("Door unlocked!");
    }
    else if (msg == 'B')
    {
      int pos;
      for (pos = 80; pos >= 0; pos--)
      {
        myservo.write(pos);
      }
      status = Status::lock;
      u8x8.clear();
      u8x8.print("CLOSED");
      Serial.print('\n');
      Serial.print("Door locked!");
    }
  }
}