import json
from django.db import models 
from django.utils import timezone
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

#UTILS [START] 

class GlobalSettingTable(models.Model):
    gs_id = models.AutoField(db_column='gs_id', primary_key=True)
    gs_name = models.CharField(max_length=100, db_column='gs_name')
    gs_value = models.TextField(db_column='gs_value', blank = True) 
    is_active = models.CharField(db_column='is_active',  default='N', max_length=10, choices=((1, "Y"), (2, "N")), help_text="'Y' or 'N'")
    create_at = models.DateTimeField(db_column='create_at', default=timezone.now) 
    status    = models.CharField(max_length=100, db_column='status')

    def __str__(self):
        role_data = {}
        role_data['gs_id'] = self.gs_id
        role_data['gs_name'] = self.gs_name
        role_data['gs_value'] = self.gs_value
        role_data['is_active'] = self.is_active
        role_data['create_at'] = str(self.create_at)
        role_data['status'] = self.status

        return json.dumps(role_data)
 
    
    class Meta:
        db_table = "GLOBAL_SETTING"

 
class StateTable(models.Model):
    state_id = models.AutoField(db_column='state_id', primary_key=True)
    state_name = models.CharField(max_length=100, db_column='state_name')
    is_active = models.CharField(db_column='is_active',  default='N', max_length=10, choices=((1, "Y"), (2, "N")), help_text="'Y' or 'N'")
    create_at = models.DateTimeField(db_column='create_at', default=timezone.now) 
    status  = models.CharField(max_length=100, db_column='status')

    def __str__(self):
        state_data = {}
        state_data['state_id'] = self.state_id
        state_data['state_name'] = self.state_name 
        state_data['is_active'] = self.is_active
        state_data['create_at'] = str(self.create_at)
        state_data['status'] = self.status

        return json.dumps(state_data)
 
    
    class Meta:
        db_table = "MASTER_STATE"


class DistrictTable(models.Model):
    district_id = models.AutoField(db_column='district_id', primary_key=True)
    district_name = models.CharField(max_length=100, db_column='district_name')
    is_active = models.CharField(db_column='is_active',  default='N', max_length=10, choices=((1, "Y"), (2, "N")), help_text="'Y' or 'N'")
    create_at = models.DateTimeField(db_column='create_at', default=timezone.now)
    status  = models.CharField(max_length=100, db_column='status')

    def __str__(self):
        district_data = {}
        district_data['district_id'] = self.district_id
        district_data['district_name'] = self.district_name 
        district_data['is_active'] = self.is_active
        district_data['create_at'] = str(self.create_at)
        district_data['status'] = self.status

        return json.dumps(district_data)
 
    
    class Meta:
        db_table = "MASTER_DISTRICT"


#[END]


class UserTable(models.Model):
    user_id = models.AutoField(db_column='user_id', primary_key=True) 
    user_name = models.CharField(max_length=500, db_column='user_name')
    last_name = models.CharField(max_length=500, db_column='last_name')
    email = models.CharField(max_length=500, db_column='email')
    phone = models.CharField(max_length=100, db_column='phone')
    dob = models.DateTimeField(db_column='dob', default=timezone.now)
    password = models.CharField(max_length=500, db_column='password')
    user_type = models.CharField(db_column='user_type',  default=None, max_length=100, choices=((1, "APP_USER"), (2, "WEB_USER")), help_text="'APP_USER', 'WEB_USER'")
    is_active = models.CharField(db_column='is_active',  default='N', max_length=10, choices=((1, "Y"), (2, "N")), help_text="'Y' or 'N'")
    create_at = models.DateTimeField(db_column='create_at', default=timezone.now)
    comment   = models.CharField(max_length=500, db_column='comment')
    status  = models.CharField(max_length=100, db_column='status')
    sponsor_id =  models.IntegerField(db_column='sponsor_id', default=0, help_text="user id")

    def __str__(self):
        table_data = {}
        table_data['user_id'] = self.user_id    
        table_data['sponsor_id'] = self.sponsor_id  
        table_data['user_name'] = self.user_name
        table_data['last_name'] = self.last_name
        table_data['email'] = self.email
        table_data['dob'] = str(self.dob)
        table_data['phone'] = self.phone
        table_data['password'] = self.password
        table_data['user_type'] = self.user_type
        table_data['is_active'] = self.is_active
        table_data['create_at'] = str(self.create_at)
        table_data['comment'] = self.comment
        table_data['status'] = self.status 

        return json.dumps(table_data)
 
    class Meta:
        db_table = "USER"

