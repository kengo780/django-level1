from django import forms

class Work01Form(forms.Form) :
    name = forms.CharField(label = "名前")
    mail = forms.EmailField(label = "メール")
    age = forms.IntegerField(label = "年齢")

class Work02Form (forms.Form):
    name = forms.CharField(
        label = "名前",
        initial = "",
        widget=forms.TextInput(attrs={"class" : "form-control"}))
    mail = forms.EmailField(
        label = "メール",
        initial = "",
        widget=forms.EmailInput(attrs={"class" : "form-control"}))
    age = forms.IntegerField(
        label = "年齢",
        initial = "",
        widget=forms.NumberInput(attrs={"class" : "form-control"}))

class Work03Form (forms.Form):
    name = forms.CharField(
        label = "名前", 
        initial = "",
        widget=forms.TextInput(attrs={"class" : "form-control"}))
    city = forms.ChoiceField(
        label = "行ってみたい都市",
        initial = "",
        choices = (
            ('Tokyo', '東京'),
            ('NewYork', 'ニューヨーク'),
            ('London', 'ロンドン'),
            ('Paris', 'パリ'),
            ('Madrid', 'マドリード')
        ),
        widget=forms.Select(attrs={"class" : "form-control"}))


class Work04Form (forms.Form):
    name = forms.CharField(
        label = "名前",
        initial = "",
        widget=forms.TextInput(attrs={"class" : "form-control"}))
    music = forms.ChoiceField(
        label="好きな音楽",
        initial = "",
        choices = (
            ('pop', 'ポップ'),
            ('rock', 'ロック'),
            ('anime', 'アニソン'),
            ('idol', 'アイドル'),
        ),
        widget=forms.RadioSelect(attrs={"class" : "form-control-custom"}))
    

class Work05Form (forms.Form):
    name = forms.CharField(
        label = "名前", 
        initial = "",
        widget=forms.TextInput(attrs={"class" : "form-control"}))
    movie = forms.MultipleChoiceField(
        label = "好きな映画",
        initial = "",
        choices = (
            ('sf', 'SF'),
            ('action', 'アクション'),
            ('comedy', 'コメディ'),
            ('suspence', 'サスペンス'),
        ),
        widget=forms.CheckboxSelectMultiple(attrs={"class" : "form-control-custom"}))

class Work06Form (forms.Form):
    name = forms.CharField(
        label = "名前",
        initial = "",
        widget=forms.TextInput(attrs={"class" : "form-control"}))
    message = forms.CharField(
        label="メッセージ",
        initial = "",
        widget=forms.Textarea(attrs={"class" : "form-control"}))
    

class Work07Form (forms.Form):
    name = forms.CharField(
        label = "名前",
        initial = "",
        widget=forms.TextInput(attrs={"class" : "form-control"}))
    secret = forms.CharField(
        initial = "this is secret",
        widget=forms.HiddenInput())

class Work08Form(forms.Form):
    school = forms.CharField(
        label="学校名",
        initial="",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    grade = forms.ChoiceField(
        label="学年",
        initial="",
        choices=(
            ('1st', '1年'),
            ('2nd', '2年'),
            ('3rd', '3年'),
        ),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    # subject field
    subject = forms.ChoiceField(
        label="好きな科目",
        initial="",
        choices=(
            ('Japanese', '国語'),
            ('Math', '数学'),
            ('English', '英語'),
            ('Science', '理科'),
            ('SocialStudies', '社会'),
        ),
        widget=forms.RadioSelect(attrs={'class': 'form-control-custom'})
    )


class Work09Form(forms.Form):
    movie = forms.CharField(
        label="好きな映画",
        initial="",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    genre = forms.MultipleChoiceField(
        label="好きな映画ジャンル",
        initial="",
        choices=(
            ('SF', 'SF'),
            ('Action', 'アクション'),
            ('Love', '恋愛'),
            ('Comedy', 'コメディ'),
            ('Horror', 'ホラー'),
        ),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control-custom'})
    )

    comment = forms.CharField(
        label="映画のコメント",
        initial="",
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )