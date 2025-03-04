#%%
import socket
from time import sleep
from umodbus import conf
from umodbus.client import tcp

#%%
# Adjust modbus configuration
conf.SIGNED_VALUES = True

# Create a socket connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
sock.connect(('94.237.57.171', 55801))
 
#command = tcp.read_holding_registers(1,0,10)
command = tcp.read_multiple_coils(slave_id=1, starting_address=1)
# Send your message to the network
tcp.send_message(command, sock)
time.sleep(1)

# Close the connection
sock.close()

# %%
