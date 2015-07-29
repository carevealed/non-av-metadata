import os
import sys

__author__ = 'California Audio Visual Preservation Project'

import imageSpecsExtractor
import NonAVModel.Instantiation
from NonAVModel import errors_report


def create_MD5(filename):
	# TODO calculate MD5
	return "asdfasdf"


def get_human_filesize(filename):
	# todo get filesize with unit
	# return (filesize, unit)
	answer = (232, "kilobytes")
	return answer
	pass


def file_metadata_builder(filename, generation, derived_from, checksum=None, checksum_type=None):

	instance = NonAVModel.Instantiation(os.path.basename(filename))
	instance.report_errors = errors_report.WARNING #todo remove this line when done building

	instance.generation = generation
	instance.derivedFrom = derived_from

	if checksum:
		instance.checksum = checksum
		instance.checksumType = checksum_type
	else:
		instance.checksum = create_MD5(filename)
		instance.checksumType = "MD5"

	file_size, file_size_unit = get_human_filesize(filename)
	instance.fileSize = file_size
	instance.fileSizeUnit = file_size_unit

	instance.technical = imageSpecsExtractor.image_specs_extractor(filename).xml

	report = instance.check_required_data()
	if report.valid:
		return instance
	else:
		sys.stdout.flush()
		if len(report.missing_fields) > 0:
			sys.stderr.write("Missing fields:\n")
			for field in report.missing_fields:
				sys.stderr.write(field + "\n")
			print("")
		if len(report.missing_attributes) > 0:
			sys.stderr.write("Missing Attributes:\n")
			for attribute in report.missing_attributes:
				sys.stderr.write(attribute + "\n")
	pass


def test(source_folder):
	include_hidden = False
	valid_file_exensions = ['.tif', '.jpg']
	if os.path.exists(source_folder):
		for root, dirs, files in os.walk(source_folder):
			for file in files:
				if not include_hidden:
					if file.startswith('.'):
						continue
				if not os.path.splitext(file)[1] in valid_file_exensions:
					continue
				test_file = os.path.join(root, file)
				print(test_file)
				print(file_metadata_builder(test_file, generation="Original", derived_from="Physical"))

def main():
	print("hello")
	test("/Volumes")



if __name__ == '__main__':
	main()