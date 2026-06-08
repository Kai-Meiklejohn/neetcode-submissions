class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {

        size_t l {0};
        size_t r {numbers.size() - 1};

        while (l < r){
            int cur {numbers[l] + numbers[r]};

            if (cur == target) {
                return {static_cast<int>(l + 1), static_cast<int>(r + 1)};
            } else if (cur > target){
                r--;
            } else {
                l++;
            }
        }

        return {};
    }
};
