'''
COMP9321 Assignment One Code Template 2019T1
Name: Hang Zhang
Student ID: z5153042
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv,json

def title_style_convertor(str):
    str = str.title()
    l = str.split()
#     print(l)
    new_str = []
    for j in l:
        if j in ['La','De']:
            new_str.append(j.lower())
            continue
        if "'" in j:
            temp = j.split("'")
            temp_ = ''
            if temp[0] == 'L' or  temp[1] == 'D':
                temp_ += temp[0].lower() + "'" + temp[1]
                new_str.append(temp_)
                continue
            
            new_str.append(j)
            continue
        new_str.append(j)
#     print(new_str)
    return ' '.join(new_str)

def q1():
    '''
    Put Your Question 1's code in this function
    '''
    accident = 'accidents_2017.csv'
    # raw_data = pd.read_csv(accident)
    # print(raw_data.head(10))

    with open(accident,encoding = 'utf8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
#     str_q1 = ''
        for row in csv_reader:
            str_q1 = ''
#         print(row)
            if line_count == 0:
                for i in row:
                    # i = title_style_convertor(i) # title style
                    if ' ' in i.strip(' '):
                        str_q1 = str_q1 + '"' + i.strip(' ') +'"' + ' '
                    else:
                        str_q1 = str_q1 + i.strip(' ') + ' '
                line_count += 1
            elif line_count <= 10:
                for i in row:
                    i = title_style_convertor(i) # title style
                    if ' ' in i.strip(' '):
                        str_q1 = str_q1 + '"' + i.strip(' ') +'"' + ' '
                    else:
                        str_q1 = str_q1 + i.strip(' ') + ' '
                line_count += 1
            else:
                break
            str_q1 = str_q1.strip(' ')

            print(str_q1)

    csv_file.close()

def q2():

    accident = 'accidents_2017.csv'
    with open(accident,encoding = 'utf8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        
        with open('result_q2.csv', mode='w',newline = '',encoding = 'utf8') as result_q2:
            result_q2_writer = csv.writer(result_q2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            line_count = 0
            seen = set()
        #     str_q1 = ''
            for row in csv_reader:
        #         str_q1 = ''
    #             print(row)
                sss = []

                if line_count == 0:
                    result_q2_writer.writerow(row)
                    line_count += 1
                else:
    #                 print(type(row))
                    if 'Unknown' in row or '-' in row:
                        line_count += 1
                        continue
                    # remove duplicate
                    if row[0] in seen:
                        line_count += 1
                        continue

                    seen.add(row[0])

                    line_count += 1
                    
                    position = 0
                    for ele in row:
    #                     print(ele)
                        if position in [0,1,2,3]:
    #                         print(ele,'---->',ele.title())
                            sss.append(title_style_convertor(ele))  
                        else:
                            sss.append(ele)
                        position += 1
    #                 print('position:',position)
    #                 print(sss)
                    
                    result_q2_writer.writerow(sss)

        result_q2.close()
    csv_file.close()
    # test
    # result_q2_temp = pd.read_csv('result_q2.csv')
    # print(result_q2_temp.head(10))

def q3():
    '''
    Put Your Question 3's code in this function 
    '''
    result = 'result_q2.csv'

    raw_data = pd.read_csv(result)
    # print(raw_data)
    gd = raw_data.groupby([pd.Grouper(key = 'District Name')]).size().reset_index(name ='Total numbers of accidents')
    # print(gd,'\n')
    order_list = []
    for index, row in gd.iterrows():
    #     print(row['District Name'], row['Total numbers of accidents'])
        order_list.append([row['District Name'],int(row['Total numbers of accidents'])])
        
    # print(order_list,'\n')

    # for i in order_list:
    #     print(i)
    l = sorted(order_list,key=lambda x: x[1],reverse = True)
    # print(l,'\n')
    print('"District Name"','"Total numbers of accidents"')
    for i in l:
        if ' ' in i[0]:
            sss = ''
            sss += '"'+i[0]+'"'
            print(sss,i[1])
        else:
            print(i[0],i[1])

def q4():
    '''
    Put Your Question 4's code in this function 
    '''
    stations = 'air_stations_Nov2017.csv'
    quality = 'air_quality_Nov2017.csv'

    # part 1

    with open(stations, encoding = 'utf8') as station_csv:
        reader = csv.reader(station_csv, delimiter=',')
        with open('temp.csv','w',newline='',encoding = 'utf8') as temp:
            
            writer = csv.writer(temp,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            
            count = 0
            
            for row in reader:
                content = []
                position = 0
                
                for ele in row:
                    if position in [0,4]:
                        content.append(title_style_convertor(ele))
                    
                    position += 1
                    
                if count != 0:
                    writer.writerow(content)
                count+=1

        temp.close()
    station_csv.close()

    with open('temp.csv', encoding = 'utf8') as temp_csv:
        reader = csv.DictReader(temp_csv,['Station','District Name'])
        out= json.dumps([row for row in reader])
        print(out)
    temp_csv.close()

    # part 1 ends

    # part 2 
    with open(quality,encoding = 'utf8') as quality_csv:
        csv_reader = csv.reader(quality_csv, delimiter=',')
        line_count = 0
        print_count = 0
    #     seen = set()
        for i in csv_reader:
            out = []
            str_q4 = ''
            if line_count == 0:
                for ele in i:
                    out.append(ele)
                line_count += 1
                for cha in out:
                    if ' ' in cha.strip(' '):
                        str_q4 = str_q4 + '"' + cha.strip(' ') + '"' + ' '
                    else:
                        str_q4 = str_q4 + cha.strip(' ') + ' '
                str_q4 = str_q4.strip(' ')
                print(str_q4)
            else:
                if '--' in i[1] or 'Good' in i[1]:
                    line_count += 1
                    continue
                else:
                    position = 0
                    line_count += 1
                    for ele in i:
                        if position in [0]:
                            out.append(title_style_convertor(ele))
                        else:
                            out.append(ele)
                        position += 1
                    for cha in out:
                        if ' ' in cha.strip(' '):
                            str_q4 = str_q4 + '"' + cha.strip(' ') + '"' + ' '
                        else:
                            str_q4 = str_q4 + cha.strip(' ') + ' '
                    str_q4 = str_q4.strip(' ')
                    print(str_q4)
                    print_count += 1
                    
                    if print_count > 10:
                        break
    # part 2 ends

    # part 3 

    with open('air_stations_Nov2017.csv', encoding = 'utf8') as station:
        stat = csv.reader(station)
        stat_district = dict()
        for i in stat:
            station_name = title_style_convertor(i[0].strip(' '))
            district_name = title_style_convertor(i[4].strip(' '))
    #         print(station_name,':',district_name)
            stat_district[station_name] = district_name
    #     print(stat_district)
    station.close()

    month_dict = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}

    with open('air_quality_Nov2017.csv', encoding = 'utf8') as quality:
        with open('result_q4.csv','w',newline='',encoding = 'utf8') as result_q4_p3:
            qual = csv.reader(quality)
            resu = csv.writer(result_q4_p3, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            with open('result_q2.csv',encoding = 'utf8') as accident_:
                acci = csv.reader(accident_)
                for i in acci:
                    resu.writerow(i)
                    break
            accident_.close()
                    
            count = 0
            count_match = 0
            for i in qual:
                if '--' in i[1] or 'Good' in i[1] or 'Air Quality' in i[1]:
                    continue
                else:
                    dis = i[0].strip(' ')
                    # print(dis) 
                    
                    date_month_time = i[13].split(' ')
                    # print(date_month_time)
                    
                    count += 1
                    district = stat_district[title_style_convertor(dis)] # distrcit
                    # print(dis,':',district)
    #                 print(type(district))

                    date, month, year = date_month_time[0].split('/')
                    # print('date,month,year:',date,month,year)
    #                 print(type(date),type(month),type(year))
                
                    time = date_month_time[1].split(':')[0]
                    # print('time:',time,'\n')
    #                 print(type(time))
                    
                    with open('result_q2.csv',encoding = 'utf8') as accident:
                        acci = csv.reader(accident)

                        for j in acci:
    #                         print(j)
    #                         print(type(j[1]),j[1],type(j[6]),j[6],type(j[7]),j[7])
                            if district == j[1].strip(' ') and date == j[6].strip(' ') and month_dict[month] == j[5] and time == j[7]:
                                count_match += 1
    #                             print(j)
    #                             print(j[1],j[6],j[7],'\n')
                                resu.writerow(j)
                                
                    
                    accident.close()

    #                 print('\n')
                            
        result_q4_p3.close()
    quality.close()

    # part 3 ends

def q5():
    '''
    Bonus Question(Optional).
    Put Your Question 5's code in this function.
    '''
    pass 


if __name__ == '__main__':
    print('Question_1 showing as below \n')
    q1()
    print('Question_2 showing as below \n')
    q2()
    print('Question_3 showing as below \n')
    q3()
    print('Question_4 showing as below \n')
    q4()





'''
edited by groupmate

