class TreeNode {
    private int data;
    public TreeNode left;
    public TreeNode right;
    private int size;

    public TreeNode(int data) {
        this.data = data;
        this.size = 1;
    }

    public int size() { return size; }
    public int data() { return data; }

    public void insert(int data) {
        if (data <= this.data) {
            if (left == null) left = new TreeNode(data);
            else left.insert(data);
        } else {
            if (right == null) right = new TreeNode(data);
            else right.insert(data);
        }
        size++;
    }

    public TreeNode find(int data) {
        if (data == this.data) return this;
        else if (data <= this.data) return left != null ? left.find(data) : null;
        else if (data > this.data) return right != null ? right.find(data) : null;
        return null;
    }

    public TreeNode getRandomNode() {
        int leftSize = left != null ? left.size() : 0;
        Random random = new Random();
        int index = random.nextInt(size);
        if (index < leftSize) return left.getRandomNode();
        else if (index == leftSize) return this;
        else return right.getRandomNode();
    }
}

// optimized
class Tree {
    TreeNode root = null;

    public int size() { return root != null ? root.size() : 0; }

    public void insert(int data) {
        if (root == null) root = new TreeNode(data);
        else root.insert(data);
    }

    public TreeNode getRandomNode() {
        if (root == null) return null;

        Random random = new Random();
        int i = random.nextInt(size());
        return root.getIthNode(i);
    }
}

class TreeNode {
    // Same as above
    public TreeNode getIthNode(i) {
        int leftSize = left != null ? left.size() : 0;
        if (i < leftSize) return left.getIthNode(i);
        else if (i == leftSize) return this;
        else right.getIthNode(i - ()leftSize + 1);
    } 
}