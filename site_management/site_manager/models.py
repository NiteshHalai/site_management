from django.db import models

# Create your models here.
class Sites(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    site_id = models.IntegerField(primary_key=True)
    site_name = models.CharField(max_length=200)
    customer_id= models.ForeignKey(to='customer', on_delete=models.PROTECT)
    site_in_charge= models.ForeignKey(to='person', on_delete=models.PROTECT)
    name_of_product= models.CharField(max_length=200)
    date_of_creation = models.DateTimeField()
    date_of_commence = models.DateTimeField()
    estimated_date_




= SITE ID
= SITE NAME
= CUSTOMER ID
= SITE IN CHARGE
= PERSONS ON SITE
= NAME OF PRODUCT
= DATE OF CREATION. (DATETIME)
= DATE OF COMMENCE.  (DATETIME)
= ESTIMATED DATE OF CLOSURE.   (DATETIME)
= ACTUAL DATE OF CLOSURE.   (DATETIME)
= IS COMPLETED   (A CHECKLIST TO BE COMPLETED BEFORE FINALISING)
**COMPLETION CHECKLIST
= SIGNED DELIVERY SENT
= SITE CLEANED UP
= TOOLS RETURNED TO STORE
= FABRIC FITTED
= PHOTOS SENT
