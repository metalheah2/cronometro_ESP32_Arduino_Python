int uni_seg, dec_seg, und_min, dec_min;
int a = 12, b = 14, c = 27, d = 26,e=25,f=33,g=32;
int buf1=4, buf2=16, buf3=17, buf4=5, punto=18;



void setup() {
  pinMode(a, OUTPUT);
  pinMode(b, OUTPUT);
  pinMode(c, OUTPUT);
  pinMode(d, OUTPUT);
  pinMode(e, OUTPUT);
  pinMode(f, OUTPUT);
  pinMode(g, OUTPUT);
  pinMode(buf1, OUTPUT);
  pinMode(buf2, OUTPUT);
  pinMode(buf3, OUTPUT);
  pinMode(buf4, OUTPUT);
  pinMode(punto, OUTPUT);
}

void loop() {
  for (dec_min; dec_min < 6; dec_min++) {
    for (und_min = 0; und_min < 10; und_min++) {
      for (dec_seg; dec_seg < 6; dec_seg++) {
        for (uni_seg; uni_seg < 10; uni_seg++) {
          for (int t = 0; t < 10; t++) {
            digitalWrite(buf1, HIGH);
            decoBCD(uni_seg);
            delay(4);
            digitalWrite(buf1, LOW);
            delay(1);
            digitalWrite(buf2, HIGH);
            decoBCD(dec_seg);
            delay(4);
            digitalWrite(buf2, LOW);
            delay(1);
            digitalWrite(buf3, HIGH);
            digitalWrite(punto,HIGH);
            decoBCD(und_min);
            delay(4);
            digitalWrite(buf3, LOW);
            digitalWrite(punto,LOW);
            delay(1);
            digitalWrite(buf4, HIGH);
            decoBCD(dec_min);
            delay(4);
            digitalWrite(buf4, LOW);
            delay(1);
          }
        }
      }
    }
  }
}


void decoBCD(int num) {
  switch (num) {
    case 0:
      binario(1,1,1,1,1,1,0);
      break;
    case 1:
      binario(0,1,1,0,0,0,0);
      break;
    case 2:
      binario(1,1,0,1,1,0,1);
      break;
    case 3:
      binario(1,1,1,1,0,0,1);
      break;
    case 4:
      binario(0,1,1,0,0,1,1);
      break;
    case 5:
      binario(1,0,1,1,0,1,1);
      break;
    case 6:
      binario(1,0,1,1,1,1,1);
      break;
    case 7:
      binario(1,1,1,0,0,0,0);
      break;
    case 8:
      binario(1,1,1,1,1,1,1);
      break;
    case 9:
      binario(1,1,1,1,0,1,1);
      break;
  }
}


void binario(byte b6,byte b5,byte b4,byte b3, byte b2, byte b1, byte b0) {
  digitalWrite(g, b6);
  digitalWrite(f, b5);
  digitalWrite(e, b4);
  digitalWrite(d, b3);
  digitalWrite(c, b2);
  digitalWrite(b, b1);
  digitalWrite(a, b0);
}
