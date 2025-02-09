## 함수 네이밍 정리
1. 모든 문제는 Solution 함수에서 input을 받고 출력을 내야한다.
2. process_input_data 함수에서는 List[str]으로 받은 값을 각 문제 형식에 맞게 변환한다.
3. 항상 함수들 순서는 위에서부터 문제 푸는 함수 - process_input_data - Solution - 단위 테스트 이다