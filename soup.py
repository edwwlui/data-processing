
from bs4 import BeautifulSoup

file_list=["english-ontonotes-5.0-train-document-ids","english-ontonotes-5.0-development-document-ids","english-ontonotes-5.0-conll-2012-test-document-ids","english-ontonotes-5.0-test-document-ids"]
for file in file_list:
    output_file="annotated-"+file[:-4]+".txt"
    output=""
    with open("server-"+file+".txt", "r") as path_f:
        for line in path_f:  #one file per line
            try:
                with open(line.strip()+".name","r") as input_file:


                    #input_file="cctv.txt"


                    soup = BeautifulSoup(input_file, 'html.parser')

                    #soup = BeautifulSoup(input_doc, 'html.parser')
                    #print(soup.get_text())

                    #print(soup)

                    name_list=[]
                    tag_string_dict={}
                    j=0
                    enamex_list = soup.find_all('enamex')
                    n_enamex_list = len(soup.find_all('enamex'))
                    while j<n_enamex_list:
                        tag=enamex_list[j]
                        
                        if tag.string==None:
                            extra_tag=int(str(tag).count("<")/2-1)  #count (the num of "<" over 2) -1 , skip this num
                            if extra_tag>0:
                                composite=str(tag)
                                temp_soup=BeautifulSoup(composite, 'html.parser')
                                composite_list=temp_soup.findAll(text=True)
                                temp_str=""
                                if_begin=True
                                string_list=[]

                                for string in composite_list:  #maybe phrases, separate into single word
                                    for word in string.split(" "): 
                                        string_list.append(word)

                                for word in string_list:
                                    if if_begin==True and word is not "":
                                        temp_str+=word+"/B-"+tag['type']+" "
                                        if_begin=False
                                    elif if_begin==False and word is not "":
                                        temp_str+=word+"/I-"+tag['type']+" "
                                name_list.append(temp_str)
                                j+=extra_tag
                        elif len(tag.string.split(" "))==1:  #single word

                            temp_str=tag.string+"/B-"+ tag['type']+" "
                            name_list.append(temp_str)

                        elif len(tag.string.split(" "))>1:
                            temp_str=""
                            if_begin=True
                            for word in tag.string.split(" "):
                                if if_begin==True:
                                    temp_str+=word+"/B-"+tag['type']+" "
                                    if_begin=False
                                elif if_begin==False:
                                    temp_str+=word+"/I-"+tag['type']+" "
                            name_list.append(temp_str)
                        try:
                            soup.enamex.extract()
                        except AttributeError as e:
                            print(e)
                        tag_string_dict[tag.string]=tag['type']  #add at the end to prevent being matched beforehand
                        j+=1
                    #print(tag_string_dict)
                    #print(name_list)
                    #soup.enamex.extract()

                    word_list=soup.get_text().strip().replace("\n"," \n ").split(" ")
                    #print(word_list)
                    output+="-DOCSTART-/O\n"
                    i=0
                    k=0
                    while k< len(word_list):
                        word=word_list[k]
                        if word != "" and word != "\n":
                            output+=word+"/O "
                            #print(output)
                        elif word is "\n":
                            output+="\n"
                            #print(output)
                        elif word is ""  and word_list[k-1] != "\n" and word_list[k+1] != "\n":
                            output+=name_list[i]
                            #print(output)
                            i+=1
                        k+=1
                    output+="\n"
                    print(line)
                    #print(tag_string_dict)
                    #print(input_doc.strip().split(" "))

            except FileNotFoundError as e:
                print(e)
    with open(output_file,"a") as output_doc:
        output_doc.write(output)

