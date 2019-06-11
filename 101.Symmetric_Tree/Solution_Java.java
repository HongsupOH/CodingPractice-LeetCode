import java.util.*;

import javax.swing.tree.TreeNode;

import java.io.*;
public class Solution {
	public boolean isSymmetric(TreeNode root) {
		if(root==null) {return true;}
		Stack<TreeNode[]> stack = new Stack<>();
		TreeNode[]tmp = new TreeNode[] {root.left,root.right};
		stack.add(tmp);
		while(!stack.isEmpty()) {
			TreeNode[] cur = stack.pop();
			TreeNode node1 = cur[0]; TreeNode node2 = cur[1];
			if(node1!=null && node2!=null) {
				if(node1.val!=node2.val) {
					return false;
				}
				else {
					TreeNode[] tmp1 = new TreeNode[]{node1.left,node2.right};
                    stack.add(tmp1);
                    TreeNode[] tmp2 = new TreeNode[]{node1.right,node2.left};
                    stack.add(tmp2);
				}
			}
			else if((node1==null &&node2!=null)||(node2==null&&node1!=null)) {
				return false;
			}
		}
		return true;
	}	
}
