
# import xml element tree
import xml.etree.ElementTree as ET
  
# import mysql connector
import mysql.connector
  
# give the connection parameters
# user name is root
# password is empty
# server is localhost
# database name is database
conn = mysql.connector.connect(user='root', 
                               password='', 
                               host='localhost', 
                               database='database')
  
# reading xml file , file name is vignan.xml
tree = ET.parse('vignan.xml')
  
# in our xml file student is the root for all 
# student data.
data2 = tree.findall('student')
  
# retrieving the data and insert into table
# i value for xml data #j value printing number of 
# values that are stored
for i, j in zip(data2, range(1, 6)):
    name = i.find('name').text
    id = i.find('id').text
    department = i.find('department').text
      
    # sql query to insert data into database
    data = """INSERT INTO vignan(name,id,department) VALUES(%s,%s,%s)"""
  
    # creating the cursor object
    c = conn.cursor()
      
    # executing cursor object
    c.execute(data, (name, id, department))
    conn.commit()
    print("vignan student No-", j, " stored successfully")
