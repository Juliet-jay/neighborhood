from django.test import TestCase
from .models import Location,Neighbourhood, Image,User, Profile
from django.core.files.uploadedfile import SimpleUploadedFile
# Create your tests here.

class NeighbourhoodTestClass(TestCase):
    

    def setUp(self):
        self.test_tags = tags(name='funny')
        self.test_tags.save()
        
     # Testing instance

    def test_instance(self):
        self.assertTrue(isinstance(self.test_tags, tags))
        
    # Testing Save method

    def test_save_method(self):
        self.test_tags.save()
        tagss = tags.objects.all()
        self.assertTrue(len(tagss) > 0)
        
    # Tear down method
    def tearDown(self):
        tags.objects.all().delete()
        
     # Testing delete method

    def test_delete_tags(self):
        self.test_tags.delete()
        self.assertEqual(len(tags.objects.all()), 0)


