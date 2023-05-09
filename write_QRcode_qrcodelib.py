#credits : https://www.learnpythonwithrune.org/how-to-scan-qr-codes-from-your-web-cam-in-3-steps/

import qrcode
img = qrcode.make('You are AWESOME')
img.save("awesome.png")