from Crypto.Cipher import DES
from Crypto import Random
import sys,binascii
import time

input_arg = sys.argv
if len(input_arg) != 5:
    print('example: python tempdes.py iv key inputfile outputfile')
    sys.exit(0)
else:
    errMsgDict = {1: "iv length invalid", 2: "iv contains invalid character", 3: "key length invalid", 4: "key contains invalid character"}
    errMsgCounter = 0
    for para in [input_arg[1], input_arg[2]]:
        errMsgCounter += 1
        if len(para) != 16:
            print(errMsgDict[errMsgCounter])
            sys.exit(0)
        try:
            errMsgCounter += 1
            int(para, 16)
        except:
            print(errMsgDict[errMsgCounter])
            sys.exit(0)

cbc_key = binascii.unhexlify(input_arg[2])  
iv = binascii.unhexlify(input_arg[1])

des1 = DES.new(cbc_key, DES.MODE_CBC, iv)
des2 = DES.new(cbc_key, DES.MODE_CBC, iv)
totalEncTime = 0
with open(input_arg[4],'wb') as outputfile:
    with open(input_arg[3],'rb') as inputfile:
        try:
            while True:
                block = inputfile.read(8)
                if not block:
                    break
                # print(len(block),type(block),block)
                if len(block) != 8:
                    intent_blank = 8 - len(block)
                    block = bytes.fromhex(block.hex() + intent_blank*'00')
                start_enc_time = time.time()
                encrypted_block = des1.encrypt(block)
                totalEncTime += time.time() - start_enc_time
                outputfile.write(encrypted_block)
                # print(encrypted_block)
        finally:
            inputfile.close()
    outputfile.close()

