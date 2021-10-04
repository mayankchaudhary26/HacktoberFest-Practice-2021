#include <bits/stdc++.h>
#include<vector>
using namespace std;

int main()
{
    int n, m;
    cin>>n>>m;
    int count = 0;
    vector<vector<int> > adjacent_list(n);
    vector<int> indegree(n,0);
    for (int i = 0; i < m; i++)
    {
        int u,v; 
        cin>>u>>v;
        adjacent_list[u].push_back(v);
        indegree[v]++;
    }

    queue<int> pq;

    for(int i=0; i<n; i++ )
    {
        if(indegree[i]==0)
        {
            pq.push(i);
        }

    }
    
    while(!pq.empty())
    {
        count++;
        int x  = pq.front();
        pq.pop();
        cout<<x<<" ";
        for(auto it: adjacent_list[x])
        {
            indegree[it]--;
            if(indegree[it]==0)
                pq.push(it);
        }
    }

//[[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]
}//0 10 3 18 5 6 11 14 13 1 15 17 4
