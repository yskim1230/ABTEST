출처와 데이터 다운 : [Kaggle - A/B Test](https://www.kaggle.com/datasets/sergylog/ab-test-data)

# 1. 개요

사이트는 수입을 늘리기 위해 A/B 테스트를 시작했습니다. 엑셀 파일에는 실험 결과(user_id), 샘플 유형(variant_name), 사용자가 가져온 수입(revenue)에 대한 원시 데이터가 포함되어 있습니다. 임무는 실험 결과를 분석하고 권장 사항을 작성하는 것입니다.


# 2. 데이터 분석
## 1). 데이터 확인
> 데이터 파일에는 다음과 같은 세 가지 열이 포함되어 있습니다:
1. USER_ID: 사용자 ID (정수)
2. VARIANT_NAME: 실험군 이름 (범주형 - 'control'과 'variant' 두 가지 범주가 있음)
3/ REVENUE: 사용자가 생성한 수익 (실수)
>
이 데이터를 사용하여 A/B 테스트 결과를 분석할 것입니다. 분석은 다음 단계로 진행됩니다:
>
* 기술통계: 두 그룹(control과 variant)의 수익에 대한 기초적인 통계를 확인합니다.
* 가설 검정: 두 그룹 간의 수익 차이가 통계적으로 유의한지 검정합니다.
* 추천 사항 제시: 분석 결과에 근거하여 추천 사항을 제시합니다.



## 2). 기술통계
>
```
import pandas as pd
from scipy.stats import ttest_ind
file_path = '/Users/youngseokkim/Desktop/AB Test/kaggle/AB_Test_Results.csv'
ab_test_data = pd.read_csv(file_path)
ab_test_data_info = ab_test_data.info()
ab_test_data_head = ab_test_data.head()
>
descriptive_stats = ab_test_data.groupby('VARIANT_NAME')['REVENUE'].describe()
print("\nDescriptive statistics:")
print(descriptive_stats)
```
> ![](https://velog.velcdn.com/images/malangcow/post/e4ea6ff7-3080-4cf7-8348-fc8d878136c7/image.png)
>![](https://velog.velcdn.com/images/malangcow/post/9b4cf741-3e6e-41e6-a030-3311949d8555/image.png)

## 3). 기술통계 결과
기술통계를 바탕으로 본 두 그룹의 수익 차이는 다음과 같습니다:

> ### Control Group (대조군):
- 샘플 수: 4984
- 평균 수익: $0.129
- 표준편차: $3.008
- 최소/최대 수익: $0.00 / $196.01

> ### Variant Group (실험군):
- 샘플 수: 5016
- 평균 수익: $0.070
- 표준편차: $1.315
- 최소/최대 수익: $0.00 / $58.63

첫눈에 대조군의 평균 수익이 실험군보다 더 높아 보입니다. 그러나 이 차이가 통계적으로 유의한지 확인하기 위해 가설 검정을 실시해야 합니다.




# 3. 가설 설정 및 검증

## 가설 설정 및 검증 결과
* 귀무 가설 (H0): 두 그룹 간의 평균 수익에 차이가 없다.
* 대립 가설 (H1): 두 그룹 간의 평균 수익에 차이가 있다.

이제 두 그룹 간의 수익 차이에 대한 t-검정을 실시하겠습니다

>
```
control_revenue = ab_test_data[ab_test_data['VARIANT_NAME'] == 'control']['REVENUE']
variant_revenue = ab_test_data[ab_test_data['VARIANT_NAME'] == 'variant']['REVENUE']
#t-test
t_stat, p_value = ttest_ind(control_revenue, variant_revenue, equal_var=False)
```
![](https://velog.velcdn.com/images/malangcow/post/8df25568-13cc-49e5-b837-1c78faa2ae49/image.png)

검증 결과 
* t 통계량: 1.268
* p-값: 0.205

이 p-값은 일반적인 유의수준(예: 0.05)보다 높습니다. 이는 두 그룹 간의 평균 수익 차이가 통계적으로 유의하지 않다는 것을 의미합니다. 즉, 귀무 가설을 기각할 충분한 근거가 없으므로, **실험군과 대조군 간에 유의한 평균 수익 차이가 없다고 결론지을 수 있습니다.**
