from django import forms


class Reg2(forms.Form):
    username = forms.CharField(max_length=30, label="请输入用户名")
    password = forms.CharField(max_length=30, label="请输入用户密码")
    password2 = forms.CharField(max_length=30, label="再次输入用户密码")

    def clean_username(self):
        name = self.cleaned_data['username']
        if '*' in name:
            raise forms.ValidationError("用户名不能为空")
        else:
            return name

    def clean(self):
        """
        表单整体验证
        :return:
        """
        pwd1 = self.cleaned_data('password')
        pwd2 = self.cleaned_data('password2')
        if pwd1 != pwd2:
            raise forms.ValidationError("两次密码不一致")
        return self.cleaned_data
