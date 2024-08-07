from django.db import models
from datetime import datetime

#!....... Create your models here........

# ! =========================================================================================================================
class Websites(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=120)
    category = models.CharField(max_length=100)
    year_of_development = models.IntegerField(default=2000)
    framework = models.CharField(max_length=100)

    def __str__(self):
        return 'Name : {} | Address : {} '.format(self.name, self.address)

    class Meta:
        verbose_name_plural = "Websites"


# ! =========================================================================================================================
class Research_Scholars(models.Model):
    name = models.CharField(max_length=100)
    research_topic = models.CharField(max_length=250)
    enrollment_date = models.DateField(auto_now_add=False)
    date_of_completion = models.CharField(max_length=10,help_text = "Please use the following format: <em>YYYY-MM-DD</em>.")
    phone = models.CharField(max_length=10,default='0000000000')
    email = models.CharField(max_length=60,default='abc123@gmail.com')
    address = models.CharField(max_length=100,help_text="Format :: Locality:/District:/State:/Country:/PIN:",default=' ')
    net_JRF = models.BooleanField(default=False)
    image = models.ImageField(upload_to ='static/profiles/rscholars/', height_field=None, width_field=None,default="static/profiles/rscholars/default.png")

    def __str__(self):
        return 'Name : {}      |      NET/JRF : {}'.format(self.name,self.net_JRF)

    class Meta:
        verbose_name_plural = "Research Scholars"



# ! =========================================================================================================================
class Invited_Lectures(models.Model):
    title = models.CharField(max_length=150,help_text="Please provide only the title...")
    date = models.CharField(max_length=12,help_text = "Please use the following format: <em>first three letters of month [.] DD,YYYY</em>. Eg: Sep.21,2021")
    event = models.CharField(max_length=200,help_text="Name of the Event on which the lecture was delivered...")
    organizer = models.CharField(max_length=100,help_text = "Name of the programme where the Lecture was held...")
    location = models.CharField(max_length=100, help_text="Please follow the below format [ Provide any 2 ]: Locality,District,State,Country...")

    def __str__(self):
        return 'ID: {}  | Title : {}...'.format(self.id,self.title[:50])

    class Meta:
        verbose_name_plural = "Invited Lectures"


# ! =========================================================================================================================
class Projects(models.Model):
    title = models.CharField(max_length=200)
    sponsored_by= models.CharField(max_length=100)
    start_date = models.CharField(max_length=30, help_text = "Format : DD[th]_Month,_YYYY  ; Example : 20th March, 2018")
    end_date = models.CharField(max_length=30, help_text = "Format : DD[th]_Month,_YYYY  ; Example : 19th March, 2019")
    duration = models.CharField(max_length=10)
    amount = models.CharField(max_length=16, help_text= "Amount allocated for the completion of Project")
    other_persons = models.CharField(max_length=100, help_text="Use a comma separated list : name1, name2, name3...",default="NA")

    def __str__(self):
        return 'Id : {} | Title : {} '.format(self.id, self.title[:50])

    class Meta:
        verbose_name_plural = "Projects"



# ! =========================================================================================================================
class Awards(models.Model):
    level_choices = (
        ('Local', 'Local'),
        ('State', 'State'),
        ('National', 'National'),
        ('International', 'International'),
    )
    name_of_the_awardees = models.CharField(max_length=80)
    name_of_the_award = models.CharField(max_length=150)
    conferred_on = models.CharField(max_length=20, help_text = "Please use the following format: DD MONTH-NAME, YYYY. Eg:21 March, 2019")
    awarding_agency = models.CharField(max_length=100)
    award_level = models.CharField(max_length=15, choices = level_choices, default= "Local")
    image = models.ImageField(upload_to ='static/gallary/awards/', height_field=None, width_field=None, blank=True, default= 'static/gallary/awards/default.jpg', help_text="Default is /static/gallary/awards/default.jpg")

    def __str__(self):
        return 'Serial No. : {} | Name Of the Award : {} | Conferred On : {}'.format(self.id, self.name_of_the_award[:30], self.conferred_on)

    class Meta:
        verbose_name_plural = "Awards"



