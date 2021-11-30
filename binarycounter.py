bool bit0=true
bool bit1=true
bool bit2=true
for(int j=0; j<2; j+=1){
  bit1=!bit1;
  for(int i=0;i<2; i+=1){
    bit0=!bit0;
    Serial.print(bit2);
    Serial.print(",");
    Serial.print(bit1);
    Serial.print(",");
    Serial.print(bit0);
  }
}
    
 
 
