import numpy as np

def filtro_mediana(image):
    height, width, channels = image.shape
    image_filtered = np.zeros_like(image)

    mask = np.array([[1, 1, 1],
                  [1, 1, 1],
                  [1, 1, 1]])
    
    media_mask = 1/9*mask
    
    for channel in range(channels):
        for i in range(height):
            for j in range(width):
                start_i = max(0, i - 1)
                end_i = min(height, i + 2)
                start_j = max(0, j - 1)
                end_j = min(width, j + 2)

                neighbors = image[start_i:end_i, start_j:end_j, channel]
                
                sum_neighbors = np.sum(neighbors)

                media_value = sum_neighbors*media_mask

                media_value = np.ceil(media_value)
                image_filtered[i, j, channel] = media_value


    
image = np.array([[2, 3, 4, 5, 3],
                  [2, 3, 5, 0, 0],
                  [2, 4, 5, 0, 0],
                  [2, 4, 5, 0, 1],
                  [2, 2, 7, 0, 0]])

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        # Aplicar el filtro de mediana a cada punto
        image_filtered[i, j] = apply_median_filter(image, i, j)

print("\nImagen original:")
print(image)
print("\nImagen filtrada con filtro de mediana:")
print(image_filtered)