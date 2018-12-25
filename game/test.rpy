init -4:

    $ m_name = ""
    $ f_name = ""
    $ m_name_last = ""
    $ f_name_last = "" 

    $ name_list = ["Paul", "John", "George", "Ringo"]
    $ l_name_list = ["McCartney", "Lennon", "Harrison", "Starr"]
    $ name_list1 = ["Elizabeth", "Imani", "Cassidy", "Helena",
                    "Faye", "Maya", "Layla", "Destiny" ]
    $ l_name_list1 = ["Addison", "Alannah", "Amani", "Kassandra",
                    "Fernanda", "Kaylin", "Audrina", "Aniyah",
                    "Remington", "Aubriella"]

init python:

    class GENERATOR1:

        def femalename(self):

            generatedname1 = renpy.random.choice(name_list1)
            generatedlastname1 = renpy.random.choice(l_name_list1)
            store.f_name = generatedname1 + " " + generatedlastname1
            store.f_name_last = generatedlastname1

    class GENERATOR:

        def malename(self):


            generatedname = renpy.random.choice(name_list)
            generatedlastname = renpy.random.choice(l_name_list)
            store.m_name = generatedname + " " + generatedlastname
            store.m_name_last = generatedlastname
