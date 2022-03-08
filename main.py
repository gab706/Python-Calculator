SETTINGS = ['LCM', 'HCF']

def getNumber(text):
  while True:
    try:
      return int(input(f"{text}: "))
    except ValueError:
      print("That is not a number please try again!")

def getSettingType():
  while True:
    ChoosenSetting = input(f"What would you like to run? ({', '.join(SETTINGS)}): ").upper()
    if ChoosenSetting in SETTINGS:
      return ChoosenSetting

def getLCM(M1, M2):
  GN = M1 if M1 > M2 else M2
  while True:
    if ((GN % M1 == 0) and (GN % M2 == 0)):
      return GN
    GN += 1;

def getHCF(M1, M2):
  LN = M1 if M1 < M2 else M2
  for i in range(1, LN + 1):
    if ((M1 % i == 0) and (M2 % i == 0)):
      return i
      
while True:
  N1 = getNumber("First Number")
  N2 = getNumber("Second Number")
  ChoosenSetting = getSettingType()
  if ChoosenSetting == 'LCM':
    print(f"Lowest Common Multiple: {getLCM(N1, N2)}")
  elif ChoosenSetting == 'HCF':
    print(f"Highest Common Factor: {getHCF(N1, N2)}")
