import csv
import math

data = []
centroids = [(2, 10), (5, 8), (1, 2)]
clusters = {}
k = 3
flag = False


def read():
	global data
	reader = csv.reader(open('kmeans_input.csv', 'r'))
	for row in reader:
		data.append((float(row[0]), float(row[1])))


def init():
	global centroids, clusters
	for key in clusters.keys():
		del clusters[key]
	clusters[centroids[0]] = []
	clusters[centroids[1]] = []
	clusters[centroids[2]] = []


def calc():
	global data, centroids, clusters
	for point in data:
			dist1 = math.sqrt((point[0] - centroids[0][0])**2 + (point[1] - centroids[0][1])**2)
			dist2 = math.sqrt((point[0] - centroids[1][0])**2 + (point[1] - centroids[1][1])**2)
			dist3 = math.sqrt((point[0] - centroids[2][0])**2 + (point[1] - centroids[2][1])**2)

			if dist1 < dist2 and dist1 < dist3:
				clusters[centroids[0]].append(point)
			elif dist2 < dist1 and dist2 < dist3:
				clusters[centroids[1]].append(point)
			elif dist3 < dist1 and dist3 < dist2:
				clusters[centroids[2]].append(point)


def update():
	global clusters, flag, centroids

	for i in range(0, len(centroids)):
		centroid = centroids[i]
		new = [0, 0]
		if len(clusters[centroid]) > 0:
			for item in clusters[centroid]:
				new[0] += item[0]
				new[1] += item[1]
			new[0] /= len(clusters[centroid])
			new[1] /= len(clusters[centroid])
		else:
			new[0] = centroid[0]
			new[1] = centroid[1]
		centroids[i] = tuple(new)
		if new[0] != centroid[0] and new[1] != centroid[1]:
			flag = False


read()
init()
count = 0

while not flag:
	flag = True
	init()
	calc()
	update()
	count += 1
	if count == 1:
		print centroids

print clusters
