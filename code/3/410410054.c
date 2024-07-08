#include <stdio.h>
#define MOD 1000000007 

long long fastpow(long long a, long long b, long long m) {
    long long ans = 1; 
    a = a % m; 
    while (b > 0) { 
        if (b & 1) { 
            ans = (ans * a) % m; 
        }
        b = b >> 1; 
        a = (a * a) % m;
    }
    return ans; 
}

int main() {
    long long a, n; 
    while (scanf("%lld %lld", &a, &n) != EOF) { 
        printf("%lld\n", fastpow(a, n, MOD)); 
    }
    return 0; 
}
