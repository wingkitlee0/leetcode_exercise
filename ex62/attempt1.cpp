#include <vector>
#include <iostream>
#include <memory>
#include <sstream>

class Solution {
public:
    int uniquePaths(int m, int n) {
        if (n>m) {
            int t = n; n = m; m = t;
        }
        if (m==1 or n==1) {
            return 1;
        }

        std::vector<int> row(m);
        int j=0;
        for (int i=0; i<n; i++) {
            if (i==0) {
                for (j=0; j<m; j++) {
                    row[j] = 1;
                }
            }
            else {
                row[0] = row[1] * 2;
                for (j=1; j<m-i; j++) {
                    row[j] = row[j-1] + row[j+1];
                }
            }
            for (j=0; j<m; j++) {
                std::cout << row[j] << " ";
            }
            std::cout << std::endl;
        }
        return row[m-n];
    }
};

int main(int argc, char** argv) {
    //std::shared_ptr<Solution> sol = std::make_shared<Solution>();
    auto sol = std::make_shared<Solution>();

    int m = 0;
    int n = 0;
    if (argc >= 2) {
        //std::stringstream a1(argv[1]);
        //std::stringstream a2(argv[2]);
        //a1 >> m; a2 >> n;
        m = std::stoi(argv[1]);
        n = std::stoi(argv[2]);
    }
    else {
        m = 0; n = 0;
    }

    std::cout << m << ", " << n << std::endl;

    auto answer = sol->uniquePaths(m, n);

    std::cout << answer << std::endl;

}