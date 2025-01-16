import math

# ‘points’ adında bir liste oluşturun. Bu liste, 2D uzaydaki noktaları temsil eden demetler (tuple) içermelidir. Örneğin, ‘(x, y)’ noktası bir demet ‘(x, y)’ olarak temsil edilecektir. kısmı-
points = [(1, 2), (4, 6), (7, 8), (2, 3)]  

# ‘euclideanDistance’ adında bir fonksiyon tanımlayın. Bu fonksiyon, iki demet (her biri bir noktayı temsil eder) almalı ve bu iki nokta arasındaki Öklid mesafesini döndürmelidir. kısmı -
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)


distances = []  

# 4. Bir döngü kullanarak, ‘points’ listesindeki her nokta çifti arasındaki Öklid mesafesini hesaplayın. Bu mesafeleri ‘distances’ adında başka bir listede saklayın. kısmı - discantesi üstte tanımladım
for i in range(len(points)):
    for j in range(i + 1, len(points)): 
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# 5. Minimum Mesafenin Bulunması
min_distance = min(distances)  
print("Minimum Öklid Mesafesi:", min_distance)