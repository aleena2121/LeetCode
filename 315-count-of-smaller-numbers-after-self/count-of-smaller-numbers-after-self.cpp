class SegmentTree{
    private:
        int n, *tree;
        void update(int id,int val,int l,int r,int i)
        {
            if(l == r){
                tree[i] += val;
                return;
            }
            int m = (l+r)>>1;
            if(m >= id) update(id,val,l,m,2*i+1);
            else update(id,val,m+1,r,2*i+2);
            tree[i] = tree[2*i+1] + tree[2*i+2];
        }
        int sum(int x,int y,int l,int r,int i)
        {
            if(y < l || x > r) return 0;
            if(x <= l && y >= r) return tree[i];
            int m = (l+r)>>1;
            int left = sum(x,y,l,m,2*i+1);
            int right = sum(x,y,m+1,r,2*i+2);
            return left + right;
        }
    public:
        SegmentTree(int n)
        {
            this->n = n;
            tree = new int[4*n];
            for(int i=0; i<4*n; ++i) tree[i] = 0;
        }
        void update(int i,int val)
        {
            update(i,val,0,n-1,0);
        }
        int sum(int x,int y)
        {
            return sum(x,y,0,n-1,0);
        }
        ~SegmentTree()
        {
            delete[] tree;
        }
};

class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        int n = nums.size();
        vector<pair<int,int>> v(n);
        for(int i=0; i<n; ++i) v[i] = {nums[i],i};
        sort(begin(v),end(v));
        map<pair<int,int>,int> pos;
        for(int i=0; i<n; ++i) pos[v[i]] = i;
        vector<int> ans(n);
        SegmentTree st(n);
        for(int i=n-1; i>-1; --i){
            int id = pos[{nums[i],i}];
            int sum = st.sum(0,id-1);
            ans[i] = sum;
            st.update(id,1);
        }
        return ans;
    }
};