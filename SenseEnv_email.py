import smtplib  #SMTP library
from email.MIMEMultipart import MIMEMultipart   #Multi Internet Mailing Extension
from email.MIMEText import MIMEText     #email extension that supports text
from sense_hat import SenseHat
import time
from time import asctime    #to bring in the current time function

sense = SenseHat()  #establishing a communication between the Sense Hat
                    #and the program.
fromaddr = "highwind.sgtester@gmail.com"
toaddr = "highwind.sgtester2@gmail.com"
msg = MIMEMultipart()   #to distribute MIME function to multiple parts below
                        #in next three lines.
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Weather from Raspi"

temp = int(sense.get_temperature())     # Obtain temperature reading as integer
humidity = int(sense.get_humidity())    # Obtain humidity reading as integer
pressure = int(sense.get_pressure())    # Obtain pressure reading as integer
#message = " T = %ddeg, H = %d, P = %d " %(temp, humidity, pressure)
message = " Temp: %s C, Humidity: %s rH, Pressure: %s Millibars " %(temp, humidity, pressure)
#sense.show_message(message, scroll_speed = (0.08), text_colour = [200,240,200], back_colour = [0,0,0])
#    time.sleep(4)
#    log = open('weather.txt', "a")  # Opens a weather text file and append
#    now = str(asctime())            # the current time and
#    log.write(now+''+message+'\n')  # write in with the message of the T, H and P.
print(message)  # At the same time, print out the message on screen.
#    log.close()     # Then close the log file for this run cycle.
msg.attach(MIMEText(message, 'plain'))
server = smtplib.SMTP('smtp.gmail.com', 25) #establishing SMTP protocol to
                                            #gmail server on tcp/25
server.starttls()   #start server
server.login(fromaddr, 'Pilakada01')    #login auth using variable fromaddr
                                        #password plaintext in the code
text = msg.as_string()  #converting the message as a plain string and
                        #putting it inside a variable as text.
server.sendmail(fromaddr, toaddr, text) #calling the function sendmail
server.quit()   #then finally quitting the connection with the mail server.

# Note that a while loop should not be set for this program as gmail server will
# detect it as spam mail if it receives in-coming mail continuously.
