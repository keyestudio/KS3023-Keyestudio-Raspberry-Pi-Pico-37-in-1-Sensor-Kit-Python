/* 
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 37
 * mfrc522
 * http://www.keyestudio.com
*/
#include <Wire.h>
#include "MFRC522_I2C.h"
//iic引脚默认为pico的4和5
// 0x28 是 SDA 上的 i2c 地址。 如果不匹配，请使用 i2cscanner 检查您的地址
MFRC522 mfrc522(0x28);   // 创建 MFRC522 实例。
String rfid_str = "";
void setup() {
  Serial.begin(115200);           // 设置波特率为115200
  Wire.begin();                   // 初始化 I2C
  mfrc522.PCD_Init();             // 初始化 MFRC522
}

void loop() {
  if ( ! mfrc522.PICC_IsNewCardPresent() || ! mfrc522.PICC_ReadCardSerial() ) {
    delay(50);
    return;
  }
  rfid_str = "";//字符串清空
  Serial.print(F("Card UID:"));
  for (byte i = 0; i < mfrc522.uid.size; i++) {// 转储 UID
    rfid_str = rfid_str + String(mfrc522.uid.uidByte[i], HEX);  //转为字符串
    //        Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
    //        Serial.print(mfrc522.uid.uidByte[i], HEX);
  }
  Serial.println(rfid_str);

}
