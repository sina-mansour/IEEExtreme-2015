def action():
	testCount = input()
	for test in range(testCount):
		roomsCount = input()
		peopleCount = input()
		people = {}
		rooms = {}
		for person in range(peopleCount):
			[r1,r2] = [int(x) for x in (raw_input().split())]
			people[person]=[r1,r2]
			rooms[r1] = rooms.get(r1,[]) + [person]
			rooms[r2] = rooms.get(r2,[]) + [person]
		# print people
		# print rooms
		mins = [roomsCount,peopleCount]
		allPeople = range(peopleCount)
		if min_exist(rooms,people,roomsCount):
			mins.append(2)
		while(len(allPeople)>0):
			person = allPeople[0]
			community = find_community([person],people,rooms,mins)
			communityPeople , communityRooms , mins = community
			for person in communityPeople:
				allPeople.remove(person)
				del people[person]
			for room in communityRooms:
				del rooms[room]
		print min(mins)

def min_exist(rooms,people,roomsCount):
	for room in rooms:
		# print 'inside\n'
		plist = rooms[room]
		for other in rooms:
			if other!=room:
				olist = rooms[other]
				com = list(set(plist)&set(olist))
				# print com
				if len(com)>2:
					return True
			# else:
			# 	print (other,room)
	return False

def find_community(personList,people,rooms,mins):
	grow = False
	communityRooms = []
	for person in personList:
		for room in people[person]:
			if room not in communityRooms:
				communityRooms.append(room)
	communityPeople = personList
	if (len(communityPeople)>len(communityRooms)):
		mins.append(len(communityRooms))
	for room in communityRooms:
		for person in rooms[room]:
			if person not in communityPeople:
				grow = True
				communityPeople.append(person)
	if not grow:
		return communityPeople, communityRooms, mins
	return find_community(communityPeople,people,rooms,mins) 

action()