# ! =========================================================================================================================
class Presentation(models.Model):
    title_of_presentation = models.CharField(max_length=200)
    # link = models.CharField(max_length=200, help_text = "Please input the file name correctly with correct extension", blank=True, null= True)
    file_name = models.FileField(upload_to= 'static/files/presentation', null= True, blank= True )
    # file_name_uploaded = models.BooleanField(default=True,help_text="If you have uploaded the file Select True, else Select False")

    def __str__(self):
        return 'Serail No : {}  |  Name Of the Presentation : {}'.format(self.id, self.title_of_presentation[:50])

    class Meta:
        verbose_name_plural = "PPT's"



# ! =========================================================================================================================
class Articles_In_Journals(models.Model):
    title_of_article = models.CharField(max_length=250,blank=False)
    journal_name = models.CharField(max_length=200,blank=False, help_text="Name of the Journal in which article was featured. Along with indexing information.")
    along_with = models.CharField(max_length=20,blank=True,null=True, help_text= "Maximum 20 characters allowed, Try to complete the name within the limit.")
    year = models.CharField(default= datetime.now().year ,max_length=5,help_text="Please provide the Year only <em>YYYY</em>. Eg: 2012")
    link = models.CharField(max_length=250, help_text = "Please input the file name correctly with correct extension", blank=True, null= True)
    file_name = models.FileField(upload_to= 'static/files/articles', null= True, blank= True )
    file_name_uploaded = models.BooleanField(default=False ,help_text="If you have uploaded the file click the box else leave it unchecked.")


    def __str__(self):
        return 'Serial No: {} | Name Of the Articles : {}...'.format(self.id, self.title_of_article[:60])

    class Meta:
        verbose_name_plural = "Articles In Journals"




# ! This page attributes have not been decided yet...Have to be implemented later...
# ! =========================================================================================================================
# class Conference_Papers(models.Model):
#     title_of_conference_papers = models.CharField(max_length=300)
#     year = models.CharField(default="NA",max_length=5,help_text="Please provide the Year only <em>YYYY</em>")
#     link = models.CharField(max_length=200, help_text = "Please input the file name correctly with correct extension", blank=True, null= True)
#     file_name = models.FileField(upload_to= 'static/files/conference_papers', null= True, blank= True )
#     file_name_uploaded = models.BooleanField(default=False,help_text="If you have uploaded the file Select True then else Select False")


#     def __str__(self):
#         return 'Name Of the Presentation : {}'.format(self.title_of_presentation[:30])

#     class Meta:
#         verbose_name_plural = "Conference Papers"





# ! =========================================================================================================================
class Chapters_In_Edited_Books(models.Model):
    chapter_title = models.CharField(max_length=150)
    book_name = models.CharField(max_length=200, help_text="Name of the book where the chapter is published.")
    editors = models.CharField(max_length=60, default="NA",help_text="Provide a comma separated list. Note: Use NA if publisher is not available. Minimum Charater 5 for Editors Name")
    published_by = models.CharField(max_length=100, default="NA",help_text="Note: Use NA if publisher is not available. Minimum Charater 5 for Publisher Name.")
    along_with = models.CharField(max_length=20,blank=True,null=True, help_text= "Maximum 20 characters allowed, Try to complete the name within the limit.")
    year = models.CharField(default="NA",max_length=5,help_text="Please provide the Year only YYYY")
    pages = models.CharField(default="NA", max_length= 14, help_text="Use format Start_page_num - Ending_page_no. Eg : 201-214")
    link = models.CharField(max_length=250, help_text = "Please input the file name correctly with correct extension", blank=True, null= True)
    link_available = models.BooleanField(default=False,help_text="If you have provided the link Select the box else leave it blank.")


    def __str__(self):
        return 'Serial No : {} | Name Of the Chapter : {}...'.format(self.id, self.chapter_title[:50])

    class Meta:
        verbose_name_plural = "Chapters In Edited Books"



