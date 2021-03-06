# -*- coding: utf-8 -*-
from django import forms
from models import *
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label = "邮箱", required = True, error_messages = {'required': "邮箱不能为空", "invalid" : "邮箱不合法"})
    username = forms.CharField(label = "用户名", error_messages = {'required': "用户名不能为空", "invalid" : "用户名不合法"})
    password1 = forms.CharField(label = "密码", error_messages = {'required': "密码存在问题"})
    password2 = forms.CharField(label = "请确认密码")
    def save(self, commit = True):
        user = super(RegisterForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
class LogForm(forms.ModelForm):
    title = forms.CharField(label = (u"标题"), max_length = 50, widget = forms.TextInput(attrs = {"placeholder":"日志标题"}))
    content = forms.CharField(label = (u"内容"), max_length = 1000, widget = forms.Textarea(attrs = {"placeholder":"请再此输入您的日志内容，不超过1000字..."}))
    class Meta:
        model = Log
        widgets = {
            "content": forms.Textarea(attrs={"col":10,"row":25},)
            }
        exclude = ['user', 'is_img', 'img_name', ]
class ProfileForm(forms.ModelForm):
    nickname = forms.CharField(label = (u"昵称"), max_length = 16, required = False,
                               widget = forms.TextInput(attrs = {"placeholder":"请输入昵称，不超过16个字，可不写"}))
    age = forms.IntegerField(label = (u"年龄"),
                             widget=forms.TextInput(attrs={"placeholder":"请输入年龄"}), required = False)
    phone = forms.CharField(label = (u"联系电话"), max_length = 20,
                            widget=forms.TextInput(attrs={"placeholder":"请输入联系方式"}), required = False)
    qq = forms.CharField(label = (u"QQ"), max_length = 20,
                         widget=forms.TextInput(attrs={"placeholder":"请输入QQ"}), required = False)
    travellike = forms.CharField(label = (u"旅游爱好"), max_length = 50, required = False,
                               widget = forms.Textarea(attrs={"placeholder":"请在此输入旅游爱好，可不写，不超过50字"}))
    class Meta:
        model = Profile
        fields = ['nickname', 'age', 'sex', 'phone', 'qq', 'travellike', ]
        widgets = {
            "question": forms.Textarea(attrs={"col":10,"row":25, }, ), 
            "answer": forms.Textarea(attrs={"col":10,"row":25},),
            "travellike": forms.Textarea(attrs={"col":10,"row":25},),
        }
class StrategyForm(forms.ModelForm):
    title = forms.CharField(label = (u"主题"), max_length = 50,
                            widget = forms.TextInput(attrs = {"placeholder":"旅游攻略主题"}))
    content = forms.CharField(label = (u"内容"), max_length = 1000,
                              widget = forms.Textarea(attrs = {"placeholder":"请再此编辑内容，不超过1000字..."}))
    class Meta:
        model = Strategy
        exclude = ['user', 'site', ]
        widgets = {
            "content": forms.Textarea(attrs={"col":10,"row":25},)
            }
class HopeForm(forms.ModelForm):
    home = forms.CharField(label = (u"出发地"), max_length = 50,
                           widget=forms.TextInput(attrs={"placeholder":"请输入出发地"}),
                           error_messages = {"required": "出发地一定要写哦"})
    goal = forms.CharField(label = (u"目的地"), max_length = 50,
                           widget=forms.TextInput(attrs={"placeholder":"请输入目的地"}),
                           error_messages = {"required": "目的地一定要写哦"})
    start_date = forms.DateField(label = (u"日期范围起点"),
                           widget=forms.TextInput(attrs={"placeholder":"请输入出发日期范围起点"}),
                           error_messages = {"required": "一定要写哦"})
    end_date = forms.DateField(label = (u"日期范围终点"),
                           widget=forms.TextInput(attrs={"placeholder":"请输入出发日期范围终点"}),
                           error_messages = {"required": "一定要写哦"})
    price = forms.IntegerField(label = (u"旅行预算"),
                               widget=forms.TextInput(attrs={"placeholder":"请输入您的旅行预算"}),
                               error_messages = {"required": "预算一定要写哦"})
    hopesry = forms.CharField(label = (u"期望去的景点"), max_length = 50, required = False,
                          widget = forms.TextInput(attrs={"placeholder":"请在此输入期望去的景点,不超过50字"}))
    tip = forms.CharField(label = (u"备注信息"), max_length = 128, required = False,
                          widget = forms.Textarea(attrs={"placeholder":"请在此输入备注信息，可不写，不超过128字"}))
    class Meta:
        model = Hope
        exclude = ['user', 'is_commit', ]
        widgets = {
            "tip": forms.Textarea(attrs={"col":10,"row":25},),
        }
        
    
class ActForm(forms.ModelForm):
    title = forms.CharField(label = (u"标题"), max_length = 20, required = True,
                          widget = forms.TextInput(attrs={"placeholder":"请在此输入标题,不超过20字"}))
    content = forms.CharField(label = (u"活动说明"), max_length = 100, required = True,
                          widget = forms.Textarea(attrs={"placeholder":"请在此输入活动说明，不超过100字"}))
    class Meta:
        model = Activity
        fields = ['title', 'content',]
        widgets = {
            'content' : forms.Textarea(attrs={"col":10,"row":20},),

            }

class SiteForm(forms.ModelForm):
    
    class Meta:
        model = Site
        exclude = ['is_img', ]
        widgets = {
            'content' : forms.Textarea(attrs={"col":10,"row":20},),
            }
class SiteCommitForm(forms.ModelForm):
    
    class Meta:
        model = SiteCommit
        fields = ['content',]
        widgets = {
            'content' : forms.Textarea(attrs={"col":10,"row":3},),
            }