finalText = ""
totalDecTime = 0
with open(input_arg[4],'rb') as inputfile:
    try:
        while True:
            block = inputfile.read(8)
            if not block:
                break
            start_dec_time = time.time()
            decrypted_block = des2.decrypt(block)
            totalDecTime += time.time() - start_dec_time
            decrypted_str = decrypted_block.decode("utf-8")
            finalText += decrypted_str.replace("\x00", "")
    finally:
        inputfile.close()
#         print(finalText, end="")
# with open(f"{input_arg[4]}.txt",'w') as outputfile:
#     outputfile.write(finalText)
# outputfile.close()

print("%s microsecends ---enc--- " % str(totalEncTime * 1e+6))
print("%s microsecends ---dec--- " % str(totalDecTime * 1e+6))

''' 


''' 4.c

from sys import argv
from Crypto.Cipher import AES
from Crypto import Random
import time

cbc_key = Random.get_random_bytes(16)
# print 'key', [x for x in cbc_key]

iv = Random.get_random_bytes(16)


aes1 = AES.new(cbc_key, AES.MODE_CBC, iv)
aes2 = AES.new(cbc_key, AES.MODE_CBC, iv)

plain_text = ""
with open(argv[1]) as f:
    raw_plain_text = f.readlines() # <- 16 bytes
    for eachsentence in raw_plain_text:
        plain_text += eachsentence
#     print(plain_text)

if len(plain_text) % 16:
    for lengthTODO in range( 16 - len(plain_text) % 16 ):
        plain_text += "\x00"
start_enc_time = time.time()
cipher_text = aes1.encrypt(plain_text)
# print(cipher_text)
print("%s microsecends ---enc--- " % str((time.time() - start_enc_time) * 1e+6))
start_dec_time = time.time()
msg=aes2.decrypt(cipher_text)
# print msg.replace("\x00", ""), 
print("%s microsecends ---dec--- " % str((time.time() - start_dec_time) * 1e+6))

'''

''' 4.d

import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast
from sys import argv
import time

random_generator = Random.new().read
key = RSA.generate(1024, random_generator) #generate pub and priv key

publickey = key.publickey() # pub key export for exchange

plain_text = ""
with open(argv[1]) as f:
    raw_plain_text = f.readlines()
    for eachsentence in raw_plain_text:
        plain_text += eachsentence
#     print(plain_text)
start_enc_time = time.time()
encrypted = publickey.encrypt(plain_text, 32)
print("%s microsecends ---enc-- " % str((time.time() - start_enc_time) * 1e+6))
#message to encrypt is in the above line 'encrypt this message'
# print ('encrypted message:', encrypted) #ciphertext

#decrypted code below
start_dec_time = time.time()
decrypted = key.decrypt(ast.literal_eval(str(encrypted)))
print("%s microsecends ---dec--- " % str((time.time() - start_dec_time) * 1e+6))
# print ('decrypted', decrypted)

'''
