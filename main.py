import urllib, os

#get current directoy
path = os.getcwd()

# create 'raw_images' directory if not exist
path += '/raw_images'
if not os.path.exists(path):
    print os.makedirs(path)
os.chdir(path)

#loop number of pages
for i in range(1,91):
#left and right page
    for j in range(0,2):
        image = 'Image'
        image = image + str('%02d' %i) + '-' + str(i) + '-' + str(j) + '.jpg'
	url = 'http://skylibrary.net/issues/com.turkishairlines.books/5F5898BB7723045C0F699EDBF3A6D102/webreaderHTML/complete/OEBPS/images/'
    	f = open(image, 'wb')
    	f.write(urllib.urlopen(url+image).read())
    	f.close()
