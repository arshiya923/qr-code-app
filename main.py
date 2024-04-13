import tkinter as tk
from tkinter import filedialog
import segno
from datetime import datetime
import cv2


def create_qr():
    qr_contents = input("Please Enter Contents : (Text, Url, ...) : ")
    generated_qr_code_image = segno.make_qr(qr_contents)

    save_file_path = filedialog.askdirectory(
        title="Select A Directory To Save Your File."
    )

    file_full_path = (
        save_file_path
        + "/"
        + str(datetime.today().strftime("%Y-%m-%d-%H-%M-%S"))
        + ".png"
    )

    generated_qr_code_image.save(
        file_full_path, scale=20, border=5, light="#D6B4FC"
    )


def read_qr():
    qr_file = filedialog.askopenfile(
        filetypes=[
            ("Image Files", "*.jpg"),
            ("Image Files", "*.png"),
            ("Image Files", "*.jpg"),
            ("Image Files", "*.jpeg"),
        ]
    )

    try:
        img = cv2.imread(qr_file.name)
        detect = cv2.QRCodeDetector()
        value, points, straight_qrcode = detect.detectAndDecode(img)
        print("The Value Of This QrCode Is : " + value)
    except:
        print("No Qrcode Found !")


def main():
    user_input = input(
        "1 - For Creating QRCode Image\n2 - For Reading QRCode Image\nInput : "
    )
    user_input = int(user_input)

    root = tk.Tk()
    root.withdraw()

    if user_input == 1:
        create_qr()
    elif user_input == 2:
        read_qr()
    else:
        main()


if __name__ == "__main__":
    main()
