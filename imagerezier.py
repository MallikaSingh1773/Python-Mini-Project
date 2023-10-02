import cv2
import os


image_path = "Sunrise.jpg"


if not os.path.isfile(image_path):
    print("Error: The image file does not exist.")
else:
  
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)


    if image is None:
        print("Error: Unable to load the image.")
    else:
       
        original_height, original_width = image.shape[:2]

        scale_percent = 50

      
        width = int(original_width * scale_percent / 100)
        height = int(original_height * scale_percent / 100)

       
        dsize = (width, height)

     
        resized_image = cv2.resize(image, dsize)

  
        cv2.imwrite('newimage.png', resized_image)

        cv2.imshow("Original Image", image)
        cv2.imshow("Resized Image", resized_image)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
