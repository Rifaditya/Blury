init -4:

    #First we set up some variables:

    $ m_name = "" #The name that will appear
    $ f_name = "" #The name that will appear
    $ m_name_last = "" #The name that will appear
    $ f_name_last = "" #The name that will appear

    #Then we create the list with possible names.

    $ name_list = ["Paul", "John", "George", "Ringo"]
    $ l_name_list = ["McCartney", "Lennon", "Harrison", "Starr"]
    $ name_list1 = ["Elizabeth", "Imani", "Cassidy", "Helena", "Faye", "Maya", "Layla", "Destiny" ]
    $ l_name_list1 = ["Addison", "Alannah", "Amani", "Kassandra", "Fernanda", "Kaylin", "Audrina", "Aniyah", "Remington", "Aubriella"]
init python:

    class GENERATOR1:
        def femalename(self):
            generatedname1 = renpy.random.choice(name_list1)
            generatedlastname1 = renpy.random.choice(l_name_list1)
            store.f_name = generatedname1 + " " + generatedlastname1
            store.f_name_last = generatedlastname1
    class GENERATOR:
        def femalename(self):
            generatedname1 = renpy.random.choice(name_list1)
            generatedlastname1 = renpy.random.choice(l_name_list1)
            store.f_name = generatedname1 + " " + generatedlastname1
            store.f_name_last = generatedlastname1
        def malename(self):


            generatedname = renpy.random.choice(name_list)

            #Take one name from the name_list list and store it at generatedname
            generatedlastname = renpy.random.choice(l_name_list)

            #Ditto

            store.m_name = generatedname + " " + generatedlastname

            store.m_name_last = generatedlastname

            #Show the result of putting both together and store it on the gen_name variable.
            #If not for the " " part we could get RingoStarr
