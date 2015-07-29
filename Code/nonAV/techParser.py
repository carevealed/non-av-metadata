import subprocess
from xml.dom.minidom import parseString

__author__ = 'California Audio Visual Preservation Project'

from PIL import Image, ExifTags
from NonAVModel import Technical, CompressionModes

height = None
width = None
imageFormat = None #todo: make more accurate
colorspace = None  #todo: change to colorspace
file_format = None
compressionMode = None
bitDepth = None

# using pillow
im = Image.open("CAVP_color.jpg")
height = im.size[1]
width = im.size[0]
file_format = im.format
colorspace = im.mode
bitDepth = im.bits
chroma_subsampling = None

#using MediaInfo

mediaInfoData = subprocess.check_output(['mediainfo', '--Output=XML', "/Users/lpsdesk/non-av-metadata/Code/nonAV/CAVP_color.jpg"], universal_newlines=True)
dom = parseString(mediaInfoData)
for node in dom.getElementsByTagName("Color_space"):
	colorspace = node.firstChild.data

for node in dom.getElementsByTagName("Chroma_subsampling"):
	chroma_subsampling = node.firstChild.data

for node in dom.getElementsByTagName("Format"):
	imageFormat = node.firstChild.data

for node in dom.getElementsByTagName("Compression_mode"):
	compression = node.firstChild.data
if compression == "Lossy":
	compressionMode = CompressionModes.LOSSY
# print(dom.toprettyxml())



xml = Technical(fileFormat=file_format, height=height, width=width, colorBitDepth=bitDepth, imageFormat=imageFormat, compressionMode=compressionMode)
xml.colorSpace = colorspace
xml.chromaSubsampling = chroma_subsampling
print(xml)




# im.show()
