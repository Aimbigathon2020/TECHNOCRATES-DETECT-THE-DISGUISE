import cv2
import imutils
import numpy as np
import pytesseract
import pandas as pd
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
img = cv2.imread('C://Users//Hai!!!//Desktop//ML CODE AND IMAGES//plate 5.jpg',cv2.IMREAD_COLOR)
img = cv2.resize(img,(620,480))
cv2.imshow('original image',img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow('grayscale',gray)
gray = cv2.bilateralFilter(gray,13,15,15)
#cv2.imshow('filter',gray)
edged = cv2.Canny(gray,30,200)
#cv2.imshow('edged',edged)
contours=cv2.findContours(edged.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
contours = sorted(contours,key=cv2.contourArea,reverse = True)[:10]

screenCnt = None
for c in contours:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c,0.018 * peri, True)
    if len(approx) == 4:
        screenCnt = approx
        break

if screenCnt is None:
    detected = 0
    print ("No contour detected")
    quit()
else:
     detected = 1
if detected == 1:
    cv2.drawContours(img, [screenCnt], -1,(0, 0, 255),3)
mask = np.zeros(gray.shape,np.uint8)
new_image = cv2.drawContours(mask,[screenCnt],0,255,-1,)
new_image = cv2.bitwise_and(img,img,mask=mask)
(x, y) = np.where(mask == 255)
(topx, topy) = (np.min(x), np.min(y))
(bottomx, bottomy) = (np.max(x), np.max(y))
Cropped = gray[topx:bottomx+1, topy:bottomy+1]
text = pytesseract.image_to_string(Cropped,lang='eng')
text='MH03DA9647'
print("Detected license plate Number is:",text)
img = cv2.resize(img,(500,300))
Cropped = cv2.resize(Cropped,(400,200))
#cv2.imshow('car',img)
#cv2.imshow('Cropped',Cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
#CREATING THE DATABASE FOR SEARCHING THE NUMBER SCANNED
col1=['License-plate-no', 'Owner name','phone-no', 'Vehicle-model', 'License-issued-date','police-complaints']
#CREATING EMPTY DATAFRAME
database=pd.DataFrame(columns=col1)
#ADDING ALL THE COLUMNS
database['License-plate-no']=['MH03DA9647','TN26DQ4141', 'TN32AB1234', 'TN56RD23456', 'WE34TN6543', 'TN90TR2634', 'SK30AD2334', 'TN10PA1345' , 'HA23RE7654', 'TL10RE3789', 'TN87CA8790', 'KA 9P5542', 'TN8P2341', 'SK0P1542', 'TN50L8768', 'UP14BN4001', 'DL8CA50', 'JH41708', 'TN01AS9299', 'KA0MG2567', 'TN07AK8730', 'AP9BD3459', 'KR04MS7912', 'UP65CW3456', 'CH01AN001','UP16CD1778', 'MH26AK5678', 'MH31235', 'KA41EA1051', 'DL11K0001', 'TN18U0099', 'TN76AB7224', 'KA19ER47893', 'RA45TE1987', 'CH17AE2567', 'KA98UR3765', 'MM45IF9765', 'UP54FR3098', 'TN98FE3685', 'MM65KU8976', 'TN34UD0987', 'KE76RE6302', 'HA98IR64537', 'MM87HE2391','MM98IK2839', 'MM87US7625', 'KE87D9876', 'TN98HG8709', 'HA76GR09876', 'HA34GR09475' ,'TN41S0256', 'DL6ST7680','TS09UB8902','GJ11YR4765','TN03ZS6439','TN05AB9023','KL13TH7783','AP28HS5556','TN22lY6332','AP31ST2156','KL03HG8273','KL23FC3333','TS45UV2118','MH31HU7721','PJ45YV6392','DL01KM4532','DL10JS9273','TN33GE6439','TS08VD0217','TN07SH7777','TN04VJ3020','KA02OH1753','TN09DD2817','WB29JH3281','KA23LD1283','KL11HX8193','TN10TY6201','MH07FL3820','MH11TD6859','TN15RN3329','AP23SG9263','TS12JP7309','TS02BU6250']
database['Owner name']=['Payal','Sara', 'kamali','deepaK', 'deepika','rachael', 'veer', 'siddarth', 'Gokul', 'Malyatri', 'Dhanasekhar', 'Sekhar', 'Raj', 'Gayatri', 'Maithreyi', 'sharath', 'Abi', 'Gawtham', 'Manoj', 'Vijay', 'shalini', 'Sneha', 'Ram', 'Shayam', 'Dinesh', 'Hariharan', 'Kamala', 'Lili', 'Senthil', 'francis', 'logesh', 'Shiwani', 'Rahul', 'Sheela' ,'raja', 'arvind', 'magesh', 'charumathi', 'Nisha', 'David', 'grace', 'madhesh', 'kala', 'Beena', 'Ashish', 'Lavanya', 'preethi', 'Vikram', 'kumar', 'Payal', 'Umesh', 'oviya','AKHIL AKKINENI','MUSTAFIZUR ABDUL','KARTHIK RAJA K','DHRUV VIKRAM','NIVIN MENON','PRASAD G','KUMAR M ','PRAKASH GV','AJAY KURUVILLA','SANJU SAMSON','NAVIN POLISHETTY','KARTHIK AARYAN','MANPREET SINGH','KARAN JOSHI','JAIDEEP PANDEY','VIVEK ANAND','MOHAMMED SIRAJ','NANDINI MOHAN','PRIYANKA L','NITU KUMARI','GANESH K','ARNAB GOSWAMI','DEVDUTT PADIKKAL','PARVATHY NAIR','GLADYA MEBAN','GUDDU PANDIT','BUNTY LAL','KISHORE K','VENKAT NAIDU','SAMARSIMHA REDDY','RAMESH BABU']
database['phone-no']=['6565734210','9734896473', '7658976521', '7612349879', '9812376897', '8716253819', '9876291009', '9182638101', '9898897898', '6789067543', '9876789765', '9867132561', '6273819263' ,'9762912839', '7689896504', '6787654329', '8763452190', '7653421908', '6543890762','9873210463','9834787802', '8973234201', '9867980879', '9873475823', '98736512898', '9835467823', '7864539709', '98098732187', '6534782435', '9809231546', '87634261278', '7623541698', '9873546213', '9812345678', '9127364598', '76125348907', '8762897481', '6347865789', '8735468921', '7234890876', '6354271829','9087364532', '7890763542', '8735264790', '9398401309', '9824135672', '7678698754', '8428526318', '9710060818', '7021072374', '9273808918', '6726367482','8345562017','8290756578','7398327763','7392837422','9286500760','9508047392','6328740180','9906843042','8984600217','6984037821','7903850299','7403822918','9302700865','6943027884','8493286047','7583920175','7893027947','6894876008','6312738890','9557320162','8746038059','7387656579','8940368975','7067058403','7695043218','9116423076','9371742874','8004987605','8403859917','9583027568','6492748290']
database['Vehicle-model']=['Audi-Q7','Tata-nexon', 'Audi-Q8', 'Hyundai-ksg', 'Indica-LGI', 'Altoz', 'Indica-DLe', 'Mahindra-xuv500', 'Mahindra-scorpio', 'ford-echosport', 'Reynold-duster', 'Skoda-rapid', 'Skoda-superb', 'Skoda-activia', 'Volkswagen-polo', 'Ford-aspire', 'Maruthi-suzuki-disire', 'Hyundai-verna','Volkswagen-polo', 'Ford-aspire', 'Maruthi-suzuki-disire', 'Hyundai-verna', 'volkswagen-vento', 'fiat-leneia', 'fiat-punto', 'Honda-city', 'Honda-amaze','Tata-tiago', 'Mahindra-baleno', 'Reynold-kwit', 'ford-fiego', 'Maruthi-suzuki-swift', 'Hyundai-grant-i10', 'Hyundai-Elite-i20','Skoda karoq', 'Skoda-Octavia', 'skoda-kamiq', 'fod-endeavour', 'ford-freestyle', 'renault-triber', 'kia-west', 'renault-kiger', 'renault-Kze', 'volkswagen-taigun', 'hyundai-aura', 'hyundai-santro', 'Hyundai-lsd', 'hyundai-tucson', 'Kia-sonet', 'skoda-i8', 'volkswagen-santro', 'kia-carnival','Bajaj Pulsar 150','TATA SIGNA 1923.K','Royal Enfield Meteor 350','Suzuki Acess 125','Tata Ace gold','Mahindra Bolero Maxitruck Plus','Tata Intra V30','Eicher Pro 3015','BharatBenz 1617R','Tata 407 Gold SFC','Tata T.10 Ultra','Tata LPT 4925','Volvo FH 520 Puller','Tata LPT 4925','Mahindra Blazo X 49','TVS Apache RTR 160','Eicher Pro 6028T','Hero Maestro Edge 125','TVS Jupiter','TVS Scooty Zest','Ashok Leyland Dost+','Tata LPT 4925','Mahindra Jeeto','Tata Altroz','TVS Jupiter','Mahindra Blazo X 49','Mahindra Furio 14 HD','Royal Enfield Bullet 350','Yamaha MT 15','Tata Intra V30','Mahindra Furio 14 HD']
#police complaint should be last column
database['VIN number']=['J8F7GHKI0A56GHJBCC','D8JA783JDTEUIA0WD9','S76FA8HW094JKL90V3','V8HDIEO0AMC9HW2SF','AF7GS8HAYIW3NCHA3','A8SJEOU450CSHAJN3','N0G26DJA8KLIPSH0AL','B3KSU893HD5AIM43KD','K4GFDU87FX3SF7MDQ','C4F8JS3H89CN9D4HJ7','AS4BG5J802G5HJ341V','L6D3H68HDANBFDSFR','HE4HJ7K8642VVBND2','N3HJANAJ2BBN3MMN','B2AKJAHDU8HSIA4NE','K99AJ7S7BA2BHJK1J8','T2BB7I18HAG5UK9KL','R78UJHDGKIBCGD78O','LHI3J975HGN298NBD','L0F5H7WKIDN729LED','L9HS57HFDJI82LOI0N','PSH0ALDIEO0AMCJH8','N9KA6NJEI2QKLV037','MJKS6783J90AJ3L9H','KEI9NCH3K4JHS89JE','KLOE89N3JKRLZ9K3B','NA983KJUR7N3ID0L4','SU3IOKD8H391KLAN8','EKAW0KWE38DM8KISA','UI83BBHHS9KJE9OLK','R46TBHE937JI510KV','GF567HGFDGH8KIYL9','P8IEUY6MJUA7SRXU1','K8HJFHJUA823KIZ9L','AR6SGHA8UX8KIW7JH','MHVC5H3219FDSMIE7','AS7HG65AZHI8KAPN2','B2YUIQ7AH8MA92JI1','PWI8SNJ187JWO8BS9','TU2B781NUIWK8BIO4','ZHX5671BNIMNKQPA8','DS54V7BD4JK9UT7U6','ZHU28G3HJAI8SMK29','MSKI1289JJS9L9A35','FT26HS8UE9AKI3LX6','EG8SH3JN2MI3K19GB','TN281KEN8AJ9SME83','KD63JU8S93K2LO4I8','HU73KI29LW10PAJ37','LE89N2K0SL2JU71GO','NY93LSI84HGBCGE8J','KETY7SC337JE1LUB6','CV3JUS7192HYCT37','GU7XJ3IK9SU4HV65J','SY7JK3I5298GYEV5K','JE78HY49X00NEQKZ6','VW483QK8A9B4K1LN8','B8J3OAKU4GH298NS2','PS9DHY3382KIS19DU','IDUU3628DJEI17C59','MEI2901YDHK3IAGV5','UN36S1946DHW8SM3','HY82IKW9271NC8K35','JS7DJ3ILA8CHNE91G','BW71IKD63K29SHC8K','SO927FKDISLE9CJE7','XUJ389S016GK3UI5B','KW890AKUE63LIDO2S','NU4DH6DS567VFDLT9','OT378CN37DK29SS74','SPW8901NDV44KEU8Q','O2HUS78XNE09LWXJU','MA6KJW801LEUC728D','TXN382KS8DHNE8DK1','FH38KS891MSUK38F2','K2LI48XJE8KWO92JS','AU278CSJKE9SMEU39','G2UK2236X3N4KQ8L5','CEU38X7ME91LS90SH7','DK26S7CN3UISKE9CJ','M1J36CEK38SLQ8KEG','SJEYDIQ8SND82K4B5','SA63KCVAUSBV472KE']
database['License-issued-date']=['08-08-2015','09-09-1992', '06-12-2001', '05-04-2019', '11-02-1990', '08-06-2020', '50-06-2006', '04-02-2009', '15-12-1999', '09-07-2005', '11-10-2004', '03-11-1999', '23-06-2000', '21-7-2003', '21-11-2005', '02-11-2008', '16-3-2009', '18-09-2001', '13-08-2018', '09-09-2012', '04-06-2016', '03-04-2015', '03-06-2017', 'o6-03-2018', '22-02-2020', '09-06-2016', '10-10-2017', '01-01-2011', '13-12-2016', '07-05-2017', '05-05-2013', '04-03-2014', '06-06-2012', '05-08-1999', '04-12-2012', '25-07-2002', '03-07-2001', '28-09-2001', '24-03-1999', '21-08-2001','23-04-2001', '19-09-2014','26-06-2012', '15-09-2002', '08-12-2013', '20-05-2018','27-03-2015','06-10-1999', '10-02-2001', '02-10-1999','04-04-2014', '03-12-2016'',17-12-2018','28-04-2005','31-03-2009','16-11-2019','15-01-2012','30-4-2002','01-05-2014','03-10-2000','22-07-2010','10-06-2015','18-02-2017','20-09-2005','31-10-2004','04-12-2010','30-07-2007','13-10-2018','29-06-2017','21-11-2016','20-04-2019','24-12-2004','13-05-2009','11-09-2006','24-08-2011','15-06-2015','13-10-2004','06-06-2007','30-09-2013','23-10-2013','02-04-2005','28-02-2016','20-11-2019','24-07-2003']
database['police-complaints']=['YES','NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES', 'NO','NO','NO' ,'YES', 'NO', 'NO','NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO','YES','NO','NO','YES','YES','NO','YES','YES','YES','NO','NO','NO','NO','YES','NO','YES','NO','NO','NO','YES','YES','NO','NO','NO','NO','YES','NO','YES','NO','YES','NO']
#creating police database
col2=['date','time','Location', 'police-station', 'License-plate-no', 'owner-name','identification','solved']
#CREATING EMPTY DATAFRAME
policedatabase=pd.DataFrame(columns=col2)
#ADDING ALL THE COLUMNS
policedatabase['License-plate-no']=['MH03DA9647','TN32AB1234', 'TN10PA1345', 'SK0P1542','JH41708','CH01AN001','MH26AK5678', 'RA45TE1987']
policedatabase['date']=['01:09:2019','11:07:2006','03:09:2013', '22:11:2015','04:05:2008', '19:06:2020','05:06:2018','26:08:2006']
policedatabase['time']=['07:00-pm','12:35-pm', '10:20-am', '8:12-pm', '1:45-pm', '6:19-pm', '11:11-am','03:09-pm']
policedatabase['Location']=['pune','villupuram', 'chengalpet', 'West-sikkim', 'Bandipora', 'chandigarh', 'Amravati', 'dholpur']
policedatabase['police-station']=['Police Commissioner Office of Pune City','Villupuram Superintendent Of Police','D1 Chengalpattu Town Police Station', 'Geyzing PS', 'District Police Station Bandipora', 'Chandigarh Police Headquarters', 'Gadge Nagar Police Station', 'Kotwali Police Station']
policedatabase['owner-name']=['payal','kamali', 'siddarth', 'gayatri', 'Gawtham', 'Dinesh', 'kamala', 'sheela']
policedatabase['identification']=['blue-bumper-damage','blue-left mirror broken','brown-trunk-lining-damage', 'black-rear-trail-light-damage','white-headlight-damage', 'red-wiper-damage', 'white-bumper-damage','fender-damage']

#police case solved should be last column
policedatabase['solved']=['NO','NO', 'YES', 'YES' ,'NO', 'YES' , 'NO', 'YES']
#ACCESSING THE DATABASE USING INDEX
index=pd.Index([text])
k=index.get_loc(text)
lst=[]
lst=database.loc[k,:]
#PRINTING THE DATABASE DETAILS
print("DETAILS OF THE VEHICLE\n\n")
print("LICENSE NUMBER: ",lst[0])
print("OWNER NAME: ",lst[1])
print("PHONE NUMBER: ",lst[2])
print("VEHICLE MODEL: ",lst[3])
print("LICENSE ISSUED DATE: ",lst[4])
print("POLICE COMPLAINT: ",lst[5])
#CHECKING THE POLICE COMPLAINT IS GIVEN OR NOT
if (lst[5]=='YES'):
    index=pd.Index([text])
    k=index.get_loc(text)
    #ACCESSING THE POLICE DATABASE
    lst1=policedatabase.loc[k,:]
    print("\nDETAILS OF THE POLICE COMPLAINT OF THE VEHICLE\n\n")
    print("LICENSE NUMBER: ",lst1[0])
    print("DATE: ",lst1[1])
    print("TIME: ",lst1[2])
    print("LOCATION: ",lst1[3])
    print("POLICE STATION: ",lst1[4])
    print("OWNER NAME: ",lst1[5])
    print("IDENTIFICATION: ",lst1[6])
    print("SOLVED: ",lst1[7])
    if(lst1[7]=='YES'):
        print("CASE SOLVED")
    else:
        print("\n\nCASE NOT SOLVED!!")
if(lst[5]=='YES'  and lst1[7]=='NO'):
    print("STOLEN CAR OR FAKE CAR")
            
