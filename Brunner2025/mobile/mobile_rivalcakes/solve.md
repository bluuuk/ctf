Difficulty: Easy
Author: KyootyBella

The secret Brunner and Othello cults are waging their battles in the streets of Denmark.

One day, you see a member of the Othello cult drop their phone out of their pocket. You grab it, but it seems to be a burner phone. You find only two custom apps, but when opening one, it instantly deletes itself - maybe there is still some data left?

In the cake cults, preferences matter - so keep an eye out and mind what you say.

Your Othello rivals are planning a secret meetup, find out where and find the password to infiltrate them!

Flag format: The flag is formatted as brunner{<w3w_code>_<password>}, where <w3w_code> is the what3words code of the location, without leading slashes. Make sure your "3 word address language" is set to English.

Example: brunner{candy.magnetic.label_hunter2}

Download Link: mobile_rivalcakes.7z
Password: VerySecurePasswordForRivalCakes_BrunnerCTF2025

```bash
❯ rg -e "part\d"
data/data/dk.brunnerctf.rivalcakes/files/menu_temp.html
1:<html><body><p>part4:Brunsviger</p></body></html>

data/data/dk.brunnerctf.rivalcakes/shared_prefs/my_prefs.xml
4:    <string name="step2_data">part2:always_better_</string>
```

```bash
sqlite> select * FROM orders limit 100;
15|Customer15|note 15|cancelled|2025-07-07 10:03:00
16|Alice|Extra frosting|delivered|2025-08-10 14:32:11
17|Bob|Meet at location in EXIF|pending|2025-08-11 09:21:44
18|Claire|part1:Othello_is_|cancelled|2025-08-12 08:59:02
20|Customer20|note 20|delivered|2025-07-03 10:02:00
```

```
❯ exiftool best_cake_in_the_world.jpg
======== best_cake_in_the_world.jpg
ExifTool Version Number         : 13.30
File Name                       : best_cake_in_the_world.jpg
Directory                       : .
File Size                       : 35 kB
File Modification Date/Time     : 2025:08:20 09:35:41-04:00
File Access Date/Time           : 2025:08:23 14:06:28-04:00
File Inode Change Date/Time     : 2025:08:23 14:06:25-04:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
Exif Byte Order                 : Big-endian (Motorola, MM)
X Resolution                    : 72
Y Resolution                    : 72
Resolution Unit                 : inches
Y Cb Cr Positioning             : Centered
Exif Version                    : 0232
Components Configuration        : Y, Cb, Cr, -
User Comment                    : part3:Than_an_ugly_
Flashpix Version                : 0100
Color Space                     : Uncalibrated
GPS Version ID                  : 2.3.0.0
GPS Latitude Ref                : North
GPS Longitude Ref               : East
Image Width                     : 584
Image Height                    : 194
Encoding Process                : Progressive DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 584x194
Megapixels                      : 0.113
GPS Latitude                    : 55 deg 40' 29.56" N
GPS Longitude                   : 12 deg 33' 52.40" E
GPS Position                    : 55 deg 40' 29.56" N, 12 deg 33' 52.40" E
```
GPS Position                    : 55 deg 40' 29.56" N, 12 deg 33' 52.40" E -> scarred.marble.improving


brunner{scarred.marble.improving_Othello_is_always_better_Than_an_ugly_Brunsviger}