class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        sort(people.begin(), people.end(), [](vector<int> &a, vector<int> &b) {
            if (a[0] == b[0]) return a[1] < b[1];
            return a[0] > b[0];
        });
        list<vector<int>> a;
        for (auto p : people) {
            auto it = a.begin();
            advance(it, p[1]);
            a.insert(it, p);
            // auto itt = a.begin();
            // for (auto it1 = a.begin(); it1 != a.end(); ++it1) {
            //     for (auto it2 = it1->begin(); it2 != it1->end(); ++it2) {
            //         cout << *it2 << " ";
            //     }
            //     cout << endl;
            // }
            // cout << "---\n";
        }
        return vector<vector<int>>(a.begin(), a.end());
    }
};
