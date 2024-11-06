import serial
porta = "COM17"
baud = 9600
arquivo = "nao_pulo.csv"

ser = serial.Serial(porta,baud)
ser.flushInput()
print("Abrindo Serial")

amostra = 30*120
linha = 0
while linha <= amostra:
    
    data = str(ser.readline().decode("utf-8"))
    print(data)
    file = open(arquivo,"a")
    file.write(data)
    linha = linha+1

print("Final de leituras")
file.close()
ser.close()
