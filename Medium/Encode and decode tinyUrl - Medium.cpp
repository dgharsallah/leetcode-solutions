class Solution {
public:

    unordered_map<string, string> in;
    
    // Encodes a URL to a shortened URL.
    string encode(string longUrl) {
        unordered_map<string, string>::hasher func = in.hash_function();   
        string hash = to_string(func(longUrl));
        in[hash] = longUrl;
        return hash;
    }

    // Decodes a shortened URL to its original URL.
    string decode(string shortUrl) {
           return in[shortUrl];
    }
};

// Your Solution object will be instantiated and called as such:
// Solution solution;
// solution.decode(solution.encode(url));
