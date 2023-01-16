
set list=%1

del /q snow.txt 
del /q SnowDay.txt 
del /q SnowNight.txt 
del /q rain.txt 
del /q rainDay.txt 
del /q rainNight.txt 
del /q Clear.txt
del /q vid2weather.bat 


type %list% | find /I "Snow" > snow.txt
type %list% | find /I "rain" > rain.txt
type %list% | find /I /V "snow" | find /I /V "rain" > Clear.txt

type snow.txt | find /I "Night" > Snow_Night.txt
type snow.txt | find /I "LowLight" > Snow_LowLight.txt
copy /y Snow_LowLight.txt+Snow_Night.txt SnowNight.txt
type snow.txt | find /I /V "night" | find /I /V "lowlight" > SnowDay.txt
del /q Snow_LowLight.txt
del /q Snow_Night.txt

type rain.txt | find /I "Night" > Rain_Night.txt
type rain.txt | find /I "LowLight" > Rain_LowLight.txt
copy /y Rain_LowLight.txt+Rain_Night.txt RainNight.txt
type Rain.txt | find /I /V "night" | find /I /V "lowlight" > RainDay.txt
del /q Rain_LowLight.txt
del /q Rain_Night.txt

type Clear.txt | find /I "Night" > Clear_Night.txt
type Clear.txt | find /I "LowLight" > Clear_LowLight.txt
copy /y Clear_LowLight.txt+Clear_Night.txt ClearNight.txt
type Clear.txt | find /I /V "night" | find /I /V "lowlight" > ClearDay.txt
del /q Clear_LowLight.txt
del /q Clear_Night.txt

del /q Clear.txt
del /q Rain.txt
del /q Snow.txt



