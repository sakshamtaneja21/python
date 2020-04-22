#Most hard drives are divided into sectors of 512 bytes each. Our disk has a size of 16 GB. Fill in the blank 
#to calculate how many sectors the disk has.

#Note: Your result should be in the format of just a number, not a sentence.

disk_size = 16*1024*1024*1024
sector_size = 512
sector_amount = disk_size/sector_size

print(sector_amount)