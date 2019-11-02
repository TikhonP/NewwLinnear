from django.http import HttpResponse
from django.shortcuts import render
import houses

def main(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'index.html', context)

    if request.method == 'POST':
        CRIM = float(request.POST.get('CRIM', ''))
        ZN = float(request.POST.get('ZN', ''))
        INDUS = float(request.POST.get('INDUS', ''))
        CHAS = float(request.POST.get('CHAS', ''))
        NOX = float(request.POST.get('NOX', ''))
        RM = float(request.POST.get('RM', ''))
        AGE = float(request.POST.get('AGE', ''))
        DIS = float(request.POST.get('DIS', ''))
        RAD = float(request.POST.get('RAD', ''))
        TAX = float(request.POST.get('TAX', ''))
        PTRATIO = float(request.POST.get('PTRATIO', ''))
        B = float(request.POST.get('B', ''))
        LSTAT = float(request.POST.get('LSTAT', ''))

        if (CRIM == '') or (ZN == '') or (INDUS == '') or (CHAS == '') or (NOX == '') or (RM == '') or (AGE == '') or (DIS == '') or (RAD == '') or (TAX == '') or (PTRATIO == '') or (B == '') or (LSTAT == ''):
            return HttpResponse("Заполните все поля")

        else:
            prediction = houses.getXandPredict(CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT)
            context = {"prediction": prediction}
            return render(request, 'indexOut.html', context)