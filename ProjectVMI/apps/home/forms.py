from django import forms
import numpy as np
from django.core.validators import MinValueValidator
from math import sqrt


class VMIform(forms.Form):
    A = forms.IntegerField()
    rows_setup = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        i, j = 0, 0
        row = []
        while j < 10:
            row.append(forms.IntegerField(required=False))
            j = j + 1
        sell = []
        while i < 5:
            sell.append(row)
            i = i + 1
        super().__init__(*args, **kwargs)


    def VMI(self, *args):
        w1 = 0.8
        w2 = 0.2
        rows_setup = args[-1]
        Q, b = [], []
        i = 0
        while i < rows_setup * 2 - 1:
            Q.append(self[i])
            b.append(self[i + 1])
            i = i + 2
        C1, C2, R, H, F = [], [], [], [], []
        i = 0
        while i < rows_setup:
            C1.append(args[0][i])
            C2.append(args[1][i])
            H.append(args[2][i])
            R.append(args[3][i])
            F.append(args[4][i])
            i = i + 1
        i = 0
        vmi = 0
        while i < rows_setup:
            vmi = vmi + (w1 * ((R[i] / Q[i]) * (C1[i] + C2[i]) + H[i] * ((Q[i] - b[i]) ** 2) / (2 * Q[i])
                     + (C1[i] + C2[i]) * (b[i] ** 2) / (2 * Q[i]) + (C1[i] + C2[i]) * b[i] * R[i] / Q[i])
                + w2 * (F[i] * (Q[i] - b[i])))
            i = i + 1
        return vmi


    def limitations(self, *args):
        rows_setup = args[-1]
        Q, b = [], []
        i = 0
        while i < rows_setup * 2 - 1:
            Q.append(self[i])
            b.append(self[i + 1])
            i = i + 2
        i = 0
        M = 0
        R = []
        while i < rows_setup:
            R.append(args[3][i])
            M = M + Q[i]
            i = i + 1
        if rows_setup == 1:
            return [Q[0] - b[0], M - R[0]/Q[0]]
        if rows_setup == 2:
            return [Q[0] - b[0], Q[1] - b[1], M - R[1]/Q[1]]
        if rows_setup == 3:
            return [Q[0] - b[0], Q[1] - b[1], Q[2] - b[2], M - R[2]/Q[2]]
        if rows_setup == 4:
            return [Q[0] - b[0], Q[1] - b[1], Q[2] - b[2], Q[3] - b[3], M - R[3]/Q[3]]
        if rows_setup == 5:
            return [Q[0] - b[0], Q[1] - b[1], Q[2] - b[2], Q[3] - b[3], Q[4] - b[4], M - R[4]/Q[4]]
        if rows_setup == 6:
            return [Q[0] - b[0], Q[1] - b[1], Q[2] - b[2], Q[3] - b[3], Q[4] - b[4], Q[5] - b[5],
                    M - R[5]/Q[5]]
        if rows_setup == 7:
            return [Q[0] - b[0], Q[1] - b[1], Q[2] - b[2], Q[3] - b[3], Q[4] - b[4], Q[5] - b[5], Q[6] - b[6],
                    M - R[6]/Q[6]]
        if rows_setup == 8:
            return [Q[0] - b[0], Q[1] - b[1], Q[2] - b[2], Q[3] - b[3], Q[4] - b[4], Q[5] - b[5], Q[6] - b[6],
                    Q[7] - b[7], M - R[7]/Q[7]]
        if rows_setup == 9:
            return [Q[0] - b[0], Q[1] - b[1], Q[2] - b[2], Q[3] - b[3], Q[4] - b[4], Q[5] - b[5], Q[6] - b[6],
                    Q[7] - b[7], Q[8] - b[8], M - R[8]/Q[8]]
        if rows_setup == 10:
            return [Q[0] - b[0], Q[1] - b[1], Q[2] - b[2], Q[3] - b[3], Q[4] - b[4], Q[5] - b[5], Q[6] - b[6],
                    Q[7] - b[7], Q[8] - b[8], Q[9] - b[9], M - R[9]/Q[9]]


    def TC(args):
        Q, b, C1, C2, H, R = args
        return ((R / Q) * (C1 + C2) + H * ((Q - b) ** 2) / (2 * Q)
                     + (C1 + C2) * (b ** 2) / (2 * Q) + (C1 + C2) * b * R / Q)

    def F(args):
        Q, b, F = args
        return F * (Q - b)