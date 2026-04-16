class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> hashSet;

        for (int num : nums) {
            if (hashSet.count(num)) {
                return true;
            }
            hashSet.insert(num);
        }
        return false; 

    }
};