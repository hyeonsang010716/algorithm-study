def solve(input):
    results = []  # 결과를 저장할 리스트
    
    # input은 리스트로 제공됨, 이를 하나씩 처리
    for input_line in input:
        # 입력이 공백을 기준으로 정확히 나누어지는지 확인
        print(f"Processing line: {input_line}")  # 디버깅: 입력된 줄을 출력해보세요
        try:
            a, b = input_line.split()  # 공백 기준으로 a와 b를 나눔
        except ValueError:
            print(f"Error: Unable to split the line: {input_line}")
            continue  # 문제가 있는 줄은 건너뛰기
        
        answer = []

        # b에서 a를 비교할 수 있는 모든 위치를 순회
        for i in range(len(b) - len(a) + 1):
            count = 0
            for j in range(len(a)):
                if a[j] != b[i + j]:  # 서로 다른 문자를 찾으면 count 증가
                    count += 1
            answer.append(count)  # 각 비교 결과를 answer에 추가
        
        results.append(str(min(answer)))  # 최소값을 results에 추가
    
    return results  # 결과 리스트 반환
