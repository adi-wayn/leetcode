#include <string>
#include <unordered_map>
#include <climits>

using std::string;
using std::unordered_map;

class Solution {
public:
    string minWindow(string s, string t) {
        if (s.empty() || t.empty()) {
            return "";
        }

        unordered_map<char, int> t_freq;
        for (char c : t) {
            t_freq[c]++;
        }

        int need = t_freq.size();
        int left = 0, right = 0;
        int have = 0;
        unordered_map<char, int> window_counts;
        int min_len = INT_MAX;
        int min_left = 0;

        while (right < s.size()) {
            char c = s[right];
            window_counts[c]++;

            if (t_freq.count(c) && window_counts[c] == t_freq[c]) {
                have++;
            }

            while (left <= right && have == need) {
                c = s[left];

                if (right - left + 1 < min_len) {
                    min_len = right - left + 1;
                    min_left = left;
                }

                window_counts[c]--;
                if (t_freq.count(c) && window_counts[c] < t_freq[c]) {
                    have--;
                }
                left++;
            }
            right++;
        }
        return min_len == INT_MAX ? "" : s.substr(min_left, min_len);
    }
};