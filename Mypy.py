import xml.etree.ElementTree as ET
import os
import lxml.etree as LS
path="C:\experiments"

#LOOPING EACH XML file in a specified folder
for desiredfile in os.listdir(path):
    #print("file name is " +desiredfile)
    #Check for the file type
    if desiredfile.endswith(".xml"):

        #getting the file name
        filenamewithpath= path + "\\" + desiredfile
        #print(filenamewithpath)

        #Passing file name with path to Element Tree
        tree = ET.parse(filenamewithpath)
        #tree=ET.fromstring(open(filenamewithpath).read())

        #getting root tag
        root =tree.getroot()
        filetype=root.tag
        print(filetype)
        #######NOW CHECKING THE FILE TYPE WHETHER IT IS APP XML

        if filetype=='Application':
            xml =root.attrib
            AppName=xml['name']
            #Type = xml['type']

            print(AppName,root)
            #print(tree.find('./Application').attrib('name'))


            ##Composing the output properties file
            outputfilename=AppName+".properties"
            #print(outputfilename)
            outputpropertiespath= path+"\\"+"Properties"+"\\"+outputfilename
            #print(outputpropertiespath)
            outputPropertiesfile = open(outputpropertiespath,"w")

            usermacro="%%"+AppName+"_"+"user"+"%%"
            drivermacro ="%%"+AppName+"_"+"driver"+"%%"
            urlmacro ="%%"+AppName+"_" +"url"+"%%"
            passwordmacro ="%%"+AppName+"_"+"password"+"%%"



            #print(elem.tag, 'name=', elem.text)


            ##Parameters to be changed
            #tree.find(".//entry[@key='driverClass']").text
            driverentry=tree.find(".//entry[@key='driverClass']")
            #print(drivervalue)
            urlentry = tree.find(".//entry[@key='url']")
            userentry = tree.find(".//entry[@key='user']")
            passwordentry=tree.find(".//entry[@key='password']")

            ##Output Parameters to be written to a file
            drivervalue=tree.find(".//entry[@key='driverClass']").attrib['value'].strip()
            #print(drivervalue)
            urlvalue = tree.find(".//entry[@key='url']").attrib['value'].strip()
            uservalue = tree.find(".//entry[@key='user']").attrib['value'].strip()
            passwordvalue = tree.find(".//entry[@key='password']").attrib['value'].strip()

            #print(drivervalue,urlvalue,uservalue,passwordvalue)

            ##Writing the output xml XML File
            outputxmlname = AppName+".xml"
            #print(outputxmlname)
            outputxmlpath = path+"\\"+"OutputFiles"+"\\"+outputxmlname
            #print(outputxmlpath)


            ##Writing the properties FIle
            outputPropertiesfile.write('######{}######\n'.format(AppName))
            outputPropertiesfile.write('{}={}\n'.format(usermacro,uservalue))
            outputPropertiesfile.write('{}={}\n'.format(drivermacro,drivervalue))
            outputPropertiesfile.write('{}={}\n'.format(urlmacro,urlvalue))
            outputPropertiesfile.write('{}={}\n'.format(passwordmacro,passwordvalue))


            if driverentry is None:
                print("driver not found")
            else:
                driverentry.set("value",drivermacro)
                tree.write(outputxmlpath)


            if urlentry is None:
                print("driver not found")
            else:
                 urlentry.set("value", urlmacro)
                 tree.write(outputxmlpath)

            if userentry is None:
                print("driver not found")
            else:
                userentry.set("value", usermacro)
                tree.write(outputxmlpath)

            if passwordentry is None:
                print("driver not found")
            else:
                passwordentry.set("value", passwordmacro)
                tree.write(outputxmlpath)

        else:
            print("file is not application xml")