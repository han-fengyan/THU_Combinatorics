// Creator: hfy
// Creat Time: 2023/10/27
// Description: calculate the number of ways to partition a number
// input: a number n
// output: the number of ways to partition n
//         the number of ways is stored in a big integer
 
#include <stdio.h>
#include <gmp.h>

void partition(int n) {
    mpz_t dp[n + 1];
    for (int i = 0; i <= n; i++) {
        mpz_init(dp[i]);
    }

    mpz_set_ui(dp[0], 1);

    for (int i = 1; i <= n; i++) {
        for (int j = i; j <= n; j++) {
            mpz_add(dp[j], dp[j], dp[j - i]);
        }
    }

    mpz_t ways;
    mpz_init(ways);
    mpz_set(ways, dp[n]);

    gmp_printf("Number of ways to partition %d is: %Zd\n", n, ways);

    for (int i = 0; i <= n; i++) {
        mpz_clear(dp[i]);
    }
    mpz_clear(ways);
}

int main() {
    int n;

    while (1) {
        printf("Enter the number to partition (0 to exit): ");
        if (scanf("%d", &n) != 1) {
            break;
        }

        if (n == 0) {
            break;
        }

        partition(n);
    }

    return 0;
}

