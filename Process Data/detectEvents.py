import numpy as np

inputFile = open("collectedDataWithGroupId.csv")

data = inputFile.readlines()

events = []
current_event = [];

def findDirection(eventArray):
	last_value_added = ''
        detect_direction_buffer = [];

	for frame in event_np:
	  if frame[2] == last_value_added:
             pass
	  else:	
	     #print frame[2], last_value_added
             #print (type(last_value_added))
	     #print len(last_value_added) 
             #print len(frame[2])
             last_value_added = frame[2]
	     detect_direction_buffer.append(frame[2])
	
	#Print out the array once it's been made
	#print (detect_direction_buffer)

	if detect_direction_buffer[0] == 'HO':
		detect_direction_buffer = detect_direction_buffer[1:]

	print (detect_direction_buffer)

	#Currenlty the code will try to guess your direction if it doesn't have enough info
	#THE STATE HO USES THE LETTER O AND NOT THE NUMBER 0

	if len(detect_direction_buffer) == 0:
		return ('?', '?')

	if len(detect_direction_buffer) == 1:
	   if detect_direction_buffer[0] == 'HA':
		return ('right', '?')
	   elif detect_direction_buffer[0] == 'HB':
		return ('left', '?')

	elif len(detect_direction_buffer) == 2:
	   if detect_direction_buffer[0] == 'HA' and detect_direction_buffer[1] == 'HB':
		return ('right', 'left')
	   elif detect_direction_buffer[0] == 'HB' and detect_direction_buffer[1] == 'HA':
		return ('left', 'right')
	   elif detect_direction_buffer[0] == 'HA' and detect_direction_buffer[1] == 'HO':
		return ('right', '?')
	   elif detect_direction_buffer[0] == 'HB' and detect_direction_buffer[1] == 'HO':
		return ('left', '?')
	   elif detect_direction_buffer[0] == 'HA' and detect_direction_buffer[1] == 'HAB':
		return ('right', 'left')
	   elif detect_direction_buffer[0] == 'HB' and detect_direction_buffer[1] == 'HAB':
		return ('left', 'right')

	elif len(detect_direction_buffer) >= 3:
	   if detect_direction_buffer[0] == 'HA' and detect_direction_buffer[1] == 'HAB' and detect_direction_buffer[2] == 'HB':
		return ('right', 'left')
	   if detect_direction_buffer[0] == 'HB' and detect_direction_buffer[1] == 'HAB' and detect_direction_buffer[2] == 'HA':
		return ('left', 'right')
	   if detect_direction_buffer[0] == 'HA' and detect_direction_buffer[1] == 'HO' and detect_direction_buffer[2] == 'HB':
		return ('right', 'left')
	   if detect_direction_buffer[0] == 'HB' and detect_direction_buffer[1] == 'HO' and detect_direction_buffer[2] == 'HA':
		return ('left', 'right')
	

i = 0
for d in data:
	d_array = d.strip().split(",")
	ts = d_array[0]
	#ts_array = ts.split('.');
	#d_array[0] = float(ts_array[0]) + float(ts_array[1])/1000000000 
	h = int(d_array[1])
	state = d_array[2]
	presence = d_array[3]
	groupID = int(d_array[4])
	
	if(groupID is not 0):
		current_event.append(d_array)
	else:
		if(len(current_event)>0):
			events.append(current_event)
			current_event = []

outputFile = open("collectedDataResults.csv", "w")

for event in events:
	#print("EventID "+str(event[0][4])_
	event_np = np.array(event)
	#print(event)
	#print(event_np)
	#print(event_np[0,0])
	#print(event_np[len(event)-1,0])
	#print(np.max(event_np[:,1].astype(int))

	directionTuple = findDirection(event_np)
	#directionTuple = ('right', 'left')

	#Go through the array and find a list of unique state changes
	#Based on the pattern of state changes you can decide entry and exit

	t_s = event_np[0, 0]
	t_e = event_np[len(event)-1, 0]
	h = np.max(event_np[:,1].astype(int))
	d_in = directionTuple[0]
	d_out = directionTuple[1]
	id = event_np[0, 4]
	outputFile.write(t_s + "," + t_e + "," + str(h) + "," + d_in + "," + d_out + "," + str(id) + "\n")
