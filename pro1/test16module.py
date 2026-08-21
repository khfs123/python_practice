#현재 모듈은 다른 package에 있는 모듈의 멤버를 사용해
# 실행을 통해 어떤 결과를 확인할 수 있는 실행파일
# 실행파일은 > python 파일명 .py   <== main module

print('사용자 정의 모듈 작성 후 호출 연습 ---')
imsi = 100  #뭔가를 하다가...

print('\n경로 지정 방법 1 : import 모듈명')
import pack1.mymod1
print(dir(pack1.mymod1))        #사용가능 모듈 목록 
print(pack1.mymod1.__file__)   #경로명 및 파일명
print(pack1.mymod1.__name__)    #모듈명

list1 = [1,2]
list2 = [3,4,5]
pack1.mymod1.listHap(list1, list2)    #([1, 2], [3, 4, 5])
if __name__ == '__main__':
    print('와우 내가 메인 모듈이야')

print('\n경로 지정 방법2 : from 모듈명 import 모듈멤버, 0...')
from pack1.mymod1 import kbsFunc
kbsFunc()

from pack1.mymod1 import mbcFunc, tot
mbcFunc()
print('tot : ', tot)

from pack1.mymod1 import *   #메모리 낭비가 심하기에 비권장

from pack1.mymod1 import kbsFunc as 케이비에스별명
케이비에스별명()   #대한민국 대표 방송

print('\n경로 지정 방법3 : import 하위패키지..., 모듈명')
import pack1.subpack1.sbs
pack1.subpack1.sbs.sbsMansae()
import pack1.subpack1.sbs as 난별명
난별명.sbsMansae()

print()
from pack1_other import mymod2
imsi = mymod2.Hap(3,4)
print(imsi)

from pack1_other.mymod2 import cha as chachacha
print(chachacha(3,4))

print('\n경로 지정 방법4 : paht 설정이 된 폴도에 모듈이 저장된 경우')
# 예 : C:\Users\acorn\anaconda3\envs\myproject\Lib
import mymod3
print(mymod3.GoP(4, 5))

#C:\Users\acorn\anaconda3\envs\myproject\Lib\site-packages\numpy
import numpy
print(numpy.mean(3,5,7))

