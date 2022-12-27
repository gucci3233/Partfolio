from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models import Model, EmailField, ForeignKey, URLField, CASCADE, CharField
from django_resized import ResizedImageField


# Create your models here.
class Profile(Model):
    image = ResizedImageField(size=[455, 268], upload_to='user/')
    name = CharField(max_length=500)
    job = CharField(max_length=900)
    description = RichTextField()

    class Meta:
        verbose_name = 'Profile'


class AboutMe(Model):
    prof_image = ForeignKey(Profile, on_delete=CASCADE)
    firstname = CharField(max_length=300)
    lastname = CharField(max_length=400)
    age = CharField(max_length=255)
    nationality = CharField(max_length=200)
    address = CharField(max_length=300)
    phone = CharField(max_length=100)
    email = EmailField()
    languages = CharField(max_length=400)
    course_name = CharField(max_length=400)
    studied_in = CharField(max_length=400)
    res_desc = RichTextUploadingField()

    class Meta:
        verbose_name = 'About'


class MyPortfolio(Model):
    project_name = CharField(max_length=300)
    project_image = ResizedImageField(size=[340, 210], upload_to='portfolio/')  # in detail 600 x 370

    def __str__(self):
        return self.project_name


class DetailPort(Model):
    portfolio = ForeignKey(MyPortfolio, on_delete=CASCADE, related_name='portfolio')
    project = CharField(max_length=400)
    worked_lang = CharField(max_length=500)
    project_url = URLField()


class ContactMe(Model):
    desc_title = CharField(max_length=252)
    description = RichTextField()
    email = EmailField()
    phone = CharField(max_length=222)


class LangImage(Model):
    image_lang = RichTextUploadingField()


class SecondResume(Model):
    course_name = CharField(max_length=400)
    studied_in = CharField(max_length=400)
    res_desc = RichTextUploadingField()
