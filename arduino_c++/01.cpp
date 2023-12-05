void setup() {
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  Serial.begin(115200);
  Serial.println("hello");
}

void loop() {
  digitalWrite(2, HIGH);
  delay(5000);
  digitalWrite(2, LOW);
  delay(0);
  digitalWrite(3, HIGH);
  delay(1000);
  digitalWrite(3, LOW);
  delay(0);
  digitalWrite(4, HIGH);
  delay(5000);
  digitalWrite(4, LOW);
  delay(0);
  digitalWrite(3, HIGH);
  delay(1000);
  digitalWrite(3, LOW);
  delay(0);