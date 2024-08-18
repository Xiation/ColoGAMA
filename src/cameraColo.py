import cv2
import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas
import time
import board
import neopixel
import os

# Import the Picamera2, controls, and Transform from the appropriate libraries
from picamera2 import Picamera2, Preview
from libcamera import controls
from libcamera import Transform

def cameraColo():

    output_directory = "/home/admin/Pictures"  # Ganti ini dengan direktori output yang diinginkan

# Generate PDF filename with date and time
    current_datetime = time.strftime("%Y%m%d_%H%M%S")
    pdf_filename = f'output_{current_datetime}.pdf'
    pdf_filepath = os.path.join(output_directory, pdf_filename)  # Path lengkap ke file PDF

# Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

# Initialize the output file number
    file_number = 1
    max_capture_count = 5

# Initialize Neopixel
    pixels1 = neopixel.NeoPixel(board.D18, 7, brightness=1)
    pixels1.fill((255, 255, 200))

# Initialize Picamera2
    picam2 = Picamera2()
    camera_config = picam2.create_still_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores", transform=Transform(vflip=1))
    picam2.configure(camera_config)
    picam2.set_controls({"AfMode": controls.AfModeEnum.Manual, "LensPosition": 11.})
    picam2.start_preview(Preview.QTGL)
    picam2.start()
    time.sleep(2)

# Inisialisasi PDF
    pdf_filepath = os.path.join(output_directory, pdf_filename)

# Hapus file PDF jika sudah ada
    if os.path.exists(pdf_filepath):
        os.remove(pdf_filepath)

# Inisialisasi PDF
    pdf = canvas.Canvas(pdf_filepath)

    while file_number <= max_capture_count:
    # Capture image using Picamera2
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = f"captured_image_{timestamp}.jpg"
        picam2.capture_file(filename)

        print(f"Image captured and saved as {filename}")

    # Baca gambar yang baru saja diambil
        captured_image = cv2.imread(filename, 1)

    # Potong gambar ke bagian tengah (160x360)
        height, width, _ = captured_image.shape
        crop_width = min(width, 160)
        crop_height = min(height, 360)
        start_x = (width - crop_width) // 2
        start_y = (height - crop_height) // 2
        cropped_image = captured_image[start_y:start_y + crop_height, start_x:start_x + crop_width]

    # Save the cropped image to a temporary file
        temp_filename = f"temp_cropped_image_{timestamp}.jpg"
        cv2.imwrite(temp_filename, cropped_image)

    # Tampilkan histogram RGB dan nilai RGB
        plt.clf()  # Membersihkan plot sebelumnya
        colors = ('b', 'g', 'r')
        for i, color in enumerate(colors):
            hist = cv2.calcHist([cropped_image], [i], None, [256], [0, 256])
            plt.plot(hist, color=color, label=f'{color.upper()} channel')
            plt.xlim([0, 256])
        plt.xlabel('Intensitas Piksel')
        plt.ylabel('Jumlah Piksel')
        plt.title(f'Histogram Warna RGB - Potret {file_number}')
        plt.legend()

    # Simpan gambar histogram sebagai PNG
        plt.savefig("output.png")

    # Simpan nilai RGB ke PDF
        B, G, R = cv2.split(cropped_image)
        avg_B = int(cv2.mean(B)[0])
        avg_G = int(cv2.mean(G)[0])
        avg_R = int(cv2.mean(R)[0])

    # Menambah halaman baru untuk setiap iterasi (kecuali untuk halaman pertama)
        if file_number > 1:
            pdf.showPage()

    # Simpan gambar cropped ke PDF
        pdf.drawInlineImage(temp_filename, 10, 720 - 40, width=80, height=390)

    # Simpan grafik histogram ke PDF
        pdf.drawInlineImage("output.png", 10, 720 - 160, width=400, height=120)

    # Spacing
        pdf.drawString(10, 720 - 280, '')

    # Tulis hasil nilai RGB dengan font Arial bold
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(10, 720 - 300, f'Hasil Nilai RGB - Potret {file_number}')
        pdf.setFont("Helvetica", 12)
        pdf.drawString(10, 720 - 315, f'R: {avg_R}, G: {avg_G}, B: {avg_B}')

    # Hapus file gambar sementara
        os.remove(temp_filename)

    # Tunggu sebentar sebelum capture berikutnya
        time.sleep(5)

    # Increment the file number
        file_number += 1

# Simpan PDF
    pdf.save()
    print(f"PDF will be saved to: {pdf_filepath}")

# Hapus file PNG histogram sementara
    os.remove("output.png")
    pixels1 = neopixel.NeoPixel(board.D18, 7, brightness=1)
    pixels1.fill((0, 0, 0))

# Tutup jendela plot terakhir jika masih terbuka
plt.close()

# Tutup jendela kamera setelah selesai
cv2.destroyAllWindows()