class WalletTable(models.Model):
    wallet_id = models.AutoField(db_column='wallet_id', primary_key=True) 
    ov_cash = models.FloatField(db_column='ov_cash',  default=0.0)
    ovr_cash = models.FloatField(db_column='ovr_cash',  default=0.0)
    total_ov_cash = models.FloatField(db_column='total_ov_cash',  default=0.0)
    total_ovr_cash = models.FloatField(db_column='total_ovr_cash',  default=0.0)
    achiver_cash_back = models.FloatField(db_column='achiver_cash_back',  default=0.0)
    reward_and_prices = models.FloatField(db_column='reward_and_prices',  default=0.0)
    is_active = models.CharField(db_column='is_active',  default='N', max_length=10, choices=((1, "Y"), (2, "N")), help_text="'Y' or 'N'")
    create_at = models.DateTimeField(db_column='create_at', default=timezone.now)
    comment = models.CharField(max_length=500, db_column='comment')
    status = models.CharField(max_length=100, db_column='status')
    user_data = models.ForeignKey(UserTable, related_name='user_data', on_delete=models.CASCADE, help_text="FK on UserTable")

    def __str__(self):
        table_data = {}
        table_data['wallet_id'] = self.wallet_id    
        table_data['user_data'] = str(self.user_data) 
        table_data['user_data_id'] = str(self.user_data) 
        table_data['ov_cash'] = self.ov_cash
        table_data['ovr_cash'] = self.ovr_cash 
        table_data['total_ov_cash'] = self.total_ov_cash
        table_data['total_ovr_cash'] = self.total_ovr_cash 
        table_data['achiver_cash_back'] = self.achiver_cash_back
        table_data['reward_and_prices'] = self.reward_and_prices 
        table_data['is_active'] = self.is_active
        table_data['create_at'] = str(self.create_at)
        table_data['comment'] = self.comment
        table_data['status'] = self.status

    # def calculateov(self):
    #     ov_cash=self.ov_cash
    #     return ov_cash * 2    
        
        return json.dumps(table_data)

    class Meta:
        db_table = "WALLET"


class TutorialTable(models.Model):
    tutorial_id = models.AutoField(db_column='wallet_id', primary_key=True) 
    name = models.CharField(max_length=500, db_column='name')
    description =  models.TextField(db_column="description", null=True, blank=True)
    video_url = models.TextField(db_column='video_url')
    img_url = models.TextField(db_column='img_url')
    is_active = models.CharField(db_column='is_active', default='N', max_length=10, choices=((1, "Y"), (2, "N")), help_text="'Y' or 'N'")
    create_at = models.DateTimeField(db_column='create_at', default=timezone.now)
    comment = models.CharField(max_length=500, db_column='comment')
    status = models.CharField(max_length=100, db_column='status')

    def __str__(self):
        table_data = {}
        table_data['tutorial_id'] = self.tutorial_id    
        table_data['name'] = self.name
        table_data['description'] = self.description 
        table_data['video_url'] = self.video_url
        table_data['img_url'] = self.img_url  
        table_data['is_active'] = self.is_active
        table_data['create_at'] = str(self.create_at)
        table_data['comment'] = self.comment
        table_data['status'] = self.status 

        return json.dumps(table_data)
 
    class Meta:
        db_table = "TUTORIAL"



