class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H) -> int:
        """
        (A,B,C,D) is (x1,y1) and (x2,y2) of rec1
        (E,F,G,H) is (x1,y2) and (x2,y2) of rec2
        """
        Area1 = abs(A-C)*abs(B-D)
        Area2 = abs(G-E)*abs(H-F)
        left = max(A,E)
        right = min(C,G)
        bottom = max(B,F)
        up = min(D,H)
        if right-left>0 and up-bottom>0:
            overLab = (right-left)*(up-bottom)
            return Area1+Area2-overLab
        else:
            return Area1+Area2
