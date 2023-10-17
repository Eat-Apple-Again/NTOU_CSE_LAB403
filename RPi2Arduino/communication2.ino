void setup() {
  Serial.begin(9600); // 設定串列通訊速率
}

void loop() {
  if (Serial.available()) {
    String receivedData = Serial.readString(); // 讀取接收到的資料
    Serial.println("Received data: " + receivedData); // 顯示接收到的資料並由傳送端readline
  }
}