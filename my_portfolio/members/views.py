#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader #불러온다는건 그걸 사용하겠다는 의미

#메인
def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
#numpy
import numpy as np
from django.shortcuts import render


def members(request):
    template = loader.get_template('members.html')
    context = {
        'greeting': 1,
    }
    return HttpResponse(template.render())

    arr = np.array([1, 2, 3, 4, 5])  # 배열 생성
    total = np.sum(arr)  # 배열의 합 계산
    mean = np.mean(arr)  # 배열의 평균 계산
    print(f"Total: {total}, Mean: {mean}")

    # 결과를 템플릿으로 전달
    return render(request, 'members.html', {'total': total, 'mean': mean})
