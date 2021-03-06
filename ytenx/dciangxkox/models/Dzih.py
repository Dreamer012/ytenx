# coding=utf-8
from django.db import models
from ytenx.kyonh.models import SieuxYonh

#單字條目
class Dzih(models.Model):
  #序號
  ziox = models.IntegerField(primary_key = True)
  #標識符
  id = models.CharField(max_length = 2, db_index = True)
  #字
  dzih = models.CharField(max_length = 1, db_index = True)
  #廣韻小韻
  sieux_yonh = models.ForeignKey(SieuxYonh, related_name='+', db_index = True, null = True)
  #聲符
  cjeng = models.ForeignKey('CjengByo', db_index = True)
  #韻部
  yonh = models.ForeignKey('YonhBox', db_index = True)
  #韻部細分
  yonh_seh = models.IntegerField()
  #擬音1
  ngix_1 = models.CharField(max_length = 16)
  #擬音2
  ngix_2 = models.CharField(max_length = 16)
  #擬音3
  ngix_3 = models.CharField(max_length = 16)
  #註釋
  tryoh = models.TextField()
  
  class Meta:
    app_label = 'dciangxkox'
  
  def __unicode__(self):
    return self.dzih
