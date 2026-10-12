from typing import List, Optional

class FenwickTree:
    __slots__=('n','data')
    def __init__(self,n): self.n=n; self.data=[0]*(n+1)
    def update(self,index,delta=1): i=index+1
        while i<=self.n: self.data[i]+=delta; i+=i&-i
    def query(self,index): i=index+1; total=0
        while i>0: total+=self.data[i]; i-=i&-i
        return total
    def find_by_prefix(self,prefix): idx=0; bit_mask=1<<(self.n.bit_length()-1)
        while bit_mask:
            next_idx=idx+bit_mask
            if next_idx<=self.n and self.data[next_idx]<prefix:
                prefix-=self.data[next_idx]; idx=next_idx
            bit_mask>>=1
        return idx
    def predecessor(self,index): count=self.query(index)
        if count==0: return None
        return self.find_by_prefix(count)
    def successor(self,index): total=self.query(self.n-1); count=self.query(index)
        if count==total: return None
        return self.find_by_prefix(count+1)

class LazySegmentTree:
    __slots__=('n','size','maxseg','lazy','left')
    def __init__(self,n,init_end): size=1
        while size<n: size<<=1
        self.n=n; self.size=size; self.maxseg=[-10**9]*(2*size); self.lazy=[None]*(2*size); self.left=[0]*(2*size)
        for i in range(size,size+n): self.left[i]=i-size; self.maxseg[i]=init_end-(i-size)
        for i in range(size+n,2*size): self.left[i]=i-size
        for i in range(size-1,0,-1): self.left[i]=self.left[2*i]; self.maxseg[i]=self.maxseg[2*i] if self.maxseg[2*i]>self.maxseg[2*i+1] else self.maxseg[2*i+1]
    def _apply(self,node,value): self.maxseg[node]=value-self.left[node]; self.lazy[node]=value
    def _push(self,node): lazy_val=self.lazy[node]
        if lazy_val is not None: self._apply(node*2,lazy_val); self._apply(node*2+1,lazy_val); self.lazy[node]=None
    def _pull(self,node): left=node*2; right=left+1; self.maxseg[node]=self.maxseg[left] if self.maxseg[left]>self.maxseg[right] else self.maxseg[right]
    def update_range(self,left,right,value,node=1,node_left=0,node_right=None):
        if node_right is None: node_right=self.size-1
        if left>node_right or right<node_left: return
        if left<=node_left and node_right<=right: self._apply(node,value); return
        self._push(node)
        mid=(node_left+node_right)//2
        self.update_range(left,right,value,node*2,node_left,mid)
        self.update_range(left,right,value,node*2+1,mid+1,node_right)
        self._pull(node)
    def query_max(self,left,right,node=1,node_left=0,node_right=None):
        if node_right is None: node_right=self.size-1
        if left>node_right or right<node_left: return -10**9
        if left<=node_left and node_right<=right: return self.maxseg[node]
        self._push(node)
        mid=(node_left+node_right)//2
        lm=self.query_max(left,right,node*2,node_left,mid)
        rm=self.query_max(left,right,node*2+1,mid+1,node_right)
        return lm if lm>rm else rm

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        max_x = 5 * 10 ** 4 + 1
        tree = LazySegmentTree(max_x, max_x)
        bit = FenwickTree(max_x)
        res: List[bool] = []
        for q in queries:
            if q[0] == 1:
                x = q[1]
                prev_obs = bit.predecessor(x - 1)
                start = 0 if prev_obs is None else prev_obs + 1
                if start <= x - 1:
                    tree.update_range(start, x - 1, x)
                bit.update(x)
            else:
                x, sz = q[1], q[2]
                if x - sz < 0:
                    res.append(False)
                else:
                    res.append(tree.query_max(0, x - sz) >= sz)
        return res


def brute(queries):
    obstacles=[]
    res=[]
    for q in queries:
        if q[0]==1:
            obstacles.append(q[1]); obstacles.sort()
        else:
            x, sz=q[1], q[2]
            possible=False
            for l in range(0, x-sz+1):
                r=l+sz
                ok=True
                for o in obstacles:
                    if o<l or o>r: continue
                    if o==l or o==r: continue
                    ok=False; break
                if ok: possible=True; break
            res.append(possible)
    return res

q=[[2, 7, 1], [2, 11, 3], [2, 1, 15], [1, 10], [2, 4, 5], [2, 13, 11], [2, 8, 11], [1, 16], [2, 13, 1], [1, 14], [2, 0, 17], [1, 18], [2, 3, 7], [2, 7, 12], [1, 15], [1, 11], [2, 11, 9], [2, 11, 15], [1, 2], [1, 7], [1, 8], [2, 15, 8], [1, 20], [1, 0], [2, 12, 3], [2, 7, 7], [2, 11, 10], [2, 20, 10], [2, 18, 14], [2, 15, 2], [1, 17], [1, 3], [2, 1, 8], [2, 15, 14], [1, 9], [2, 17, 13], [2, 5, 3], [2, 7, 14], [2, 2, 13], [2, 5, 16], [1, 5], [2, 2, 2], [2, 18, 20], [1, 19], [2, 6, 6], [2, 17, 2], [2, 12, 12], [2, 1, 16], [2, 8, 8], [2, 9, 3]]
sol=Solution()
obs=[]
res=[]
for idx,qitem in enumerate(q):
    if qitem[0]==1:
        x=qitem[1]
        prev=sol.__class__.__mro__[1].__name__ if False else None
    # no
print('done')