# ! =========================================================================================================================
class Books(models.Model):
    color_choices = (
        ('rose', 'Rose'),
        ('pink', 'Pink'),
        ('fuchsia', 'Purple'),
        ('violet','Violet'),
        ('indigo','Indigo'),
        ('blue','Blue'),
        ('cyan','Light Blue'),
        ('teal','Teal'),
        ('emerald','Dark Green'),
        ('green','Light Green'),
        ('lime','Parrot'),
        ('yellow','Yellow'),
        ('orange','Orange'),
        ('red','Red'),
        ('stone','Brown'),
        ('gray','Gray')
    )
    availability_choices = (
        ('proceed', 'BUY'),
        ('link', 'Link'),
        ('unavailable', 'Unavailable'),
        ('no_stock', 'Out of Stock'),
    )
    title = models.TextField(max_length=150,blank=False)
    sub_title = models.TextField(max_length=300,default="NA", help_text= "Maximum Length is 300 characters.Minimum is 5 characters.")
    author_editor_compiler = models.CharField(max_length=100, default="Dr. Badan Barman",help_text="In case of multiple authors use a comma separated list.")
    contributors = models.CharField(max_length=100, default="Dr. Badan Barman", help_text="Maximum 100 charaters allowd in this field.")
    about_the_book = models.TextField(max_length=2000, default="NA", help_text="Minimum text 20 characters is needed about the book. Maximum 2000 characters.")
    publisher = models.CharField(max_length=60,default="NA",help_text="Maximum 60 characters allowed in this field.")
    binding = models.CharField(max_length=40,default="PaperBack")
    language = models.CharField(max_length=60,default="English")
    genre = models.CharField(max_length=80,default="Language Arts")
    place = models.CharField(max_length=60,default="Guwahati, Assam", help_text="Maximum 60 charaters allowed in this field.")
    year = models.CharField(default="2000",max_length=4,help_text="Please provide the Year only <em>YYYY</em>")
    pages = models.IntegerField(default=0,help_text="Total no of pages here.")
    dimensions = models.CharField(default="NA",help_text="format = Height X Width X Depth. Eg: 28cm X 8cm X 2cm",max_length=20)
    weight = models.CharField(default="NA", help_text= "format = Value Kg. Eg: 2.1 Kg.", max_length = 10,null=True, blank=True)
    original_price = models.IntegerField(default=0, help_text="The Price written on the Book")
    sale_price = models.IntegerField(default=0,help_text="The Price for which the Book is to be sold")
    isbn_issn = models.CharField(max_length=60,default="NA")
    show_total_no_of_units_sold = models.BooleanField(default=False)
    total_no_of_units_sold = models.CharField(max_length=50,help_text="Eg: 1 million +",default="NA")
    availability = models.CharField(max_length=20, choices = availability_choices, default= "Unavailable", help_text="If Link selected then provide the link below.")
    is_book_link_available = models.BooleanField(default= False)
    book_link_to_other_sources = models.CharField(default="NA",max_length=200)
    image = models.ImageField(upload_to ='static/gallary/books/', height_field=None, width_field=None, blank=True, default= 'static/gallary/books/default.jpg')
    book_cover_color = models.CharField(max_length=15, choices = color_choices, default= "Gray",help_text="This color is use to match the background in HTML Document with that of the book.")
    priority = models.IntegerField(unique = True, null= False, blank= False, help_text = "This Number is used to denote the priority of the book. Higher the No. higher is the positon of the book in the HTML.")

    def __str__(self):
        return 'Book_ID : {} | Book : {}... '.format(self.id, self.title[:30])

    class Meta:
        verbose_name_plural = "Books"



# ! =========================================================================================================================
class Periodicals(models.Model):
    title = models.CharField(max_length=200,blank=False)
    about_the_book = models.TextField(max_length=1000,default="NA")
    author_editor_compiler = models.TextField(max_length=300, default="NA")
    publisher = models.CharField(max_length=60,default="NA")
    place = models.CharField(max_length=60,default="Guwahati")
    volume = models.CharField(max_length=15,default="NA")
    issue = models.CharField(default="NA",max_length=20)
    month = models.CharField(default="Jan",max_length=20,help_text="Provide the First 3 letter of the Month only if possible. Eg: Jan-Feb or Apr")
    year = models.CharField(default="2000",max_length=5,help_text="Please provide the Year only <em>YYYY</em>")
    pages = models.CharField(default="NA",max_length=10)
    price = models.IntegerField(default=0, help_text="The Price of the Periodical.")
    isbn_issn = models.CharField(max_length=50,default="NA")
    is_purchase_possible = models.BooleanField(default= False,help_text="Is the book available to purchase. If YES ,tick the checkbox.")
    link = models.CharField(default="NA",max_length=200,help_text="Provide the link to Purchase or Download the edition.")
    image = models.ImageField(upload_to ='static/gallary/periodicals/', height_field=None, width_field=None, blank=True, default= 'static/gallary/periodicals/default.jpg')

    def __str__(self):
        return 'Name : {} | Publisher : {} '.format(self.title, self.publisher)

    class Meta:
        verbose_name_plural = "Periodicals"