#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

// 조합 계산 함수
int getanswer(int M, int N) {
    if (N > M) return 0; // N이 M보다 크면 조합 불가능
    if (N == 0 || N == M) return 1; // N == 0 또는 N == M이면 조합은 1
    
    long long numerator = 1; // 분자
    long long denominator = 1; // 분모
    
    // 분자 계산 (M * (M-1) * ... * (M-N+1))
    for (int i = 0; i < N; i++) {
        numerator *= (M - i);
        denominator *= (i + 1); // 분모 계산 (N!)
    }
    
    return (int)(numerator / denominator); // 정수로 반환
}
