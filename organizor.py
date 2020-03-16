####zdzdzd####


################## fonction de lecture de la database ###########

import os

from collections import OrderedDict


#cette fonction permet de récupérer les données présentes dnas le fichier input et d'en faire une liste


############ utilitaires #################"


def read_csv(csv_file):
    with open(csv_file,'r') as csv_file:
        csv_brut = csv_file.readlines()
        csv_list = []
        for line in csv_brut:
            line = line.split(',')
            csv_line = []
            for item in line:
                item = item.split('\n')
                csv_line.append(item[0])
            csv_list.append(csv_line)


    return csv_list
                
            


############lecture lists #############""

def input_list():
    
    with open('database/input_list.txt') as input:
        input = input.read()
        input_list = input.split('\n')
        for i in input_list:
            if i =='':
                input_list.remove(i)
                

    return input_list

def category_list():

    dico_categories = {}

    with open('database/tags/categories.csv','r') as file_categories:
        categories = file_categories.readlines()
        dico_categories = {}
        for line in categories:
            line = line.split(',')
            name = line[1]
            name = name.split('\n')
            dico_categories[line[0]] = name[0]   


    return dico_categories

def tag_list():

    dico_tags = {}

    dico_categories = (category_list())

    for id in range(1,len(dico_categories)+1):
        category = dico_categories[str(id)]
        tag_list_line = read_csv('database/tags/' + category + '.csv')
        #print (tag_list_line)
        dico_tag_line = {}
        for tag in tag_list_line:
            dico_tag_line[tag[0]] = tag[1]
        dico_tags[str(id)] = dico_tag_line

    return dico_tags


################################# fonctions ####################################


#traitement iput il faut que je relise exactement le passage GTD sur le traitement des inputs

def add_input():

    print('Note the new item to add in the input list')
    with open('database/input_list.txt', 'a') as file:
        item = input()

        while item != '':
            file.write(item + ' \n')
            item = input()

def traiter_input():
    

    print('stat by reading all you email, delete the useless ones, and stor the others by importance, add the important emails in the input list')
    print()
    add_input()

    list_input  = input_list()

    for item in list_input:

        print(item)
        print()
        
        action = input('Is this item actionable ? ')
        
        if action == 'n':
            action = input('Is this trash [1], reference [2], sometime/maybe [3]' )
            if action == '1':
                list_input.remove(item)
            elif action == '2':
                with open('database/reference/reference_list.txt','a') as file:
                    ref = input('note the reference name : ')
                    file.write(ref)
            elif action == '3':
                with open('database/sometime-maybe/reference_list.txt','a') as file:
                    ref = input('note the sometime-maybe name : ')
                    file.write(ref)

        if action == 'y':

            print('determine the next action \n')

            print('Can you do it in less than 2 min [1], is it an acion that you do yourself [2], do you need to delegate it ? [3]')
            action =input()

            if action == '1':
                print('do it now \n')
                action = input('is it done ?')
                if action == y:
                    print(congrats)
                    list_input.remove(item)
                
            if action == '2':
                print('toto')

                
    return

def revue_action(action_dico):

    print('voulez-vous avoir les actions spécifiques à des tags ? ')
    selected_tags = []
    tag = input()
    while tag != '': 
        selected_tags.append(tag)
        tag = input()
    print()
    print('########## liste des actions #############')


    #selection des actions qui correspondent aux tags
    for name in action_dico:
        
        tag_test = 0
        tag_list = action_dico[name][1]
        for i in selected_tags:
            for j in tag_list:
                if i == j:
                    tag_test = tag_test + 1

       
                    
        if tag_test == len(selected_tags):
            projet = action_dico[name][0]
            tags = ''
            for tag in tag_list:
                tags = tags + ' ' + tag

            deadline_list = action_dico[name][3]

            deadline = ''

            if deadline_list !=[]:

                for i in deadline_list:
                    if deadline == '':
                        deadline = i
                    else:
                        deadline = deadline + '/' + i
            else:
                deadline = ' ND'



            print('-----------')
            print()
            print(name)
            print()
            print('projet : ' + projet[0])
            print()
            print('tags : ' + tags)
            print()
            print('deadline :' + deadline)
            print()
            pause = input()
        

    return

 # def ajouter_projet():
 #    file = open('database/test.txt', 'w+')
 #    'Notez les nouveaux items de la liste input'

 #    print('write the text (enter then stop will stop the writing')
 #    print()

 #    text = ''

 #    while text != 'stop':
 #        text = input('')
 #        if text != 'stop':
 #            file.write(text + '\n')
 #    file.close

def create_project():

    project_name = input('What is the poject_name ? : ')

    with open('./database/projects/project_list.txt','a') as f:
        f.write(project_name + '\n')

    os.mkdir('database/projects/' + project_name)
    
    os.mkdir('database/projects/' + project_name +'/actions')
    os.mknod('database/projects/'+ project_name +  '/actions/action_list.txt')

    os.mkdir('database/projects/' + project_name +'/completed_actions')
    os.mknod('database/projects/'+ project_name +  '/completed_actions/completed_action_list.txt')

    print('\n describe the project (enter stop will stop the writing')

    text = ''

    with open('./database/projects/' + project_name +'/description.txt','w+') as file:
        while text != 'stop':
            text = input()
            if text != 'stop':
                file.write(text + '\n')

    return


def create_tag():
    print('\n The existing categories are : ')

    dico_categories = category_list()

    print(dico_categories)
            
    print('\n' + 'Add a new category (y/n) ?')
    action = input()
    if action == 'y':
        print('new category name ? ')
        chosen_category = input()
        with open('database/tags/categories.csv','a') as file:
            file.write('\n ' + str(len(dico_categories) + 1)  + ',' + chosen_category)
            os.mknod('database/tags/' + chosen_category + '.csv')
            print('\n Add your new tag')
            new_tag = input()

            with open ('database/tags/' + chosen_category + '.csv', 'a') as file_category:
                file_category.write('\n 1'+ ',' + new_tag)
                print('\n The tag ' + new_tag + ' has been added to the category' + chosen_category)
           
    elif action == 'n':
        print('chose your category by chosing the id ')
        id = input()
        chosen_category = dico_categories[id]

        dico_tags = tag_list()
        print() 
        print(dico_tags[id])


        print('\n Add your new tag')
        new_tag = input()

        with open ('database/tags/' + chosen_category + '.csv', 'a') as file_category:
            new_id = str(len(dico_tags[id]) +1)
            file_category.write('\n' + new_id + ',' + new_tag)
        print('\n The tag ' + new_tag + ' has been added to the category' + chosen_category)
     

################### exécution  #######################""


create_tag()
                    
#category_list()
#tag_list()





#Réflexions sur le progamme :
#peut être faudrait-il associer les tags à des ID permettant de les sélectionner plus facilement sans avoir besoin de taper leur nom et en les séparant de manière intelligent, par exemple les 1 correspondent à un type de travail (perso, boulot), perso 1.1 boulot 1.2, pour les lieux cela peut être 2 (maison 2.1, bureau 2.2 labo 2.3...) les 3 un type de travail genre ordi 3.1, livre 3.2..


