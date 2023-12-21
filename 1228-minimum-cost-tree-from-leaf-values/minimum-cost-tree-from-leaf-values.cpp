class Solution {
public:
    int bottomUp(vector<int>& arr,map<pair<int,int>, int> &maxi,int n){
        vector<vector<int>> dp(n+1,vector<int>(n+1,0));
        for(int left=n-1;left>=0;left--){
            for(int right=0;right<n;right++){
                if(left>=right)
                    continue;
                else{
                    int ans=INT_MAX;
                    for(int i=left;i<right;i++){
                        ans=min(ans,
                        (maxi[{left,i}]*maxi[{i+1,right}]+
                        dp[left][i]
                        +dp[i+1][right]));
                    }
                    dp[left][right]=ans;
                }
            }
        }
        return dp[0][n-1];
    }

    int mctFromLeafValues(vector<int>& arr) {
        map<pair<int,int>, int> maxi;
        for(int i=0;i<arr.size();i++){
            maxi[{i,i}]=arr[i];
             //this is basically 
                // pair<int,int> p;
                // p.first=i;
                // p.second=i;
                // maxi[p]=arr[i];
            for(int j=i+1;j<arr.size();j++){
                maxi[{i,j}]=max(arr[j],maxi[{i,j-1}]);
            }
        }
        int n=arr.size();
        return bottomUp(arr,maxi,n);
      }
};