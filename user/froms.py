from django import forms
from user.models import User, Profile


# 用forms.ModelForm来创建表单
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nickname','sex','birth_day','location']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        # fields = ['dating_sex','dating_location','min_dating_age','max_dating_age','min_distance','max_distance','vibration','only_matche','auto_play',]

    # 以此种方式命名比较字段函数 def clean_<field_name>
    def clean_max_dating_age(self):
        """检查最大交友年龄"""
        """
        检查的form字段使用is_valid(),内部调用clean()函数,调用is_valid()之后才能使用cleaned_data属性查看所有字段
        """
        cleaned = super().clean()
        if cleaned['max_dating_age'] < cleaned['min_dating_age']:
            raise forms.ValidationError('max_dating_age 必须大于 min_dating_age')
        else:
            return cleaned['max_dating_age']

    def clean_max_distance(self):
        """检查最大距离字段"""
        cleaned = super().clean()
        if cleaned['max_distance'] < cleaned['min_distance']:
            raise forms.ValidationError('max_distance 必须大于 min_distance')
        else:
            return cleaned['max_distance']





