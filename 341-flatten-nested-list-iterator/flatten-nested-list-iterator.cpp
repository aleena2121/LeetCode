class NestedIterator {
public:
    NestedIterator(vector<NestedInteger> &nestedList) {
        flatten(nestedList);
        currentIndex = 0;
    }

    int next() {
        return flattened[currentIndex++];
    }

    bool hasNext() {
        return currentIndex < flattened.size();
    }

private:
    vector<int> flattened;
    int currentIndex;

    void flatten(const vector<NestedInteger>& nestedList) {
        for (const auto& item : nestedList) {
            if (item.isInteger()) {
                flattened.push_back(item.getInteger());
            } else {
                flatten(item.getList());
            }
        }
    }
};