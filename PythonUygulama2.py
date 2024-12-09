import math

def euclideanDistance(point1, point2):
  """İki nokta arasındaki Öklid mesafesini hesaplar."""
  return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Noktalar listesi
points = [(1, 2), (3, 4), (5, 1), (7, 3), (9,5)]

# Mesafeler listesi
distances = []

# Her nokta çifti için mesafeyi hesapla
for i in range(len(points)):
  for j in range(i + 1, len(points)):
    distance = euclideanDistance(points[i], points[j])
    distances.append(distance)
    print(f"{points[i]} ve {points[j]} noktaları arasındaki mesafe: {distance}")


# Minimum mesafeyi bul ve yazdır
if distances:
    min_distance = min(distances)
    print(f"\nMinimum mesafe: {min_distance}")
else:
    print("Mesafe hesaplanamadı çünkü listede yeterli nokta yok.")
