void    setup()
{
    pinMode (13, OUTPUT);
}
void loop () 
{
    digitalWrite(13, HIGH) ;   // turn the LED on (HIGH)
    delay(1000);              // wait for a second
    digitalWrite(13, LOW);    // turn the LED off by making the voltage
    delay(1000);               // stay off for a second
}