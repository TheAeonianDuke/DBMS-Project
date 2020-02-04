import cv2
import numpy as np
import sqlite3

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam=cv2.VideoCapture(0);
rec=cv2.face.LBPHFaceRecognizer_create()
rec.read("recognizer_trainningData.yml")
font=cv2.FONT_HERSHEY_SIMPLEX

def connect_db():
	facedb=sqlite3.connect("dbms_db.db")
	c=facedb.cursor()

	# create_userdb_cmd="""CREATE TABLE IF NOT EXISTS `users` (
 # 						`user_id` INTEGER NOT NULL,
 #  						`first_name` varchar(255) default NULL,
 #  						`last_name` varchar(255) default NULL,
 #  						`age` mediumint default NULL,
 #  						`gender` varchar(255) default NULL,
 #  						`phone` varchar(100) default NULL,
 #  						PRIMARY KEY (`user_id`)
	# 					);
	# 					"""
	# insert_dummyuser= """INSERT INTO `users` (`user_id`,`first_name`,`last_name`,`age`,`gender`,`phone`) VALUES (1,"Benedict","Sweeney",62,"Male","545-7444"),(2,"Jayme","Francis",57,"Male","681-2925"),(3,"Stella","Harris",4,"Female","201-4272"),(4,"Irene","Mcguire",49,"Male","1-627-849-0939"),(5,"Jerry","Sanders",50,"Female","658-2002"),(6,"Jeanette","Villarreal",7,"Male","1-334-697-2971"),(7,"Austin","Bradley",42,"Male","1-265-953-6473"),(8,"Donovan","Holloway",15,"Male","459-9708"),(9,"Dale","Olsen",45,"Female","238-1923"),(10,"Lacey","Schwartz",31,"Male","1-651-535-6851"),(11,"Grace","Terrell",52,"Male","124-6024"),(12,"Bethany","Bush",72,"Female","527-0433"),(13,"Ulysses","Parker",9,"Male","342-9056"),(14,"Orla","Shannon",67,"Male","966-7138"),(15,"Illiana","Sims",74,"Female","1-751-610-4248"),(16,"Cruz","Chandler",44,"Male","383-4689"),(17,"Melanie","Richard",73,"Female","1-987-123-4042"),(18,"Emerald","Hutchinson",5,"Male","748-8896"),(19,"Henry","Oneal",56,"Female","1-582-130-7760"),(20,"Stewart","Potter",83,"Male","1-699-229-1821"),(21,"Ariel","Rivera",46,"Male","371-2416"),(22,"Jesse","Gilliam",2,"Female","1-693-270-9037"),(23,"Simone","Salazar",10,"Female","1-416-886-9219"),(24,"Addison","Young",78,"Female","853-6989"),(25,"Karyn","Forbes",28,"Male","1-915-805-2062"),(26,"Phelan","Hart",73,"Female","1-135-777-6231"),(27,"Jason","Kemp",13,"Male","935-0420"),(28,"Cooper","Porter",94,"Female","1-609-828-5543"),(29,"Moses","Daniel",68,"Female","348-7333"),(30,"Ralph","Rollins",72,"Female","804-6205"),(31,"Armand","Hawkins",66,"Male","1-909-790-9305"),(32,"Shellie","Sanchez",74,"Female","740-6122"),(33,"Blossom","Rowland",70,"Female","649-8798"),(34,"Joshua","Wiggins",3,"Male","443-9271"),(35,"Simon","Frye",47,"Male","1-648-854-6164"),(36,"Barbara","Booker",93,"Male","1-855-237-5528"),(37,"Trevor","Cervantes",73,"Female","1-215-888-0651"),(38,"Timothy","Ramirez",79,"Male","749-9714"),(39,"Justina","Santana",42,"Male","1-856-558-8916"),(40,"Breanna","Clemons",23,"Female","1-737-219-5892"),(41,"Sonia","Noel",13,"Male","1-451-622-6016"),(42,"Rosalyn","Sampson",6,"Female","1-128-648-7465"),(43,"Moana","Joseph",39,"Male","1-260-803-4462"),(44,"Oleg","Pena",98,"Female","1-404-226-7464"),(45,"Cody","Foster",95,"Male","767-1245"),(46,"Howard","Robinson",83,"Male","265-2580"),(47,"Wesley","Hewitt",66,"Female","207-2569"),(48,"Nero","Summers",4,"Female","1-475-437-3976"),(49,"Jared","Reed",84,"Male","751-5742"),(50,"Erasmus","Rosa",94,"Male","279-1880"),(51,"Desiree","Maldonado",48,"Female","1-772-220-6866"),(52,"Ferris","Mclean",30,"Male","275-5128"),(53,"Merritt","Terry",49,"Female","798-3118"),(54,"Caryn","Gomez",30,"Female","1-578-824-6208"),(55,"Armando","Blankenship",24,"Female","1-223-370-6876"),(56,"Leilani","Pierce",89,"Female","1-354-340-3393"),(57,"Allegra","Poole",64,"Female","849-6673"),(58,"Nasim","Solis",7,"Male","595-6355"),(59,"Knox","Moses",100,"Female","521-3865"),(60,"Travis","Garza",17,"Female","463-5842"),(61,"Justin","Newton",74,"Female","931-4867"),(62,"Kasper","Wheeler",21,"Male","1-287-264-6978"),(63,"Haley","Reed",70,"Female","828-0891"),(64,"Chadwick","Marshall",96,"Female","149-9424"),(65,"Zeph","Dale",67,"Male","1-974-209-1097"),(66,"Regina","Hinton",99,"Male","927-7936"),(67,"Hedley","Thomas",40,"Female","809-9741"),(68,"Gavin","Cardenas",68,"Female","119-4696"),(69,"Jescie","Wilcox",87,"Female","490-7645"),(70,"Angelica","Wooten",20,"Male","478-9187"),(71,"Doris","Glass",26,"Female","1-284-921-0978"),(72,"Susan","Marsh",36,"Male","727-1552"),(73,"Brady","Gutierrez",93,"Male","1-706-564-1735"),(74,"Joel","Blanchard",4,"Male","1-304-657-2648"),(75,"Keith","Shields",94,"Female","128-3434"),(76,"Halla","Montgomery",66,"Male","892-0988"),(77,"Uriah","Hayes",58,"Male","723-9069"),(78,"Madaline","Parrish",15,"Male","1-280-249-8377"),(79,"Mari","Hopkins",9,"Male","1-736-990-0442"),(80,"Zeph","Skinner",74,"Female","1-723-290-7005"),(81,"Amaya","Herrera",59,"Male","265-6620"),(82,"Iliana","Schmidt",12,"Male","395-3334"),(83,"Emerald","Whitaker",98,"Female","1-694-967-5689"),(84,"Lucy","Colon",12,"Male","1-728-174-1337"),(85,"Heidi","Stokes",21,"Male","1-355-817-2119"),(86,"Wade","Hewitt",45,"Male","183-5709"),(87,"Halla","Richards",88,"Female","654-7881"),(88,"Kameko","Carver",26,"Female","605-2212"),(89,"Lane","Brock",64,"Female","570-4166"),(90,"Melyssa","Sutton",25,"Female","856-1094"),(91,"Travis","Lowe",2,"Male","213-5296"),(92,"Hamish","Hanson",31,"Female","161-4823"),(93,"Eden","Ortiz",26,"Male","1-849-734-9593"),(94,"Xandra","Schultz",80,"Male","145-9796"),(95,"Sage","Prince",77,"Male","510-4957"),(96,"Moses","Blackburn",19,"Male","1-734-976-3077"),(97,"Alexis","Casey",13,"Male","525-6447"),(98,"Blossom","Ortega",2,"Female","1-581-393-4533"),(99,"Berk","Griffin",65,"Male","770-7281"),(100,"Isaac","Rojas",18,"Male","1-349-272-5779");
	# 				"""

	# create_cmd="""CREATE TABLE IF NOT EXISTS `user_image` (
 #  					`userimage_id` INTEGER NOT NULL,
 #  					`user_id` INTEGER,
 #  					`image` varchar(255),
 #  					`timestamp` varchar(255),
 #  					PRIMARY KEY (`userimage_id`)
	# 				); """

	
	# c.execute(create_userdb_cmd)
	# c.execute(create_cmd)
	# c.execute(insert_dummyuser)
	# c.execute(insert_dummyimg)
	# facedb.commit()
	# print(c.fetchall())
	return facedb


facedb=connect_db()



def getProfile(facedb,id):  
    cmd="SELECT * FROM users WHERE user_id="+str(id)
    cursor=facedb.execute(cmd)
    profile=None
    for row in cursor:
        profile=row
    # facedb.close()
    return profile

while(True):
    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        profile=getProfile(facedb,id)
        if(profile!=None):
            cv2.putText(img,"Name : "+str(profile[1]),(x,y+h+20),font,0.5,(0,255,0));
            cv2.putText(img,"Age : "+str(profile[2]),(x,y+h+45),font,0.5,(0,255,0));
            cv2.putText(img,"Gender : "+str(profile[3]),(x,y+h+70),font,0.5,(0,255,0));
    cv2.imshow("Face",img);
    if(cv2.waitKey(1)==ord('q')):
        break;
cam.release()
cv2.destroyAllWindows()