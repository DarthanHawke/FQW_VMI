from django import forms
from django.core.validators import MinValueValidator
from math import sqrt


class VMIform(forms.Form):
    C1 = forms.IntegerField()
    C2 = forms.IntegerField()
    R = forms.IntegerField()
    H = forms.IntegerField()
    F = forms.IntegerField()
    D = forms.IntegerField()
    A = forms.IntegerField()


    def VMI(self, *args):
        w1 = 0.8
        w2 = 0.2
        q, k = self
        C1, C2, R, H, F, D = args
        return w1 * ((C1 * R / (q * k)) + (H * ((q * k) - (k - 1) * q / 2)) +
                     (C2 * R * k / q) + ((H * (q * k)) / (2 * k))) + w2 * (q * k * F + q * F)


    def limitations(self, *args):
        q, k = self
        C1, C2, R, H, F, D = args
        Q = sqrt(2 * (C1 + C2) * R / H)
        return [k - Q/q, D - q * F]


    def TC(args):
        q, k, C1, C2, R, H, F, D = args
        return ((C1 * R / (q * k)) + (H * ((q * k) - (k - 1) * q / 2)) +
                (C2 * R * k / q) + ((H * (q * k)) / (2 * k)))