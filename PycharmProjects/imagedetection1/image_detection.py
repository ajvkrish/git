from pytesseract import Output
import pytesseract
import cv2

from os import listdir

listOfFiles = listdir("Resources/jpegs")

for file in listOfFiles:

  input_file = "Resources/jpegs/%s" % file
  print(input_file)
  image = cv2.imread(input_file)
  rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  results = pytesseract.image_to_data(rgb, output_type=Output.DICT)

  for i in range(0, len(results["text"])):
    x = results["left"][i]
    y = results["top"][i]
    w = results["width"][i]
    h = results["height"][i]
    confidence = results['conf'][i]
    text = results['text'][i].strip()

    if len(text) > 0:

      img = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
      cv2.imwrite('Resources/green/green_output_%s' % file, img)