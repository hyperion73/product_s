from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd

def home(request):
    return render(request, 'home.html')

def sample_download(request):
    df = pd.DataFrame({
        '날짜': pd.date_range(start='2024-03-01', periods=30),
        '상품명': ['전자제품'] * 30,
        '매출': [100000 + i*1000 for i in range(30)],
        '광고비': [20000 + i*500 for i in range(30)]
    })
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="sample.xlsx"'
    with pd.ExcelWriter(response, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='상품 매출 통계', index=False)
    return response
