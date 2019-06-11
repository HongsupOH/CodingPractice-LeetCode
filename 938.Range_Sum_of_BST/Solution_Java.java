import java.util.*;
import java.io.*;

public class Solution {
	public int rangeSumBST(TreeNode root, int L, int R) {
		Stack<TreeNode> stack = new Stack<>();
		stack.add(root);
		int total = 0;
		while(!stack.isEmpty()) {
			TreeNode node = stack.pop();
			if (node!=null){
				if(L<=node.val && node.val<=R) {
					total+=node.val;
				}
				stack.add(node.left);
				stack.add(node.right);
			}
		}
		return total;
	}
}

