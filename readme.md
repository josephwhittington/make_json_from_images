### Dependencies:
1. Python 2.7.*
### Description
This program generates a json file with filenames of images found in the directory of the make_json.py file as the suppilied first argument when running the script. The generated file gets optput in the directory of the script
### How to Use
Run the program by typing: 
```bash 
python make_json.py with valid flag arguments
```
### Valid Arguments:
1. ```--first=<filename_property>```
2. ```--output=<json_file_name>```
3. ```--additional=prop_one,prop_two```
### Valid Argument Values:
1. ```--first```
-This is the name of the property that will have the value of the image names
2. ```--output```
-Specify the name of the json file to generate
3.```additional```
-Takes in comma separated values and uses those arguments as additional fields in the json file with empty values, don't use spaces because that would be separate arguments