/* 문제 : https://www.acmicpc.net/problem/12851 */

#include <iostream>
#include <deque>
#include <cstring>
using namespace std;
const int MIN_IDX = 0;
const int MAX_IDX = 100000;


pair<int, int> bfs(int soobin, int sister) {
    pair<int, int> ret;

    if (soobin >= sister) {
        ret.first = soobin - sister;
        ret.second = 1;
        return ret;
    }


    bool visited[MAX_IDX + 1];
    memset(visited, false, sizeof(visited));
    int min_time = sister - soobin;
    int cnt = 0;

    // pair<location, time> 
    deque<pair<int, int>> queue;
    queue.push_back(make_pair(soobin, 0));

    while (!queue.empty()){
        pair<int, int> entry = *(queue.begin());
        int cur_loc = entry.first;
        int time = entry.second;
        queue.pop_front();
        visited[cur_loc] = true;

        if (time > min_time)
            break;

        // sister 찾았을 때
        if (cur_loc == sister) {
            if (time < min_time) {
                min_time = time;
                cnt = 1;
            }
            else { // time == min_time
                cnt++;
            }
            continue;
        }

        // sister 못찾았을 때
        int next_loc = cur_loc - 1;
        if ((MIN_IDX <= next_loc) && (!visited[next_loc])) {
            queue.push_back(make_pair(next_loc, time + 1));
        }
        next_loc = cur_loc + 1;
        if ((next_loc <= MAX_IDX) && (!visited[next_loc])) {
            queue.push_back(make_pair(next_loc, time + 1));
        }
        next_loc = cur_loc * 2;
        if ((next_loc <= MAX_IDX) && (!visited[next_loc])) {
            queue.push_back(make_pair(next_loc, time + 1));
        }

    }

    ret.first = min_time;
    ret.second = cnt;
    return ret;
}

int main() {
    int soobin, sister;
    cin >> soobin >> sister;

    pair<int, int> ret = bfs(soobin, sister);
    cout << ret.first << endl;
    cout << ret.second << endl;
}
