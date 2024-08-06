import qrcode

class qrc():


    def CreateQr(link, size, name):
        qr = qrcode.make(link)
        if size < 5 or size > 10:
            return 'Invalid size'
        
        else:
            qr.save(name + '.jpg', scale = size)
            return 'Succefuly saved'