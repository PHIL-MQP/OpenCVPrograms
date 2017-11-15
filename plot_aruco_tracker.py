import matplotlib.pyplot as plt

rawtext = open("walkback.txt")

def representsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def representsFloat(s):
    try: 
        float(s)
        return True
    except ValueError:
        return False        

class Pose(object):
	"""docstring for Pose"""
	def __init__(self):
		self._x = None
		self._y = None
		self._z = None

		self._rx = None
		self._ry = None
		self._rz = None
		

class Marker(object):
	"""docstring for Marker"""
	def __init__(self):
		self._id = None
		self._pose = Pose()
		self._corners = [None for i in range(0,4)]

# ['1=(87.2463,150.672)', '(82.247,73.2315)', '(159.959,69.0628)', '(169.01,143.008)', 'Txyz=-0.00988328', '-0.00268059', '0.136991', 'Rxyz=2.0313', '-2.23137', '0.404038', '\n']

	def initTxt(self, line):
		strs = line.split(" ")
		if(representsInt(strs[0].split('=')[0])):
			self._id = int(strs[0].split('=')[0])
			for i in range(0,4):
				self._corners[i] = (float(strs[i].split('(')[1].split(',')[0]), float(strs[i].split(',')[1].split(')')[0]))
			self._pose._x = float(strs[4].split('=')[1])
			self._pose._y = float(strs[5])
			self._pose._z = float(strs[6])
			self._pose._rx = float(strs[7].split('=')[1])
			self._pose._ry = float(strs[8])
			self._pose._rz = float(strs[9])
			return True
		else:
			return
			False

		

markers = []
x_vals = []
y_vals = []
colors = []
ctr = 1000.
delta = 20.
i = 0

for line in rawtext:
	marker = Marker()
	if(marker.initTxt(line)):
		markers.append(marker)
		x_vals.append(marker._pose._x)
		y_vals.append(marker._pose._y)
		colors.append([(ctr-(i*delta))/ctr, (ctr-(i*delta))/ctr, (ctr-(i*delta))/ctr ])
		i += 1

	# print(line)
fig, ax = plt.subplots()
ax.scatter(x_vals, y_vals, facecolors=colors)
plt.show()