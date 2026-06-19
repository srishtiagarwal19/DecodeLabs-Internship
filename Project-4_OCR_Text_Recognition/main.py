import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img = cv2.imread("sample.jpg")

if img is None:
    print("Error: Could not find sample.jpg")
    exit()
output_img = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(
    gray,
    0,
    255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)[1]
cv2.imwrite("processed.jpg", thresh)
text = pytesseract.image_to_string(thresh)

print("\n==============================")
print("DETECTED TEXT")
print("==============================\n")
print(text)

with open("output.txt", "w", encoding="utf-8") as file:
    file.write(text)

print("\nText saved to output.txt")
print("Processed image saved to processed.jpg")
data = pytesseract.image_to_data(
    thresh,
    output_type=pytesseract.Output.DICT
)

print("\n==============================")
print("WORD CONFIDENCE SCORES")
print("==============================\n")

n_boxes = len(data['text'])

for i in range(n_boxes):

    word = data['text'][i].strip()

    if word != "":

        confidence = float(data['conf'][i])

        print(f"{word} -> Confidence: {confidence:.2f}%")

        if confidence > 40:

            x = data['left'][i]
            y = data['top'][i]
            w = data['width'][i]
            h = data['height'][i]

            cv2.rectangle(
                output_img,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

cv2.imshow("Processed Image", thresh)
cv2.imshow("Detected Text Boxes", output_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
