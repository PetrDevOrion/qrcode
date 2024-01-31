def generate_qr_code(link, back_color, fill_color, size=5, error_correction='H'):

  if error_correction == 'L':
    error_correction=qrcode.constants.ERROR_CORRECT_L
  elif error_correction == 'Q':
    error_correction=qrcode.constants.ERROR_CORRECT_Q
  elif error_correction == 'H':
    error_correction=qrcode.constants.ERROR_CORRECT_H
  else:
    error_correction=qrcode.constants.ERROR_CORRECT_M


  qr = qrcode.QRCode(
    version=5,
    box_size=size,
    error_correction=error_correction)

  qr.add_data(link)

  img = qr.make_image(back_color = back_color, fill_color = fill_color )

  img.save("some_file.png")



def main():
  link = 'https://docs-python.ru/packages/generator-qr-kodov/'

  generate_qr_code(link, 'black', (0, 204, 204), 5)



if __name__ == "__main__": 
    main()
