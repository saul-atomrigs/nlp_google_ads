# Recommendation System for Google Ads
## Utilizing NLP for more efficient Google Ads Campaigns 

풀고자 하는 비즈니스 문제: 추천 알고리즘을 이용하여 구글 키워드 광고를 더 효과적으로 집행하는 방안입니다. 이를 통해 고객 기업의 click through rate 상승, 키워드 단가 절감 등을 이룰 수 있습니다. 

사용된 기술스택: 
- 파이썬
- MySQL
- Tensorflow
- Keras

개발환경:
- 파이썬 GPU (AWS EC2)

How: 
1. API 이용하여 트위터, 레딧, 구글 등 3곳에서 해당 산업의(본 프로젝트에서는 K-뷰티 산업) 주요 키워드를 스크래핑하여 최근 트렌딩 제품들을 선별합니다
2. word2vec 모델을 적용하여 키워드들을 인덱싱 한 후 검색/언급량이 많은 순서대로 가중치를 부여합니다
3. 구글 Ads에서 각 키워드별 단가를 추출합니다
4. 

프로젝트 진행 중 발생한 문제 & 해결 방법
