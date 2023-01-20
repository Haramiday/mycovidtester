from django import forms

choice = (("1","Yes"),
		("2","No"))

class Question(forms.Form):
	Do_you_have_Diarrhea = forms.ChoiceField(choices = choice)
	Do_you_have_Fever = forms.ChoiceField(choices = choice)
	Are_you_experiencing_Coughing = forms.ChoiceField(choices = choice)
	Do_you_have_ShortnessOfBreath = forms.ChoiceField(choices = choice)
	Do_you_have_SoreThroat = forms.ChoiceField(choices = choice)
	Are_you_experiencing_NauseaVomitting = forms.ChoiceField(choices = choice)
	Do_you_have_Fatigue = forms.ChoiceField(choices = choice)