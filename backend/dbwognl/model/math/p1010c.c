#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

// 팩토리얼 계산 함수
int factorial(int n) {
    int num=1;
    for(int i=1; i<n+1; i++)
        num=num*i;
    return num;
}

// 조합 계산 함수

// 결과를 반환하는 함수
int getanswer(int N, int M) {
    return factorial(N) / (factorial(N) * factorial (M-N)); // 정수형으로 변환 후 반환
}
