// Define the address and data bus pin arrays
const uint8_t ADDRESSES[] = {22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52};
const uint8_t DATABUS[] = {39, 41, 43, 45, 47, 49, 51, 53};

// Define the clock pin
#define CLOCK 2

// Define read and write pin
#define READ_WRITE 3

void setup() {
  // Set address pins as input
  for (int n = 0; n < 16; n++) {
    pinMode(ADDRESSES[n], INPUT);
  }

  // Set data bus pins as input
  for (int n = 0; n < 8; n++) {
    pinMode(DATABUS[n], INPUT);
  }

  // Set clock pin as input
  pinMode(CLOCK, INPUT);

  // Set read & write pin as input
  pinMode(READ_WRITE, INPUT);

  // Attach interrupt to the clock pin, triggering on rising edge
  attachInterrupt(digitalPinToInterrupt(CLOCK), onClock, RISING);

  // Initialize serial communication at 57600 baud rate
  Serial.begin(57600);
}

// Declare variables for address and data, marked as volatile since they are used in ISR
volatile unsigned int address = 0;
volatile unsigned int data = 0;

// ISR to handle clock signal
void onClock() {
  char output[20]; // Buffer for formatted output
  address = 0;     // Reset address

  // Read 16 address bits
  for (int n = 0; n < 16; n++) {
    int bit = digitalRead(ADDRESSES[n]) ? 1 : 0; // Read bit from address pin
    Serial.print(bit); // Print bit to serial
    address = (address << 1) + bit; // Shift address left and add new bit
  }

  Serial.print("    "); // Print space for separation

  data = 0; // Reset data

  // Read 8 data bits
  for (int n = 0; n < 8; n++) {
    int bit = digitalRead(DATABUS[n]) ? 1 : 0; // Read bit from data bus pin
    Serial.print(bit); // Print bit to serial
    data = (data << 1) + bit; // Shift data left and add new bit
  }

  // Format and print address, read/write status, and data as hexadecimal
  sprintf(output, "   %04x  %c %02x", address, digitalRead(READ_WRITE) ? 'r' : 'W', data);
  Serial.println(output); // Print formatted output
}

void loop() {
  // Empty loop since all operations are handled by the ISR
}
