from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    # Load image and convert to byte array
    image = Image.open(image_path)
    image_data = np.array(image)
    flat_image_data = image_data.flatten()

    # Apply XOR operation with key
    encrypted_data = [byte ^ key for byte in flat_image_data]

    # Convert back to image format
    encrypted_image_data = np.array(encrypted_data).reshape(image_data.shape)
    encrypted_image = Image.fromarray(encrypted_image_data.astype('uint8'))
    encrypted_image.save('encrypted_image.png')

def decrypt_image(encrypted_image_path, key):
    # Load encrypted image and convert to byte array
    encrypted_image = Image.open(encrypted_image_path)
    encrypted_image_data = np.array(encrypted_image)
    flat_encrypted_data = encrypted_image_data.flatten()

    # Apply XOR operation with key
    decrypted_data = [byte ^ key for byte in flat_encrypted_data]

    # Convert back to original image format
    decrypted_image_data = np.array(decrypted_data).reshape(encrypted_image_data.shape)
    decrypted_image = Image.fromarray(decrypted_image_data.astype('uint8'))
    decrypted_image.save('decrypted_image.png')

# Example usage
encryption_key = 123  # Example key, should be kept secret
encrypt_image('original_image.png', encryption_key)
decrypt_image('encrypted_image.png', encryption_key)
