import mimetypes
import os
import subprocess
from xml.dom.minidom import parseString
import sys

__author__ = 'California Audio Visual Preservation Project'

from PIL import Image, ExifTags
from NonAVModel import Technical, CompressionModes


image_file = "CAVP_color.jpg"


def image_specs_extractor(file):
	height = None
	width = None
	imageFormat = None #todo: make more accurate
	colorspace = None  #todo: change to colorspace
	file_format = None
	compressionMode = None
	bitDepth = None
	imageFormat = None


	#standard Python
	file_format = mimetypes.types_map[os.path.splitext(image_file)[1]]

	# using pillow
	im = Image.open(image_file)
	height = im.size[1]
	width = im.size[0]
	compression = None
	compressionMode = None
	colorspace = im.mode
	bitDepth = im.bits
	chroma_subsampling = None


	#using MediaInfo

	mediaInfoData = subprocess.check_output(['mediainfo', '--Output=XML', file], universal_newlines=True)
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
	elif compression == "Lossless":
		compressionMode = CompressionModes.LOSSLESS

	# print(dom.toprettyxml())

	xml = Technical(fileFormat=file_format,
					height=height,
					width=width,
					colorBitDepth=bitDepth)
	if imageFormat:
		xml.imageFormat = imageFormat
	xml.colorSpace = colorspace
	if chroma_subsampling:
		xml.chromaSubsampling = chroma_subsampling

	if compressionMode:
		xml.compressionMode = compressionMode
	return xml

def main():
	if len(sys.argv) < 2:
		sys.stderr.write("Needs at least one argument.\n")
		exit(-1)

	if not os.path.exists(sys.argv[1]):
		sys.stderr.write("File doesn't exists.\n")
		exit(-1)
	else:
		print("\nTechnical metadata for: " + os.path.basename(sys.argv[1]) + "\n")
		print(image_specs_extractor(sys.argv[1]))


if __name__ == '__main__':
    main()