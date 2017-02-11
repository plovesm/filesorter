# @author Paul Ottley
# @copyright 2017
# File used to start the FilesSorter program

from app import FileSorter

fs = FileSorter(r"/Volumes/MyBook2TB/Backups/Pictures", r"/Volumes/Elements2TB/SortTarget")
# fs = FileSorter(r"/Volumes/Elements2TB/OttleyFamilyShare/FamilyShare.photoslibrary/Masters", r"/Volumes/Elements2TB/SortTarget")
# fs = FileSorter(r"/Users/paulottley/Desktop/MomsDadsPhotos", r"/Users/paulottley/Desktop/SortTarget")
fs.start_up()
