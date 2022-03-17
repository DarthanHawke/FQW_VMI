from django import forms
from django.core.validators import MinValueValidator
from math import sqrt


class VMIform(forms.Form):
    C1 = forms.IntegerField()
    C2 = forms.IntegerField()
    R = forms.IntegerField()
    H = forms.IntegerField()
    F = forms.IntegerField()
    A = forms.IntegerField()


    def VMI(self, *args):
        w1 = 0.8
        w2 = 0.2
        Q = self
        C1, C2, R, H, F = args
        return w1 * ((R / Q) * (C1 + C2) + H * Q / 2) + w2 * (Q * F)


    def limitations(self, *args):
        return 0


    def TC(args):
        Q, C1, C2, R, H = args
        return (R / Q) * (C1 + C2) + H * Q / 2