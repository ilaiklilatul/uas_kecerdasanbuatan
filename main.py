import speech_recognition as srec
from gtts import gTTS
import os

def perintah():
    mendengar = srec.Recognizer()
    with srec.Microphone() as source:
        print('Mendengarkan....')
        try:
            suara = mendengar.listen(source, phrase_time_limit=1)
            print('Diterima...')
            dengar = mendengar.recognize_google(suara, language='id-ID')
            print(dengar)
            return dengar
        except srec.UnknownValueError:
            print("Tidak dapat mengenali suara.")
        except srec.RequestError as e:
            print(f"Permintaan gagal; {e}")
        except KeyboardInterrupt:
            print("Program dihentikan.")
            exit()
        return ""

def ngomong(teks):
    if teks:
        bahasa = 'id'
        namafile = 'Ngomong.mp3'
        suara = gTTS(text=teks, lang=bahasa, slow=False)
        suara.save(namafile)
        os.system(f'start {namafile}')

def run_michelle():
    Layanan = perintah()
    if Layanan:
        ngomong(Layanan)

if __name__ == "__main__":
    try:
        run_michelle()
    except KeyboardInterrupt:
        print("Program dihentikan.")
