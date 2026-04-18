class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() !=  t.length()) return false;
        return sortString(s) == sortString(t);
    }

    string sortString(string s) {
        // Array to keep the count of char
        // 26 == number of alphabets
        int charCount[26] = {0};
        string newString;

        // traverse the string and increment char count
        for (int i = 0; i < s.size(); i++) {
            charCount[s[i] - 'a']++;
        }

        // return sorted array
        for (int i = 0; i < 26; i++) {
            for (int j = 0; j < charCount[i]; j++) {
                newString += 'a' + i;
            }
        }

        return newString;
    }
};
