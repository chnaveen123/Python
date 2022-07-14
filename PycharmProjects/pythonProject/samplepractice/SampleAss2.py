import sampleAss
import samplePrtc

dat_file= r"C:\Users\nc67322\PycharmProjects\pythonProject\samplepractice\Root\Three\Data2\emp3.dat"

with open(dat_file,'r') as file:
    text = file.read()
    print(text)

df = pd.read_csv("C:\Users\nc67322\PycharmProjects\pythonProject\samplepractice\Root\Three\Data2\emp3.dat")

