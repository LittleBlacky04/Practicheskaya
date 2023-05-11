from django import forms

class LoginUser(forms.Form):
    # Поле  ввода Логина
    login = forms.CharField(label='Логин', widget=forms.TextInput(attrs={"class": ""}))
    # Поле ввода пароля
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={"class": ""}))

class Registration(forms.Form):
    # Поле ввода почты, используется для создания аккаунта
    email = forms.EmailField(label='login', widget=forms.EmailInput(attrs={"class": ""}))
    # Поле ввода пароля
    password = forms.PasswordInput(label='Пароль', widget=forms.PasswordInput(attrs={"class": ""}))

class ProfileEdite(forms.Form):
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={"class":""}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={"class":""}))
    email = forms.EmailField(label='Почта', widget=forms.EmailInput)
    phone_number = forms.CharField(label='Телефон', max_length=12, null=True, blank=True,
                                   widget=forms.TextInput(attrs={"class":""}))
    organization = forms.CharField(label='Организация', widget=forms.TextInput(attrs={"class":""}))
    education = forms.CharField(label='Образование', widget=forms.TextInput(attrs={"class": ""}))
    about = forms.CharField(label='О себе', widget=forms.TextInput(attrs={"class": ""}))
    image = forms.ImageField(label='Фото', widget=forms.ImageField(attrs={"class":""}))

class EventEdite(forms.Form):
    name = forms.CharField(label='Название', widget=forms.TextInput(attrs={"class":""}))
    place = forms.CharField(label='Место проведения', widget=forms.TextInput(attrs={"class":""}))
    address = forms.CharField(label='Адрес', widget=forms.TextInput(attrs={"class":""}))
    about = forms.CharField(label='О мероприятии', widget=forms.TextInput(attrs={"class":""}))
    date_start = forms.DateField(label="Дата начала", widget=forms.DateTimeField(attrs={"class":""}))
    date_end = forms.DateField(label="Дата окончания", widget=forms.DateTimeField(attrs={"class":""}))
    image = forms.ImageField(label='Фото', widget=forms.ImageField(attrs={"class":""}))

class ArticleEdite(forms.Form):
    title = forms.CharField(label='Название', widget=forms.TextInput(attrs={"class":""}))
    about = forms.CharField(label='О статье', widget=forms.TextInput(attrs={"class":""}))
    date = forms.DateField(label="Дата публикации", widget=forms.DateTimeField(attrs={"class":""}))
    image = forms.ImageField(label='Фото', widget=forms.ImageField(attrs={"class":""}))
    file = forms.FileField(label='Файл', widget=forms.FileInput(attrs={"class":""}))