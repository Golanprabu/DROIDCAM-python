import cv2
import numpy as np

def main():
    # Ganti alamat IP dan nomor port dengan nilai yang sesuai dari perangkat seluler Anda
    ip_address = "alamat_ip_perangkat_anda"
    port = "nomor_port_perangkat_anda"

    # Buat URL untuk mengakses kamera dari alamat IP dan nomor port
    url = f"http://{ip_address}:{port}/video"

    cap = cv2.VideoCapture(url)

    if not cap.isOpened():
        print("Kamera tidak dapat diakses.")
        return

    while True:
        # Baca frame dari kamera
        ret, frame = cap.read()

        if not ret:
            print("Tidak dapat membaca frame.")
            break

        # Tampilkan frame pada jendela
        cv2.imshow('Camera', frame)

        # Jika tombol 'q' ditekan, keluar dari loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Tutup kamera dan jendela
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
